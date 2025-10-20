# Docs-to-Skill: Scraping and Generation Guide

This guide documents the process of converting external documentation into Copilot Skills using the `docs-to-skill` system.

## Overview

The `docs-to-skill` skill automates the creation of Copilot Skills from documentation websites. It scrapes documentation, organizes it by category, and generates skill files following the Copilot Skills Architecture.

**Key Files:**
- Scraper: `.github/copilot-skills/docs-to-skill/scripts/scrape_docs.py`
- Configs: `.github/copilot-skills/docs-to-skill/configs/`
- Output: `.github/copilot-skills/{skillname}/`

## How It Works

### Step 1: Create Configuration

Create a JSON config file in `.github/copilot-skills/docs-to-skill/configs/`:

```json
{
  "name": "example",
  "description": "Brief description",
  "base_url": "https://docs.example.com/",
  "start_urls": ["https://docs.example.com/getting-started"],
  "max_pages": 150,
  "rate_limit": 1.0,
  "file_patterns": ["**/*.tsx", "**/*.jsx"],
  "selectors": {
    "title": "h1, title",
    "main_content": "main, article",
    "code_blocks": "pre code"
  },
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/.*"],
    "exclude": ["#.*", "/blog/.*"]
  },
  "categories": {
    "getting_started": ["installation", "setup"],
    "guides": ["guide", "how-to"]
  },
  "checkpoint": {
    "enabled": true,
    "interval": 40
  }
}
```

**Configuration Fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Short identifier, lowercase, no spaces |
| `description` | ✅ | One-sentence purpose |
| `base_url` | ✅ | Documentation root URL |
| `start_urls` | ✅ | Array of starting pages to crawl |
| `max_pages` | ✅ | Maximum pages to scrape (50-200 recommended) |
| `rate_limit` | ✅ | Seconds between requests (0.5-1.0) |
| `file_patterns` | ❌ | When to auto-load instructions |
| `selectors` | ✅ | CSS selectors for content extraction |
| `url_patterns` | ❌ | Include/exclude URL regex patterns |
| `categories` | ❌ | Keyword-based category detection |
| `checkpoint` | ❌ | Save progress every N pages |

### Step 2: Test with Dry Run

Preview what will be scraped without actually scraping:

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/example.json \
  --dry-run
