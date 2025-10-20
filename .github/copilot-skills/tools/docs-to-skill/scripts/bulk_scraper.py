#!/usr/bin/env python3
"""
Bulk Documentation Scraper for UI Frameworks
Scrapes multiple documentation sites and generates Copilot Skills
"""

import sys
import json
import subprocess
import os
from pathlib import Path

# Frameworks to scrape
FRAMEWORKS = [
    {
        "name": "chakra-ui",
        "url": "https://chakra-ui.com/docs",
        "base_url": "https://chakra-ui.com/",
        "max_pages": 100
    },
    {
        "name": "material-ui",
        "url": "https://mui.com/material-ui/getting-started/overview/",
        "base_url": "https://mui.com/",
        "max_pages": 120
    },
    {
        "name": "ant-design",
        "url": "https://ant.design/docs/react/introduce",
        "base_url": "https://ant.design/",
        "max_pages": 100
    },
    {
        "name": "mantine",
        "url": "https://mantine.dev/docs/",
        "base_url": "https://mantine.dev/",
        "max_pages": 80
    },
    {
        "name": "daisyui",
        "url": "https://daisyui.com/docs/",
        "base_url": "https://daisyui.com/",
        "max_pages": 60
    },
    {
        "name": "headless-ui",
        "url": "https://headlessui.com/react",
        "base_url": "https://headlessui.com/",
        "max_pages": 50
    },
    {
        "name": "bootstrap",
        "url": "https://getbootstrap.com/docs/",
        "base_url": "https://getbootstrap.com/",
        "max_pages": 100
    },
    {
        "name": "tailwind-css",
        "url": "https://tailwindcss.com/docs",
        "base_url": "https://tailwindcss.com/",
        "max_pages": 100
    }
]

def create_config(framework):
    """Create scraper configuration for a framework"""
    config = {
        "name": framework["name"],
        "base_url": framework["base_url"],
        "start_urls": [framework["url"]],
        "max_pages": framework["max_pages"],
        "rate_limit": 0.8,
        "selectors": {
            "title": "h1, title",
            "main_content": "main, article, div[role='main'], #content",
            "code_blocks": "pre code, code[class*='language-']"
        },
        "url_patterns": {
            "include": [],
            "exclude": []
        },
        "checkpoint": {
            "enabled": True,
            "interval": 20
        }
    }
    return config

def run_scraper(framework):
    """Run scraper for a single framework"""
    print(f"\n{'='*70}")
    print(f"🔄 SCRAPING: {framework['name'].upper()}")
    print(f"{'='*70}")
    print(f"📖 URL: {framework['url']}")
    
    # Create config file
    config = create_config(framework)
    config_path = f".github/copilot-skills/docs-to-skill/configs/{framework['name']}.json"
    
    print(f"📝 Creating config: {config_path}")
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Run scraper
    cmd = [
        "python3",
        ".github/copilot-skills/docs-to-skill/scripts/scrape_docs.py",
        "--config", config_path
    ]
    
    print(f"🚀 Running scraper...\n")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=False,
            text=True,
            timeout=600  # 10 minute timeout per framework
        )
        
        if result.returncode == 0:
            print(f"\n✅ {framework['name']} scraped successfully!")
            return True
        else:
            print(f"\n❌ {framework['name']} scraping failed")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"\n⏱️  {framework['name']} scraping timed out (10 mins)")
        return False
    except Exception as e:
        print(f"\n❌ Error scraping {framework['name']}: {e}")
        return False

def main():
    """Run bulk scraping"""
    # Ensure venv is active
    venv_bin = ".venv/bin/python3"
    if not os.path.exists(venv_bin):
        print("⚠️  Virtual environment not found. Creating...")
        os.system("python3 -m venv .venv")
        os.system("source .venv/bin/activate && pip install -q requests beautifulsoup4")
    
    print("\n" + "="*70)
    print("🎯 BULK DOCUMENTATION SCRAPER")
    print("="*70)
    print(f"Frameworks to scrape: {len(FRAMEWORKS)}")
    for fw in FRAMEWORKS:
        print(f"  • {fw['name']} ({fw['max_pages']} pages max)")
    print("="*70)
    
    # Create configs directory
    Path(".github/copilot-skills/docs-to-skill/configs").mkdir(parents=True, exist_ok=True)
    Path("output").mkdir(parents=True, exist_ok=True)
    
    # Run scrapers
    results = {}
    for i, framework in enumerate(FRAMEWORKS, 1):
        print(f"\n[{i}/{len(FRAMEWORKS)}] Starting {framework['name']}...")
        success = run_scraper(framework)
        results[framework['name']] = "✅ Success" if success else "❌ Failed"
    
    # Summary
    print(f"\n{'='*70}")
    print("📊 SCRAPING SUMMARY")
    print(f"{'='*70}")
    for name, status in results.items():
        print(f"  {status} - {name}")
    
    print(f"\n{'='*70}")
    print("✨ Bulk scraping complete!")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
