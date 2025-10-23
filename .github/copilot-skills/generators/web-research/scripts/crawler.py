#!/usr/bin/env python3
"""
Web Research - Crawler
Scrapes and extracts content from discovered sources
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Optional
from collections import deque
import time

class WebCrawler:
    """Crawl documentation sources and extract content"""
    
    def __init__(self, base_url: str, max_pages: int = 50):
        self.base_url = base_url
        self.max_pages = max_pages
        self.visited_urls = set()
        self.pending_urls = deque([base_url])
        self.pages = []
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        self.timeout = 10
    
    def is_valid_url(self, url: str) -> bool:
        """Check if URL is valid for crawling"""
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        
        # Same domain check
        if parsed.netloc != base_parsed.netloc:
            return False
        
        # Avoid problematic paths
        blocked_patterns = ['.pdf', '.jpg', '.png', '.zip', '/search', '/login', '/admin']
        if any(pattern in url for pattern in blocked_patterns):
            return False
        
        return True
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a single page"""
        try:
            headers = {"User-Agent": self.user_agent}
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            return BeautifulSoup(response.content, 'html.parser')
        
        except Exception as e:
            print(f"   ⚠ Failed to fetch {url}: {str(e)[:50]}")
            return None
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract structured content from page"""
        page = {
            'url': url,
            'title': '',
            'content': '',
            'headings': [],
            'code_samples': [],
            'links': []
        }
        
        # Extract title
        title_elem = soup.find('h1') or soup.find('title')
        if title_elem:
            page['title'] = title_elem.get_text(strip=True)[:100]
        
        # Find main content
        main = soup.find('main') or soup.find('article') or soup.find('div', {'class': 'content'})
        if not main:
            main = soup.find('body')
        
        if main:
            # Extract headings
            for h in main.find_all(['h2', 'h3']):
                page['headings'].append(h.get_text(strip=True))
            
            # Extract code samples
            for code in main.find_all('code'):
                code_text = code.get_text(strip=True)
                if len(code_text) > 10:  # Only meaningful code
                    page['code_samples'].append(code_text[:200])
            
            # Extract paragraphs
            paragraphs = []
            for p in main.find_all('p'):
                text = p.get_text(strip=True)
                if len(text) > 20:
                    paragraphs.append(text[:200])
            
            page['content'] = ' '.join(paragraphs[:5])  # First 5 paragraphs
            
            # Extract links
            for a in main.find_all('a', href=True):
                href = a.get('href', '')
                text = a.get_text(strip=True)
                if href and text:
                    page['links'].append({'url': href, 'text': text})
        
        return page
    
    def crawl(self, max_depth: int = 2) -> List[Dict]:
        """Crawl site with BFS"""
        depth = 0
        pages_at_depth = {0: 1}
        
        while self.pending_urls and len(self.visited_urls) < self.max_pages:
            url = self.pending_urls.popleft()
            
            if url in self.visited_urls:
                continue
            
            self.visited_urls.add(url)
            
            # Track depth
            if len(self.visited_urls) > sum(pages_at_depth.get(d, 0) for d in range(depth + 1)):
                depth += 1
            
            if depth > max_depth:
                continue
            
            print(f"   Crawling ({len(self.visited_urls)}/{self.max_pages}): {url[:60]}")
            
            soup = self.fetch_page(url)
            if not soup:
                continue
            
            # Extract content
            page = self.extract_content(soup, url)
            self.pages.append(page)
            
            # Discover new links
            for link in page['links'][:5]:  # Limit links per page
                new_url = urljoin(self.base_url, link['url'])
                if self.is_valid_url(new_url) and new_url not in self.visited_urls:
                    self.pending_urls.append(new_url)
            
            # Rate limiting
            time.sleep(0.5)
        
        return self.pages
