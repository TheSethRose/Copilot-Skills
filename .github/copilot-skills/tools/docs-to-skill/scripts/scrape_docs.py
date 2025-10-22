#!/usr/bin/env python3
"""
Documentation to Copilot Skill Converter
Automatically scrapes documentation websites and generates Copilot Skills Architecture format.

Usage:
    python3 scrape_docs.py --interactive
    python3 scrape_docs.py --config configs/shadcn.json
    python3 scrape_docs.py --config configs/shadcn.json --dry-run
"""

import os
import sys
import json
import time
import re
import argparse
import hashlib
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque, defaultdict

# Try to import sitemap loader
try:
    from sitemap_loader import SitemapLoader
    SITEMAP_AVAILABLE = True
except ImportError:
    SITEMAP_AVAILABLE = False
    print("ℹ️  sitemap_loader not available (sitemap support disabled)")


class DocsToCopilotSkill:
    """Convert documentation websites into Copilot Skills Architecture format"""
    
    def __init__(self, config, dry_run=False, resume=False):
        self.config = config
        self.name = config['name']
        self.base_url = config['base_url']
        self.dry_run = dry_run
        self.resume = resume
        
        # Paths - output to .github directories
        self.data_dir = f"output/{self.name}_data"
        self.checkpoint_file = f"{self.data_dir}/checkpoint.json"
        
        # Checkpoint config
        checkpoint_config = config.get('checkpoint', {})
        self.checkpoint_enabled = checkpoint_config.get('enabled', True)
        self.checkpoint_interval = checkpoint_config.get('interval', 50)
        
        # State
        self.visited_urls = set()
        self.pages = []
        self.pages_scraped = 0
        
        # Initialize URLs (sitemap or manual)
        if config.get('use_sitemap', False) and SITEMAP_AVAILABLE:
            self.pending_urls = deque(self._load_urls_from_sitemap())
        else:
            start_urls = config.get('start_urls', [self.base_url])
            self.pending_urls = deque(start_urls)
        
        # Create data directory for caching
        if not dry_run:
            os.makedirs(f"{self.data_dir}/pages", exist_ok=True)
        
        # Load checkpoint if resuming
        if resume and not dry_run:
            self.load_checkpoint()
    
    def is_valid_url(self, url):
        """Check if URL should be scraped based on patterns"""
        if not url.startswith(self.base_url):
            return False
        
        # Include patterns
        includes = self.config.get('url_patterns', {}).get('include', [])
        if includes and not any(re.search(pattern, url) for pattern in includes):
            return False
        
        # Exclude patterns
        excludes = self.config.get('url_patterns', {}).get('exclude', [])
        if any(re.search(pattern, url) for pattern in excludes):
            return False
        
        return True
    
    def _load_urls_from_sitemap(self):
        """Load URLs from sitemap if available"""
        if not SITEMAP_AVAILABLE:
            print("  ⚠️  Sitemap loader not available, falling back to crawler")
            return [self.base_url]
        
        print(f"\n🗺️  Loading URLs from sitemap...")
        
        # Extract base domain for sitemap discovery
        parsed = urlparse(self.base_url)
        sitemap_base = f"{parsed.scheme}://{parsed.netloc}"
        
        loader = SitemapLoader(sitemap_base)
        
        # Get URL patterns from config
        includes = self.config.get('url_patterns', {}).get('include', [])
        excludes = self.config.get('url_patterns', {}).get('exclude', [])
        max_pages = self.config.get('max_pages', None)
        
        urls = loader.get_urls(
            include_patterns=includes,
            exclude_patterns=excludes,
            max_urls=max_pages
        )
        
        if not urls:
            print("  ⚠️  No URLs found in sitemap, falling back to crawler")
            return [self.base_url]
        
        return urls
    
    def save_checkpoint(self):
        """Save progress checkpoint"""
        if not self.checkpoint_enabled or self.dry_run:
            return
        
        checkpoint_data = {
            "config": self.config,
            "visited_urls": list(self.visited_urls),
            "pending_urls": list(self.pending_urls),
            "pages_scraped": self.pages_scraped,
            "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
        
        try:
            with open(self.checkpoint_file, 'w') as f:
                json.dump(checkpoint_data, f, indent=2)
            print(f"  💾 Checkpoint: {self.pages_scraped} pages")
        except Exception as e:
            print(f"  ⚠️  Checkpoint failed: {e}")
    
    def load_checkpoint(self):
        """Load progress from checkpoint"""
        if not os.path.exists(self.checkpoint_file):
            print("ℹ️  Starting fresh (no checkpoint)")
            return
        
        try:
            with open(self.checkpoint_file, 'r') as f:
                checkpoint_data = json.load(f)
            
            self.visited_urls = set(checkpoint_data["visited_urls"])
            self.pending_urls = deque(checkpoint_data["pending_urls"])
            self.pages_scraped = checkpoint_data["pages_scraped"]
            
            print(f"✅ Resumed from checkpoint")
            print(f"   Pages: {self.pages_scraped}")
            print(f"   Visited: {len(self.visited_urls)}")
            print(f"   Pending: {len(self.pending_urls)}")
            print(f"   Updated: {checkpoint_data['last_updated']}\n")
        except Exception as e:
            print(f"⚠️  Checkpoint load failed: {e}")
            print("   Starting fresh\n")
    
    def extract_content(self, soup, url):
        """Extract structured content from page"""
        page = {
            'url': url,
            'title': '',
            'content': '',
            'headings': [],
            'code_samples': [],
            'patterns': [],
            'links': []
        }
        
        selectors = self.config.get('selectors', {})
        
        # Extract title
        title_selector = selectors.get('title', 'h1, title')
        title_elem = soup.select_one(title_selector)
        if title_elem:
            page['title'] = self.clean_text(title_elem.get_text())
        
        # Find main content area
        main_selector = selectors.get('main_content', 'main, article, div[role="main"], #content')
        main = soup.select_one(main_selector)
        
        if not main:
            print(f"    ⚠️  No content: {url}")
            return page
        
        # Extract headings with hierarchy
        for h in main.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            text = self.clean_text(h.get_text())
            if text:
                page['headings'].append({
                    'level': h.name,
                    'text': text,
                    'id': h.get('id', '')
                })
        
        # Extract code samples with language detection
        code_selector = selectors.get('code_blocks', 'pre code, code[class*="language-"]')
        for code_elem in main.select(code_selector):
            code = code_elem.get_text()
            if len(code.strip()) > 10:
                lang = self.detect_language(code_elem, code)
                page['code_samples'].append({
                    'code': code.strip(),
                    'language': lang
                })
        
        # Extract common patterns
        page['patterns'] = self.extract_patterns(main)
        
        # Extract paragraphs
        paragraphs = []
        for p in main.find_all('p'):
            text = self.clean_text(p.get_text())
            if text and len(text) > 20:
                paragraphs.append(text)
        
        page['content'] = '\n\n'.join(paragraphs)
        
        # Extract valid links
        for link in main.find_all('a', href=True):
            href = urljoin(url, link['href'])
            if self.is_valid_url(href):
                page['links'].append(href)
        
        return page
    
    def detect_language(self, elem, code):
        """Detect programming language from code block"""
        # Check class attributes
        classes = elem.get('class', [])
        for cls in classes:
            if 'language-' in cls:
                return cls.replace('language-', '')
            if 'lang-' in cls:
                return cls.replace('lang-', '')
        
        # Check parent pre element
        parent = elem.parent
        if parent and parent.name == 'pre':
            classes = parent.get('class', [])
            for cls in classes:
                if 'language-' in cls:
                    return cls.replace('language-', '')
        
        # Heuristic detection
        if 'import ' in code and 'from ' in code:
            return 'python'
        if ('const ' in code or 'let ' in code or '=>' in code or 
            'function' in code or 'import {' in code):
            return 'javascript'
        if 'import React' in code or 'export default' in code or 'tsx' in code:
            return 'typescript'
        if 'def ' in code and ':' in code:
            return 'python'
        if '#include' in code or 'int main' in code:
            return 'cpp'
        if '<template>' in code or '<script>' in code:
            return 'vue'
        
        return 'text'
    
    def extract_patterns(self, main):
        """Extract common coding patterns and examples"""
        patterns = []
        
        # Look for example sections
        for elem in main.find_all(['p', 'div', 'section']):
            text = elem.get_text().lower()
            if any(word in text for word in ['example:', 'pattern:', 'usage:', 'how to']):
                # Get following code block
                next_code = elem.find_next(['pre', 'code'])
                if next_code:
                    patterns.append({
                        'description': self.clean_text(elem.get_text())[:200],
                        'code': next_code.get_text().strip()[:500]
                    })
        
        return patterns[:5]
    
    def clean_text(self, text):
        """Clean and normalize text"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def save_page(self, page):
        """Save page data to cache"""
        url_hash = hashlib.md5(page['url'].encode()).hexdigest()[:10]
        safe_title = re.sub(r'[^\w\s-]', '', page['title'])[:50]
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        
        filename = f"{safe_title}_{url_hash}.json"
        filepath = os.path.join(self.data_dir, "pages", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(page, f, indent=2, ensure_ascii=False)
    
    def scrape_page(self, url):
        """Scrape a single page"""
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Copilot Skills Documentation Scraper)'}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            page = self.extract_content(soup, url)
            
            self.save_page(page)
            self.pages.append(page)
            
            # Add new URLs to queue
            for link in page['links']:
                if link not in self.visited_urls and link not in self.pending_urls:
                    self.pending_urls.append(link)
            
            # Rate limiting
            time.sleep(self.config.get('rate_limit', 0.5))
            
        except Exception as e:
            print(f"    ✗ Error: {e}")
    
    def scrape_all(self):
        """Scrape all pages with BFS traversal"""
        print(f"\n{'='*60}")
        print(f"{'DRY RUN' if self.dry_run else 'SCRAPING'}: {self.name}")
        print(f"{'='*60}")
        print(f"URL: {self.base_url}")
        
        if self.dry_run:
            print(f"Mode: Preview only (first 20 URLs)\n")
        else:
            print(f"Data: {self.data_dir}\n")
        
        max_pages = self.config.get('max_pages', 500)
        preview_limit = 20 if self.dry_run else max_pages
        
        while self.pending_urls and len(self.visited_urls) < preview_limit:
            url = self.pending_urls.popleft()
            
            if url in self.visited_urls:
                continue
            
            self.visited_urls.add(url)
            
            if self.dry_run:
                print(f"  [Preview] {url}")
                # Simulate link discovery
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Copilot Skills Scraper)'}
                    response = requests.get(url, headers=headers, timeout=10)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    main_selector = self.config.get('selectors', {}).get('main_content', 'main')
                    main = soup.select_one(main_selector)
                    
                    if main:
                        for link in main.find_all('a', href=True):
                            href = urljoin(url, link['href'])
                            if self.is_valid_url(href) and href not in self.visited_urls:
                                self.pending_urls.append(href)
                except:
                    pass
            else:
                print(f"  {url}")
                self.scrape_page(url)
                self.pages_scraped += 1
                
                # Checkpoint
                if self.checkpoint_enabled and self.pages_scraped % self.checkpoint_interval == 0:
                    self.save_checkpoint()
            
            if len(self.visited_urls) % 10 == 0:
                print(f"    [{len(self.visited_urls)} pages]")
        
        if self.dry_run:
            print(f"\n✅ Dry run complete: ~{len(self.visited_urls)} pages found")
            print(f"💡 Remove --dry-run to actually scrape")
            self.preview_skill_output()
        else:
            print(f"\n✅ Scraped {len(self.visited_urls)} pages")
            self.save_summary()
    
    def save_summary(self):
        """Save scraping summary"""
        summary = {
            'name': self.name,
            'total_pages': len(self.pages),
            'base_url': self.base_url,
            'pages': [{'title': p['title'], 'url': p['url']} for p in self.pages]
        }
        
        with open(f"{self.data_dir}/summary.json", 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
    
    def preview_skill_output(self):
        """Preview what the generated skill files would look like"""
        print(f"\n{'='*60}")
        print(f"PREVIEW: Skill Output Structure")
        print(f"{'='*60}\n")
        
        description = self.config.get('description', f'{self.name} development assistance')
        file_patterns = self.config.get('file_patterns', ['**/*'])
        
        print("📁 Files that would be generated:\n")
        print(f"   .github/prompts/{self.name}.skill.prompt.md")
        print(f"   .github/instructions/{self.name}.instructions.md")
        print(f"   .github/copilot-skills/{self.name}/patterns.md")
        print(f"   .github/copilot-skills/{self.name}/reference.md")
        print(f"   .github/copilot-skills/{self.name}/references/[categories].md")
        print(f"   .github/copilot-skills/{self.name}/scripts/")
        print(f"   .github/copilot-skills/{self.name}/assets/")
        
        print(f"\n{'─'*60}")
        print(f"📄 .github/prompts/{self.name}.skill.prompt.md")
        print(f"{'─'*60}")
        print(f"""---
description: {description}
---

# {self.name.title()}

**Purpose**: {description}

## When to Use This Skill

Use this skill when:
- Working with {self.name} projects
- Implementing {self.name} features
- Debugging {self.name} code
- Learning {self.name} best practices

**Keywords**: {self.name}, [auto-detected from content]

## Quick Reference

### Common Patterns
[5-10 code patterns extracted from docs]

### Code Examples
[Real examples from documentation]

## Reference Documentation

Comprehensive docs in `.github/copilot-skills/{self.name}/references/`:
- getting_started.md
- api_reference.md
- [auto-categorized files]

## How to Use
Ask about {self.name} features or check reference files for details.
""")
        
        print(f"\n{'─'*60}")
        print(f"📄 .github/instructions/{self.name}.instructions.md")
        print(f"{'─'*60}")
        print(f"""# {self.name.title()} Instructions

**Auto-loaded when**: `{', '.join(file_patterns)}`

## Default Behaviors

1. Follow official {self.name} patterns
2. Use best practices from documentation
3. Implement proper error handling

## Common Workflows

### Setup
Check references/getting_started.md

### Development
Reference official patterns and examples

## Quality Guidelines

✅ Use official {self.name} APIs
✅ Follow community standards
⚠️ Avoid deprecated features
""")
        
        print(f"\n{'─'*60}")
        print(f"📄 .github/copilot-skills/{self.name}/patterns.md")
        print(f"{'─'*60}")
        print(f"""# {self.name.title()} - Common Patterns

Quick reference for common {self.name} patterns and usage.

## Code Patterns

### 1. [Pattern description]
```
[Code example from docs]
```

### 2-8. [More patterns...]

## Examples

### Example 1
```typescript
[Real code from documentation]
```

## Categories
See organized documentation in `references/`:
- components.md
- installation.md
[auto-detected categories]
""")
        
        print(f"\n{'─'*60}")
        print(f"� .github/copilot-skills/{self.name}/reference.md")
        print(f"{'─'*60}")
        print(f"""# {self.name.title()} - Reference Documentation

Comprehensive {self.name} documentation extracted from official sources.

## Overview

Categories:

### Components
**File**: `references/components.md`
**Pages**: [count]

### Installation
**File**: `references/installation.md`
**Pages**: [count]

[More categories...]

## How to Use
- Navigate to relevant category file
- Scan table of contents
- Read sections and copy examples
""")
        
        print(f"\n{'─'*60}")
        print(f"📂 .github/copilot-skills/{self.name}/references/")
        print(f"{'─'*60}")
        print(f"""
components.md      - Component documentation
installation.md    - Setup and installation
theming.md         - Theming and styling
[auto-categorized].md - Other topics

Each file contains:
- Page titles and URLs
- Table of contents from headings
- Content summaries (up to 2000 chars per page)
- Code examples with language tags
- Links to original documentation
""")
        
        print(f"\n{'='*60}")
        print(f"💡 To generate these files, run without --dry-run")
        print(f"{'='*60}\n")
    
    def load_scraped_data(self):
        """Load previously scraped pages from cache"""
        pages = []
        pages_dir = Path(self.data_dir) / "pages"
        
        if not pages_dir.exists():
            return []
        
        for json_file in sorted(pages_dir.glob("*.json")):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    pages.append(json.load(f))
            except Exception as e:
                print(f"    ⚠️  Error loading {json_file.name}: {e}")
        
        return pages
    
    def smart_categorize(self, pages):
        """Categorize pages by URL patterns and content"""
        category_defs = self.config.get('categories', {})
        
        # Auto-detect categories if none provided
        if not category_defs:
            category_defs = self.infer_categories(pages)
        
        categories = {cat: [] for cat in category_defs.keys()}
        categories['other'] = []
        
        for page in pages:
            url = page['url'].lower()
            title = page['title'].lower()
            content = page.get('content', '').lower()[:500]
            
            categorized = False
            
            # Match against category keywords
            for cat, keywords in category_defs.items():
                score = 0
                for keyword in keywords:
                    keyword = keyword.lower()
                    if keyword in url:
                        score += 3
                    if keyword in title:
                        score += 2
                    if keyword in content:
                        score += 1
                
                if score >= 2:
                    categories[cat].append(page)
                    categorized = True
                    break
            
            if not categorized:
                categories['other'].append(page)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}
    
    def infer_categories(self, pages):
        """Infer categories from URL structure"""
        url_segments = defaultdict(int)
        
        for page in pages:
            path = urlparse(page['url']).path
            segments = [s for s in path.split('/') 
                       if s and s not in ['en', 'stable', 'latest', 'docs', 'documentation']]
            
            for seg in segments:
                url_segments[seg] += 1
        
        # Use top segments as categories
        top_segments = sorted(url_segments.items(), key=lambda x: x[1], reverse=True)[:8]
        
        categories = {}
        for seg, count in top_segments:
            if count >= 3:
                categories[seg] = [seg]
        
        # Add common defaults
        if not any('getting' in cat or 'intro' in cat for cat in categories):
            categories['getting_started'] = ['getting-started', 'intro', 'quickstart', 'installation']
        
        if not any('api' in cat or 'reference' in cat for cat in categories):
            categories['api_reference'] = ['api', 'reference', 'class', 'method']
        
        return categories
    
    def build_skill(self):
        """Build Copilot Skill from scraped data"""
        print(f"\n{'='*60}")
        print(f"BUILDING COPILOT SKILL: {self.name}")
        print(f"{'='*60}\n")
        
        # Load scraped data
        print("Loading data...")
        pages = self.load_scraped_data()
        
        if not pages:
            print("✗ No data found! Run scraper first.")
            return False
        
        print(f"  ✓ Loaded {len(pages)} pages\n")
        
        # Categorize pages
        print("Categorizing...")
        categories = self.smart_categorize(pages)
        print(f"  ✓ {len(categories)} categories\n")
        
        # Generate outputs
        print("Generating skill files...")
        self.create_prompt_file(pages, categories)
        self.create_instructions_file(pages, categories)
        self.create_detail_files(categories)
        
        print(f"\n✅ Copilot Skill created!")
        print(f"\n📁 Generated files:")
        print(f"   .github/prompts/{self.name}.skill.prompt.md")
        print(f"   .github/instructions/{self.name}.instructions.md")
        print(f"   .github/copilot-skills/{self.name}/patterns.md")
        print(f"   .github/copilot-skills/{self.name}/reference.md")
        print(f"   .github/copilot-skills/{self.name}/references/ (organized docs)")
        
        return True
    
    def create_prompt_file(self, pages, categories):
        """Generate skill prompt with workflow"""
        description = self.config.get('description', f'Comprehensive {self.name} development assistance')
        
        # Extract common patterns
        all_patterns = []
        for page in pages[:20]:
            all_patterns.extend(page.get('patterns', []))
        
        # Get best code examples
        examples = []
        for page in pages[:10]:
            for sample in page.get('code_samples', [])[:2]:
                if sample.get('language') != 'text' and len(sample['code']) < 300:
                    examples.append(sample)
                if len(examples) >= 5:
                    break
            if len(examples) >= 5:
                break
        
        content = f"""---
description: {description}
---

# {self.name.title()}

**Purpose**: {description}

## When to Use This Skill

Use this skill when:
- Working with {self.name} projects
- Implementing {self.name} features
- Debugging {self.name} code
- Learning {self.name} best practices
- Building applications with {self.name}

**Keywords**: {self.name}, {', '.join(categories.keys())}

## Quick Reference

### Common Patterns

"""
        
        # Add patterns
        for i, pattern in enumerate(all_patterns[:5], 1):
            content += f"**{i}. {pattern.get('description', 'Common pattern')[:80]}**\n\n"
            content += f"```\n{pattern.get('code', '')[:200]}\n```\n\n"
        
        # Add examples
        if examples:
            content += "### Code Examples\n\n"
            for i, ex in enumerate(examples, 1):
                lang = ex.get('language', 'text')
                content += f"**Example {i}** ({lang}):\n```{lang}\n{ex['code'][:250]}\n```\n\n"
        
        content += f"""## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/{self.name}/references/`:

"""
        
        for cat in sorted(categories.keys()):
            content += f"- **{cat}.md** - {cat.replace('_', ' ').title()} documentation\n"
        
        content += f"""
## How to Use

### For Quick Answers
Ask directly about {self.name} features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- None (standalone skill)

## More Information

- **Base Documentation**: {self.base_url}
- **Generated**: {time.strftime("%Y-%m-%d")}
- **Total Pages**: {len(pages)}
"""
        
        os.makedirs('.github/prompts', exist_ok=True)
        filepath = f'.github/prompts/{self.name}.skill.prompt.md'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ {self.name}.skill.prompt.md")
    
    def create_instructions_file(self, pages, categories):
        """Generate instructions for auto-loading"""
        file_patterns = self.config.get('file_patterns', ['**/*'])
        
        content = f"""# {self.name.title()} Instructions

**Auto-loaded when**: Working with files matching: `{', '.join(file_patterns)}`

## Default Behaviors

When working with {self.name}:

1. **Follow Official Patterns**: Use patterns from official {self.name} documentation
2. **Code Quality**: Follow {self.name} best practices and conventions
3. **Error Handling**: Implement robust error handling appropriate for {self.name}
4. **Documentation**: Include inline comments for complex {self.name} usage

## Common Workflows

### Setup & Installation

Check `references/getting_started.md` for:
- Installation steps
- Configuration options
- Initial setup

### Development

1. Reference official documentation patterns
2. Use type-safe code when applicable
3. Follow {self.name} naming conventions
4. Test thoroughly

### Debugging

Common issues and solutions documented in `references/` files.

## Quality Guidelines

- ✅ Use official {self.name} APIs and patterns
- ✅ Follow community best practices
- ✅ Write maintainable, readable code
- ✅ Include error handling
- ⚠️ Avoid deprecated features
- ⚠️ Don't bypass {self.name} safety features

## Resources

- Skill prompt: `.github/prompts/{self.name}.skill.prompt.md`
- References: `.github/copilot-skills/{self.name}/references/`
- Official docs: {self.base_url}
"""
        
        os.makedirs('.github/instructions', exist_ok=True)
        filepath = f'.github/instructions/{self.name}.instructions.md'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ {self.name}.instructions.md")
    
    def create_detail_files(self, categories):
        """Create patterns.md, reference.md, and organized references/"""
        skill_dir = f'.github/copilot-skills/{self.name}'
        os.makedirs(f'{skill_dir}/references', exist_ok=True)
        os.makedirs(f'{skill_dir}/scripts', exist_ok=True)
        os.makedirs(f'{skill_dir}/assets', exist_ok=True)
        
        # Create patterns.md (quick reference patterns)
        self.create_patterns_file(categories, skill_dir)
        
        # Create reference.md (overview of all docs)
        self.create_reference_overview(categories, skill_dir)
        
        # Create organized references/ (categorized docs)
        self.create_reference_files(categories, skill_dir)
    
    def create_patterns_file(self, categories, skill_dir):
        """Create patterns.md with common code patterns"""
        # Collect patterns from all pages
        all_patterns = []
        for pages in categories.values():
            for page in pages[:10]:
                all_patterns.extend(page.get('patterns', []))
        
        # Get best code examples
        examples = []
        for pages in categories.values():
            for page in pages[:10]:
                for sample in page.get('code_samples', [])[:2]:
                    if sample.get('language') != 'text' and len(sample['code']) < 400:
                        examples.append(sample)
                    if len(examples) >= 10:
                        break
                if len(examples) >= 10:
                    break
            if len(examples) >= 10:
                break
        
        content = f"""# {self.name.title()} - Common Patterns

Quick reference for common {self.name} patterns and usage.

## Code Patterns

"""
        
        # Add patterns
        for i, pattern in enumerate(all_patterns[:8], 1):
            content += f"### {i}. {pattern.get('description', 'Common pattern')[:100]}\n\n"
            code = pattern.get('code', '')
            if code:
                content += f"```\n{code[:300]}\n```\n\n"
        
        # Add examples
        if examples:
            content += "## Examples\n\n"
            for i, ex in enumerate(examples, 1):
                lang = ex.get('language', 'text')
                content += f"### Example {i}\n\n"
                content += f"```{lang}\n{ex['code'][:400]}\n```\n\n"
        
        content += f"""
## Categories

See organized documentation in `references/`:

"""
        
        for cat in sorted(categories.keys()):
            content += f"- `references/{cat}.md` - {cat.replace('_', ' ').title()}\n"
        
        with open(f'{skill_dir}/patterns.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ patterns.md")
    
    def create_reference_overview(self, categories, skill_dir):
        """Create reference.md with documentation overview"""
        content = f"""# {self.name.title()} - Reference Documentation

Comprehensive {self.name} documentation extracted from official sources.

## Overview

This reference includes documentation organized into the following categories:

"""
        
        for cat, pages in sorted(categories.items()):
            content += f"### {cat.replace('_', ' ').title()}\n\n"
            content += f"**File**: `references/{cat}.md`  \n"
            content += f"**Pages**: {len(pages)}\n\n"
            content += "**Topics**:\n"
            for page in pages[:5]:
                content += f"- {page['title']}\n"
            if len(pages) > 5:
                content += f"- *...and {len(pages) - 5} more*\n"
            content += "\n"
        
        content += f"""
## How to Use

### Navigation
Each category file in `references/` contains:
- Page titles and URLs
- Table of contents from headings
- Content summaries
- Code examples with language tags

### Finding Information
1. Check category that matches your topic
2. Scan table of contents
3. Read relevant sections
4. Copy code examples as needed

### Common Patterns
See `patterns.md` for frequently used code patterns.

## Source

- **Base URL**: {self.config['base_url']}
- **Generated**: {time.strftime("%Y-%m-%d")}
"""
        
        with open(f'{skill_dir}/reference.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ reference.md")
    
    def create_reference_files(self, categories, skill_dir):
        """Create categorized reference files in references/"""
        
        for cat, pages in categories.items():
            lines = []
            lines.append(f"# {self.name.title()} - {cat.replace('_', ' ').title()}\n")
            lines.append(f"**Pages**: {len(pages)}\n")
            lines.append("---\n")
            
            for page in pages:
                lines.append(f"## {page['title']}\n")
                lines.append(f"**URL**: {page['url']}\n")
                
                # TOC from headings
                if page.get('headings'):
                    lines.append("**Contents**:")
                    for h in page['headings'][:8]:
                        level = int(h['level'][1])
                        indent = "  " * max(0, level - 2)
                        lines.append(f"{indent}- {h['text']}")
                    lines.append("")
                
                # Content
                if page.get('content'):
                    content = page['content'][:2000]
                    if len(page['content']) > 2000:
                        content += "\n\n*[Content truncated - see full docs]*"
                    lines.append(content)
                    lines.append("")
                
                # Code examples
                if page.get('code_samples'):
                    lines.append("**Examples**:\n")
                    for i, sample in enumerate(page['code_samples'][:3], 1):
                        lang = sample.get('language', 'text')
                        code = sample.get('code', '')
                        lines.append(f"```{lang}")
                        lines.append(code[:500])
                        if len(code) > 500:
                            lines.append("...")
                        lines.append("```\n")
                
                lines.append("---\n")
            
            filepath = f'{skill_dir}/references/{cat}.md'
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            
            print(f"  ✓ references/{cat}.md")


def main():
    parser = argparse.ArgumentParser(description='Convert documentation to Copilot Skill')
    parser.add_argument('--config', help='Config file path')
    parser.add_argument('--interactive', action='store_true', help='Interactive config creation')
    parser.add_argument('--dry-run', action='store_true', help='Preview without scraping')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint')
    parser.add_argument('--build-only', action='store_true', help='Build skill from existing data')
    
    args = parser.parse_args()
    
    if args.interactive:
        print("Interactive mode not yet implemented")
        print("Please create a config file manually")
        return 1
    
    if not args.config:
        print("Error: --config required")
        print("Usage: python3 scrape_docs.py --config configs/shadcn.json")
        return 1
    
    # Load config
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return 1
    
    # Create converter
    converter = DocsToCopilotSkill(config, dry_run=args.dry_run, resume=args.resume)
    
    # Build-only mode
    if args.build_only:
        return 0 if converter.build_skill() else 1
    
    # Scrape
    converter.scrape_all()
    
    # Build skill
    if not args.dry_run:
        converter.build_skill()
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
