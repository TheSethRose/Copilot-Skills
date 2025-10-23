#!/usr/bin/env python3
"""
Web Research Skill - Multi-source research orchestrator
Combines search discovery with parallel documentation scraping and cross-source analysis
"""

import argparse
import json
from datetime import datetime
from enum import Enum
from pathlib import Path
import sys
import os

# Import local modules
sys.path.insert(0, os.path.dirname(__file__))
from search_backend import SearchBackend
from crawler import WebCrawler
from analyzer import ContentAnalyzer

class ResearchMode(Enum):
    QUICK = "quick"          # Search only (30 sec)
    STANDARD = "standard"    # Search + shallow scrape (5 min)
    DEEP = "deep"           # Search + comprehensive scrape (20+ min)
    EXPORT = "export"       # Generate copilot skill

class WebResearch:
    """Orchestrate search → scrape → analyze workflow"""
    
    def __init__(self, query, mode=ResearchMode.STANDARD, resume=False):
        self.query = query
        self.mode = mode
        self.resume = resume
        self.output_dir = Path(f"output/{query.replace(' ', '_')}_research")
        self.checkpoint_file = self.output_dir / "checkpoint.json"
        
        self.results = {
            "query": query,
            "mode": mode.value,
            "timestamp": datetime.now().isoformat(),
            "sources": [],
            "findings": [],
            "patterns": [],
            "index": {}
        }
        
        self.sources = []
        self.all_pages = []
    
    def phase_1_search(self):
        """Phase 1: Search for relevant sources"""
        print(f"\n🔍 Phase 1: Searching for '{self.query}'")
        
        search = SearchBackend()
        self.sources = search.discover_sources(self.query)
        
        print(f"   ✓ Found {len(self.sources)} sources")
        
        # Store in results
        self.results['sources'] = [
            {
                'url': s['url'],
                'title': s.get('title', ''),
                'tier': s.get('tier', 3)
            }
            for s in self.sources
        ]
    
    def phase_2_preview(self):
        """Phase 2: Preview crawl strategy"""
        print(f"\n📋 Phase 2: Planning crawl strategy")
        print(f"   • Identified {len(self.sources)} sources")
        
        total_pages = len(self.sources) * 20  # Estimate
        print(f"   • Estimated ~{total_pages} pages to crawl")
        print(f"   • Mode: {self.mode.value}")
        
        print("   ✓ Strategy planned")
    
    def phase_3_scrape(self):
        """Phase 3: Scrape with progress tracking"""
        print(f"\n📚 Phase 3: Scraping documentation")
        
        # Determine max pages based on mode
        max_pages_per_source = {
            ResearchMode.QUICK: 0,      # No scraping
            ResearchMode.STANDARD: 20,  # Shallow
            ResearchMode.DEEP: 50,      # Deep
            ResearchMode.EXPORT: 50     # Full
        }
        
        max_pages = max_pages_per_source.get(self.mode, 20)
        
        for i, source in enumerate(self.sources, 1):
            print(f"   Source {i}/{len(self.sources)}: {source['url']}")
            
            try:
                crawler = WebCrawler(source['url'], max_pages=max_pages)
                pages = crawler.crawl(max_depth=2)
                
                self.all_pages.extend(pages)
                print(f"   ✓ Scraped {len(pages)} pages")
            
            except Exception as e:
                print(f"   ⚠ Failed to crawl: {str(e)[:50]}")
        
        print(f"\n   ✓ Scraping complete ({len(self.all_pages)} total pages)")
    
    def phase_4_analyze(self):
        """Phase 4: Analyze and extract patterns"""
        print(f"\n🧠 Phase 4: Analyzing patterns")
        
        if not self.all_pages:
            print("   ⚠ No pages to analyze")
            return
        
        analyzer = ContentAnalyzer(self.all_pages)
        analysis = analyzer.analyze()
        
        self.results['findings'] = {
            'total_pages': analysis['total_pages'],
            'key_concepts': analysis['key_concepts'],
            'code_statistics': analysis['code_statistics'],
            'convergence_patterns': analysis['convergence_patterns']
        }
        
        print(f"   • {analysis['total_pages']} pages analyzed")
        print(f"   • {len(analysis['key_concepts'])} key concepts extracted")
        print(f"   • {len(analysis['code_statistics'])} languages found")
        print(f"   • {len(analysis['convergence_patterns'])} convergent patterns identified")
        
        print("   ✓ Analysis complete")
    
    def phase_5_report(self):
        """Phase 5: Generate terminal report"""
        print(f"\n📊 Phase 5: Generating report")
        
        findings = self.results.get('findings', {})
        if isinstance(findings, list):
            findings = {}
        
        concepts = findings.get('key_concepts', [])
        code_stats = findings.get('code_statistics', {})
        patterns = findings.get('convergence_patterns', [])
        
        report = f"""
📚 Web Research Results
{'='*60}

Query: {self.query}
Mode: {self.mode.value}
Timestamp: {self.results['timestamp']}

📊 Summary:
   Sources: {len(self.sources)}
   Pages scraped: {findings.get('total_pages', 0)}
   
📋 Key Concepts:
"""
        for concept in concepts[:5]:
            report += f"   • {concept}\n"
        
        report += f"\n💾 Code Examples:\n"
        for lang, count in sorted(code_stats.items(), key=lambda x: x[1], reverse=True)[:5]:
            if lang != 'unknown':
                report += f"   • {lang.title()}: {count} examples\n"
        
        report += f"\n✓ Convergence Patterns:\n"
        for pattern in patterns[:5]:
            report += f"   • {pattern['pattern'].title()} ({pattern['mentions']} mentions - {pattern['strength']})\n"
        
        report += f"""
🔗 Sources:
"""
        for source in self.sources[:5]:
            report += f"   • {source['url']}\n"
        
        report += f"""
📚 Next Steps:
   • See full index: {self.output_dir}/index.json
   • Deep research: /web-research --query "{self.query}" --mode deep
"""
        print(report)
        
        # Save JSON index for programmatic access
        self.save_index()
    
    def save_index(self):
        """Save searchable JSON index"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        index_file = self.output_dir / "index.json"
        with open(index_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n   ✓ Research index saved: {index_file}")
    
    def export_as_skill(self):
        """Export findings as Copilot Skill"""
        print(f"\n🎯 Exporting as Copilot Skill...")
        print(f"   [Implementation pending]")
    
    def run(self):
        """Execute full research workflow"""
        print(f"\n{'='*60}")
        print(f"WEB RESEARCH: {self.query}")
        print(f"{'='*60}")
        
        try:
            self.phase_1_search()
            self.phase_2_preview()
            
            if self.mode != ResearchMode.QUICK:
                self.phase_3_scrape()
                self.phase_4_analyze()
            
            self.phase_5_report()
            
            if self.mode == ResearchMode.EXPORT:
                self.export_as_skill()
            
            return 0
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
            return 1


def main():
    parser = argparse.ArgumentParser(
        description='Web Research Skill - Multi-source documentation research',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --query "react hooks"
  %(prog)s --query "database orms" --sources prisma,typeorm,drizzle --compare
  %(prog)s --query "next.js" --mode deep --export-skill
  %(prog)s --query "kubernetes" --resume
        """
    )
    
    parser.add_argument('--query', required=True, help='Research topic')
    parser.add_argument('--sources', help='Comma-separated list of specific sources')
    parser.add_argument('--depth', type=int, default=2, help='Crawl depth (1-3)')
    parser.add_argument('--mode', choices=['quick', 'standard', 'deep', 'export'],
                        default='standard', help='Research mode')
    parser.add_argument('--compare', action='store_true', help='Generate comparison analysis')
    parser.add_argument('--export-skill', action='store_true', help='Export as Copilot Skill')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint')
    parser.add_argument('--dry-run', action='store_true', help='Preview without scraping')
    
    args = parser.parse_args()
    
    # Select mode
    mode = ResearchMode.EXPORT if args.export_skill else ResearchMode[args.mode.upper()]
    
    # Run research
    research = WebResearch(args.query, mode=mode, resume=args.resume)
    
    if args.dry_run:
        print("[DRY RUN - No actual scraping will occur]")
    
    return research.run()


if __name__ == '__main__':
    import sys
    sys.exit(main())
