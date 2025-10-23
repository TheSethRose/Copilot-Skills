# Web Research Reference

## Overview

Web Research enables multi-source documentation research through a 5-phase workflow: search → preview → scrape → analyze → report.

## Configuration

### Basic Configuration

```bash
# Quick research (30 seconds)
/web-research --query "topic"

# Standard research (5 minutes)
/web-research --query "topic" --mode standard

# Deep research (20+ minutes)
/web-research --query "topic" --mode deep

# Generate skill
/web-research --query "topic" --export-skill
```

### Advanced Options

```bash
# Specific sources
/web-research --query "ORMs" --sources prisma,typeorm,drizzle

# Comparison analysis
/web-research --query "ORMs" --sources prisma,typeorm,drizzle --compare

# Custom depth
/web-research --query "topic" --depth 3

# Resume from checkpoint
/web-research --query "topic" --resume

# Dry run (preview)
/web-research --query "topic" --dry-run
```

## Output Formats

### Terminal Report

Human-readable findings output to terminal:
```
📚 Web Research Results
Query: "react hooks"
Sources: 3
Pages: 127

📋 Key Findings
💾 Code Examples
🔗 Top Resources
⚡ Quick Wins
📚 Next Steps
```

### JSON Index

Programmatically queryable research data:
```
output/{query}_research/index.json
- metadata (query, timestamp, mode, counts)
- sources (tier, pages)
- findings (url, title, topic, patterns, code_samples)
- search_index (full-text search map)
```

### Skill Export

Generate complete Copilot Skill:
```
.github/prompts/web-research-{query}.skill.prompt.md
.github/instructions/web-research-{query}.instructions.md
.github/copilot-skills/generators/web-research-{query}/
  ├── README.md
  ├── patterns.md
  ├── reference.md
  └── scripts/
```

## API / Configuration Reference

### Mode Configuration

| Mode | Duration | Depth | Use Case |
|------|----------|-------|----------|
| `quick` | 30 sec | Search only | Fast overview |
| `standard` | 5 min | 2-3 sources | Learning |
| `deep` | 20+ min | All sources | Comprehensive |
| `export` | 10-20 min | Generate skill | Documentation |

### Source Tier Weights

| Tier | Priority | Examples | Weight |
|------|----------|----------|--------|
| 1 | Official docs | react.dev, nodejs.org | 1.0 |
| 2 | Curated | MDN, Dev.to | 0.7 |
| 3 | Community | SO, Medium | 0.5 |

### Language Detection

Supported languages for code extraction:
- JavaScript / TypeScript
- Python
- Rust
- Go
- Java
- C++
- Ruby
- PHP
- SQL
- HTML / CSS

### Checkpoint Format

Resume state saved as JSON:
```json
{
  "timestamp": "2025-10-22T10:30:00Z",
  "query": "topic",
  "pages_scraped": 45,
  "pending_urls": ["url1", "url2", ...],
  "cache": {
    "url": {"title": "...", "content": "..."}
  }
}
```

## Integration with Other Skills

### With `/context7`

```bash
/web-research --query "react" --use-context7
# Combines web research with Context7 latest docs
# Preferred for library research
```

### With `/langchain`

```bash
/web-research --query "RAG" --export-langchain
# Exports findings as LangChain document loader
# Ready for vector database
```

### With `/claude`

```bash
/web-research --query "topic" --analyze-with-claude
# Pipes findings to Claude for synthesis
# Get AI-powered summaries
```

### With `/docs-to-skill`

```bash
# Use web-research to discover documentation
/web-research --query "next.js"

# Then use docs-to-skill to convert single site to skill
python docs-to-skill.py --config nextjs.json
```

### With `/servicenow-docs`

```bash
# web-research auto-delegates ServiceNow queries
/web-research --query "ServiceNow incident management"
→ Routes to /servicenow-docs skill
```

## Performance Tuning

### Checkpoint Interval

```bash
# Save checkpoint every 50 pages (default)
/web-research --query "topic" --checkpoint-interval 50

# Save more frequently for unreliable networks
/web-research --query "topic" --checkpoint-interval 20

# Disable checkpointing (for quick research)
/web-research --query "topic" --mode quick
```

### Parallel Crawling

```bash
# Crawl 1 source at a time (slower, less resources)
/web-research --query "topic" --parallel 1

# Crawl 3 sources in parallel (default, balanced)
/web-research --query "topic" --parallel 3

# Crawl 10 sources in parallel (fast, resource-heavy)
/web-research --query "topic" --parallel 10
```

