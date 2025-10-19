---
description: Auto-loaded guidance for converting documentation websites into Claude skills
---

# Docs to Skill - Instructions

When working with documentation scraping, skill generation, or queries containing "docs to skill" or "documentation converter", this context activates.

## Core Purpose

Transform ANY documentation website into a production-ready Claude skill automatically. Scrape, organize, enhance, and package documentation using the Skill Seekers toolchain.

**Key Distinction**: This skill GENERATES Claude skills from documentation. For project documentation, use `/document-project`.

## Default Behaviors

### When user mentions "docs to skill" or "scrape docs"
1. Suggest `/docs-to-skill` skill
2. Check if Skill Seekers is available in `examples/Skill_Seekers/`
3. Determine workflow: preset, interactive, or custom
4. Estimate page count before scraping
5. Recommend enhancement after scraping

### When user has documentation URL
1. Suggest creating config file
2. Run page estimation first
3. Choose appropriate workflow based on page count:
   - <500 pages: Standard scrape
   - 500-10K pages: Standard with checkpoint
   - >10K pages: Split strategy recommended

### When analyzing documentation sites
1. Check `robots.txt` compliance
2. Estimate total pages
3. Identify documentation structure
4. Recommend selectors and patterns
5. Suggest appropriate rate limiting

## Quality Guidelines

### ✅ Do
- Always estimate page count before scraping
- Use presets when available (React, Godot, Django, etc.)
- Enable checkpoints for scrapes >1000 pages
- Use local enhancement (free, fast, high quality)
- Split documentation >10K pages
- Respect `robots.txt` and rate limits
- Test with `--dry-run` first
- Package skills before uploading

### ❌ Don't
- Scrape without estimating first
- Skip enhancement (75-line vs 500-line SKILL.md)
- Ignore robots.txt or rate limits
- Set rate_limit <0.3 seconds
- Scrape non-documentation content
- Generate skills for this Copilot Skills system itself
- Overwrite existing skills without backup

## Workflow Templates

### Standard Workflow (200-500 pages)
```bash
# 1. Estimate (1-2 minutes)
python3 examples/Skill_Seekers/cli/estimate_pages.py examples/Skill_Seekers/configs/react.json

# 2. Scrape (20-40 minutes)
python3 examples/Skill_Seekers/cli/doc_scraper.py --config examples/Skill_Seekers/configs/react.json

# 3. Enhance (60 seconds)
python3 examples/Skill_Seekers/cli/enhance_skill_local.py examples/Skill_Seekers/output/react/

# 4. Package (instant)
python3 examples/Skill_Seekers/cli/package_skill.py examples/Skill_Seekers/output/react/

# Result: examples/Skill_Seekers/output/react.zip ready to upload!
```

### Large Documentation Workflow (10K-40K+ pages)
```bash
# 1. Estimate
python3 examples/Skill_Seekers/cli/estimate_pages.py examples/Skill_Seekers/configs/godot.json
# Output: ~40,000 pages

# 2. Split into focused sub-skills
python3 examples/Skill_Seekers/cli/split_config.py \
  examples/Skill_Seekers/configs/godot.json \
  --strategy router \
  --target-pages 5000

# 3. Scrape all in parallel
for config in examples/Skill_Seekers/configs/godot-*.json; do
  python3 examples/Skill_Seekers/cli/doc_scraper.py --config $config &
done
wait

# 4. Generate router skill
python3 examples/Skill_Seekers/cli/generate_router.py examples/Skill_Seekers/configs/godot-*.json

# 5. Package all
python3 examples/Skill_Seekers/cli/package_multi.py examples/Skill_Seekers/output/godot*/
```

### Interactive Custom Workflow
```bash
# 1. Interactive configuration
python3 examples/Skill_Seekers/cli/doc_scraper.py --interactive
# Wizard guides through:
# - Skill name, base URL, description
# - CSS selectors, URL patterns
# - Rate limiting, max pages

# 2. Estimate
python3 examples/Skill_Seekers/cli/estimate_pages.py examples/Skill_Seekers/configs/my-docs.json

# 3. Scrape
python3 examples/Skill_Seekers/cli/doc_scraper.py --config examples/Skill_Seekers/configs/my-docs.json

# 4. Enhance
python3 examples/Skill_Seekers/cli/enhance_skill_local.py examples/Skill_Seekers/output/my-docs/

# 5. Package
python3 examples/Skill_Seekers/cli/package_skill.py examples/Skill_Seekers/output/my-docs/
```

