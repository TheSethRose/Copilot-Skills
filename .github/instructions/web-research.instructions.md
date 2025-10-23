# Web Research Instructions

**Auto-loaded when**: Working with files matching: `**/*.py, **/*.js, **/*.ts, **/*.md, **/research*, **/web*, **/scrape*, **/crawler*, **/knowledge*`

**Triggers**: research, web, search, documentation, scrape, crawler, learning, knowledge-base

## Default Behaviors

When conducting research on web topics:

1. **Search First**: Always start with authoritative sources (official docs, MDN, GitHub)
2. **Multi-Source**: Never rely on single source—verify patterns across sources
3. **Incremental Scraping**: Use checkpoint system for long-running crawls
4. **Pattern Extraction**: Look for repeated patterns across all sources
5. **Code Examples**: Always extract and categorize code samples with language detection
6. **Cache Results**: Reuse previous research for related queries
7. **Terminal Output**: All research reports output to terminal for human review

## Common Workflows

### Quick Topic Research
```bash
/web-research --query "topic" --quick
# Returns: Key concepts, examples, recommended resources
# Time: 30 seconds
# Best for: Quick overview before deeper research
```

### Comprehensive Library Research
```bash
/web-research --query "React hooks" --sources react.dev,reactjs.org --depth 3
# Returns: All documentation, patterns, code examples
# Time: 2-5 minutes (with caching)
# Best for: Learning new library thoroughly
```

### Comparative Research
```bash
/web-research --query "ORMs" --sources prisma,typeorm,drizzle --compare
# Returns: Feature comparison, when to use each
# Time: 3-10 minutes
# Best for: Technology selection and comparison
```

### Generate Skill from Research
```bash
/web-research --query "Next.js" --scrape --export-skill
# Returns: Complete skill directory with patterns.md, reference.md
# Time: 10-20 minutes
# Best for: Creating permanent Copilot Skills from research
```

### Deep Research Project
```bash
/web-research --query "kubernetes architecture" --depth 3 --resume
# Returns: Comprehensive 30+ page research report
# Time: 30+ minutes (checkpoint enables resumption)
# Best for: Deep technical analysis with recovery
```

## Search Configuration

### Source Priority (Tier System)

**Tier 1 - Official Documentation** (highest authority):
- Official sites: react.dev, nextjs.org, vue.io, angular.io
- Language sites: nodejs.org, python.org, rust-lang.org
- Official repos: github.com/facebook/react, etc.

**Tier 2 - Curated Resources** (high quality):
- MDN Web Docs
- Dev.to, CSS-Tricks, Smashing Magazine
- Official blogs and tutorials
- Verified community guides

**Tier 3 - Community** (verify quality):
- Stack Overflow (high-vote answers)
- Medium, Hashnode posts
- Community wikis

### Query Construction

✅ **Good queries** (specific, 3-5 words):
```
- "React hooks best practices"
- "database migration patterns"
- "TypeScript generics advanced"
- "async/await performance"
- "REST vs GraphQL tradeoffs"
```

❌ **Poor queries** (too broad or too narrow):
```
- "React"
- "databases"
- "TypeScript"
- "what is async"
```

**Tips**:
- Use 3-5 words for best results
- Include specific topic or framework name
- Mention desired outcome (best practices, patterns, comparison)

## Scraping Strategy

### Sitemap Loading
When available:
1. Discover sitemap.xml at domain root
2. Parse all documented URLs
3. Filter by content patterns (exclude archives, old versions)
4. Build crawl priority queue

### Multi-Site Traversal
```
1. Search identifies sources
2. Load each site's structure
3. Queue pages by relevance
4. Crawl in parallel with checkpoints
5. Merge results from all sources
```

### Content Extraction from Each Page

Extract structured elements:
- Title (h1, <title> tag)
- Heading hierarchy (h1-h6 with nesting)
- Code blocks (with language detection)
- Main content paragraphs
- Related links and cross-references

### Checkpoint System

Enables recovery from interruptions:
```
- Save progress every 50 pages
- Record checkpoint data: visited URLs, pending URLs, cached content
- Resume with --resume flag
- Shows: "Resumed from checkpoint: 45/127 pages, resuming from page 46"
```

## Analysis Phase

### Categorization (by topic, language, complexity)

Content automatically grouped by:
- **Topic**: Concepts, How-tos, API Reference, Examples, Troubleshooting
- **Language**: JavaScript, TypeScript, Python, Java, Rust, Go, etc.
- **Complexity**: Beginner, Intermediate, Advanced, Expert
- **Use case**: Performance, Security, Patterns, Best practices

### Pattern Extraction

Identify recurring patterns across all sources:
```javascript
// Pattern detection examples
- Hook patterns: use[A-Z]\w+\(.*\)  (useStateeffect, useCallback, etc.)
- Decorators: @[a-zA-Z]+ (Python/TypeScript)
- Async patterns: async function|await|Promise
- Class patterns: class X extends|implements
```

