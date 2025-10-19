# Docs to Skill - Documentation to Claude Skill Converter

---
name: "Docs to Skill"
description: "Automatically convert documentation websites into production-ready Claude skills"
version: "1.0.0"
tags: ["documentation", "scraping", "skill-generation", "automation", "claude"]
dependencies: ["python3", "documentation-scraper-tool"]
attribution: "Based on Skill Seekers by @yusufkaraaslan"
---

Transform ANY documentation website into a structured, production-ready Claude skill through automated scraping, organization, and enhancement.

## Quick Links

- **Slash Command**: `/docs-to-skill`
- **Skill Prompt**: `.github/prompts/docs-to-skill.prompt.md`
- **Instructions**: `.github/instructions/docs-to-skill.instructions.md`
- **Reference Tool**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

## What This Skill Does

**Docs to Skill** teaches AI agents how to:

1. **Discover** documentation scraping tools in the workspace
2. **Estimate** documentation size before scraping
3. **Configure** scraping parameters for any documentation site
4. **Execute** scraping with appropriate strategies
5. **Enhance** generated skills with AI-powered improvements
6. **Package** skills for deployment to Claude

## Core Principles (Tool-Agnostic)

This skill teaches **principles and capabilities**, not specific commands. Any documentation scraping tool should provide:

## Core Principles (Tool-Agnostic)

This skill teaches **principles and capabilities**, not specific commands. Any documentation scraping tool should provide:

### 1. Tool Discovery
**Capability**: Find and validate documentation scraping tools in the workspace

**How to Discover**:
```bash
# Look for documentation scraper directories
find . -name "*doc*scrap*" -o -name "*skill*seek*" -type d

# Check for Python scraping tools
find . -name "doc_scraper.py" -o -name "*scrape*.py" -type f

# Look for configuration directories
ls -la */configs/ examples/*/configs/ 2>/dev/null

# Check for scraping tools help
python3 PATH_TO_TOOL/doc_scraper.py --help 2>/dev/null
```

**What to Look For**:
- Scraping scripts (usually Python)
- Configuration directory with `.json` files
- CLI tools with help documentation
- Output directories for generated skills

### 2. Estimation
**Capability**: Determine documentation size before scraping

**Discovery Pattern**:
```bash
# Find estimation tool
find . -name "*estimate*.py" -type f

# Check tool help
python3 PATH_TO_TOOL/estimate_pages.py --help

# Look for estimation in main scraper
python3 PATH_TO_TOOL/doc_scraper.py --help | grep -i estimate
```

**Core Concepts**:
- Always estimate before full scrape
- Check page count to determine strategy
- <500 pages: Standard scrape
- 500-10K pages: Use checkpoints
- >10K pages: Consider splitting

### 3. Configuration
**Capability**: Create configuration for any documentation site

**Discovery Pattern**:
```bash
# Find existing configs for reference
find . -name "*.json" -path "*/configs/*"

# Look for interactive mode
python3 PATH_TO_TOOL/doc_scraper.py --help | grep -i interactive

# Check for config templates
cat PATH_TO_CONFIGS/react.json  # Use as template
```

**Configuration Schema** (Universal):
```json
{
  "name": "skill-name",
  "description": "When to use this skill",
  "base_url": "https://docs.example.com/",
  "max_pages": 200,
  "rate_limit": 0.5,
  "selectors": {
    "main_content": "CSS_SELECTOR",
    "title": "CSS_SELECTOR",
    "code_blocks": "CSS_SELECTOR"
  },
  "url_patterns": {
    "include": ["REGEX_PATTERNS"],
    "exclude": ["REGEX_PATTERNS"]
  }
}
```

### 4. Scraping
**Capability**: Extract documentation with appropriate strategy

**Discovery Pattern**:
```bash
# Find main scraping tool
find . -name "*scraper*.py" -o -name "*scrape*.py" -type f

# Check available modes
python3 PATH_TO_TOOL/doc_scraper.py --help

# Look for dry-run option
python3 PATH_TO_TOOL/doc_scraper.py --help | grep -i dry

# Check for resume capability
python3 PATH_TO_TOOL/doc_scraper.py --help | grep -i resume
```

