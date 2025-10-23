#!/usr/bin/env python3
"""
scrape_docs.py - Scrape documentation websites and generate Copilot Skills

Simplified version that actually works for static HTML documentation.
"""

import json
import sys
import time
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from urllib.parse import urljoin, urlparse
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Required packages not installed")
    print("Install with: pip install requests beautifulsoup4")
    sys.exit(1)


class DocsToSkillScraper:
    def __init__(self, config_path: str):
        """Initialize scraper with configuration"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.name = self.config['name']
        self.base_url = self.config['base_url']
        self.max_pages = self.config.get('max_pages', 100)
        self.rate_limit = self.config.get('rate_limit', 0.5)
        
        # Setup paths
        self.workspace_root = Path(__file__).parent.parent.parent.parent.parent
        self.skill_dir = self.workspace_root / '.github' / 'copilot-skills' / self.name
        self.output_dir = self.skill_dir / 'references'
        
        self.pages_scraped: Dict[str, Dict] = {}
        self.urls_visited: Set[str] = set()
        self.errors: List[str] = []
        
        print(f"🔧 Scraper Configuration:")
        print(f"  Name: {self.name}")
        print(f"  Base URL: {self.base_url}")
        print(f"  Max Pages: {self.max_pages}")
        print(f"  Rate Limit: {self.rate_limit}s")
        print(f"  Output: {self.skill_dir}")
    
    def should_include_url(self, url: str) -> bool:
        """Check if URL matches include/exclude patterns"""
        patterns = self.config.get('url_patterns', {})
        
        # Check exclude patterns
        for pattern in patterns.get('exclude', []):
            if re.search(pattern, url):
                return False
        
        # Check include patterns
        include_patterns = patterns.get('include', [])
        if include_patterns:
            for pattern in include_patterns:
                if re.search(pattern, url):
                    return True
            return False
        
        return True
    
    def extract_content(self, html: str, url: str) -> Dict:
        """Extract content from HTML using configured selectors"""
        soup = BeautifulSoup(html, 'html.parser')
        selectors = self.config.get('selectors', {})
        
        # Extract title
        title = "Untitled"
        for selector in selectors.get('title', ['h1', 'title']).split(', '):
            elem = soup.select_one(selector)
            if elem:
                title = elem.get_text(strip=True)
                break
        
        # Extract main content
        content = ""
        for selector in selectors.get('main_content', ['main', 'article']).split(', '):
            elem = soup.select_one(selector)
            if elem:
                content = elem.get_text(separator='\n', strip=True)
                break
        
        # Extract code blocks
        code_blocks = []
        for selector in selectors.get('code_blocks', ['pre code']).split(', '):
            for elem in soup.select(selector):
                code_blocks.append(elem.get_text())
        
        # Extract headings for TOC
        headings = []
        for h in soup.select('h1, h2, h3, h4, h5, h6'):
            level = int(h.name[1])
            headings.append({
                'level': level,
                'text': h.get_text(strip=True)
            })
        
        return {
            'title': title,
            'url': url,
            'content': content,
            'code_blocks': code_blocks,
            'headings': headings,
            'timestamp': datetime.now().isoformat()
        }
    
    def scrape_page(self, url: str) -> Optional[Tuple[Dict, List[str]]]:
        """Scrape a single page and return (page_data, links) or None"""
        if url in self.urls_visited:
            return None
        
        if not self.should_include_url(url):
            return None
        
        self.urls_visited.add(url)
        
        try:
            print(f"  📄 Scraping: {url}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            page_data = self.extract_content(response.text, url)
            
            # Find links to other pages
            soup = BeautifulSoup(response.text, 'html.parser')
            links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                
                # Remove fragments
                full_url = full_url.split('#')[0]
                
                # Check if URL is within scope
                if full_url.startswith(self.base_url.rstrip('/').split('/docs')[0]):
                    if self.should_include_url(full_url):
                        links.append(full_url)
            
            time.sleep(self.rate_limit)
            return (page_data, links)
            
        except Exception as e:
            error_msg = f"Error scraping {url}: {str(e)}"
            print(f"    ❌ {error_msg}")
            self.errors.append(error_msg)
            return None
    
    def categorize_page(self, title: str, url: str, content: str) -> str:
        """Categorize page based on content and keywords"""
        categories = self.config.get('categories', {})
        
        search_text = f"{title} {url} {content}".lower()
        
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in search_text:
                    return category
        
        return 'reference'
    
    def dry_run(self):
        """Preview pages without scraping"""
        print("\n🔍 DRY RUN - Previewing pages to scrape")
        print("=" * 60)
        
        try:
            start_url = self.config.get('start_url', self.base_url)
            response = requests.get(start_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = set()
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(start_url, href)
                full_url = full_url.split('#')[0]
                
                if self.should_include_url(full_url):
                    links.add(full_url)
            
            print(f"\n📊 Preview Results:")
            print(f"  Found ~{min(len(links), self.max_pages)} pages")
            print(f"  Will scrape up to: {self.max_pages} pages")
            print(f"  Rate limit: {self.rate_limit}s between requests")
            print(f"  Estimated time: {(self.max_pages * self.rate_limit / 60):.1f} minutes")
            
            print(f"\n📑 Sample URLs (first 10):")
            for url in sorted(links)[:10]:
                print(f"    • {url}")
            
            print(f"\n✅ Dry run complete. Ready to scrape!")
            
        except Exception as e:
            print(f"❌ Dry run error: {e}")
    
    def run(self):
        """Execute scraper"""
        print(f"\n🕷️  Starting scrape of {self.name} documentation")
        print("=" * 60)
        
        # Setup output directories
        self.skill_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Scrape pages
        to_visit = [self.config.get('start_url', self.base_url)]
        checkpoint_count = 0
        
        while to_visit and len(self.pages_scraped) < self.max_pages:
            url = to_visit.pop(0)
            
            result = self.scrape_page(url)
            if result:
                page_data, links = result
                self.pages_scraped[url] = page_data
                
                # Add new links to visit
                for link in links:
                    if link not in self.urls_visited:
                        to_visit.append(link)
                
                checkpoint_count += 1
                if self.config.get('checkpoint', {}).get('enabled') and \
                   checkpoint_count >= self.config['checkpoint'].get('interval', 50):
                    print(f"\n💾 Checkpoint: Scraped {len(self.pages_scraped)} pages")
                    checkpoint_count = 0
        
        print(f"\n✅ Scraped {len(self.pages_scraped)} pages")
        
        # Generate skill files
        if self.pages_scraped:
            print(f"\n📝 Generating skill files...")
            self.generate_skill_files()
        else:
            print(f"⚠️  No pages scraped. Check URL patterns and site accessibility.")
        
        print(f"\n✅ Complete!")
        print(f"Location: {self.skill_dir}")
    
    def generate_skill_files(self):
        """Generate Copilot Skill files"""
        # Group pages by category
        categories = {}
        for url, page_data in self.pages_scraped.items():
            category = self.categorize_page(
                page_data['title'],
                url,
                page_data['content'][:200]
            )
            if category not in categories:
                categories[category] = []
            categories[category].append((url, page_data))
        
        # Generate reference files for each category
        for category, pages in sorted(categories.items()):
            self.generate_reference_file(category, pages)
        
        # Generate index
        self.generate_reference_index(categories)
        
        # Generate skill prompt
        self.generate_skill_prompt(categories)
        
        # Generate instructions
        self.generate_instructions()
    
    def generate_reference_file(self, category: str, pages: List):
        """Generate a reference file for a category"""
        filepath = self.output_dir / f"{category}.md"
        
        with open(filepath, 'w') as f:
            f.write(f"# {category.replace('_', ' ').title()}\n\n")
            
            for url, page_data in pages:
                f.write(f"## {page_data['title']}\n\n")
                f.write(f"**Source**: [{url}]({url})\n\n")
                
                if page_data.get('headings'):
                    f.write("**Topics**:\n")
                    for heading in page_data['headings'][:5]:
                        indent = "  " * max(0, heading['level'] - 2)
                        f.write(f"{indent}• {heading['text']}\n")
                    f.write("\n")
                
                if page_data.get('content'):
                    f.write("**Summary**:\n")
                    summary = page_data['content'][:300].strip()
                    f.write(f"{summary}...\n\n")
                
                f.write("---\n\n")
    
    def generate_reference_index(self, categories: Dict):
        """Generate reference overview"""
        filepath = self.skill_dir / 'reference.md'
        
        with open(filepath, 'w') as f:
            f.write(f"# {self.name.title()} - Reference\n\n")
            f.write(f"{self.config['description']}\n\n")
            
            f.write("## Documentation Categories\n\n")
            for category in sorted(categories.keys()):
                count = len(categories[category])
                f.write(f"- **{category.replace('_', ' ').title()}**: {count} pages\n")
            
            f.write(f"\n**Total Pages**: {len(self.pages_scraped)}\n")
            f.write(f"**Generated**: {datetime.now().isoformat()}\n")
    
    def generate_skill_prompt(self, categories: Dict):
        """Generate skill prompt file"""
        filepath = self.workspace_root / '.github' / 'prompts' / f"{self.name}.skill.prompt.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            f.write(f"# {self.name.title()}\n\n")
            f.write(f"**Purpose**: {self.config['description']}\n\n")
            
            f.write("## When to Use This Skill\n\n")
            f.write(f"Use this skill when working with {self.name}:\n")
            for category in sorted(categories.keys()):
                f.write(f"- {category.replace('_', ' ')}\n")
            
            f.write("\n## Reference\n\n")
            f.write(f"Full documentation: `.github/copilot-skills/{self.name}/`\n")
            f.write(f"\nCategories: {', '.join(sorted(categories.keys()))}\n")
    
    def generate_instructions(self):
        """Generate instructions file"""
        filepath = self.workspace_root / '.github' / 'instructions' / f"{self.name}.instructions.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            f.write(f"# {self.name.title()} Instructions\n\n")
            f.write(f"Auto-loaded when editing {self.name}-related files.\n\n")
            
            f.write("## File Patterns\n\n")
            for pattern in self.config.get('file_patterns', []):
                f.write(f"- `{pattern}`\n")
            
            f.write(f"\n## Documentation\n\n")
            f.write(f"See `.github/copilot-skills/{self.name}/` for complete reference.\n")


def main():
    if '--help' in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return 1
    
    config_path = None
    if '--config' in sys.argv:
        idx = sys.argv.index('--config')
        if idx + 1 < len(sys.argv):
            config_path = sys.argv[idx + 1]
    
    if not config_path:
        print("❌ --config parameter required")
        return 1
    
    scraper = DocsToSkillScraper(config_path)
    
    if '--dry-run' in sys.argv:
        scraper.dry_run()
        return 0
    
    scraper.run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
