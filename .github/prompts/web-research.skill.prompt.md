---
description: Research web topics - combine search + doc scraping for comprehensive answers
---

# Web Research

**Purpose**: Research any topic by combining web search with targeted documentation scraping, enabling comprehensive multi-source learning and knowledge base generation.

## When to Use This Skill

Use this skill when:
- 🔍 Learning a new framework or library unfamiliar to you
- 📚 Building a knowledge base from multiple documentation sources
- 🤔 Answering complex questions requiring multiple authoritative sources
- 📊 Comparing patterns and features across similar technologies
- 🧠 Deep-diving into emerging tools, frameworks, or best practices
- 🔬 Extracting and analyzing patterns across a domain
- 🎯 Generating comprehensive skill documentation from research

**Keywords**: research, web, search, documentation, scrape, crawler, learning, knowledge-base, investigation, discovery

## Quick Start

### Quick Research (30 seconds)
```bash
/web-research --query "react hooks best practices"
```
Returns: Key concepts, examples, recommended resources.

### Standard Research (5 minutes)
```bash
/web-research --query "database migration patterns" --sources prisma,typeorm,drizzle
```
Returns: Aggregated findings with code examples and patterns.

### Deep Research (20+ minutes)
```bash
/web-research --query "rust async ecosystem" --depth 3 --scrape
```
Returns: Comprehensive analysis with full documentation.

### Generate Skill
```bash
/web-research --query "Next.js 14" --export-skill
```
Returns: Complete Copilot Skill with patterns.md and reference.md.

## Workflow

1. **Search** - Find relevant authoritative documentation sources
2. **Preview** - Show identified URLs and proposed crawl strategy
3. **Scrape** - Extract content from all sources with checkpoint recovery
4. **Analyze** - Categorize content and extract cross-source patterns
5. **Report** - Display findings in terminal with actionable insights

## Output Options

- **Terminal Report**: Immediate findings with examples and recommendations
- **Searchable Index**: JSON index with full-text search capabilities
- **Skill Format**: Generate new Copilot Skill from research (beta)
- **CSV Export**: Structured data tables for further analysis

## Research Modes

### Quick Mode (`--quick`)
- Search only, 30 seconds
- No scraping
- Best for: Rapid overview

### Standard Mode (default)
- Search + shallow scrape from top sources
- 5 minutes typical
- Best for: Learning and overview

### Deep Mode (`--depth 3`)
- Search + comprehensive scrape from all sources
- 20+ minutes typical
- Best for: Comprehensive research, skill generation

## Integration Points

- **`/context7`** - Lookup latest library documentation versions
- **`/servicenow-docs`** - Delegate ServiceNow-specific research
- **`/langchain`** - Build RAG systems from research findings
- **`/claude`** - Summarize and synthesize findings with Claude API

See also: `/servicenow-docs`, `/context7`, `/langchain`, `/claude`

## Examples

### Example 1: Learning React Hooks
```
User: /web-research --query "react hooks best practices"

→ Searches for React hooks documentation
→ Scrapes react.dev, reactjs.org, MDN React pages
→ Extracts 20+ code examples
→ Identifies 5 core patterns:
   • useCallback for performance
   • useContext for state sharing
   • Custom hooks for reuse
   • Dependency array best practices
   • Error boundaries with hooks

→ Terminal report shows findings + links to sources
```

### Example 2: Comparing ORMs
```
User: /web-research --query "node.js ORMs" --sources prisma,typeorm,drizzle --compare

→ Fetches documentation for each ORM
→ Extracts common patterns from all three
→ Builds comparison table:
   • Performance characteristics
   • Query syntax differences
   • Type safety approaches
   • Community size and maturity
   • When to use each

→ Report shows pros/cons of each with code examples
```

### Example 3: Deep Dive Into Testing
```
User: /web-research --query "testing strategies" --depth 3

→ Searches testing frameworks: Jest, Vitest, Playwright, Cypress
→ Scrapes 200+ pages from all sources
→ Analyzes patterns and best practices
→ Generates report with:
   • Unit vs E2E vs Integration testing
   • Framework comparisons
   • 30+ runnable code examples
   • Performance testing patterns
   • CI/CD integration patterns

→ Creates searchable JSON index for reference
```

### Example 4: Generate Skill from Research
```
User: /web-research --query "tailwind css v4" --export-skill

→ Researches Tailwind CSS documentation
→ Analyzes patterns and common use cases
→ Generates complete Copilot Skill:
   .github/prompts/tailwind-v4.skill.prompt.md
   .github/instructions/tailwind-v4.instructions.md
   .github/copilot-skills/frontend/tailwind-v4/patterns.md
   .github/copilot-skills/frontend/tailwind-v4/reference.md

→ New skill ready to register in routing map
```

## Research Strategy

### Source Priority

**Tier 1 - Official Documentation** (highest authority)
- Official docs: react.dev, nextjs.org, vue.io, angular.io, svelte.dev
- Language sites: nodejs.org, python.org, rust-lang.org, go.dev
- Official GitHub repositories and READMEs

**Tier 2 - Curated Resources** (high quality)
- MDN Web Docs
- Dev.to, CSS-Tricks, Smashing Magazine
- Official blogs and tutorials
- Community wikis from verified sources

**Tier 3 - Community** (verify quality)
- Stack Overflow (answers with high scores)
- Medium, Hashnode, Dev.to posts
- Open source project tutorials

### Query Tips

✅ **Good queries** (specific, searchable):
- "React hooks best practices"
- "Database migration patterns"
- "TypeScript generics advanced"
- "Async/await performance optimization"

❌ **Poor queries** (too broad):
- "React"
- "Databases"
- "TypeScript"

Better results with 3-5 word queries focused on specific topics.

## Common Workflows

### Learning New Framework
```bash
/web-research --query "Vue.js Composition API" --quick
# Get quick overview in 30 seconds
# Then use for deeper exploration with --depth 2
```

### Project Stack Comparison
```bash
/web-research --query "backend frameworks" --sources fastapi,fastify,springboot --compare
# Compare frameworks for your next project
# See patterns and when to use each
```

### Finding Best Practices
```bash
/web-research --query "react performance optimization" --scrape
# Aggregate best practices from all sources
# Get actionable patterns with examples
```

### Building Documentation Skill
```bash
/web-research --query "framework name" --export-skill
# Generate complete Copilot Skill
# Ready to commit and use in team
```

## Related Skills

- **`/servicenow-docs`** – Specialized ServiceNow research (auto-routes if detected)
- **`/context7`** – Latest library documentation versions
- **`/claude`** – Analyze and synthesize research findings
- **`/langchain`** – Build knowledge bases and RAG from research
- **`/docs-to-skill`** – Convert single documentation site to skill

## Error Handling

**"No sources found"** → Refine query with more specific keywords

**"Rate limited"** → Retry with `--resume` flag (uses checkpoints)

**"Content extraction failed"** → Continue with available sources (logged)

## Output Data Format

Research results are available as:
- **Terminal output**: Human-readable findings with examples
- **JSON index**: Programmatically queryable search index
- **CSV export**: For analysis in spreadsheet tools
- **Skill files**: Ready to commit and use (with `--export-skill`)

---

**Ready?** Start with a quick research: `/web-research --query "your topic"`
