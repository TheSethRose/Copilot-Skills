---
description: Convert any documentation website into a production-ready Claude skill
---

# Docs to Skill

**Slash Command**: `/docs-to-skill`  
**Purpose**: Transform documentation websites into structured, uploadable Claude skills

## When to Use This Skill

Use `/docs-to-skill` when you need to:

- 📚 Convert framework documentation (React, Vue, Django) into Claude skills
- 🎮 Create skills from game engine docs (Godot, Unity)
- 🔧 Generate skills from API documentation
- 📖 Transform internal company docs into searchable skills
- 🚀 Build comprehensive reference skills for any technology

**Keywords**: docs, documentation site, scrape docs, doc to skill, generate skill, claude skill, documentation converter

## Quick Start

Run `/docs-to-skill` to begin. Choose your workflow:

1. **Preset** - Use pre-configured setups (React, Godot, Django, etc.)
2. **Interactive** - Guided configuration wizard
3. **Custom** - Specify URL and options directly
4. **Large Docs** - Handle 10K-40K+ page documentation with intelligent splitting

## The 4-Phase Workflow

### Phase 1: Configuration

Choose your approach:

**Option A: Use Preset** (Fastest)
```bash
# Available presets: godot, react, vue, django, fastapi, tailwind
/docs-to-skill --preset react
```

**Option B: Interactive Mode**
```bash
/docs-to-skill --interactive
# Wizard prompts for:
# - Skill name
# - Documentation URL
# - Description
# - Max pages
# - Rate limiting
```

**Option C: Quick Command**
```bash
/docs-to-skill --url https://react.dev/ --name react
```

### Phase 2: Estimation

Before scraping, estimate page count:

```bash
# Quick estimate (1-2 minutes)
.github/copilot-skills/docs-to-skill/scripts/quick_estimate.sh react.json

# Output (JSON):
{
  "estimated_pages": 150,
  "recommended_max": 180,
  "strategy": "standard",
  "time_estimate": "15-20 minutes"
}
```

**For large documentation (10K+ pages)**:
- Auto-suggests splitting into sub-skills
- Recommends router strategy
- Estimates parallel scraping time

### Phase 3: Generation

Scrape and build the skill:

**Standard Documentation (<1000 pages)**:
```bash
/docs-to-skill --generate --config configs/react.json
```

**Large Documentation (10K-40K pages)**:
```bash
# 1. Split into focused sub-skills
/docs-to-skill --split configs/godot.json --strategy router

# Creates:
# - godot-scripting.json (5K pages)
# - godot-2d.json (8K pages)
# - godot-3d.json (10K pages)
# - etc.

# 2. Scrape all in parallel (4-8 hours instead of 20-40!)
/docs-to-skill --generate-parallel configs/godot-*.json

# 3. Generate intelligent router skill
/docs-to-skill --create-router configs/godot-*.json
```

**What Gets Created**:
```
output/
├── {skill}_data/              # Raw scraped data
│   ├── pages/                # JSON per page
│   └── summary.json          # Overview
│
└── {skill}/                   # The Claude skill
    ├── SKILL.md              # Main skill file
    ├── references/           # Categorized documentation
    │   ├── index.md
    │   ├── getting_started.md
    │   ├── api_reference.md
    │   └── [categories].md
    ├── scripts/              # Empty (user adds custom)
    └── assets/               # Empty (user adds custom)
```

### Phase 4: Enhancement & Packaging

**AI Enhancement** (Recommended):
```bash
# Option 1: Local enhancement (FREE - uses Claude Code Max)
/docs-to-skill --enhance-local output/react/

# Option 2: API enhancement (~$0.15-$0.30, requires API key)
/docs-to-skill --enhance output/react/ --api-key sk-ant-...
```

**What Enhancement Does**:
- Analyzes reference documentation
- Extracts 5-10 best code examples
- Creates comprehensive quick reference
- Adds domain-specific triggers
- Provides navigation guidance
- Transforms basic templates into 500+ line guides

