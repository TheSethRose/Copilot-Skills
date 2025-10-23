# Docs to Skill

Automatically scrape documentation websites and generate Copilot Skills in the proper architecture format.

## What This Does

Converts any documentation site into a **Copilot Skill** with:
- 📚 Organized reference documentation by category
- 🎯 Searchable skill prompt with quick examples
- 📋 Auto-loaded instructions for file patterns
- 🔗 Proper architecture alignment

## Quick Start

### 1. Preview Pages (Dry Run)

```bash
cd scripts
python3 scrape_docs.py --config ../configs/bun.json --dry-run
```

**Output:**
```
📊 Preview Results:
  Found ~67 pages
  Will scrape up to: 150 pages
  Estimated time: 2.0 minutes

📑 Sample URLs (first 10):
    • https://bun.sh/docs/
    • https://bun.sh/docs/bundler
    ...
```

### 2. Scrape Documentation

```bash
python3 scrape_docs.py --config ../configs/bun.json
```

**Generates:**
- `.github/prompts/bun.skill.prompt.md` - Skill prompt
- `.github/instructions/bun.instructions.md` - Instructions
- `.github/copilot-skills/bun/reference.md` - Index
- `.github/copilot-skills/bun/references/*.md` - Categorized docs

### 3. Use Available Presets

```bash
# List available configs
ls configs/

# Use a preset
python3 scrape_docs.py --config configs/shadcn.json
```

## Scraper Types

### Static Sites (HTML/CSS)

Use `scrape_docs.py` for traditional documentation sites:
- Works with most framework docs (React, Next.js, Vue, etc.)
- Fast and lightweight
- No browser overhead

**Example:**
```bash
python3 scrape_docs.py --config configs/react.json
```

### Dynamic Sites (JavaScript/SPA)

Use `scrape_docs_dynamic.py` for JS-rendered documentation:
- Works with Next.js 13+ (app router)
- Gatsby, Remix, SvelteKit docs
- Single-page apps with client-side routing
- **Requires Playwright**

**Setup:**
```bash
pip install playwright beautifulsoup4
playwright install chromium
```

**Usage:**
```bash
python3 scrape_docs_dynamic.py --config ../configs/bun.json --dry-run
python3 scrape_docs_dynamic.py --config ../configs/bun.json --headless
python3 scrape_docs_dynamic.py --config ../configs/bun.json --debug
```

## Configuration

### Creating a Config

Create `configs/mylib.json`:

```json
{
  "name": "mylib",
  "description": "Brief description of library",
  "base_url": "https://docs.example.com/",
  "start_url": "https://docs.example.com/",
  "max_pages": 150,
  "rate_limit": 0.8,
  "file_patterns": [
    "**/*.js",
    "**/*.ts",
    "**/package.json"
  ],
  "selectors": {
    "main_content": "main, article, div[role='main']",
    "title": "h1, .title",
    "code_blocks": "pre code"
  },
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/.*"],
    "exclude": ["/blog/.*", "#.*"]
  },
  "categories": {
    "getting_started": ["installation", "setup", "quick-start"],
    "api": ["api", "reference"],
    "guides": ["guide", "tutorial", "example"]
  },
  "checkpoint": {
    "enabled": true,
    "interval": 50
  }
}
```

### Configuration Fields

| Field | Required | Type | Example |
|-------|----------|------|---------|
| `name` | ✅ | string | `"bun"` |
| `description` | ✅ | string | `"Fast JavaScript runtime"` |
| `base_url` | ✅ | string | `"https://bun.sh/docs/"` |
| `start_url` | ❌ | string | `"https://bun.sh/docs"` |
| `max_pages` | ✅ | number | `150` |
| `rate_limit` | ✅ | number | `0.8` |
| `file_patterns` | ❌ | array | `["**/*.ts"]` |
| `selectors` | ❌ | object | `{"main_content": "main"}` |
| `url_patterns` | ❌ | object | `{"include": [...]}` |
| `categories` | ❌ | object | `{"api": ["api", "reference"]}` |
| `checkpoint` | ❌ | object | `{"enabled": true, "interval": 50}` |

