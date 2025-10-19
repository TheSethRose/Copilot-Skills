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

## Core Philosophy

This skill teaches **discovery and adaptation** rather than specific commands:

1. **Discover** - Find documentation scraping tools in the workspace
2. **Understand** - Learn tool capabilities through help documentation
3. **Configure** - Set up scraping parameters for any documentation site
4. **Execute** - Run workflows that scale from small to massive documentation
5. **Enhance** - Improve generated skills with AI
6. **Deploy** - Package and upload to Claude

## The 4-Phase Workflow (Universal)

### Phase 1: Tool Discovery & Validation

**Find the Documentation Scraping Tool**:

```bash
# Discover documentation scraping tools
find . -name "*doc*scrap*" -o -name "*skill*seek*" -type d

# Look for Python scraping scripts
find . -name "doc_scraper.py" -o -name "*scrape*.py" -type f

# Common locations:
# - examples/Skill_Seekers/
# - tools/doc_scraper/
# - scripts/documentation/
```

**Validate Tool Capabilities**:

```bash
# Get tool help
python3 <discovered-path>/doc_scraper.py --help

# Essential capabilities to look for:
# ✅ Configuration (--config FILE or --interactive)
# ✅ Estimation (--estimate or separate estimate tool)
# ✅ Dry-run (--dry-run for testing)
# ✅ Resume (--resume for interrupted scrapes)

# Advanced capabilities:
# ⭐ Enhancement (--enhance or --enhance-local)
# ⭐ Splitting (for large documentation)
# ⭐ Checkpoints (auto-save progress)
```

**Find Example Configurations**:

```bash
# Locate config directory
find . -name "configs" -type d

# List available presets
ls <config-dir>/*.json | xargs -n1 basename | sed 's/.json//'

# Examine preset structure
cat <config-dir>/react.json
```

### Phase 2: Configuration

**Principle**: Define what to scrape and how to scrape it

#### Strategy A: Use Preset (Fastest)

```bash
# 1. List available presets
ls <config-dir>/*.json

# 2. Choose preset for your documentation
# Common presets: react, vue, django, fastapi, godot, tailwind

# 3. Use preset configuration
python3 <tool-path>/doc_scraper.py --config <config-dir>/preset.json
```

#### Strategy B: Interactive Mode (Guided)

```bash
# 1. Check for interactive capability
python3 <tool-path>/doc_scraper.py --help | grep -i interactive

# 2. Launch interactive wizard
python3 <tool-path>/doc_scraper.py --interactive

# 3. Answer prompts:
#    - Skill name: Short identifier (e.g., "tailwind")
#    - Base URL: Documentation root (e.g., "https://tailwindcss.com/docs/")
#    - Description: When to use this skill
#    - Max pages: Limit (e.g., 200)
#    - Rate limit: Delay between requests (e.g., 0.5 seconds)
```

#### Strategy C: Manual Configuration (Full Control)

**Create Configuration File**:

```bash
# Create configs directory if needed
mkdir -p configs

# Create config file
cat > configs/my-docs.json << 'EOF'
{
  "name": "my-docs",
  "description": "My custom documentation skill for X framework",
  "base_url": "https://docs.example.com/",
  "max_pages": 200,
  "rate_limit": 0.5,
  "selectors": {
    "main_content": "article, div[role='main'], main",
    "title": "h1, title",
    "code_blocks": "pre code, code[class*='language-']"
  },
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/(guide|api)/.*"],
    "exclude": ["^https://docs\\.example\\.com/blog/.*"]
  },
  "checkpoint": {
    "enabled": true,
    "interval": 1000
  }
}
EOF
```

**Configuration Schema** (Universal):

```json
{
  "name": "skill-name",                    // Required: Short identifier
  "description": "Skill description",      // Required: When to use
  "base_url": "https://docs.example.com/", // Required: Root URL
  "max_pages": 200,                        // Required: Page limit
  "rate_limit": 0.5,                       // Required: Seconds between requests
  
  // Optional: CSS selectors for content extraction
  "selectors": {
    "main_content": "article",             // Main content container
    "title": "h1",                         // Page title
    "code_blocks": "pre code"              // Code examples
  },
  
  // Optional: URL filtering
  "url_patterns": {
    "include": ["regex"],                  // URLs to scrape
    "exclude": ["regex"]                   // URLs to skip
  },
  
  // Optional: Progress saving
  "checkpoint": {
    "enabled": true,
    "interval": 1000                       // Save every N pages
  }
}
```