**Package for Upload**:
```bash
/docs-to-skill --package output/react/

# Output: output/react.zip
# Ready to upload to Claude!
```

## Key Features

### 1. Universal Scraper
Works with ANY documentation website:
- Automatically detects content structure
- Respects robots.txt
- Handles JavaScript-rendered content
- Smart categorization

### 2. Smart Categorization
Automatically organizes content:
- API references
- Getting started guides
- Tutorials
- Advanced topics
- By URL structure and content keywords

### 3. Code Language Detection
Recognizes and annotates:
- Python, JavaScript, TypeScript
- C++, C#, Go, Rust
- GDScript (Godot)
- And more...

### 4. Large Documentation Support
Handle massive documentation sites:
- **Split Strategy**: Auto, category, router, size
- **Parallel Scraping**: Process multiple skills simultaneously
- **Router Skills**: Intelligent routing to specialized sub-skills
- **Checkpoint/Resume**: Never lose progress on long scrapes

### 5. AI-Powered Enhancement
Two enhancement options:
- **Local** (FREE): Uses Claude Code Max plan, no API key
- **API** ($0.15-$0.30): Uses Anthropic API

Both transform basic templates into comprehensive guides with:
- Real code examples from docs
- Key concepts explained
- Navigation guidance
- Best practices

### 6. Caching System
Scrape once, rebuild instantly:
- Raw data cached in `{skill}_data/`
- Rebuild skills from cache without re-scraping
- Update configurations and regenerate

### 7. Checkpoint/Resume
Never lose progress:
- Automatic checkpoints every 1000 pages
- Resume interrupted scrapes
- Progress tracking and ETA

## Configuration Schema

```json
{
  "name": "react",
  "description": "React framework for building user interfaces",
  "base_url": "https://react.dev/",
  "start_urls": ["https://react.dev/learn", "https://react.dev/reference"],
  "max_pages": 200,
  "rate_limit": 0.5,
  "selectors": {
    "main_content": "div[role='main']",
    "title": "title",
    "code_blocks": "pre code"
  },
  "url_patterns": {
    "include": ["/learn/", "/reference/"],
    "exclude": ["/blog/", "/community/"]
  },
  "checkpoint": {
    "enabled": true,
    "interval": 1000
  }
}
```

## Available Presets

Pre-configured for popular documentation:

| Preset | Pages | Category | Time |
|--------|-------|----------|------|
| **react** | ~200 | Frontend | 20-30 min |
| **vue** | ~150 | Frontend | 15-20 min |
| **godot** | ~40K | Game Engine | 20-40 hours (split recommended) |
| **django** | ~500 | Backend | 45-60 min |
| **fastapi** | ~300 | Backend | 30-40 min |
| **tailwind** | ~250 | CSS | 25-35 min |

## Workflow Examples

### Example 1: React Documentation

```bash
# 1. Estimate
/docs-to-skill --estimate configs/react.json
# → ~200 pages, 20-30 minutes

# 2. Generate with enhancement
/docs-to-skill --generate --enhance-local configs/react.json
# → Creates output/react/ with enhanced SKILL.md

# 3. Package
/docs-to-skill --package output/react/
# → Creates output/react.zip

# 4. Upload to Claude
# → Done!
```

### Example 2: Large Documentation (Godot 40K Pages)

```bash
# 1. Estimate
/docs-to-skill --estimate configs/godot.json
# → ⚠️  40,000 pages detected! Recommend splitting.

# 2. Auto-split with router strategy
/docs-to-skill --split configs/godot.json --strategy router --target-pages 5000

# Creates 5 focused sub-skills:
# - godot-scripting.json (5K pages)
# - godot-2d.json (8K pages)
# - godot-3d.json (10K pages)
# - godot-physics.json (6K pages)
# - godot-shaders.json (11K pages)

# 3. Scrape all in parallel
/docs-to-skill --generate-parallel configs/godot-*.json
# → 4-8 hours (parallel) instead of 20-40 hours (serial)

# 4. Generate router skill
/docs-to-skill --create-router configs/godot-*.json
# → Creates godot.zip with intelligent routing

# 5. Upload all .zip files
# → Users ask naturally, router directs to right sub-skill
```