### Source Filtering

```bash
# Only search official documentation
/web-research --query "topic" --tier 1

# Include official + curated
/web-research --query "topic" --tier 1,2

# Include all tiers
/web-research --query "topic" --tier 1,2,3
```

## Common Queries

### Learning Queries

```bash
# Framework overview
/web-research --query "React best practices" --quick

# Library deep dive
/web-research --query "Next.js app router patterns" --mode deep

# Specific feature
/web-research --query "TypeScript generics advanced"
```

### Comparison Queries

```bash
# Framework comparison
/web-research --query "Frontend frameworks" --sources react,vue,svelte --compare

# ORM comparison
/web-research --query "Node.js ORMs" --sources prisma,typeorm,sequelize --compare

# Build tool comparison
/web-research --query "Build tools" --sources webpack,vite,esbuild --compare
```

### Problem-Solving Queries

```bash
# Find best practices
/web-research --query "React performance optimization"

# Find patterns
/web-research --query "Database migration patterns"

# Find alternatives
/web-research --query "REST API alternatives"
```

### Knowledge Base Queries

```bash
# Extract for skill
/web-research --query "Vue.js 3" --export-skill

# Research and analyze
/web-research --query "Rust async ecosystem" --mode deep

# Generate documentation
/web-research --query "GraphQL best practices" --export-skill
```

## Troubleshooting

### No Results

**Problem**: `/web-research --query "xyz"` returns nothing

**Solutions**:
1. Check query specificity (add framework/library name)
2. Try different keywords
3. Use `--sources` to specify domains
4. Check if topic is too new (documentation may not exist)

### Rate Limited

**Problem**: "Rate limited by domain"

**Solutions**:
```bash
# Wait and resume
/web-research --query "topic" --resume

# Reduce parallel crawling
/web-research --query "topic" --parallel 1

# Retry with slower pace
/web-research --query "topic" --delay 2
```

### Extraction Failed

**Problem**: Some pages fail to extract

**Solutions**:
1. Usually continues automatically (shows in final report)
2. Check page logged in `output/{query}_research/errors.log`
3. Sites with unusual HTML structures may not extract fully

### Out of Memory

**Problem**: Research fails with memory error

**Solutions**:
```bash
# Use smaller checkpoint interval
/web-research --query "topic" --checkpoint-interval 20

# Reduce parallel crawling
/web-research --query "topic" --parallel 1

# Use quick mode instead
/web-research --query "topic" --quick
```

## File Locations

| File | Purpose |
|------|---------|
| `.github/prompts/web-research.skill.prompt.md` | Skill prompt |
| `.github/instructions/web-research.instructions.md` | Auto-loaded context |
| `.github/copilot-skills/generators/web-research/` | Skill directory |
| `.github/copilot-skills/generators/web-research/scripts/web_research.py` | Main script |
| `output/{query}_research/index.json` | Research results |
| `output/{query}_research/checkpoint.json` | Resume state |

## Examples

### Example 1: Quick Learning
```bash
/web-research --query "React useEffect hook" --quick
→ 30 seconds, key concepts + links
```

### Example 2: Building Knowledge Base
```bash
/web-research --query "TypeScript patterns" --mode deep
→ 20 minutes, comprehensive findings
→ Save as: output/typescript_patterns_research/index.json
```

### Example 3: Technology Evaluation
```bash
/web-research --query "web frameworks" --sources nextjs,remix,sveltekit --compare
→ 5 minutes, side-by-side comparison
```

### Example 4: Generate Permanent Skill
```bash
/web-research --query "Tailwind CSS v4" --export-skill
→ Create .github/copilot-skills/generators/web-research-tailwind-v4/
→ Ready to commit and register
```

## Related Documentation

- [Web Research Skill Prompt](./../../../prompts/web-research.skill.prompt.md)
- [Web Research Instructions](./../../../instructions/web-research.instructions.md)
- [Web Research Patterns](./patterns.md)
- [Create Skill Guide](./../../../instructions/create-skill.instructions.md)

## Version History

**v1.0.0** (Oct 22, 2025)
- Initial release
- Multi-source search integration
- Parallel scraping with checkpoints
- Cross-source pattern analysis
- Terminal-based reporting
- Skill export capability

---

**Status**: ✅ Validated for Phase 4 Implementation  
**Next**: Phase 5 - Integration (register in routing map)