**Core Concepts**:
- Use `--dry-run` to test configuration
- Enable checkpoints for long scrapes
- Use `--resume` to continue interrupted scrapes
- Respect `robots.txt` and rate limits

### 5. Enhancement
**Capability**: Improve generated skills with AI

**Discovery Pattern**:
```bash
# Find enhancement tools
find . -name "*enhance*.py" -type f

# Check for local vs API enhancement
ls PATH_TO_TOOL/*enhance*.py

# Look for enhancement options in main tool
python3 PATH_TO_TOOL/doc_scraper.py --help | grep -i enhance
```

**Enhancement Options** (Usually Two Types):
- **Local/Free**: Uses AI in workspace (no API key needed)
- **API/Paid**: Uses external AI service (requires API key)

**Core Concepts**:
- Enhancement transforms basic templates → comprehensive guides
- Extracts best code examples from documentation
- Adds domain-specific guidance
- Creates navigation structure

### 6. Packaging
**Capability**: Create uploadable `.zip` files

**Discovery Pattern**:
```bash
# Find packaging tool
find . -name "*package*.py" -type f

# Check packaging options
python3 PATH_TO_TOOL/package_skill.py --help

# Look for multi-packaging for split docs
find . -name "*package_multi*.py" -type f
```

**Output Structure** (Standard):
```
output/
├── skill-name_data/          # Raw scraped data (cache)
└── skill-name/               # Generated skill
    ├── SKILL.md              # Main file
    ├── references/           # Organized docs
    ├── scripts/              # Optional tools
    └── assets/               # Optional resources
```

## Tool Discovery Workflow

### Step 1: Validate Tool Availability

```bash
# 1. Check for documentation scraping tool
if [ -d "examples/Skill_Seekers" ]; then
  echo "✓ Skill Seekers found"
  TOOL_PATH="examples/Skill_Seekers/cli"
elif [ -d "tools/doc_scraper" ]; then
  echo "✓ Custom scraper found"
  TOOL_PATH="tools/doc_scraper"
else
  echo "✗ No documentation scraper found"
  echo "→ Clone or install a documentation scraping tool"
  exit 1
fi

# 2. Check Python dependencies
python3 -c "import requests, bs4" 2>/dev/null || \
  echo "→ Install: pip3 install requests beautifulsoup4"

# 3. Discover available tools
ls $TOOL_PATH/*.py
```

### Step 2: Discover Available Presets

```bash
# Find config directory
CONFIG_DIR=$(find . -name "configs" -type d | head -1)

# List available presets
ls $CONFIG_DIR/*.json | xargs -n1 basename | sed 's/.json//'

# Example presets to look for:
# - react, vue, django, fastapi (web frameworks)
# - godot, unity (game engines)
# - tailwind (CSS)
```

### Step 3: Get Tool Help

```bash
# Main scraper help
python3 $TOOL_PATH/doc_scraper.py --help

# Estimator help
python3 $TOOL_PATH/estimate_pages.py --help 2>/dev/null || \
  python3 $TOOL_PATH/doc_scraper.py --help | grep -i estimate

# Enhancement help
python3 $TOOL_PATH/enhance_skill*.py --help 2>/dev/null

# Packaging help
python3 $TOOL_PATH/package_skill.py --help 2>/dev/null
```

## Universal Workflow (Adapt to Your Tool)

### Workflow 1: Using Preset Configuration

```bash
# 1. Discover tool and configs
TOOL_PATH="<discovered-path>/cli"
CONFIG="<discovered-path>/configs/react.json"

# 2. Estimate (if available)
python3 $TOOL_PATH/estimate*.py $CONFIG

# 3. Scrape
python3 $TOOL_PATH/*scraper.py --config $CONFIG

# 4. Enhance (if available)
python3 $TOOL_PATH/enhance*.py output/react/

# 5. Package (if available)
python3 $TOOL_PATH/package*.py output/react/
```

### Workflow 2: Interactive Custom Configuration