### Example 3: Custom Internal Documentation

```bash
# 1. Interactive mode
/docs-to-skill --interactive
# Enter: name, URL, description, max pages

# 2. Test with dry-run
/docs-to-skill --generate --config configs/my-docs.json --dry-run
# → Preview what will be scraped

# 3. Full generation
/docs-to-skill --generate --config configs/my-docs.json

# 4. Enhance and package
/docs-to-skill --enhance-local output/my-docs/
/docs-to-skill --package output/my-docs/
```

## Command Reference

### Estimation
```bash
quick_estimate.sh <config-file>
```

### Generation
```bash
generate_skill.sh <config-file> [--enhance] [--dry-run]
```

### Validation
```bash
validate_config.sh <config-file>
```

### Enhancement
```bash
# Local (FREE)
enhance_skill_local.py <skill-dir>

# API (paid)
enhance_skill.py <skill-dir> --api-key <key>
```

### Packaging
```bash
package_skill.py <skill-dir>
```

### Large Documentation Tools
```bash
# Split configuration
split_config.py <config-file> --strategy router

# Generate router
generate_router.py <config-pattern>

# Package multiple
package_multi.py <skill-dirs>
```

## Quality Standards

**What Makes a Good Skill**:
- ✅ Comprehensive coverage of documentation
- ✅ Well-organized categories
- ✅ Real code examples with language tags
- ✅ Clear navigation structure
- ✅ Accurate triggers and use cases
- ✅ Quick reference with best examples

**Enhancement Quality**:
- Transforms 75-line templates → 500+ line guides
- Success rate: 9/10 (tested on multiple frameworks)
- Extracts 5-10 practical, short examples
- Adds domain-specific concepts
- Provides beginner → advanced navigation

## Performance Tips

1. **Use Estimation First**: Save time by checking page count
2. **Enable Checkpoints**: For scrapes >1000 pages
3. **Parallel Scraping**: For split large documentation
4. **Cache Raw Data**: Scrape once, rebuild configurations quickly
5. **Rate Limiting**: Respect servers, avoid being blocked
6. **Dry Run**: Test configuration before full scrape

## Troubleshooting

### "Too Many Pages"
```bash
# Check estimate first
quick_estimate.sh config.json

# If >10K pages, split it
/docs-to-skill --split config.json --strategy router
```

### "Resume Interrupted Scrape"
```bash
# Checkpoints enabled by default
/docs-to-skill --generate --config config.json --resume
```

### "Improve Categorization"
```bash
# Edit config.json url_patterns to guide categorization
{
  "url_patterns": {
    "category_hints": {
      "/api/": "api_reference",
      "/guide/": "guides",
      "/tutorial/": "tutorials"
    }
  }
}
```

## Related Skills

- `/create-skill` - Create new skills with guided workflow
- `/document-project` - Generate project documentation
- `/git-ops` - Commit generated skills to Git

## Notes

- **Self-awareness**: This skill creates Claude skills from external documentation
- **Respect robots.txt**: Always honors website scraping rules
- **Rate limiting**: Default 0.5s delay between requests
- **Cache-aware**: Re-run without re-scraping using cached data
- **Deterministic**: Scripts output JSON to terminal, no side effects

## More Information

See `.github/instructions/docs-to-skill.instructions.md` for:
- Detailed configuration options
- Advanced splitting strategies
- Troubleshooting guide
- Best practices

---

**Ready to convert documentation?** Run `/docs-to-skill` and choose your workflow!