### Phase 3: Estimation (Always Do This First!)

**Principle**: Know the scope before committing to a full scrape

```bash
# 1. Find estimation tool
find <tool-path> -name "*estimate*.py" -type f

# 2. Run estimation
python3 <tool-path>/estimate_pages.py <config-file>

# OR check if main tool has estimation
python3 <tool-path>/doc_scraper.py --help | grep -i estimate
python3 <tool-path>/doc_scraper.py --estimate --config <config-file>
```

**Interpret Results**:

```
Output: ~250 pages estimated
Strategy: Standard scrape (15-25 minutes)
```

**Decision Tree**:

```
Pages?
│
├─ <500 pages
│  └─ Strategy: Standard scrape
│     ├─ Enable checkpoints
│     └─ Time: 15-30 minutes
│
├─ 500-10K pages
│  └─ Strategy: Standard with checkpoints
│     ├─ Enable resume capability
│     ├─ Monitor progress closely
│     └─ Time: 1-6 hours
│
└─ >10K pages
   └─ Strategy: Splitting required
      ├─ Find split tool
      ├─ Split into 5K page chunks
      ├─ Scrape in parallel
      ├─ Generate router skill
      └─ Time: 4-24 hours
```

### Phase 4: Execution

**Principle**: Scrape, organize, enhance, and package

#### For Standard Documentation (<10K pages)

```bash
# 1. Test configuration with dry-run (if available)
python3 <tool-path>/doc_scraper.py --config <config-file> --dry-run

# 2. Run full scrape
python3 <tool-path>/doc_scraper.py --config <config-file>

# 3. Monitor progress
# Look for:
# - Pages scraped count
# - Checkpoint saves
# - Errors or warnings

# 4. If interrupted, resume
python3 <tool-path>/doc_scraper.py --config <config-file> --resume
```

#### For Large Documentation (>10K pages)

```bash
# 1. Find splitting capability
find <tool-path> -name "*split*.py" -type f

# 2. Split configuration
python3 <tool-path>/split_config.py <config-file> --strategy router

# Output: Multiple config files
# - my-docs-api.json
# - my-docs-guides.json
# - my-docs-tutorials.json

# 3. Scrape all in parallel
for config in configs/my-docs-*.json; do
  python3 <tool-path>/doc_scraper.py --config $config &
done
wait

# 4. Generate router skill (if available)
python3 <tool-path>/generate_router.py configs/my-docs-*.json
```

## Enhancement (Recommended)

**Principle**: Transform basic templates into comprehensive guides

### Find Enhancement Tool

```bash
# Look for enhancement scripts
find <tool-path> -name "*enhance*.py" -type f

# Check if main tool supports enhancement
python3 <tool-path>/doc_scraper.py --help | grep -i enhance
```

### Enhancement Options (Usually Two Types)

**Option 1: Local Enhancement** (FREE)
```bash
# Uses AI in your workspace (e.g., Claude Code Max)
python3 <tool-path>/enhance_skill_local.py <output-dir>/

# Benefits:
# - No API key needed
# - Free (uses your Claude plan)
# - Fast (~60 seconds)
# - Quality: 9/10
```

**Option 2: API Enhancement** (Paid)
```bash
# Uses external AI service
export ANTHROPIC_API_KEY=sk-ant-...
python3 <tool-path>/enhance_skill.py <output-dir>/

# Benefits:
# - More consistent
# - No local dependency
# - Cost: ~$0.15-$0.30 per skill
```

**What Enhancement Does**:
- Reads all reference documentation
- Extracts 5-10 best code examples
- Creates comprehensive quick reference
- Adds domain-specific triggers
- Provides navigation guidance
- Transforms 75-line template → 500+ line guide

### Enhancement During Scraping

```bash
# Many tools support inline enhancement
python3 <tool-path>/doc_scraper.py \
  --config <config-file> \
  --enhance-local

# OR with API
python3 <tool-path>/doc_scraper.py \
  --config <config-file> \
  --enhance \
  --api-key sk-ant-...
```