```

Output shows:
- Number of pages that will be scraped
- Generated file structure
- Sample prompt files

### Step 3: Generate Skill

Run the full generation:

```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/example.json
```

Generation produces:
- `.github/prompts/{name}.skill.prompt.md` - Executable skill prompt
- `.github/instructions/{name}.instructions.md` - Auto-loaded instructions
- `.github/copilot-skills/{name}/patterns.md` - Common code patterns
- `.github/copilot-skills/{name}/reference.md` - Documentation overview
- `.github/copilot-skills/{name}/references/*.md` - Organized by category

### Step 4: Register Skill

Add to keyword routing map in `.github/copilot-instructions.md`:

```markdown
#### Example Framework
**Keywords**: example, framework, example-docs
**Suggest**: `/example`
**Auto-context**: `.github/instructions/example.instructions.md`
**Skill**: `.github/copilot-skills/example/`
```

## Tested Documentation Sites

### ✅ Working Sites (Successful Scraping)

| Site | Framework | Pages | Status |
|------|-----------|-------|--------|
| Headless UI | React/Vue | 27 | ✅ Generated |
| Ant Design | React | 22 | ✅ Generated |
| React | JavaScript | ~80 | 🔄 In Progress |
| Next.js | React | ~100+ | 🔄 In Progress |
| Vue | JavaScript | ~50+ | 🔄 In Progress |
| Prisma | ORM | ~100+ | 🔄 In Progress |
| Supabase | Firebase Alt | ~80+ | ⏳ Tested |
| Mantine | React | 150 | ⏳ Tested (limit) |
| FastAPI | Python | ~50+ | ⏳ Tested |
| LangChain | Python AI | ~80+ | ⏳ Tested |

### ❌ Anti-Scraping Sites

These sites have protections and require special handling:

| Site | Issue | Solution |
|------|-------|----------|
| Tailwind CSS | Redirects/Anti-scraping | Manual URL list + Firecrawl |
| DaisyUI | Limited pages returned | Check CSS selectors |
| Chakra UI | Only 1 page | Update start URL |
| OpenAI API | Only 1 page | Likely has redirects |

## Common Issues & Solutions

### Issue: Only 1-2 pages scraped

**Cause:** Site redirects or CSS selectors don't match content

**Solution:**
1. Check actual site structure in browser
2. Update `start_urls` to more specific page
3. Inspect `selectors.main_content` CSS selector
4. Try alternative selectors: `"main, article, .content, [role='main']"`

### Issue: KeyboardInterrupt during scraping

**Cause:** Process interrupted (Ctrl+C or timeout)

**Solution:**
Resume with checkpoint flag:
```bash
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config configs/example.json \
  --resume
```

### Issue: Rate limit too high

**Cause:** Getting blocked by server

**Solution:**
1. Increase `rate_limit` to 1.5-2.0 seconds
2. Add delays between checkpoint intervals
3. Use Firecrawl API for reliable scraping

### Issue: Content extraction empty

**Cause:** CSS selectors don't match page structure

**Solution:**
1. Inspect page with browser DevTools
2. Test selectors in console: `document.querySelectorAll('main')`
3. Try more generic selectors

## Performance & Time Estimates

Based on actual runs:

- **Small docs (20-30 pages):** 30 seconds - 2 minutes
- **Medium docs (50-100 pages):** 5-15 minutes
- **Large docs (100-200 pages):** 15-30 minutes
- **Very large docs (200+ pages):** 30-60+ minutes

**Factors affecting speed:**
- Site response time
- Number of pages to scrape
- `rate_limit` setting (higher = slower but more respectful)
- Network speed
- Server load

## Handling Anti-Scraping Sites

For sites like Tailwind that have protection mechanisms:

### Option 1: Use Firecrawl API
```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="your-key")
result = app.scrapeUrl(url, {"formats": ["markdown"]})
```

Requires: Firecrawl subscription (~$20+/month)

### Option 2: Manual URL Lists
1. Create `.github/copilot-skills/docs-to-skill/url-lists/{name}-urls.md`
2. List all documentation URLs
3. Modify scraper to read URL list instead of crawling

Example: See `.github/copilot-skills/docs-to-skill/url-lists/tailwind-v4-urls.md`

### Option 3: Skip Anti-Scraping Sites
Document as "manual skill creation recommended"

## Batch Processing

Generate multiple skills sequentially:

```bash
#!/bin/bash
configs=("react" "nextjs" "vue" "prisma" "supabase")

for config in "${configs[@]}"; do
  echo "Generating: $config"
  python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
    --config .github/copilot-skills/docs-to-skill/configs/${config}.json
done
```

Or run in background:
```bash
nohup ./batch_generate_skills.sh > generation.log 2>&1 &
```

## Debugging

### Check logs
```bash
tail -f ./output/skill_generation_logs/*.log
```

### Check scrape data
```bash
ls -la ./output/{name}_data/
cat ./output/{name}_data/checkpoint.json
```

### Validate generated skills
```bash
# Check skill prompt syntax
head -20 .github/prompts/{name}.skill.prompt.md

# Check references were created
ls -la .github/copilot-skills/{name}/references/
```

## Best Practices

### ✅ Do

- **Test with dry-run first** - Preview before scraping
- **Use appropriate rate limits** - 0.5-1.5 seconds between requests
- **Enable checkpoints** - Resume interrupted scrapes
- **Specify start URLs carefully** - Use specific documentation entry points
- **Keep max_pages reasonable** - 100-150 is usually sufficient
- **Test CSS selectors** - Verify with browser DevTools before running
- **Respect site policies** - Check robots.txt and terms of service

### ❌ Don't

- **Skip dry-run** - Could waste time scraping wrong site
- **Use rate_limit < 0.3** - May get blocked by server
- **Scrape entire web** - Set max_pages limit
- **Ignore checkpoints** - Could lose progress on large scrapes
- **Scrape against robots.txt** - Check site policies first
- **Parse blog/marketing content** - Use `url_patterns.exclude`

## Adding New Skills

1. **Create config** in `.github/copilot-skills/docs-to-skill/configs/{name}.json`
2. **Test dry-run**: `--dry-run` flag
3. **Fix issues**: Update selectors, start URLs, patterns
4. **Generate**: Run full scrape (go get coffee ☕)
5. **Register**: Add to `.github/copilot-instructions.md` routing map
6. **Delete if needed**: Remove old version with `rm -rf .github/copilot-skills/{name}`

## Current Status

**Completed:** 2 skills (Headless UI, Ant Design)  
**In Progress:** 3 skills (React, Next.js, Vue, Prisma, etc.)  
**Ready:** 10+ configs tested and working  
**Skipped:** 5 sites with anti-scraping (Tailwind, OpenAI, etc.)

See `SKILL_GENERATION_PROGRESS.md` for detailed status.

## References

- **Scraper**: `.github/copilot-skills/docs-to-skill/scripts/scrape_docs.py`
- **Examples**: Example skills in `.github/copilot-skills/docs-to-skill/configs/`
- **Architecture**: `.github/copilot-skills/README.md`
- **Progress**: `SKILL_GENERATION_PROGRESS.md`
- **Inspiration**: https://github.com/Saraceni/TailwindCSSAiAgent