## Configuration Schema

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
  "description": "Comprehensive documentation skill",
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
  "split_strategy": "auto",
  "split_config": {
    "target_pages_per_skill": 5000,
    "create_router": true
  }
}
```

## Available Scripts

### estimate_pages.py
**Purpose**: Estimate page count before scraping

```bash
python3 examples/Skill_Seekers/cli/estimate_pages.py CONFIG_FILE [--max-discovery N]
```

**Output**:
```
📊 Estimation Results:
Base URL: https://react.dev/
Discovered URLs: 287
Estimated Total: 250-300 pages
Recommendation: Standard scrape (20-40 min)
```

### doc_scraper.py
**Purpose**: Main scraping tool

```bash
python3 examples/Skill_Seekers/cli/doc_scraper.py [OPTIONS]
```

**Options**:
- `--config FILE` - Load from config file
- `--interactive` - Interactive wizard
- `--name NAME` - Skill name
- `--url URL` - Base URL
- `--dry-run` - Preview without scraping
- `--resume` - Resume from checkpoint
- `--enhance-local` - Enhance after scraping (local)
- `--enhance` - Enhance after scraping (API, requires key)

### enhance_skill_local.py
**Purpose**: AI enhancement using Claude Code Max (FREE)

```bash
python3 examples/Skill_Seekers/cli/enhance_skill_local.py OUTPUT_DIR
```

**What it does**:
- Reads reference files
- Opens Claude Code in new terminal
- Extracts best 5-10 code examples
- Creates comprehensive SKILL.md
- Backs up original

**Time**: 60 seconds  
**Cost**: Free (uses Claude Code Max plan)

### enhance_skill.py
**Purpose**: AI enhancement using Anthropic API

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 examples/Skill_Seekers/cli/enhance_skill.py OUTPUT_DIR
```

**Cost**: ~$0.15-$0.30 per skill

### package_skill.py
**Purpose**: Create uploadable .zip file

```bash
python3 examples/Skill_Seekers/cli/package_skill.py OUTPUT_DIR
```

**Output**: `output/skill-name.zip`

### split_config.py
**Purpose**: Split large documentation configs

```bash
python3 examples/Skill_Seekers/cli/split_config.py CONFIG_FILE --strategy STRATEGY
```

**Strategies**:
- `auto` - Intelligently detect best strategy
- `category` - Split by documentation categories
- `router` - Create hub + specialized sub-skills (recommended)
- `size` - Split every N pages

### generate_router.py
**Purpose**: Generate router/hub skill

```bash
python3 examples/Skill_Seekers/cli/generate_router.py PATTERN
```

**Example**:
```bash
python3 examples/Skill_Seekers/cli/generate_router.py examples/Skill_Seekers/configs/godot-*.json
```

## Generated Structure

```
examples/Skill_Seekers/output/
├── skill-name_data/          # Raw scraped data
│   ├── pages/                # JSON files (one per page)
│   ├── summary.json          # Overview
│   └── checkpoint.json       # Resume checkpoint
│
└── skill-name/               # The Claude skill
    ├── SKILL.md              # Main skill file (enhanced)
    ├── SKILL.md.backup       # Original (pre-enhancement)
    ├── references/           # Categorized documentation
    │   ├── index.md          # Navigation index
    │   ├── api.md            # API reference
    │   ├── guides.md         # Tutorials/guides
    │   └── ...               # Auto-categorized
    ├── scripts/              # (empty, for custom tools)
    └── assets/               # (empty, for templates)
```

## Features

### Smart Categorization
Automatically organizes content by:
- URL structure analysis
- Page title patterns
- Content keywords
- Category scoring

**Example categories**: api, guides, tutorials, reference, getting_started, advanced

### Code Language Detection
Auto-detects and annotates:
- Python (`def`, `import`, `from`)
- JavaScript (`const`, `let`, `=>`, `function`)
- TypeScript (`.ts`, type annotations)
- GDScript (`func`, `var`, `extends`)
- C++ (`#include`, `int main`, `::`)
- Go (`package`, `func`, `import`)
- Rust (`fn`, `let`, `impl`)
- And more...

### Checkpoint/Resume System
- Auto-saves every N pages (configurable)
- Stores: visited URLs, scraped pages, progress
- Resume with `--resume` flag
- Never lose progress on long scrapes

### Large Documentation Support
Handle 10K-40K+ pages:
- **Split strategies** for focused sub-skills
- **Parallel scraping** for faster completion
- **Router skills** for intelligent query routing
- **Target pages per skill** configurable

## Enhancement Details

### What Enhancement Does
1. Reads all reference files (api.md, guides.md, etc.)
2. Analyzes documentation structure
3. Extracts 5-10 best code examples
4. Creates practical quick reference
5. Writes domain-specific triggers
6. Adds navigation guidance
7. Backs up original SKILL.md

### Before Enhancement (Auto-Generated)
```markdown
## Quick Reference

### Common Patterns

*Quick reference patterns will be added as you use the skill.*
```

**Length**: ~75 lines

### After Enhancement (AI-Powered)
```markdown
## Quick Reference

### Common Patterns

**1. Create a Component**
```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

**2. Use State Hook**
```javascript
const [count, setCount] = useState(0);
```

...10 more practical examples...
```

**Length**: ~500+ lines  
**Quality**: 9/10 based on testing

## Common Patterns

### Pattern 1: Quick Preset Scrape
```bash
# For known documentation
python3 examples/Skill_Seekers/cli/doc_scraper.py \
  --config examples/Skill_Seekers/configs/react.json \
  --enhance-local

python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/react/
```

### Pattern 2: Custom Documentation
```bash
# Interactive config
python3 examples/Skill_Seekers/cli/doc_scraper.py --interactive

