# Web Research Patterns

## 1. Multi-Phase Research Workflow

### Pattern: Discovery → Aggregation → Crawl → Analysis → Report

**Structure**:
```
Query Input
    ↓
Phase 1: Search for sources
    ↓
Phase 2: Preview crawl strategy
    ↓
Phase 3: Multi-site scraping with checkpoints
    ↓
Phase 4: Cross-source pattern analysis
    ↓
Phase 5: Terminal report + optional skill export
```

**When to use**: Any research task requiring multiple sources

**Example**:
```bash
/web-research --query "react hooks best practices"
# Follows all 5 phases, returns findings in 5 minutes
```

## 2. Checkpoint Recovery Pattern

### Pattern: Save state every N pages, enable resumption

**Implementation**:
```python
def save_checkpoint(pages_scraped, pending_urls, cached_content):
    checkpoint = {
        "timestamp": datetime.now().isoformat(),
        "pages_scraped": pages_scraped,
        "pending_urls": pending_urls,
        "cache": cached_content
    }
    with open("checkpoint.json", "w") as f:
        json.dump(checkpoint, f)

# Resume with: /web-research --query "..." --resume
```

**Benefits**:
- Recover from interruptions
- Resume long crawls
- No data loss

## 3. Content Extraction with Language Detection

### Pattern: Extract code blocks with automatic language detection

**Detection heuristic**:
```python
def detect_language(code_elem, code_text):
    classes = code_elem.get('class', [])
    
    # Check explicit class markers
    if 'language-python' in classes or 'lang-python' in classes:
        return 'python'
    
    # Heuristic detection from code patterns
    if 'import React' in code_text or 'export default' in code_text:
        return 'typescript'
    if 'def ' in code_text and ':' in code_text:
        return 'python'
    if '#include' in code_text or 'int main' in code_text:
        return 'cpp'
    
    return 'text'  # Unknown
```

**Coverage**: JavaScript, TypeScript, Python, Rust, Go, Java, C++, etc.

## 4. Cross-Source Pattern Convergence

### Pattern: Highlight when multiple sources agree on pattern

**Implementation**:
```python
def find_convergence(findings_by_source):
    pattern_counts = defaultdict(list)
    
    for source, findings in findings_by_source.items():
        for pattern in findings:
            pattern_counts[pattern].append(source)
    
    convergence = {
        pattern: sources
        for pattern, sources in pattern_counts.items()
        if len(sources) >= 2  # Converged if 2+ sources agree
    }
    
    return convergence
```

**Report format**:
```
✓ Converged Patterns (3+ sources agree):
  • useCallback for performance → 3 sources
  • useContext for state sharing → 3 sources
  • Custom hooks for reuse → 3 sources

⚠ Mixed Approaches (2 sources):
  • Hook testing strategies → 2 sources
  • Suspense integration → 2 sources

✨ Unique Approaches (1 source only):
  • Advanced hook debugging → 1 source
```

## 5. Progressive Research Modes

### Pattern: Tradeoff speed vs. depth

| Mode | Time | Depth | When |
|------|------|-------|------|
| Quick | 30 sec | Search only | Quick overview |
| Standard | 5 min | Top 2-3 sources | Learning |
| Deep | 20+ min | All sources | Comprehensive |
| Export | 10-20 min | Generate skill | Documentation |

**Implementation**:
```python
DEPTH_CONFIG = {
    'quick': {'max_sources': 1, 'max_pages': 0, 'scrape': False},
    'standard': {'max_sources': 3, 'max_pages': 50, 'scrape': True},
    'deep': {'max_sources': 10, 'max_pages': 500, 'scrape': True},
    'export': {'max_sources': 'all', 'max_pages': 'all', 'export': True}
}
```

## 6. Source Priority Tier System

### Pattern: Prioritize official → curated → community

