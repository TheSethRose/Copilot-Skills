# Docs to Skill - Documentation to Claude Skill Converter

---
name: "Docs to Skill"
description: "Automatically convert documentation websites into production-ready Claude skills"
version: "1.0.0"
tags: ["documentation", "scraping", "skill-generation", "automation", "claude"]
dependencies: ["python3", "requests", "beautifulsoup4"]
attribution: "Based on Skill Seekers by @yusufkaraaslan"
---

Transform ANY documentation website into a structured, production-ready Claude skill in 20-40 minutes.

## Quick Links

- **Slash Command**: `/docs-to-skill`
- **Skill Prompt**: `.github/prompts/docs-to-skill.prompt.md`
- **Instructions**: `.github/instructions/docs-to-skill.instructions.md`
- **Source**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

## What This Skill Does

**Docs to Skill** automates the conversion of documentation websites into Claude skills:

1. **Scrapes** documentation websites automatically
2. **Organizes** content into categorized reference files
3. **Enhances** with AI to extract best examples
4. **Packages** everything into uploadable `.zip` files

## Key Features

- 🌐 **Universal Scraper** - Works with any documentation website
- 🤖 **AI Enhancement** - Transforms basic templates into comprehensive guides
- 📦 **One-Command Packaging** - Ready-to-upload `.zip` files
- 🎯 **Smart Categorization** - Automatically organizes by topic
- 💻 **Code Detection** - Recognizes Python, JavaScript, C++, GDScript, etc.
- 📊 **Page Estimation** - Check size before scraping
- 🔄 **Checkpoint/Resume** - Never lose progress
- 🏗️ **Large Doc Support** - Handle 10K-40K+ pages with splitting
- 🎮 **Router Skills** - Intelligent query routing for split documentation
- 🆓 **FREE Enhancement** - Local AI enhancement using Claude Code Max

## When to Use

- Creating skills for frameworks (React, Vue, Django, FastAPI)
- Generating skills from game engine docs (Godot, Unity)
- Building internal API documentation skills
- Transforming team knowledge bases
- Learning new technologies with comprehensive references

## The 5-Minute Workflow

### Standard Documentation (200-500 pages)

```bash
# 1. Estimate pages (1-2 minutes)
python3 examples/Skill_Seekers/cli/estimate_pages.py \
  examples/Skill_Seekers/configs/react.json

# 2. Scrape documentation (20-40 minutes)
python3 examples/Skill_Seekers/cli/doc_scraper.py \
  --config examples/Skill_Seekers/configs/react.json

# 3. Enhance with AI (60 seconds, FREE)
python3 examples/Skill_Seekers/cli/enhance_skill_local.py \
  examples/Skill_Seekers/output/react/

# 4. Package for upload (instant)
python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/react/

# Result: examples/Skill_Seekers/output/react.zip ready to upload!
```

## Workflow Options

### 1. Preset Configuration (Fastest)

Use pre-configured documentation:

```bash
# Available presets:
# godot, react, vue, django, fastapi, steam, laravel, tailwind

python3 examples/Skill_Seekers/cli/doc_scraper.py \
  --config examples/Skill_Seekers/configs/react.json \
  --enhance-local

python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/react/
```

### 2. Interactive Configuration

Guided wizard for custom documentation:

```bash
python3 examples/Skill_Seekers/cli/doc_scraper.py --interactive
# Prompts for:
# - Skill name, base URL, description
# - CSS selectors (optional)
# - URL patterns (optional)
# - Rate limit, max pages
```

### 3. Custom Command-Line

Specify options directly:

```bash
python3 examples/Skill_Seekers/cli/doc_scraper.py \
  --name tailwind \
  --url https://tailwindcss.com/docs/ \
  --description "Tailwind CSS utility framework" \
  --enhance-local

python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/tailwind/
```

### 4. Large Documentation (10K-40K+ pages)

For massive documentation sites:

```bash
# 1. Estimate
python3 examples/Skill_Seekers/cli/estimate_pages.py \
  examples/Skill_Seekers/configs/godot.json
# Output: ~40,000 pages

# 2. Split into focused sub-skills
python3 examples/Skill_Seekers/cli/split_config.py \
  examples/Skill_Seekers/configs/godot.json \
  --strategy router \
  --target-pages 5000

# 3. Scrape all in parallel (4-8 hours instead of 20-40!)
for config in examples/Skill_Seekers/configs/godot-*.json; do
  python3 examples/Skill_Seekers/cli/doc_scraper.py --config $config &
done
wait

# 4. Generate router skill
python3 examples/Skill_Seekers/cli/generate_router.py \
  examples/Skill_Seekers/configs/godot-*.json

# 5. Package all skills
python3 examples/Skill_Seekers/cli/package_multi.py \
  examples/Skill_Seekers/output/godot*/
```

## Available Tools

### 1. estimate_pages.py

Estimate documentation size before scraping:

```bash
python3 examples/Skill_Seekers/cli/estimate_pages.py CONFIG_FILE
```

