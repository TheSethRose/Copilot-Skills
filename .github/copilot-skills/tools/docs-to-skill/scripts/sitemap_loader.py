#!/usr/bin/env python3
"""
Sitemap loader module for documentation scraper.
Provides utilities to fetch and parse XML sitemaps.

Usage:
    from sitemap_loader import SitemapLoader
    
    loader = SitemapLoader("https://docs.example.com")
    urls = loader.get_urls(
        include_patterns=["^https://docs\\.example\\.com/en/.*"],
        exclude_patterns=["/blog/.*", "#.*"]
    )
"""

import re
import requests
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree as ET


class SitemapLoader:
    """Load and parse XML sitemaps to extract documentation URLs"""
    
    def __init__(self, base_url, timeout=10):
        """
        Initialize sitemap loader
        
        Args:
            base_url: Base URL of the documentation site
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.sitemap_urls = self._discover_sitemaps()
    
    def _discover_sitemaps(self):
        """Discover sitemap URLs from common locations"""
        sitemap_paths = [
            '/sitemap.xml',
            '/sitemap_index.xml',
            '/sitemap-index.xml',
            '/sitemap/sitemap.xml'
        ]
        
        discovered = []
        for path in sitemap_paths:
            sitemap_url = urljoin(self.base_url, path)
            try:
                response = requests.head(sitemap_url, timeout=self.timeout, allow_redirects=True)
                if response.status_code == 200:
                    discovered.append(sitemap_url)
            except Exception:
                continue
        
        # Try robots.txt for sitemap reference
        try:
            robots_url = urljoin(self.base_url, '/robots.txt')
            response = requests.get(robots_url, timeout=self.timeout)
            if response.status_code == 200:
                for line in response.text.split('\n'):
                    if line.lower().startswith('sitemap:'):
                        sitemap_url = line.split(':', 1)[1].strip()
                        if sitemap_url and sitemap_url not in discovered:
                            discovered.append(sitemap_url)
        except Exception:
            pass
        
        return discovered
    
    def _fetch_sitemap(self, sitemap_url):
        """Fetch and parse a sitemap XML file"""
        try:
            response = requests.get(sitemap_url, timeout=self.timeout)
            response.raise_for_status()
            return ET.fromstring(response.content)
        except Exception as e:
            print(f"  ⚠️  Failed to fetch {sitemap_url}: {e}")
            return None
    
    def _extract_urls_from_sitemap(self, root):
        """Extract URLs from sitemap XML"""
        urls = []
        
        # Handle namespace variations
        namespaces = {
            'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9',
            '': 'http://www.sitemaps.org/schemas/sitemap/0.9'
        }
        
        # Try to find URL elements with and without namespace
        for ns_prefix in ['sm:', '']:
            # Check for sitemap index (contains other sitemaps)
            for sitemap_elem in root.findall(f'.//{ns_prefix}sitemap', namespaces):
                loc_elem = sitemap_elem.find(f'{ns_prefix}loc', namespaces)
                if loc_elem is not None and loc_elem.text:
                    # Recursively fetch nested sitemap
                    nested_urls = self._fetch_and_parse_sitemap(loc_elem.text)
                    urls.extend(nested_urls)
            
            # Check for URL entries
            for url_elem in root.findall(f'.//{ns_prefix}url', namespaces):
                loc_elem = url_elem.find(f'{ns_prefix}loc', namespaces)
                if loc_elem is not None and loc_elem.text:
                    urls.append(loc_elem.text.strip())
        
        return urls
    
    def _fetch_and_parse_sitemap(self, sitemap_url):
        """Fetch a sitemap and extract all URLs"""
        root = self._fetch_sitemap(sitemap_url)
        if root is None:
            return []
        
        return self._extract_urls_from_sitemap(root)
    
    def get_urls(self, include_patterns=None, exclude_patterns=None, max_urls=None):
        """
        Get all URLs from discovered sitemaps with optional filtering
        
        Args:
            include_patterns: List of regex patterns - only URLs matching these will be included
            exclude_patterns: List of regex patterns - URLs matching these will be excluded
            max_urls: Maximum number of URLs to return (None for unlimited)
        
        Returns:
            List of filtered URLs
        """
        if not self.sitemap_urls:
            print("  ℹ️  No sitemaps discovered")
            return []
        
        print(f"  📍 Found {len(self.sitemap_urls)} sitemap(s)")
        
        all_urls = []
        for sitemap_url in self.sitemap_urls:
            print(f"     Parsing: {sitemap_url}")
            urls = self._fetch_and_parse_sitemap(sitemap_url)
            all_urls.extend(urls)
        
        print(f"  📄 Extracted {len(all_urls)} URLs from sitemap(s)")
        
        # Remove duplicates
        all_urls = list(set(all_urls))
        
        # Apply filters
        filtered_urls = []
        for url in all_urls:
            # Include patterns
            if include_patterns:
                if not any(re.search(pattern, url) for pattern in include_patterns):
                    continue
            
            # Exclude patterns
            if exclude_patterns:
                if any(re.search(pattern, url) for pattern in exclude_patterns):
                    continue
            
            filtered_urls.append(url)
            
            # Check max_urls limit
            if max_urls and len(filtered_urls) >= max_urls:
                break
        
        print(f"  ✅ {len(filtered_urls)} URLs after filtering")
        return filtered_urls
    
    @staticmethod
    def is_available(base_url, timeout=5):
        """
        Check if a site has an accessible sitemap
        
        Args:
            base_url: Base URL of the documentation site
            timeout: Request timeout in seconds
        
        Returns:
            True if sitemap is available, False otherwise
        """
        loader = SitemapLoader(base_url, timeout=timeout)
        return len(loader.sitemap_urls) > 0


# CLI usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python sitemap_loader.py <base_url> [include_pattern] [exclude_pattern]")
        print("\nExample:")
        print("  python sitemap_loader.py https://docs.claude.com '^https://docs\\.claude\\.com/en/.*' '/de/.*'")
        sys.exit(1)
    
    base_url = sys.argv[1]
    include = [sys.argv[2]] if len(sys.argv) > 2 else None
    exclude = [sys.argv[3]] if len(sys.argv) > 3 else None
    
    print(f"\n🔍 Loading sitemap from: {base_url}\n")
    
    loader = SitemapLoader(base_url)
    urls = loader.get_urls(include_patterns=include, exclude_patterns=exclude, max_urls=20)
    
    print(f"\n📋 Sample URLs ({min(20, len(urls))} of {len(urls)}):\n")
    for i, url in enumerate(urls[:20], 1):
        print(f"   {i}. {url}")
    
    if len(urls) > 20:
        print(f"\n   ... and {len(urls) - 20} more")