**Implementation**:
```python
SOURCE_TIERS = {
    1: {  # Official documentation (highest priority)
        'patterns': [r'react\.dev', r'nextjs\.org', r'nodejs\.org'],
        'weight': 1.0
    },
    2: {  # Curated resources (medium priority)
        'patterns': [r'mdn\.org', r'dev\.to', r'github\.com/.*/wiki'],
        'weight': 0.7
    },
    3: {  # Community sources (lower priority)
        'patterns': [r'stackoverflow\.com', r'medium\.com'],
        'weight': 0.5
    }
}

def prioritize_sources(urls):
    scored = []
    for url in urls:
        for tier, config in SOURCE_TIERS.items():
            for pattern in config['patterns']:
                if re.search(pattern, url):
                    scored.append((url, tier, config['weight']))
                    break
    
    return sorted(scored, key=lambda x: x[2], reverse=True)
```

## 7. Sitemap-Based Crawl Strategy

### Pattern: Use sitemap.xml for efficient crawling

**Implementation**:
```python
def build_crawl_queue_from_sitemap(base_url):
    parsed = urlparse(base_url)
    sitemap_url = f"{parsed.scheme}://{parsed.netloc}/sitemap.xml"
    
    try:
        response = requests.get(sitemap_url, timeout=5)
        soup = BeautifulSoup(response.content, 'xml')
        
        urls = [loc.text for loc in soup.find_all('loc')]
        # Filter by patterns, sort by priority
        
        return sorted_urls
    except:
        # Fallback to BFS from base_url
        return bfs_discover_urls(base_url)
```

**Benefits**:
- Crawl entire documentation efficiently
- Respect site structure
- Fallback to BFS if unavailable

## 8. JSON Index Structure for Later Querying

### Pattern: Export findings in queryable JSON format

**Structure**:
```json
{
  "metadata": {
    "query": "react hooks",
    "timestamp": "2025-10-22T10:30:00Z",
    "mode": "standard",
    "sources_count": 3,
    "pages_total": 127
  },
  "sources": [
    {
      "url": "react.dev",
      "tier": 1,
      "pages_scraped": 58
    }
  ],
  "findings": [
    {
      "url": "https://react.dev/reference/react/useState",
      "title": "useState",
      "topic": "API",
      "patterns": ["state-management", "reactive"],
      "code_samples": [
        {
          "language": "typescript",
          "code": "const [count, setCount] = useState(0);",
          "context": "Basic counter"
        }
      ]
    }
  ],
  "search_index": {
    "useState": [0, 1, 3, ...],
    "hooks": [0, 1, 2, 4, ...],
    "performance": [5, 7, 12, ...]
  }
}
```

**Enables**: Full-text search, filtering, analysis

## 9. Skill Export Pattern

### Pattern: Generate Copilot Skill from research findings

**Generated files**:
```
.github/copilot-skills/generators/web-research-{query}/
├── README.md (overview of findings)
├── patterns.md (extracted patterns)
├── reference.md (organized findings by topic)
└── scripts/
    └── web_research_{query}.py (specific research script)

.github/prompts/web-research-{query}.skill.prompt.md
.github/instructions/web-research-{query}.instructions.md
```

**Content generation**:
- Prompt from: Key findings + use cases
- Instructions from: Patterns + code examples
- Patterns.md from: Cross-source patterns
- Reference.md from: Organized topic hierarchy

## 10. Error Recovery with Terminal Output

### Pattern: All errors to terminal, no silent failures

**Implementation**:
```python
def handle_error(error_type, details, context):
    print(f"\n⚠️  {error_type}")
    print(f"   {details}")
    print(f"   Context: {context}")
    
    if error_type == "rate_limit":
        print(f"   💡 Resume later with: /web-research --resume")
    elif error_type == "extraction_failed":
        print(f"   💡 Continuing with other pages (logged)")
    elif error_type == "no_sources":
        print(f"   💡 Try more specific query (e.g., '... patterns')")
    
    return False  # Continue or fail
```

**Ensures**: Visibility, recoverability, user guidance

---

## Related Patterns

- **Git Operations**: git_safe_exec.sh (checkpoint pattern)
- **PDF Handling**: Content extraction techniques
- **Docs-to-Skill**: Skill file generation
- **MCP Builder**: Cross-tool orchestration