**Output**:
```
📊 Estimation Results:
Base URL: https://react.dev/
Discovered URLs: 287
Estimated Total: 250-300 pages
Recommendation: Standard scrape (20-40 min)
```

### 2. doc_scraper.py

Main scraping tool with multiple modes:

```bash
# Preset config
python3 examples/Skill_Seekers/cli/doc_scraper.py --config CONFIG_FILE

# Interactive
python3 examples/Skill_Seekers/cli/doc_scraper.py --interactive

# Quick command
python3 examples/Skill_Seekers/cli/doc_scraper.py --name NAME --url URL

# With options
--dry-run          # Preview without scraping
--resume           # Resume from checkpoint
--enhance-local    # Enhance after scraping (free)
--enhance          # Enhance with API (requires key)
```

### 3. enhance_skill_local.py

FREE AI enhancement using Claude Code Max:

```bash
python3 examples/Skill_Seekers/cli/enhance_skill_local.py OUTPUT_DIR
```

**What it does**:
- Extracts 5-10 best code examples
- Creates comprehensive quick reference
- Adds domain-specific guidance
- Improves navigation instructions
- Backs up original SKILL.md

**Time**: 60 seconds  
**Cost**: Free  
**Quality**: 9/10

### 4. enhance_skill.py

API-based enhancement (requires Anthropic API key):

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 examples/Skill_Seekers/cli/enhance_skill.py OUTPUT_DIR
```

**Cost**: ~$0.15-$0.30 per skill

### 5. package_skill.py

Create uploadable `.zip` file:

```bash
python3 examples/Skill_Seekers/cli/package_skill.py OUTPUT_DIR
```

**Output**: `output/skill-name.zip`

### 6. split_config.py

Split large documentation configs:

```bash
python3 examples/Skill_Seekers/cli/split_config.py CONFIG_FILE --strategy STRATEGY
```

**Strategies**:
- `auto` - Auto-detect best approach
- `category` - Split by doc categories
- `router` - Hub + specialized sub-skills (recommended)
- `size` - Split every N pages

### 7. generate_router.py

Generate router/hub skill:

```bash
python3 examples/Skill_Seekers/cli/generate_router.py PATTERN
```

### 8. package_multi.py

Package multiple skills at once:

```bash
python3 examples/Skill_Seekers/cli/package_multi.py OUTPUT_DIRS
```

## Generated Structure

```
examples/Skill_Seekers/output/
├── skill-name_data/           # Raw scraped data
│   ├── pages/                 # JSON (one per page)
│   ├── summary.json           # Overview
│   └── checkpoint.json        # Resume support
│
└── skill-name/                # The Claude skill
    ├── SKILL.md               # Main file (enhanced)
    ├── SKILL.md.backup        # Original backup
    ├── references/            # Categorized docs
    │   ├── index.md           # Navigation
    │   ├── api.md             # API reference
    │   ├── guides.md          # Tutorials
    │   └── ...                # Auto-categorized
    ├── scripts/               # (empty, for custom)
    └── assets/                # (empty, for templates)
```

## Configuration

### Minimal Config

```json
{
  "name": "my-docs",
  "base_url": "https://docs.example.com/",
  "description": "My documentation skill",
  "rate_limit": 0.5,
  "max_pages": 200
}
```

### Full Config

```json
{
  "name": "my-docs",
  "description": "Comprehensive documentation",
  "base_url": "https://docs.example.com/",
  "start_urls": [
    "https://docs.example.com/guide/",
    "https://docs.example.com/api/"
  ],
  "rate_limit": 0.5,
  "max_pages": 500,
  "selectors": {
    "main_content": "div[role='main']",
    "title": "title",
    "code_blocks": "pre code",
    "navigation": "nav.sidebar"
  },
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/(guide|api)/.*"],
    "exclude": ["^https://docs\\.example\\.com/blog/.*"]
  },
  "checkpoint": {
    "enabled": true,
    "interval": 1000
  },
  "split_config": {
    "target_pages_per_skill": 5000,
    "create_router": true,
    "split_by_categories": ["api", "guides", "tutorials"]
  }
}
```

## Available Presets

Check `examples/Skill_Seekers/configs/` for ready-to-use configurations:

- **godot.json** - Godot game engine (40K pages)
- **react.json** - React documentation
- **vue.json** - Vue.js documentation
- **django.json** - Django web framework
- **fastapi.json** - FastAPI documentation
- **steam.json** - Steam Web API
- **laravel.json** - Laravel PHP framework
- **tailwind.json** - Tailwind CSS

## Features in Detail

### Smart Categorization

Automatically organizes content by:
- URL structure analysis
- Page title patterns
- Content keywords
- Category scoring

**Common categories**: api, guides, tutorials, reference, getting_started, advanced

### Code Language Detection

Auto-detects and annotates:
- Python, JavaScript, TypeScript
- C++, GDScript, Go, Rust
- Java, C#, PHP, Ruby
- And more...

### Checkpoint/Resume

- Auto-saves every N pages
- Stores visited URLs and progress
- Resume with `--resume` flag
- Never lose progress

### Large Documentation Support

- Split strategies for focused skills
- Parallel scraping
- Router skills for intelligent routing
- Handles 10K-40K+ pages

### AI Enhancement

Transforms 75-line templates into 500+ line comprehensive guides:
- Extracts best code examples
- Creates practical quick reference
- Adds navigation guidance
- Domain-specific triggers
- Quality: 9/10

## Examples

### Example 1: React Documentation

```bash
# Estimate
python3 examples/Skill_Seekers/cli/estimate_pages.py \
  examples/Skill_Seekers/configs/react.json