## Packaging

**Principle**: Create uploadable .zip file

```bash
# 1. Find packaging tool
find <tool-path> -name "*package*.py" -type f

# 2. Package single skill
python3 <tool-path>/package_skill.py <output-dir>/

# Output: <output-dir>.zip

# 3. For multiple skills (split documentation)
python3 <tool-path>/package_multi.py <output-dir1>/ <output-dir2>/ ...

# OR with wildcard
python3 <tool-path>/package_multi.py output/my-docs*/
```

## Expected Output Structure

```
output/
├── skill-name_data/              # Cache (raw scraped pages)
│   ├── pages/
│   │   ├── 001_page.json
│   │   ├── 002_page.json
│   │   └── ...
│   ├── summary.json
│   └── checkpoint.json
│
└── skill-name/                   # Generated Claude skill
    ├── SKILL.md                  # Main skill file (enhanced)
    ├── SKILL.md.backup           # Original (pre-enhancement)
    ├── references/               # Organized documentation
    │   ├── index.md              # Navigation/TOC
    │   ├── getting_started.md    # Intro content
    │   ├── api.md                # API reference
    │   ├── guides.md             # Tutorials
    │   └── [auto-categories].md  # Smart categorization
    ├── scripts/                  # (empty, for customization)
    └── assets/                   # (empty, for templates)
```

## Complete Workflow Examples

### Example 1: Quick Preset Scrape

```bash
# 1. Discover tool and presets
TOOL_PATH=$(find . -name "doc_scraper.py" | head -1 | xargs dirname)
ls $(dirname $TOOL_PATH)/configs/*.json

# 2. Estimate
python3 $TOOL_PATH/estimate*.py $(dirname $TOOL_PATH)/configs/react.json

# 3. Scrape with enhancement
python3 $TOOL_PATH/doc_scraper.py \
  --config $(dirname $TOOL_PATH)/configs/react.json \
  --enhance-local

# 4. Package
python3 $TOOL_PATH/package*.py output/react/

# Result: output/react.zip ready to upload!
```

### Example 2: Custom Documentation (Interactive)

```bash
# 1. Find tool
TOOL_PATH=$(find . -name "doc_scraper.py" | head -1 | xargs dirname)

# 2. Interactive configuration
python3 $TOOL_PATH/doc_scraper.py --interactive
# Follow prompts...

# 3. Estimate generated config
python3 $TOOL_PATH/estimate*.py configs/my-docs.json

# 4. Test with dry-run
python3 $TOOL_PATH/doc_scraper.py --config configs/my-docs.json --dry-run

# 5. Full scrape
python3 $TOOL_PATH/doc_scraper.py --config configs/my-docs.json

# 6. Enhance
python3 $TOOL_PATH/enhance*.py output/my-docs/

# 7. Package
python3 $TOOL_PATH/package*.py output/my-docs/
```

### Example 3: Large Documentation (40K pages)

```bash
# 1. Find and set tool path
TOOL_PATH=$(find . -name "doc_scraper.py" | head -1 | xargs dirname)

# 2. Create config for large docs
cat > configs/godot.json << 'EOF'
{
  "name": "godot",
  "base_url": "https://docs.godotengine.org/",
  "max_pages": 45000,
  "rate_limit": 0.5
}
EOF

# 3. Estimate
python3 $TOOL_PATH/estimate*.py configs/godot.json
# Output: ~40,000 pages - splitting recommended

# 4. Split configuration
python3 $TOOL_PATH/split*.py configs/godot.json --strategy router

# Creates:
# - godot-scripting.json (5K pages)
# - godot-2d.json (8K pages)
# - godot-3d.json (10K pages)
# - godot-physics.json (6K pages)
# - godot-shaders.json (11K pages)

# 5. Scrape all in parallel
for config in configs/godot-*.json; do
  python3 $TOOL_PATH/doc_scraper.py --config $config &
done
wait

# 6. Generate router skill
python3 $TOOL_PATH/*router*.py configs/godot-*.json

# 7. Package all
python3 $TOOL_PATH/package_multi*.py output/godot*/

# Result: Multiple .zip files + router for intelligent routing
```

