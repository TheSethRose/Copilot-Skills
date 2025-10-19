---
description: Convert any documentation website into a Copilot Skill
---

# Docs to Skill

**Purpose**: Automatically scrape documentation websites and generate Copilot Skills in the proper architecture format.

## When to Use This Skill

Use this skill when:
- Converting framework documentation (React, shadcn, Vue) into Copilot Skills
- Creating skills from library documentation (Tailwind, Prisma, etc.)
- Building reference skills from API documentation
- Transforming any documentation site into a searchable skill

**Keywords**: documentation, docs to skill, scrape docs, generate skill, documentation converter

## Quick Start

### 1. Dry Run (Preview)

Test what pages would be scraped:

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/shadcn.json \
  --dry-run
```

### 2. Full Scrape

Generate the actual skill:

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/shadcn.json
```

### 3. Use Available Presets

```bash
# List available configs
ls .github/copilot-skills/docs-to-skill/configs/

# Use a preset
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/react.json
```

## Configuration

### Using a Preset

Check existing presets in `.github/copilot-skills/docs-to-skill/configs/`:
- `shadcn.json` - shadcn/ui component library
- `react.json` - React documentation
- `tailwind.json` - Tailwind CSS

### Creating Custom Config

Create a JSON config file:

```json
{
  "name": "skill-name",
  "description": "Brief description for the skill",
  "base_url": "https://docs.example.com/",
  "max_pages": 200,
  "rate_limit": 0.5,
  "file_patterns": [
    "**/*.jsx",
    "**/*.tsx"
  ],
  "selectors": {
    "main_content": "main, article",
    "title": "h1, title",
    "code_blocks": "pre code"
  },
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/.*"],
    "exclude": ["/blog/.*", "#.*"]
  },
  "categories": {
    "getting_started": ["installation", "setup", "getting-started"],
    "api": ["api", "reference"],
    "components": ["component", "widget"]
  },
  "checkpoint": {
    "enabled": true,
    "interval": 50
  }
}
```

### Configuration Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Short identifier (used in file names) |
| `description` | ✅ | Brief skill purpose |
| `base_url` | ✅ | Documentation root URL |
| `max_pages` | ✅ | Maximum pages to scrape |
| `rate_limit` | ✅ | Seconds between requests (0.5 recommended) |
| `file_patterns` | ❌ | When to auto-load instructions |
| `selectors` | ❌ | CSS selectors for content extraction |
| `url_patterns` | ❌ | Include/exclude URL patterns (regex) |
| `categories` | ❌ | Category keywords for organization |
| `checkpoint` | ❌ | Enable progress saving |

## What Gets Generated

The scraper creates a **Copilot Skills Architecture** skill:

```
.github/prompts/{name}.skill.prompt.md
.github/instructions/{name}.instructions.md
.github/copilot-skills/{name}/
├── patterns.md           # Common code patterns
├── reference.md          # Documentation overview
├── references/           # Organized categorized docs
│   ├── components.md
│   ├── installation.md
│   └── [auto-detected].md
├── scripts/              # Empty (for custom tools)
└── assets/               # Empty (for templates)
```

### Generated Files

**Skill Prompt** (`.github/prompts/{name}.skill.prompt.md`):
- When to use the skill
- Quick reference with code examples
- How to use the documentation

**Instructions** (`.github/instructions/{name}.instructions.md`):
- Auto-loads based on file patterns
- Default behaviors and guidelines
- Common workflows

**patterns.md**:
- 5-10 common code patterns extracted from docs
- Real examples with language tags
- Links to reference categories

**reference.md**:
- Overview of all documentation
- Category summaries
- Navigation guide

**references/**:
- Organized by auto-detected categories
- Page titles, URLs, and content
- Code examples from each page
- Table of contents from headings

## Advanced Usage

### Resume Interrupted Scrape

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config configs/large-docs.json \
  --resume
```

### Build from Existing Data

If you already scraped but want to rebuild the skill files:

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config configs/shadcn.json \
  --build-only
```

## Best Practices

### ✅ Do

- **Always dry-run first** to preview page count
- **Use presets** when available
- **Set appropriate rate limits** (0.5s minimum)
- **Enable checkpoints** for large docs (>100 pages)
- **Test selectors** on a few pages first
- **Respect robots.txt**

### ❌ Don't

- Skip dry-run for unknown documentation
- Use rate limits <0.3s (may get blocked)
- Scrape non-documentation content
- Ignore checkpoint warnings
- Scrape without testing selectors

## Performance Expectations

| Pages | Time | Strategy |
|-------|------|----------|
| <100 | 5-10 min | Standard |
| 100-500 | 15-30 min | Enable checkpoints |
| 500-1000 | 30-60 min | Monitor progress |
| >1000 | 1+ hours | Consider splitting |

## Troubleshooting

### No Content Extracted

Check CSS selectors in config:

```json
{
  "selectors": {
    "main_content": "main, article, div[role='main']",
    "title": "h1, title",
    "code_blocks": "pre code"
  }
}
```

### Pages Not Found

Check URL patterns:

```json
{
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/.*"],
    "exclude": ["/blog/.*", "#.*"]
  }
}
```

### Scrape Interrupted

Use `--resume` to continue:

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config configs/my-docs.json \
  --resume
```

## Creating Configs for Popular Docs

Reference the docs list in `examples/docs.md` for URLs.

### Example: Creating Tailwind Config

```json
{
  "name": "tailwind",
  "description": "Utility-first CSS framework",
  "base_url": "https://tailwindcss.com/docs/",
  "max_pages": 200,
  "rate_limit": 0.5,
  "file_patterns": [
    "**/*.css",
    "**/*.jsx",
    "**/*.tsx",
    "**/tailwind.config.*"
  ],
  "selectors": {
    "main_content": "main",
    "title": "h1",
    "code_blocks": "pre code"
  },
  "categories": {
    "core_concepts": ["installation", "configuration", "utility"],
    "layout": ["container", "flex", "grid"],
    "typography": ["font", "text", "color"],
    "components": ["button", "form", "card"]
  }
}
```

## Example Workflow

### Full Workflow: shadcn/ui

```bash
# 1. Dry run
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/shadcn.json \
  --dry-run

# Output preview shows:
# - ~20+ pages found
# - File structure
# - Example content

# 2. Full scrape (15-20 minutes)
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/shadcn.json

# 3. Generated files:
# .github/prompts/shadcn.skill.prompt.md
# .github/instructions/shadcn.instructions.md
# .github/copilot-skills/shadcn/patterns.md
# .github/copilot-skills/shadcn/reference.md
# .github/copilot-skills/shadcn/references/*.md

# 4. Register skill
# Add entry to .github/copilot-instructions.md keyword routing map

# 5. Test skill
# /shadcn in Copilot Chat
```

## Related Skills

- `/create-skill` - Further customize generated skills
- `/document-project` - Document YOUR project (different use case)

## More Information

- **Scraper**: `.github/copilot-skills/docs-to-skill/scripts/scrape_docs.py`
- **Configs**: `.github/copilot-skills/docs-to-skill/configs/`
- **Docs List**: `examples/docs.md` (300+ documentation URLs)