### Selectors Guide

CSS selectors for content extraction:

```json
{
  "selectors": {
    "main_content": "main, article, div[role='main'], .markdown-body",
    "title": "h1, .title, [data-title]",
    "code_blocks": "pre code, .code-block, [data-language]"
  }
}
```

**Finding selectors:**
1. Open documentation page in browser
2. Right-click → Inspect
3. Look for main content container
4. Use Browser DevTools to test selectors

### URL Patterns Guide

Regex patterns to control which pages are scraped:

```json
{
  "url_patterns": {
    "include": [
      "^https://docs\\.example\\.com/.*",
      "^https://api\\.example\\.com/.*"
    ],
    "exclude": [
      "/blog/.*",          # Exclude blog posts
      "/archive/.*",       # Exclude archived docs
      "\\?.*",            # Exclude URLs with query params
      "#.*"               # Exclude fragments
    ]
  }
}
```

### Categories Guide

Keyword-based categorization:

```json
{
  "categories": {
    "getting_started": ["installation", "setup", "quickstart", "intro"],
    "api_reference": ["api", "reference", "function", "method"],
    "guides": ["guide", "tutorial", "example", "pattern"],
    "advanced": ["advanced", "performance", "optimization"],
    "troubleshooting": ["troubleshoot", "faq", "error", "debug"]
  }
}
```

Pages are categorized by matching title/URL/content against keywords.

## Generated Output

### Directory Structure

```
.github/
├── prompts/
│   └── bun.skill.prompt.md           # Skill prompt
├── instructions/
│   └── bun.instructions.md           # Auto-load instructions
└── copilot-skills/
    └── bun/
        ├── reference.md              # Overview
        ├── references/
        │   ├── getting_started.md
        │   ├── runtime.md
        │   ├── bundler.md
        │   └── ...
        └── .scrape_cache.json        # Progress tracking
```

### Generated Files

**Skill Prompt** (`.github/prompts/{name}.skill.prompt.md`):
- When to use the skill
- Quick reference categories
- Example code patterns
- Documentation overview

**Instructions** (`.github/instructions/{name}.instructions.md`):
- Auto-loads on file pattern match
- File patterns that trigger this skill
- Link to documentation

**Reference** (`.github/copilot-skills/{name}/reference.md`):
- Index of all documentation
- Categories summary
- Page count by category

**Category Files** (`.github/copilot-skills/{name}/references/*.md`):
- Organized by auto-detected category
- Page titles and URLs
- Key topics from each page
- Code examples
- Content summary

## Advanced Usage

### Resume Interrupted Scrape

If scraping is interrupted, resume from checkpoint:

```bash
python3 scrape_docs.py --config configs/bun.json --resume
```

Checkpoints save progress every 50 pages (configurable).

### Rebuild Without Scraping

If you already scraped but want to regenerate skill files:

```bash
python3 scrape_docs.py --config configs/bun.json --build-only
```

### Debug Mode

For troubleshooting, use debug output:

```bash
# Static scraper
python3 scrape_docs.py --config configs/bun.json --debug

# Dynamic scraper (shows browser window)
python3 scrape_docs_dynamic.py --config configs/bun.json --debug
```

## Best Practices

### ✅ Do

- **Always dry-run first** to preview pages
- **Use presets** when available
- **Set appropriate rate limits** (0.5-1.0s typical)
- **Enable checkpoints** for large docs (>100 pages)
- **Test selectors** on sample pages first
- **Respect robots.txt** and site terms
- **Review generated files** before committing

### ❌ Don't

- Skip dry-run for unknown documentation
- Use rate limits <0.3s (may get blocked)
- Scrape non-documentation content
- Ignore checkpoint warnings
- Scrape without testing selectors
- Violate site terms of service

## Performance

| Pages | Time | Strategy | Scraper |
|-------|------|----------|---------|
| <50 | 1-3 min | Standard | Static |
| 50-150 | 5-15 min | Checkpoints | Static |
| 150-300 | 15-30 min | Monitor | Static |
| 300+ | 30+ min | Split into sections | Static |
| Any | 2-5x slower | Use when needed | Dynamic |

