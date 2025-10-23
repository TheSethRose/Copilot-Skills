#!/usr/bin/env python3
"""
scrape_docs_dynamic.py - Scrape JavaScript-rendered documentation sites

Uses Playwright to handle dynamic/SPA documentation sites (Next.js, Gatsby, etc.)
Captures fully rendered HTML for content extraction.

Usage:
    python3 scrape_docs_dynamic.py --config configs/bun.json --dry-run
    python3 scrape_docs_dynamic.py --config configs/bun.json
    python3 scrape_docs_dynamic.py --config configs/bun.json --headless
    python3 scrape_docs_dynamic.py --config configs/bun.json --debug
"""

import json
import sys
import time
import re
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from urllib.parse import urljoin, urlparse
from datetime import datetime

try:
    from playwright.async_api import async_playwright, Browser, Page
    import asyncio
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Required packages not installed")
    print("Install with: pip install playwright beautifulsoup4")
    print("Then: playwright install chromium")
    sys.exit(1)


class DynamicDocsToSkillScraper:
    def __init__(self, config_path: str, headless: bool = True, debug: bool = False):
        """Initialize scraper for dynamic sites"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.name = self.config['name']
        self.base_url = self.config['base_url']
        self.max_pages = self.config.get('max_pages', 100)
        self.rate_limit = self.config.get('rate_limit', 0.5)
        self.headless = headless
        self.debug = debug
        
        # Setup paths
        self.workspace_root = Path(__file__).parent.parent.parent.parent.parent
        self.skill_dir = self.workspace_root / '.github' / 'copilot-skills' / self.name
        self.output_dir = self.skill_dir / 'references'
        self.cache_file = self.skill_dir / '.scrape_cache.json'
        
        self.pages_scraped: Dict[str, Dict] = {}
        self.urls_visited: Set[str] = set()
        self.errors: List[str] = []
        
        self.browser: Optional[Browser] = None
        
        print(f"🔧 Dynamic Scraper Configuration:")
        print(f"  Name: {self.name}")
        print(f"  Base URL: {self.base_url}")
        print(f"  Max Pages: {self.max_pages}")
        print(f"  Rate Limit: {self.rate_limit}s")
        print(f"  Headless: {self.headless}")
        print(f"  Debug: {self.debug}")
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
    
    async def scrape_page(self, page: Page, url: str) -> Optional[Tuple[Dict, List[str]]]:
        """Scrape a single page with JavaScript rendering"""
        if url in self.urls_visited:
            return None
        
        if not self.should_include_url(url):
            return None
        
        self.urls_visited.add(url)
        
        try:
            print(f"  📄 Scraping: {url}")
            
            # Navigate to page
            await page.goto(url, wait_until='networkidle', timeout=30000)
            
            # Wait for main content to load
            selectors = self.config.get('selectors', {})
            main_selector = selectors.get('main_content', 'main')
            try:
                await page.wait_for_selector(main_selector, timeout=5000)
            except:
                print(f"    ⚠️  Main content selector not found, using full page")
            
            # Get rendered HTML
            html = await page.content()
            
            # Extract content
            page_data = self.extract_content(html, url)
            
            # Find links (from rendered page)
            link_elements = await page.query_selector_all('a[href]')
            links = []
            for elem in link_elements:
                href = await elem.get_attribute('href')
                if href:
                    full_url = urljoin(url, href)
                    full_url = full_url.split('#')[0]
                    
                    if full_url.startswith(self.base_url.split('/docs')[0]):
                        links.append(full_url)
            
            await asyncio.sleep(self.rate_limit)
            return page_data, links
            
        except Exception as e:
            error_msg = f"Error scraping {url}: {str(e)}"
            print(f"    ❌ {error_msg}")
            self.errors.append(error_msg)
            return None
    
    def extract_content(self, html: str, url: str) -> Dict:
        """Extract content from rendered HTML"""
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
    
    async def dry_run_async(self):
        """Preview pages without scraping (async)"""
        print("\n🔍 DRY RUN - Previewing pages to scrape")
        print("=" * 60)
        
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                
                start_url = self.config.get('start_url', self.base_url)
                await page.goto(start_url, wait_until='networkidle', timeout=30000)
                
                # Get all links
                link_elements = await page.query_selector_all('a[href]')
                links = set()
                
                for elem in link_elements:
                    href = await elem.get_attribute('href')
                    if href:
                        full_url = urljoin(self.base_url, href)
                        full_url = full_url.split('#')[0]
                        
                        if self.should_include_url(full_url):
                            links.add(full_url)
                
                print(f"\n📊 Preview Results:")
                print(f"  Found ~{min(len(links), self.max_pages)} pages")
                print(f"  Will scrape up to: {self.max_pages} pages")
                print(f"  Rate limit: {self.rate_limit}s between requests")
                estimated_minutes = (self.max_pages * self.rate_limit / 60)
                print(f"  Estimated time: {estimated_minutes:.1f} minutes")
                
                print(f"\n📑 Sample URLs (first 10):")
                for url in sorted(links)[:10]:
                    print(f"    • {url}")
                
                print(f"\n✅ Dry run complete. Ready to scrape!")
                
                await browser.close()
                
        except Exception as e:
            print(f"❌ Dry run error: {e}")
    
    async def run_async(self):
        """Execute scraper asynchronously"""
        print(f"\n🕷️  Starting dynamic scrape of {self.name} documentation")
        print("=" * 60)
        
        # Setup output directories
        self.skill_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            
            to_visit = [self.config.get('start_url', self.base_url)]
            checkpoint_count = 0
            
            while to_visit and len(self.pages_scraped) < self.max_pages:
                url = to_visit.pop(0)
                page = await browser.new_page()
                
                try:
                    result = await self.scrape_page(page, url)
                    if result:
                        page_data, links = result
                        self.pages_scraped[url] = page_data
                        to_visit.extend([link for link in links if link not in self.urls_visited])
                        
                        checkpoint_count += 1
                        if self.config.get('checkpoint', {}).get('enabled') and \
                           checkpoint_count >= self.config['checkpoint'].get('interval', 50):
                            print(f"\n💾 Checkpoint: Scraped {len(self.pages_scraped)} pages")
                            checkpoint_count = 0
                finally:
                    await page.close()
            
            await browser.close()
        
        print(f"\n✅ Scraped {len(self.pages_scraped)} pages")
        
        # Generate skill files
        print(f"\n📝 Generating skill files...")
        self.generate_skill_files()
        
        print(f"\n✅ Skill generation complete!")
        print(f"Location: {self.skill_dir}")
    
    def categorize_page(self, title: str, url: str, content: str) -> str:
        """Categorize page based on content and keywords"""
        categories = self.config.get('categories', {})
        
        search_text = f"{title} {url} {content}".lower()
        
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in search_text:
                    return category
        
        return 'reference'
    
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
        for category, pages in categories.items():
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
                f.write(f"**URL**: {url}\n\n")
                
                if page_data.get('headings'):
                    f.write("**Topics**:\n")
                    for heading in page_data['headings'][:5]:
                        indent = "  " * (heading['level'] - 1)
                        f.write(f"{indent}• {heading['text']}\n")
                    f.write("\n")
                
                if page_data.get('code_blocks'):
                    f.write("**Code Examples**:\n```\n")
                    for code in page_data['code_blocks'][:2]:
                        f.write(code[:200] + "\n...\n")
                    f.write("```\n\n")
                
                # First 500 chars of content
                if page_data.get('content'):
                    f.write("**Summary**:\n")
                    f.write(page_data['content'][:500] + "...\n\n")
                
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
            
            f.write(f"\nTotal Pages: {len(self.pages_scraped)}\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Method: Playwright (JavaScript-rendered sites)\n")
    
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
            
            f.write("\n## Quick Reference\n\n")
            f.write("### Categories\n\n")
            for category in sorted(categories.keys()):
                count = len(categories[category])
                f.write(f"- **{category}**: {count} documentation pages\n")
            
            f.write("\n## Reference Documentation\n\n")
            f.write(f"Complete documentation available in `.github/copilot-skills/{self.name}/references/`\n")
            f.write(f"\nTotal pages: {len(self.pages_scraped)}\n")
    
    def generate_instructions(self):
        """Generate instructions file"""
        filepath = self.workspace_root / '.github' / 'instructions' / f"{self.name}.instructions.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            f.write(f"# {self.name.title()} Instructions\n\n")
            f.write(f"Auto-loaded context when editing {self.name}-related files.\n\n")
            
            f.write("## Quick Start\n\n")
            f.write("```bash\n")
            f.write(f"# Find documentation in\n")
            f.write(f".github/copilot-skills/{self.name}/\n")
            f.write("```\n\n")
            
            f.write("## File Patterns\n\n")
            for pattern in self.config.get('file_patterns', []):
                f.write(f"- `{pattern}`\n")
            
            f.write("\n## Documentation Reference\n\n")
            f.write(f"See `.github/copilot-skills/{self.name}/reference.md` for overview.\n")
            f.write(f"\n**Generated from**: {self.config['base_url']}\n")
            f.write(f"**Method**: Playwright (JavaScript-rendered)\n")
    
    def run(self):
        """Sync wrapper for async run"""
        asyncio.run(self.run_async())
    
    def dry_run(self):
        """Sync wrapper for async dry-run"""
        asyncio.run(self.dry_run_async())


def main():
    if '--help' in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return 1
    
    config_path = None
    if '--config' in sys.argv:
        idx = sys.argv.index('--config')
        config_path = sys.argv[idx + 1]
    else:
        print("❌ --config parameter required")
        print(__doc__)
        return 1
    
    headless = '--headless' not in sys.argv  # Default: headless=True
    debug = '--debug' in sys.argv
    
    scraper = DynamicDocsToSkillScraper(config_path, headless=headless, debug=debug)
    
    if '--dry-run' in sys.argv:
        scraper.dry_run()
        return 0
    
    scraper.run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