# Estimate
python3 examples/Skill_Seekers/cli/estimate_pages.py examples/Skill_Seekers/configs/custom.json

# Scrape with checkpoint
python3 examples/Skill_Seekers/cli/doc_scraper.py \
  --config examples/Skill_Seekers/configs/custom.json

# Enhance locally
python3 examples/Skill_Seekers/cli/enhance_skill_local.py \
  examples/Skill_Seekers/output/custom/

# Package
python3 examples/Skill_Seekers/cli/package_skill.py \
  examples/Skill_Seekers/output/custom/
```

### Pattern 3: Large Documentation (Router Strategy)
```bash
# Estimate first
python3 examples/Skill_Seekers/cli/estimate_pages.py examples/Skill_Seekers/configs/large.json
# Output: 25,000 pages

# Split with router
python3 examples/Skill_Seekers/cli/split_config.py \
  examples/Skill_Seekers/configs/large.json \
  --strategy router \
  --target-pages 5000

# Scrape all in parallel
for config in examples/Skill_Seekers/configs/large-*.json; do
  python3 examples/Skill_Seekers/cli/doc_scraper.py --config $config &
done
wait

# Generate router
python3 examples/Skill_Seekers/cli/generate_router.py \
  examples/Skill_Seekers/configs/large-*.json

# Package all
python3 examples/Skill_Seekers/cli/package_multi.py \
  examples/Skill_Seekers/output/large*/
```

## Error Handling

### "No such file or directory"
```bash
# Ensure Skill Seekers is in examples/
ls examples/Skill_Seekers/
# If missing, user needs to clone it
```

### "Too many pages estimated"
```bash
# Use splitting
python3 examples/Skill_Seekers/cli/split_config.py CONFIG --strategy router
```

### "Scrape interrupted"
```bash
# Resume from checkpoint
python3 examples/Skill_Seekers/cli/doc_scraper.py --config CONFIG --resume
```

### "Enhancement failed"
```bash
# Restore backup
mv examples/Skill_Seekers/output/SKILL/SKILL.md.backup \
   examples/Skill_Seekers/output/SKILL/SKILL.md

# Try local enhancement
python3 examples/Skill_Seekers/cli/enhance_skill_local.py examples/Skill_Seekers/output/SKILL/
```

### "Rate limit exceeded"
```bash
# Increase rate_limit in config
"rate_limit": 1.0  # seconds between requests
```

### "robots.txt disallows"
```bash
# Check robots.txt first
curl https://docs.example.com/robots.txt

# Respect restrictions or contact site owner
```

## Best Practices

### Before Scraping
1. Check `robots.txt` for restrictions
2. Estimate page count
3. Start with lower `max_pages` for testing
4. Use `--dry-run` to preview
5. Enable checkpoints for >1000 pages

### During Scraping
1. Monitor progress in terminal
2. Check for errors in output
3. Respect rate limits
4. Don't interrupt unnecessarily

### After Scraping
1. Always enhance SKILL.md (local or API)
2. Review generated content
3. Test package before uploading
4. Document custom selectors used

### For Large Documentation
1. Always split >10K pages
2. Use router strategy
3. Scrape sub-skills in parallel
4. Generate router last
5. Package all together

## Integration with Other Skills

### With /create-skill
```bash
# After generating skill, customize it
/create-skill
# Modify SKILL.md, add custom scripts
```

### With /document-project
```bash
# Document YOUR project, not convert external docs
/document-project
```

### With /git-ops
```bash
# Commit generated skills
git add examples/Skill_Seekers/output/my-skill.zip
git commit -m "feat: add my-skill Claude skill"
```

## Performance Tips

### Faster Scraping
- Use parallel scraping for split configs
- Enable checkpoint for resume capability
- Set appropriate `rate_limit` (0.3-0.5)
- Limit `max_pages` for testing

### Better Quality
- Always use enhancement (local or API)
- Choose meaningful skill names
- Write clear descriptions
- Test selectors with `--dry-run`

### Resource Usage
- Monitor disk space (scraped data can be large)
- Use `--skip-scrape` to regenerate without re-scraping
- Clean old data: `rm -rf examples/Skill_Seekers/output/*_data/`

## Self-Awareness Rule

**CRITICAL**: This skill NEVER generates skills for:
- This Copilot Skills system
- Skill architecture documentation
- This skill's own implementation
- Other skills in this repository

The Copilot Skills system has its own documentation in:
- `.github/copilot-instructions.md`
- `.github/copilot-skills/README.md`

## Conventional Commits

When committing generated skills:

```bash
# New skill generated
git commit -m "feat(skills): add react-docs Claude skill"

# Update existing
git commit -m "docs(skills): update godot-docs with latest documentation"

# Fix skill
git commit -m "fix(skills): correct vue-docs selectors"
```

## Related Resources

- **Skill Seekers**: https://github.com/yusufkaraaslan/Skill_Seekers
- **Skill Directory**: `.github/copilot-skills/docs-to-skill/`
- **Scripts**: `.github/copilot-skills/docs-to-skill/scripts/`
- **Examples**: `examples/Skill_Seekers/`

---

**Key Principle**: Always estimate first, enhance after scraping, and respect documentation site policies.
