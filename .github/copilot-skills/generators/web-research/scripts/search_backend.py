#!/usr/bin/env python3
"""
Web Research - Search Backend
Discovers authoritative documentation sources using multiple strategies
Uses DuckDuckGo search (no API key required) inspired by gpt-researcher
"""

import requests
from urllib.parse import quote, urljoin
from typing import List, Dict, Optional
import os
import json

class SearchBackend:
    """Multi-backend search with graceful fallback to DuckDuckGo"""
    
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        self.timeout = 10
        
        # Check for available API keys
        self.tavily_key = os.getenv('TAVILY_API_KEY')
        self.serper_key = os.getenv('SERPER_API_KEY')
    
    def search_tavily(self, query: str, limit: int = 10) -> List[Dict]:
        """Search using Tavily API (requires API key)"""
        if not self.tavily_key:
            return []
        
        print(f"   → Querying Tavily API...")
        try:
            url = "https://api.tavily.com/search"
            headers = {"Content-Type": "application/json"}
            data = {
                "api_key": self.tavily_key,
                "query": query,
                "search_depth": "basic",
                "max_results": limit
            }
            
            response = requests.post(url, json=data, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            results = response.json()
            result_list = [
                {
                    'url': result['url'],
                    'title': result['title'],
                    'snippet': result['content'][:150],
                    'source': 'tavily',
                    'tier': 1
                }
                for result in results.get('results', [])
            ]
            print(f"   ✓ Tavily returned {len(result_list)} results")
            return result_list
        
        except Exception as e:
            print(f"   ⚠ Tavily search failed: {str(e)[:50]}")
            return []
    
    def search_serper(self, query: str, limit: int = 10) -> List[Dict]:
        """Search using Serper API (requires API key)"""
        if not self.serper_key:
            return []
        
        print(f"   → Querying Serper (Google) API...")
        try:
            url = "https://google.serper.dev/search"
            headers = {
                'X-API-KEY': self.serper_key,
                'Content-Type': 'application/json'
            }
            data = {"q": query, "num": limit}
            
            response = requests.post(url, json=data, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            results = response.json()
            result_list = [
                {
                    'url': result['link'],
                    'title': result['title'],
                    'snippet': result.get('snippet', '')[:150],
                    'source': 'serper',
                    'tier': 1
                }
                for result in results.get('organic', [])
            ]
            print(f"   ✓ Serper returned {len(result_list)} results")
            return result_list
        
        except Exception as e:
            print(f"   ⚠ Serper search failed: {str(e)[:50]}")
            return []
    
    def search_duckduckgo(self, query: str, limit: int = 10) -> List[Dict]:
        """Search using DuckDuckGo HTML endpoint (no API key required)"""
        results = []
        
        print(f"   → Querying DuckDuckGo...")
        try:
            from bs4 import BeautifulSoup
            
            # DuckDuckGo HTML search endpoint
            url = "https://duckduckgo.com/html"
            params = {"q": query}
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "DNT": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1"
            }
            
            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            # Parse results from HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find result links - DuckDuckGo uses <a class="result__a">
            for result in soup.find_all('a', {'class': 'result__a'})[:limit]:
                href = result.get('href', '')
                if isinstance(href, str) and href and not href.startswith('javascript'):
                    title = result.get_text(strip=True)
                    
                    # Extract actual URL from DuckDuckGo redirect
                    if 'uddg=' in href:
                        try:
                            from urllib.parse import urlparse, parse_qs
                            parsed = urlparse(href)
                            actual_url = parse_qs(parsed.query).get('uddg', [href])[0]
                            href = actual_url
                        except:
                            pass
                    
                    # Skip if still a relative URL
                    if not href.startswith('http'):
                        continue
                    
                    results.append({
                        'url': href,
                        'title': title[:100],
                        'snippet': '',
                        'source': 'duckduckgo',
                        'tier': 2
                    })
            
            print(f"   ✓ DuckDuckGo returned {len(results)} results")
        
        except Exception as e:
            print(f"   ⚠ DuckDuckGo search failed: {str(e)[:50]}")
        
        return results
    
    def search_github(self, query: str, limit: int = 5) -> List[Dict]:
        """Search GitHub repositories (no auth required for basic search)"""
        results = []
        
        print(f"   → Querying GitHub API...")
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": f"{query} language:markdown language:json",
                "sort": "stars",
                "per_page": limit
            }
            headers = {"User-Agent": self.user_agent}
            
            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            for item in data.get('items', []):
                results.append({
                    'url': item['html_url'],
                    'title': item['full_name'],
                    'description': item.get('description', ''),
                    'source': 'github',
                    'stars': item['stargazers_count']
                })
            
            print(f"   ✓ GitHub returned {len(results)} repositories")
        
        except Exception as e:
            print(f"   ⚠ GitHub search failed: {str(e)[:50]}")
        
        return results
    
    def discover_sources(self, query: str) -> List[Dict]:
        """Discover all relevant sources for query"""
        all_results = []
        
        # Try premium search APIs first (if API keys available)
        if self.tavily_key:
            tavily = self.search_tavily(query, limit=10)
            all_results.extend(tavily)
        
        if self.serper_key:
            serper = self.search_serper(query, limit=10)
            all_results.extend(serper)
        
        # Always search DuckDuckGo as fallback or supplement
        ddg = self.search_duckduckgo(query, limit=10)
        all_results.extend(ddg)
        
        github = self.search_github(query, limit=5)
        all_results.extend(github)
        
        # Deduplicate by domain
        seen_domains = set()
        unique_results = []
        
        for result in sorted(all_results, key=lambda x: x.get('tier', 3)):
            try:
                domain = result['url'].split('/')[2]
                if domain not in seen_domains:
                    seen_domains.add(domain)
                    unique_results.append(result)
            except (IndexError, KeyError):
                continue
        
        return unique_results[:15]  # Return top 15 unique sources
