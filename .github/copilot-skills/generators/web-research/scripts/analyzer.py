#!/usr/bin/env python3
"""
Web Research - Analyzer
Analyzes scraped content and extracts patterns
"""

from typing import List, Dict, Set
from collections import defaultdict
import re

class ContentAnalyzer:
    """Analyze scraped content for patterns"""
    
    def __init__(self, pages: List[Dict]):
        self.pages = pages
        self.patterns = []
        self.findings = []
    
    def detect_language(self, code: str) -> str:
        """Detect programming language from code"""
        if 'import React' in code or 'export default' in code or 'tsx' in code:
            return 'typescript'
        if 'import ' in code and 'from ' in code and '=' not in code[:20]:
            return 'python'
        if 'def ' in code and ':' in code:
            return 'python'
        if 'const ' in code or 'let ' in code or '=>' in code:
            return 'javascript'
        if '#include' in code or 'int main' in code:
            return 'cpp'
        if 'fn ' in code and '->' in code:
            return 'rust'
        if 'func ' in code:
            return 'go'
        
        return 'unknown'
    
    def extract_code_samples(self) -> List[Dict]:
        """Extract and categorize code samples"""
        samples = []
        lang_counts = defaultdict(int)
        
        for page in self.pages:
            for code in page.get('code_samples', []):
                lang = self.detect_language(code)
                lang_counts[lang] += 1
                
                samples.append({
                    'language': lang,
                    'code': code[:150],  # Truncate long code
                    'from_url': page['url']
                })
        
        return samples, dict(lang_counts)
    
    def extract_key_concepts(self) -> List[str]:
        """Extract key concepts from headings"""
        concepts = set()
        
        for page in self.pages:
            for heading in page.get('headings', []):
                # Capitalize and clean
                concept = heading.strip()
                if len(concept) > 5:
                    concepts.add(concept)
        
        return sorted(list(concepts))[:20]  # Top 20
    
    def find_convergence(self, threshold: int = 2) -> List[Dict]:
        """Find patterns mentioned in multiple sources"""
        pattern_mentions = defaultdict(list)
        
        all_text = ' '.join([
            page.get('content', '') + ' ' + ' '.join(page.get('headings', []))
            for page in self.pages
        ]).lower()
        
        # Common pattern keywords
        common_patterns = [
            'best practice', 'performance', 'optimization', 'security',
            'pattern', 'example', 'tutorial', 'guide', 'reference',
            'architecture', 'design', 'approach', 'strategy',
            'error handling', 'testing', 'validation', 'authentication'
        ]
        
        convergence = []
        for pattern in common_patterns:
            count = all_text.count(pattern)
            if count >= threshold:
                convergence.append({
                    'pattern': pattern,
                    'mentions': count,
                    'strength': 'strong' if count >= 5 else 'moderate'
                })
        
        return sorted(convergence, key=lambda x: x['mentions'], reverse=True)[:10]
    
    def analyze(self) -> Dict:
        """Run full analysis"""
        results = {
            'total_pages': len(self.pages),
            'key_concepts': self.extract_key_concepts(),
            'convergence_patterns': self.find_convergence(),
            'code_statistics': {},
            'code_samples': []
        }
        
        # Get code samples and language stats
        samples, lang_counts = self.extract_code_samples()
        results['code_samples'] = samples[:10]  # Top 10
        results['code_statistics'] = lang_counts
        
        return results