### Cross-Source Convergence

Highlight when multiple sources agree:
- "3 sources recommend approach X" (strong signal)
- "Approaches vary (A: 2 sources, B: 1 source)" (mixed signal)
- "Only source X mentions approach Z" (unique/new approach)

## Analysis Output

### Terminal Report Format
```
📚 Web Research Results
======================

Query: "React hooks best practices"
Sources: 3 (react.dev, nextjs.org, Dev.to)
Pages scraped: 127
Patterns found: 24

📋 Key Concepts:
- useCallback for performance optimization
- useContext for prop drilling elimination
- Custom hooks for logic extraction

💾 Code Examples: 18 total
- JavaScript/TSX: 12
- TypeScript patterns: 4
- Performance optimization: 2

🔗 Top Resources:
1. react.dev/reference/react/hooks (58 pages)
2. nextjs.org/docs/advanced (32 pages)
3. dev.to/tagged/react-hooks (37 pages)

⚡ Quick Wins:
- Start with useState + useEffect basics
- Move to useCallback for performance
- Create custom hooks for reuse

📚 Next Steps:
- See full research index: ./output/react_data/index.json
- Generate skill: /web-research --export-skill
- Deep dive: /web-research --query "hooks" --depth 3
```

### Searchable Index (JSON)
```json
{
  "query": "React hooks",
  "timestamp": "2025-10-22T10:30:00Z",
  "sources": [
    {
      "domain": "react.dev",
      "pages_scraped": 58,
      "content_hash": "abc123..."
    }
  ],
  "results": [
    {
      "url": "https://react.dev/reference/react/useState",
      "title": "useState",
      "topic": "API Reference",
      "code_samples": [
        {
          "language": "typescript",
          "code": "const [count, setCount] = useState(0);",
          "context": "Basic state counter"
        }
      ],
      "patterns": ["state management", "reactive", "immutable"]
    }
  ],
  "index": {
    "useState": [0, 1, 2, ...],
    "hooks": [0, 1, 3, 4, ...],
    "performance": [5, 7, 12, ...]
  }
}
```

## Integration Patterns

### With `/context7`
```bash
/web-research --query "React latest" --use-context7
# Uses Context7 for up-to-date library versions
# Combines with general web search
```

### With `/langchain`
```bash
/web-research --query "RAG patterns" --export-langchain
# Exports as LangChain-compatible document loader
# Ready for vector database ingestion
```

### With `/claude`
```bash
/web-research --query "topic" --analyze-with-claude
# Pipe findings to Claude for synthesis
# Get summaries and insights
```

## Error Handling

### Common Issues and Solutions

**"Sitemap not found"**
- Fallback to BFS traversal from base_url
- Use common documentation paths: /docs/, /learn/, /guide/
- Continue with available heuristics

**"Rate limited"**
- Automatic backoff strategy (exponential delay)
- Use --resume to continue later
- Shows: "Rate limited by domain. Continuing next batch in 5m."

**"Content extraction failed for page X"**
- Log page for manual review (shows URL)
- Continue with next page
- Report count in final summary: "3/127 pages had extraction issues"

**"Crawl interrupted"**
- Checkpoint saves every 50 pages automatically
- Resume with: /web-research --query "..." --resume
- Shows: "Resuming from checkpoint: 45/127 pages complete"

## Related Skills

- **`/servicenow-docs`** – Specialized ServiceNow documentation research
- **`/context7`** – Latest library documentation versions and lookup
- **`/claude`** – Synthesis and analysis of research findings
- **`/langchain`** – Build RAG systems from research data
- **`/docs-to-skill`** – Convert research into permanent Copilot Skill

## Quality Guidelines

✅ **Do**:
- Start with official documentation
- Verify patterns across multiple sources
- Extract code examples with language tags
- Use checkpoints for long research
- Export quality research as skills

⚠️ **Avoid**:
- Single-source research (unreliable)
- Outdated sources without verification
- Mixing different framework versions
- Skipping error analysis

## Resources

- Skill prompt: `.github/prompts/web-research.skill.prompt.md`
- Scripts: `.github/copilot-skills/generators/web-research/scripts/`
- Patterns: `.github/copilot-skills/generators/web-research/patterns.md`
- Reference: `.github/copilot-skills/generators/web-research/reference.md`

## Typical Research Timeline

| Mode | Time | Depth |
|------|------|-------|
| Quick | 30 sec | Search only |
| Standard | 5 min | 2-3 top sources |
| Deep | 20+ min | All relevant sources |
| Comprehensive | 30+ min | 100+ pages with analysis |

Use `--mode` flag to control depth vs speed tradeoff.