# Output: ~250 pages

# Scrape with local enhancement
python3 examples/Skill_Seekers/cli/doc_scraper.py \
  --config examples/Skill_Seekers/configs/react.json \
  --enhance-local

# Package
python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/react/

# Result: examples/Skill_Seekers/output/react.zip
```

### Example 2: Custom Internal Docs

```bash
# Interactive configuration
python3 examples/Skill_Seekers/cli/doc_scraper.py --interactive
# Enter:
# - name: company-api
# - url: https://docs.company.com/
# - description: Internal API documentation
# - max_pages: 150

# Enhance
python3 examples/Skill_Seekers/cli/enhance_skill_local.py \
  examples/Skill_Seekers/output/company-api/

# Package
python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/company-api/
```

### Example 3: Godot (Large Documentation)

```bash
# Split
python3 examples/Skill_Seekers/cli/split_config.py \
  examples/Skill_Seekers/configs/godot.json \
  --strategy router

# Scrape all in parallel
for config in examples/Skill_Seekers/configs/godot-*.json; do
  python3 examples/Skill_Seekers/cli/doc_scraper.py --config $config &
done
wait

# Generate router
python3 examples/Skill_Seekers/cli/generate_router.py \
  examples/Skill_Seekers/configs/godot-*.json

# Package all
python3 examples/Skill_Seekers/cli/package_multi.py \
  examples/Skill_Seekers/output/godot*/
```

## Quality Standards

### Documentation Standards

**Before Scraping**:
- Check `robots.txt`
- Estimate page count
- Test with `--dry-run`
- Enable checkpoints for >1000 pages

**During Scraping**:
- Monitor progress
- Respect rate limits
- Check for errors

**After Scraping**:
- Always enhance SKILL.md
- Review generated content
- Test package

### Best Practices

✅ Always estimate first  
✅ Use local enhancement (free)  
✅ Enable checkpoints for long scrapes  
✅ Split documentation >10K pages  
✅ Test with presets first  
✅ Respect `robots.txt`  
✅ Package before uploading

❌ Don't skip estimation  
❌ Don't ignore rate limits  
❌ Don't scrape non-documentation  
❌ Don't skip enhancement

## Troubleshooting

### "Too many pages"
```bash
python3 examples/Skill_Seekers/cli/split_config.py CONFIG --strategy router
```

### "Scrape interrupted"
```bash
python3 examples/Skill_Seekers/cli/doc_scraper.py --config CONFIG --resume
```

### "Enhancement failed"
```bash
mv examples/Skill_Seekers/output/SKILL/SKILL.md.backup \
   examples/Skill_Seekers/output/SKILL/SKILL.md
```

### "Rate limit exceeded"
```json
{"rate_limit": 1.0}  // Increase in config
```

## Integration with Other Skills

- `/create-skill` - Customize generated skills
- `/document-project` - Document YOUR project (different use case)
- `/git-ops` - Commit generated skills

## Performance

- **Standard docs** (200-500 pages): 20-40 minutes
- **Large docs** (10K-40K pages): 4-8 hours with splitting
- **Enhancement**: 60 seconds (local) or API call
- **Packaging**: Instant

## Attribution

This skill is based on [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) by [@yusufkaraaslan](https://github.com/yusufkaraaslan).

**License**: MIT (both Skill Seekers and this skill)

## Files in This Directory

```
docs-to-skill/
├── README.md (this file)
├── workflows.md (detailed workflows)
├── configs.md (configuration reference)
├── enhancement.md (AI enhancement guide)
├── large-docs.md (large documentation strategies)
└── scripts/
    └── (wrappers for Skill Seekers tools)
```

## Getting Started

1. Ensure Skill Seekers is in `examples/Skill_Seekers/`
2. Run `/docs-to-skill`
3. Choose workflow (preset, interactive, custom)
4. Estimate pages
5. Scrape documentation
6. Enhance with AI
7. Package and upload

## Support

- 💬 Questions? Use `/docs-to-skill` command
- 📖 Details? See `.github/instructions/docs-to-skill.instructions.md`
- 🔍 Examples? Check `examples/Skill_Seekers/`
- 🌐 Skill Seekers: https://github.com/yusufkaraaslan/Skill_Seekers

---

**Ready to convert documentation?** Run `/docs-to-skill` and transform any docs into a Claude skill!