```bash
# 1. Run interactive mode
python3 $TOOL_PATH/*scraper.py --interactive

# 2. Estimate generated config
python3 $TOOL_PATH/estimate*.py configs/my-docs.json

# 3. Test with dry-run
python3 $TOOL_PATH/*scraper.py --config configs/my-docs.json --dry-run

# 4. Full scrape
python3 $TOOL_PATH/*scraper.py --config configs/my-docs.json

# 5. Enhance and package
python3 $TOOL_PATH/enhance*.py output/my-docs/
python3 $TOOL_PATH/package*.py output/my-docs/
```

### Workflow 3: Large Documentation (>10K Pages)

```bash
# 1. Estimate to confirm size
python3 $TOOL_PATH/estimate*.py configs/large.json
# Output: 40,000+ pages → splitting recommended

# 2. Look for splitting capability
find $TOOL_PATH -name "*split*.py" -type f

# 3. Split configuration (if available)
python3 $TOOL_PATH/split*.py configs/large.json --strategy router

# 4. Scrape all splits in parallel
for config in configs/large-*.json; do
  python3 $TOOL_PATH/*scraper.py --config $config &
done
wait

# 5. Generate router (if available)
python3 $TOOL_PATH/*router*.py configs/large-*.json

# 6. Package all
python3 $TOOL_PATH/package_multi*.py output/large*/
```

## Key Capabilities to Look For

When discovering documentation scraping tools, look for these capabilities:

### Essential Capabilities
- ✅ **Estimation** - Discover page count before scraping
- ✅ **Configuration** - Create/modify scraping parameters
- ✅ **Scraping** - Extract documentation content
- ✅ **Organization** - Categorize content automatically
- ✅ **Packaging** - Create uploadable artifacts

### Advanced Capabilities
- ⭐ **Interactive Mode** - Guided configuration wizard
- ⭐ **Dry Run** - Test configuration without scraping
- ⭐ **Checkpoints** - Resume interrupted scrapes
- ⭐ **Enhancement** - AI-powered skill improvement
- ⭐ **Splitting** - Handle large documentation (>10K pages)
- ⭐ **Router Generation** - Intelligent routing for split docs
- ⭐ **Parallel Scraping** - Process multiple configs simultaneously

### Quality Features
- 🎯 **Smart Categorization** - Automatically organizes by topic
- 💻 **Code Detection** - Recognizes multiple programming languages
- 🤖 **AI-Ready** - Generates AI-friendly skill format
- 🔒 **robots.txt Respect** - Follows website scraping policies
- ⏱️ **Rate Limiting** - Prevents server overload

## How to Use This Skill

### For First-Time Users

1. **Discover the Tool**
```bash
# Find documentation scraping tools in workspace
find . -name "*doc*scrap*" -type d
ls examples/*/cli/*.py 2>/dev/null
```

2. **Check Tool Help**
```bash
# Get available commands and options
python3 <tool-path>/doc_scraper.py --help
```

3. **Find Example Configs**
```bash
# Look for preset configurations
find . -name "*.json" -path "*/configs/*"
cat <config-path>/react.json  # Use as template
```

4. **Run Estimation**
```bash
# Determine documentation size
python3 <tool-path>/estimate*.py <config-file>
```

5. **Execute Workflow**
- Use preset if available
- Or create custom config
- Run with appropriate strategy based on size

### For Experienced Users

**Quick Commands** (adapt to your tool):
```bash
# Preset scrape
python3 <tool>/doc_scraper.py --config configs/react.json

# Interactive config
python3 <tool>/doc_scraper.py --interactive

# Custom quick scrape
python3 <tool>/doc_scraper.py --name skill --url https://docs.example.com/

# With enhancement
python3 <tool>/doc_scraper.py --config config.json --enhance-local
```

## Decision Tree: Choosing the Right Strategy

```
Documentation Size?
│
├─ <500 pages
│  └─ Use: Standard scrape
│     ├─ Enable checkpoints
│     └─ Enhance after scraping
│
├─ 500-10K pages  
│  └─ Use: Standard with checkpoints
│     ├─ Enable resume capability
│     ├─ Monitor progress
│     └─ Enhance after scraping
│
└─ >10K pages
   └─ Use: Splitting strategy
      ├─ Split into sub-skills (5K pages each)
      ├─ Scrape in parallel
      ├─ Generate router skill
      └─ Package all together
```