## Troubleshooting

### No Content Extracted

**Problem:** Pages have content but extraction fails

**Solution:** Update CSS selectors in config:

```json
{
  "selectors": {
    "main_content": "main, article, .content, div[class*='doc'], div[class*='markdown']"
  }
}
```

Test selectors in browser console:
```js
document.querySelectorAll("main");  // Check if main exists
document.querySelector("main").innerText;  // Preview content
```

### Pages Not Found

**Problem:** Only scraping 1-2 pages

**Solution:** Check URL patterns:

```json
{
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/.*"],
    "exclude": []  # Clear excludes temporarily
  }
}
```

### Getting Blocked

**Problem:** 429 errors or IP blocking

**Solution:** Increase rate limit:

```json
{
  "rate_limit": 2.0  // Increase from 0.5
}
```

### Dynamic Site Not Rendering

**Problem:** Playwright scraper sees blank pages

**Solution:** Increase wait time and check selectors:

```bash
# Use debug mode to see browser
python3 scrape_docs_dynamic.py --config configs/bun.json --debug

# Check page loads in browser
# Verify selectors in DevTools
```

## Configuration Examples

### React Docs

```json
{
  "name": "react",
  "description": "React JavaScript library for building UIs",
  "base_url": "https://react.dev/",
  "max_pages": 100,
  "rate_limit": 0.5,
  "file_patterns": ["**/*.jsx", "**/*.tsx"],
  "selectors": {
    "main_content": "main",
    "title": "h1"
  }
}
```

### shadcn/ui

```json
{
  "name": "shadcn",
  "description": "Beautifully designed components built with Radix UI",
  "base_url": "https://ui.shadcn.com/docs/",
  "max_pages": 150,
  "rate_limit": 0.8,
  "file_patterns": ["**/*.tsx", "**/*.jsx"],
  "categories": {
    "installation": ["installation", "setup"],
    "components": ["button", "card", "dialog", "form"]
  }
}
```

### Tailwind CSS

```json
{
  "name": "tailwind",
  "description": "Utility-first CSS framework",
  "base_url": "https://tailwindcss.com/docs/",
  "max_pages": 200,
  "rate_limit": 0.5,
  "file_patterns": ["**/*.css", "**/*.jsx", "**/tailwind.config.js"],
  "categories": {
    "core": ["installation", "configuration", "responsive"],
    "layout": ["container", "flex", "grid"],
    "components": ["button", "form", "table"]
  }
}
```

## Adding to Copilot

After generating skill files:

1. **Register in routing map** - Add to `.github/copilot-instructions.md`:

```markdown
#### My Skill Name
**Keywords:** keyword1, keyword2, keyword3
**Suggest:** `/my-skill-name`
**Auto-context:** `.github/instructions/my-skill-name.instructions.md`
```

2. **Test in Copilot** - Use `/my-skill-name` command
3. **Verify file patterns** - Instructions load when editing relevant files

## Workflow Example

```bash
#!/bin/bash
# Complete docs-to-skill workflow

cd .github/copilot-skills/docs-to-skill/scripts

# 1. Create config
cat > ../configs/mylib.json << 'EOF'
{
  "name": "mylib",
  "description": "My Library",
  "base_url": "https://docs.mylib.com/",
  "max_pages": 100,
  "rate_limit": 0.5,
  "file_patterns": ["**/*.ts"]
}
EOF

# 2. Preview
python3 scrape_docs.py --config ../configs/mylib.json --dry-run

# 3. Scrape
python3 scrape_docs.py --config ../configs/mylib.json

# 4. Register (manually edit .github/copilot-instructions.md)

# 5. Test
# Use /mylib in Copilot Chat
```

## Related Skills

- `/create-skill` - Further customize generated skills
- `/document-project` - Document YOUR project (different use case)

## More Information

- **Static Scraper**: `scripts/scrape_docs.py`
- **Dynamic Scraper**: `scripts/scrape_docs_dynamic.py`
- **Configs**: `configs/`
- **Docs List**: `examples/docs.md` (reference URLs)