## Key Capabilities Reference

### Essential Capabilities (Must Have)
- ✅ **Configuration** - Define scraping parameters
- ✅ **Scraping** - Extract documentation content
- ✅ **Organization** - Categorize content automatically

### Recommended Capabilities (Should Have)
- ⭐ **Estimation** - Preview documentation size
- ⭐ **Dry-run** - Test configuration without scraping
- ⭐ **Checkpoints** - Auto-save progress
- ⭐ **Resume** - Continue interrupted scrapes

### Advanced Capabilities (Nice to Have)
- 🚀 **Interactive Mode** - Guided configuration wizard
- 🚀 **Enhancement** - AI-powered skill improvement
- 🚀 **Splitting** - Handle massive documentation
- 🚀 **Router Generation** - Intelligent routing
- 🚀 **Parallel Scraping** - Speed up large docs

## Quality Checklist

### Before Scraping
- [ ] Tool discovered and validated
- [ ] Configuration created or preset selected
- [ ] Estimation run (know page count)
- [ ] robots.txt checked and respected
- [ ] Dry-run tested (if available)
- [ ] Checkpoints enabled for >1000 pages

### During Scraping
- [ ] Progress monitored
- [ ] Errors logged and addressed
- [ ] Rate limiting respected (0.5s minimum)

### After Scraping
- [ ] Generated content reviewed
- [ ] Enhancement applied (local or API)
- [ ] Output structure validated
- [ ] Package created successfully
- [ ] Ready for Claude upload

## Troubleshooting

### Problem: Tool Not Found
```bash
# Solution: Install or clone documentation scraper
# Example for Skill Seekers:
git clone https://github.com/yusufkaraaslan/Skill_Seekers examples/Skill_Seekers
```

### Problem: Estimation Shows >10K Pages
```bash
# Solution: Use splitting strategy
python3 <tool>/split*.py config.json --strategy router
```

### Problem: Scrape Interrupted
```bash
# Solution: Resume from checkpoint
python3 <tool>/doc_scraper.py --config config.json --resume
```

### Problem: Poor Categorization
```json
// Solution: Add category hints to config
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

### Problem: Enhancement Failed
```bash
# Solution 1: Restore backup
mv output/skill/SKILL.md.backup output/skill/SKILL.md

# Solution 2: Try alternative method
# If local failed → try API
# If API failed → try local

# Solution 3: Manual enhancement
# Edit SKILL.md directly
```

## Performance Expectations

| Documentation Size | Strategy | Estimated Time | Notes |
|-------------------|----------|----------------|-------|
| <500 pages | Standard | 15-30 min | Quick turnaround |
| 500-5K pages | Standard + checkpoints | 1-3 hours | Monitor progress |
| 5K-10K pages | Standard + checkpoints | 3-6 hours | Consider splitting |
| 10K-40K pages | Split + parallel | 4-8 hours | Requires splitting |
| >40K pages | Split + parallel + router | 8-24 hours | Multi-phase approach |

**Notes**:
- Times assume 0.5s rate limit
- Enhancement adds ~60s per skill
- Parallel scraping significantly faster for split docs

## Best Practices

### ✅ Do
- Discover tool capabilities first
- Always estimate before scraping
- Use presets when available
- Enable checkpoints for >1000 pages
- Test with dry-run
- Enhance generated skills
- Respect robots.txt and rate limits
- Split documentation >10K pages
- Package before uploading

### ❌ Don't
- Skip estimation step
- Ignore rate limits (<0.3s)
- Scrape without testing config
- Forget to enable checkpoints
- Skip enhancement step
- Interrupt scrapes unnecessarily
- Scrape non-documentation content
- Overwrite without backup

## Related Skills

- `/create-skill` - Further customize generated skills
- `/document-project` - Document YOUR project (different use case)
- `/git-ops` - Commit generated skills to repository

## More Information

- **Instructions**: `.github/instructions/docs-to-skill.instructions.md`
- **Skill Directory**: `.github/copilot-skills/skills/docs-to-skill/`
- **Reference Tool**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

---

**Remember**: This skill teaches **principles and discovery**, not specific commands. Tools evolve, but core concepts remain constant. Always discover, understand, then execute. 🚀