## Common Preset Patterns

Documentation scraping tools often include presets for popular frameworks:

| Category | Examples | Typical Size |
|----------|----------|--------------|
| **Frontend** | React, Vue, Svelte, Angular | 150-500 pages |
| **Backend** | Django, FastAPI, Laravel, Rails | 300-800 pages |
| **Game Engines** | Godot, Unity, Unreal | 5K-40K pages |
| **CSS** | Tailwind, Bootstrap, Bulma | 200-400 pages |
| **Database** | PostgreSQL, MongoDB, Redis | 500-2K pages |
| **Cloud** | AWS, Azure, GCP | 10K-100K+ pages |

**Discovery Pattern**:
```bash
# List available presets
ls <config-dir>/*.json | xargs -n1 basename | sed 's/.json//'

# Check preset content
cat <config-dir>/react.json
```

## Configuration Patterns

### Minimal Configuration (Quick Start)
```json
{
  "name": "my-docs",
  "base_url": "https://docs.example.com/",
  "max_pages": 200
}
```

### Standard Configuration (Recommended)
```json
{
  "name": "my-docs",
  "description": "When to use this skill",
  "base_url": "https://docs.example.com/",
  "max_pages": 500,
  "rate_limit": 0.5
}
```

### Advanced Configuration (Full Control)
```json
{
  "name": "my-docs",
  "description": "Detailed skill description",
  "base_url": "https://docs.example.com/",
  "start_urls": ["https://docs.example.com/guide/", "https://docs.example.com/api/"],
  "max_pages": 500,
  "rate_limit": 0.5,
  "selectors": {
    "main_content": "article, div[role='main']",
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
```

## Quality Standards & Best Practices

### Documentation Quality Indicators

**Signs of Good Documentation to Scrape**:
- ✅ Clear navigation structure
- ✅ Consistent URL patterns
- ✅ Rich code examples
- ✅ Well-organized content
- ✅ Active maintenance

**Red Flags** (May Need Manual Intervention):
- ⚠️ Heavy JavaScript rendering (may not scrape well)
- ⚠️ Dynamic content loading
- ⚠️ Authentication required
- ⚠️ Rate limiting < 0.3s
- ⚠️ robots.txt restrictions

### Before Scraping Checklist

1. **Check robots.txt**
```bash
curl https://docs.example.com/robots.txt
```

2. **Estimate page count**
```bash
python3 <tool>/estimate*.py <config>
```

3. **Test with dry-run** (if available)
```bash
python3 <tool>/*scraper.py --config <config> --dry-run
```

4. **Enable checkpoints** for >1000 pages
```json
{"checkpoint": {"enabled": true, "interval": 1000}}
```

### During Scraping

- Monitor progress logs
- Check for errors
- Respect rate limits (0.5s minimum recommended)
- Don't interrupt unless necessary (use resume)

### After Scraping

1. **Review generated content**
2. **Enhance SKILL.md** (local or API)
3. **Validate structure**
4. **Test package**
5. **Upload to Claude**

## Expected Output Structure

Regardless of tool, expect this general structure:

```
output/
├── {skill-name}_data/           # Cache (optional in some tools)
│   ├── pages/                   # Raw scraped pages
│   ├── summary.json             # Metadata
│   └── checkpoint.json          # Resume data
│
└── {skill-name}/                # Generated Claude skill
    ├── SKILL.md                 # Main skill file
    ├── SKILL.md.backup          # Pre-enhancement backup
    ├── references/              # Organized documentation
    │   ├── index.md             # Navigation/table of contents
    │   ├── getting_started.md   # Intro content
    │   ├── api.md               # API reference
    │   ├── guides.md            # Tutorials/guides
    │   └── [category].md        # Auto-categorized
    ├── scripts/                 # (empty, for user customization)
    └── assets/                  # (empty, for user templates)
```

## Enhancement Transformation

### What Enhancement Does (Universal Concept)

Enhancement transforms auto-generated skills from basic templates into comprehensive guides:

**Before** (75-100 lines):
```markdown
## Quick Reference

### Common Patterns

*Quick reference patterns will be added as you use the skill.*
```

**After** (500+ lines):
```markdown
## Quick Reference

### 1. Basic Usage
```javascript
// Real example from docs
import { Component } from 'library'

function App() {
  return <Component prop="value" />
}
```

### 2. Advanced Pattern
```javascript
// Another real example
const result = await api.method({
  option: 'value'
})
```

[...8-10 more practical examples...]

## Key Concepts

### Concept 1: Architecture
Explanation of core concept...

### Concept 2: Best Practices
Guidelines from official docs...
```

**Metrics**:
- Lines: 75 → 500+
- Examples: 0 → 5-10 real code snippets
- Quality: 9/10 based on testing
- Time: ~60 seconds

## Troubleshooting Guide

### Problem: Tool Not Found

**Solution**:
```bash
# Check workspace
find . -name "*doc*scrap*" -o -name "*skill*seek*"

# If not found, need to install/clone documentation scraper
# Example: git clone https://github.com/yusufkaraaslan/Skill_Seekers examples/Skill_Seekers
```

### Problem: Too Many Pages Detected

**Solution**:
```bash
# 1. Check estimation
python3 <tool>/estimate*.py config.json

# 2. If >10K pages, look for splitting capability
find <tool> -name "*split*.py"

# 3. Split configuration
python3 <tool>/split*.py config.json --strategy router
```

### Problem: Scrape Interrupted

**Solution**:
```bash
# Check for resume capability
python3 <tool>/*scraper.py --help | grep -i resume

# Resume if available
python3 <tool>/*scraper.py --config config.json --resume

# Otherwise, re-run (checkpoints may help)
```

### Problem: Poor Categorization

**Solution**:
1. Add `category_hints` to config
2. Refine `url_patterns` include/exclude
3. Adjust `selectors` for better content extraction

### Problem: Enhancement Failed

**Solution**:
```bash
# 1. Restore backup
mv output/skill/SKILL.md.backup output/skill/SKILL.md

# 2. Try alternative enhancement method
# If API failed, try local; if local failed, try API

# 3. Manual enhancement is always an option
```

## Integration with Other Skills

- `/create-skill` - Further customize generated skills
- `/document-project` - Document YOUR project (different use case)
- `/git-ops` - Commit generated skills

## Performance Expectations

| Documentation Size | Strategy | Time | Notes |
|-------------------|----------|------|-------|
| <500 pages | Standard | 15-30 min | Quick turnaround |
| 500-5K pages | Standard + checkpoints | 1-3 hours | Monitor progress |
| 5K-10K pages | Standard + checkpoints | 3-6 hours | Consider splitting |
| 10K-40K pages | Split + parallel | 4-8 hours | Requires splitting |
| >40K pages | Split + parallel + router | 8-24 hours | Multi-phase approach |

**Note**: Times assume:
- 0.5s rate limit
- Stable internet connection
- No interruptions
- Enhancement time not included (add ~60s per skill)

## Attribution & License

This skill documents principles and patterns for converting documentation websites into Claude skills.

**Reference Implementation**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) by [@yusufkaraaslan](https://github.com/yusufkaraaslan)

**License**: MIT (both Skill Seekers and this skill documentation)

## Related Documentation

- **Skill Prompt**: `.github/prompts/docs-to-skill.prompt.md`
- **Instructions**: `.github/instructions/docs-to-skill.instructions.md`
- **Skill Seekers**: https://github.com/yusufkaraaslan/Skill_Seekers

## Getting Started

1. **Discover Tool**: Find documentation scraping tool in workspace
2. **Check Help**: Read tool's help documentation
3. **Find Presets**: Look for example configurations
4. **Estimate First**: Always check page count before scraping
5. **Choose Strategy**: Standard, checkpoint, or splitting based on size
6. **Execute Workflow**: Scrape, enhance, package
7. **Upload to Claude**: Deploy your skill

---

**Remember**: This skill teaches **principles and discovery**, not specific commands. Tools evolve, but the concepts remain constant. Always check tool help and adapt accordingly. 🚀
