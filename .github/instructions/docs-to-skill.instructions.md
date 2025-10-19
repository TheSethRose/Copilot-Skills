---
description: Auto-loaded guidance for converting documentation websites into Claude skills
---

# Docs to Skill - Instructions

When working with documentation scraping, skill generation, or queries containing "docs to skill" or "documentation converter", this context activates.

## Core Purpose

Teach AI agents how to discover and use documentation scraping tools to transform ANY documentation website into production-ready Claude skills.

**Key Distinction**: This skill GENERATES Claude skills from external documentation. For project documentation, use `/document-project`.

## Auto-Loaded Behaviors

### When user mentions "docs to skill" or "scrape docs"

**Immediate Actions**:
1. Suggest `/docs-to-skill` skill
2. Discover available documentation scraping tools
3. Validate tool capabilities  
4. Guide workflow selection

**Discovery Pattern**:
```bash
# Find documentation scraping tools
find . -name "*doc*scrap*" -o -name "*skill*seek*" -type d

# Validate Python scraping tools
find . -name "doc_scraper.py" -type f

# Check for configuration directories
find . -name "configs" -type d -path "*/examples/*" -o -path "*/tools/*"
```

### When user has documentation URL

**Immediate Actions**:
1. Discover available tool
2. Check for matching preset
3. Estimate documentation size
4. Recommend appropriate strategy

**Decision Tree**:
```
Has URL → Find tool → Check presets → Estimate → Choose strategy
                                          ↓
                           <500pg  500-10K  >10K
                              ↓       ↓       ↓
                          Standard  +Checkpoint  Split
```

### When analyzing documentation sites

**Validate Before Scraping**:
1. Check `robots.txt` compliance
2. Identify documentation structure
3. Estimate total pages
4. Recommend selectors and patterns
5. Suggest appropriate rate limiting (0.5s minimum)

## Tool Discovery Protocol

### Step 1: Find Available Tools

```bash
# Search for documentation scraping directories
SCRAPER_DIRS=$(find . -maxdepth 3 -name "*doc*scrap*" -o -name "*skill*seek*" -type d)

# Search for scraping scripts
SCRAPER_SCRIPTS=$(find . -name "doc_scraper.py" -o -name "*scrape*.py" -type f)

# Common locations to check:
# - examples/Skill_Seekers/
# - examples/*/cli/
# - tools/doc_scraper/
# - scripts/scraping/
```

### Step 2: Validate Tool Capabilities

```bash
# Get tool help
python3 <discovered-path>/doc_scraper.py --help

# Check for essential capabilities:
grep -i "config\|estimate\|interactive\|dry-run\|resume\|enhance"

# Validate Python dependencies
python3 -c "import requests, bs4" 2>/dev/null && echo "✓ Dependencies OK"
```

### Step 3: Discover Configuration Templates

```bash
# Find config directory
CONFIG_DIR=$(find . -name "configs" -type d | head -1)

# List available presets
[ -d "$CONFIG_DIR" ] && ls $CONFIG_DIR/*.json | xargs -n1 basename | sed 's/.json//'

# Common presets to look for:
# Frontend: react, vue, svelte, angular
# Backend: django, fastapi, laravel, rails
# Game: godot, unity
# CSS: tailwind, bootstrap
```

## Universal Workflow Templates

### Template 1: Standard Workflow (<500 pages)

**Use When**: Documentation is well-structured, < 500 pages

```bash
# 1. Discover tool
TOOL=$(find . -name "doc_scraper.py" | head -1)
TOOL_DIR=$(dirname $TOOL)

# 2. Estimate (if available)
find $TOOL_DIR -name "*estimate*.py" -exec python3 {} configs/my-docs.json \;

# 3. Scrape
python3 $TOOL --config configs/my-docs.json

# 4. Enhance (if available)
find $TOOL_DIR -name "*enhance*.py" -exec python3 {} output/my-docs/ \;

# 5. Package (if available)
find $TOOL_DIR -name "*package*.py" -exec python3 {} output/my-docs/ \;
```

### Template 2: Large Documentation Workflow (>10K pages)

**Use When**: Documentation is massive (game engines, cloud providers)

```bash
# 1. Discover tool and capabilities
TOOL=$(find . -name "doc_scraper.py" | head -1)
TOOL_DIR=$(dirname $TOOL)

# 2. Estimate
python3 $TOOL_DIR/*estimate*.py configs/large.json
# Output: ~40,000 pages detected

# 3. Check for splitting capability
SPLIT_TOOL=$(find $TOOL_DIR -name "*split*.py" | head -1)

if [ -n "$SPLIT_TOOL" ]; then
  # 4. Split into sub-skills
  python3 $SPLIT_TOOL configs/large.json --strategy router
  
  # 5. Scrape all in parallel
  for config in configs/large-*.json; do
    python3 $TOOL --config $config &
  done
  wait
  
  # 6. Generate router (if available)
  find $TOOL_DIR -name "*router*.py" -exec python3 {} configs/large-*.json \;
  
  # 7. Package all (if available)
  find $TOOL_DIR -name "*package_multi*.py" -exec python3 {} output/large*/ \;
else
  echo "⚠️  Splitting not available - proceed with caution"
  echo "→ Consider manual splitting or reducing max_pages"
fi
```

### Template 3: Interactive Custom Workflow

**Use When**: Creating config for new/unknown documentation

```bash
# 1. Discover tool
TOOL=$(find . -name "doc_scraper.py" | head -1)

# 2. Check for interactive mode
python3 $TOOL --help | grep -i interactive

if [ $? -eq 0 ]; then
  # 3. Run interactive wizard
  python3 $TOOL --interactive
  
  # 4. Test generated config
  python3 $TOOL --config configs/generated.json --dry-run
  
  # 5. Full scrape
  python3 $TOOL --config configs/generated.json
else
  echo "→ Interactive mode not available, create config manually"
fi
```

## Configuration Principles

### Universal Configuration Schema

Every documentation scraping tool should support this basic schema:

```json
{
  "name": "skill-name",
  "description": "AI trigger description",
  "base_url": "https://docs.example.com/",
  "max_pages": 200,
  "rate_limit": 0.5
}
```

### Extended Configuration (Tool-Specific)

```json
{
  "name": "skill-name",
  "description": "When to use this skill",
  "base_url": "https://docs.example.com/",
  "start_urls": ["https://docs.example.com/guide/"],
  "max_pages": 500,
  "rate_limit": 0.5,
  
  "selectors": {
    "main_content": "article, div[role='main']",
    "title": "h1, title",
    "code_blocks": "pre code"
  },
  
  "url_patterns": {
    "include": ["^https://docs\\.example\\.com/(guide|api)/.*"],
    "exclude": ["^https://docs\\.example\\.com/blog/.*"],
    "category_hints": {
      "/api/": "api_reference",
      "/guide/": "guides",
      "/tutorial/": "tutorials"
    }
  },
  
  "checkpoint": {
    "enabled": true,
    "interval": 1000
  }
}
```

### Configuration Validation

```bash
# Check if tool has validation
TOOL_DIR=$(dirname $(find . -name "doc_scraper.py" | head -1))
find $TOOL_DIR -name "*validate*.py"

# If available, validate config
python3 $TOOL_DIR/*validate*.py configs/my-docs.json
```

## Strategy Selection Guide

### Decision Matrix

| Pages | Complexity | Strategy | Checkpoints | Splitting | Time |
|-------|-----------|----------|-------------|-----------|------|
| <500 | Simple | Standard | Optional | No | 15-30 min |
| 500-5K | Moderate | Standard | Yes | No | 1-3 hours |
| 5K-10K | Complex | Standard | Yes | Consider | 3-6 hours |
| 10K-40K | Very Complex | Split | Yes | Required | 4-8 hours |
| >40K | Massive | Split + Router | Yes | Required | 8-24 hours |

### Strategy Implementation

**Standard Strategy**:
```json
{
  "max_pages": 500,
  "rate_limit": 0.5,
  "checkpoint": {"enabled": true, "interval": 100}
}
```

**Splitting Strategy** (requires tool support):
```bash
# Auto-detect and split
python3 <tool>/split*.py config.json --strategy auto

# Or manual strategies:
# - router: Hub + specialized sub-skills (recommended)
# - category: Split by content categories
# - size: Split every N pages
```

## Enhancement Patterns

### Discovery Pattern

```bash
# Find enhancement tools
TOOL_DIR=$(dirname $(find . -name "doc_scraper.py" | head -1))
find $TOOL_DIR -name "*enhance*.py"

# Types usually available:
# - enhance_skill_local.py (FREE - uses local AI)
# - enhance_skill.py (Paid - uses API)
```

### Enhancement Execution

**Local Enhancement** (Preferred - FREE):
```bash
# Find local enhancement tool
ENHANCE_LOCAL=$(find $TOOL_DIR -name "*enhance*local*.py" | head -1)

if [ -n "$ENHANCE_LOCAL" ]; then
  python3 $ENHANCE_LOCAL output/skill-name/
else
  echo "→ Local enhancement not available"
fi
```

**API Enhancement** (Alternative):
```bash
# Check for API enhancement
ENHANCE_API=$(find $TOOL_DIR -name "enhance_skill.py" | head -1)

if [ -n "$ENHANCE_API" ]; then
  # Requires API key
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 $ENHANCE_API output/skill-name/
else
  echo "→ API enhancement not available"
fi
```

### Enhancement Quality Expectations

**Before Enhancement**:
- ~75 lines
- Generic templates
- No code examples
- Basic structure

**After Enhancement**:
- ~500+ lines
- Real code examples (5-10)
- Domain-specific guidance
- Navigation instructions
- Quality: 9/10 (tested across multiple frameworks)

## Expected Output Structure

Regardless of tool version, expect this structure:

```
output/
├── {skill-name}_data/           # Cache (optional)
│   ├── pages/
│   │   ├── 001_*.json
│   │   ├── 002_*.json
│   │   └── ...
│   ├── summary.json
│   └── checkpoint.json
│
└── {skill-name}/                # Generated skill
    ├── SKILL.md                 # Main file (enhanced)
    ├── SKILL.md.backup          # Original backup
    ├── references/              # Organized docs
    │   ├── index.md
    │   ├── getting_started.md
    │   ├── api.md
    │   ├── guides.md
    │   └── [auto-categories].md
    ├── scripts/                 # (empty)
    └── assets/                  # (empty)
```

## Quality Standards

### ✅ Before Scraping Checklist

```bash
# 1. Tool discovered and validated
[ -f "$TOOL" ] && echo "✓ Tool found" || echo "✗ Tool missing"

# 2. Configuration created or preset selected
[ -f "configs/my-docs.json" ] && echo "✓ Config ready"

# 3. Estimation run
python3 $TOOL_DIR/*estimate*.py configs/my-docs.json

# 4. robots.txt checked
curl -s https://docs.example.com/robots.txt | grep -i "disallow"

# 5. Dry-run tested (if available)
python3 $TOOL --config configs/my-docs.json --dry-run 2>/dev/null

# 6. Checkpoints enabled (for >1000 pages)
grep -q '"checkpoint".*true' configs/my-docs.json && echo "✓ Checkpoints enabled"
```

### ✅ During Scraping Monitoring

```bash
# Watch progress
tail -f <output-dir>/scraping.log

# Check for errors
grep -i "error\|fail\|warn" <output-dir>/scraping.log

# Monitor page count
find <output-dir>_data/pages/ -name "*.json" | wc -l
```

### ✅ After Scraping Validation

```bash
# 1. Check generated structure
[ -f "output/skill/SKILL.md" ] && echo "✓ SKILL.md generated"
[ -d "output/skill/references" ] && echo "✓ References created"

# 2. Count reference files
ls output/skill/references/*.md | wc -l

# 3. Validate SKILL.md size
SIZE=$(wc -l < output/skill/SKILL.md)
[ $SIZE -gt 50 ] && echo "✓ SKILL.md has content ($SIZE lines)"

# 4. Check for enhancement backup
[ -f "output/skill/SKILL.md.backup" ] && echo "✓ Backup exists (enhancement was applied)"
```

## Error Handling

### Common Issues & Solutions

**Issue: Tool Not Found**
```bash
# Solution: Check common locations
find . -maxdepth 3 -name "*doc*scrap*" -type d
find . -name "Skill_Seekers" -type d

# If not found:
echo "→ Install documentation scraper tool"
echo "Example: git clone https://github.com/yusufkaraaslan/Skill_Seekers examples/Skill_Seekers"
```

**Issue: Estimation Shows >10K Pages**
```bash
# Solution: Check for splitting capability
SPLIT_TOOL=$(find $TOOL_DIR -name "*split*.py" | head -1)

if [ -n "$SPLIT_TOOL" ]; then
  python3 $SPLIT_TOOL configs/large.json --strategy router
else
  echo "→ Reduce max_pages or scrape in batches"
fi
```

**Issue: Scrape Interrupted**
```bash
# Solution: Resume from checkpoint
python3 $TOOL --config configs/my-docs.json --resume

# If resume not available:
# Check checkpoint file
[ -f "output/my-docs_data/checkpoint.json" ] && \
  echo "→ Checkpoint available but resume not supported" || \
  echo "→ No checkpoint, must restart"
```

**Issue: Poor Categorization**
```json
// Solution: Add category hints to config
{
  "url_patterns": {
    "category_hints": {
      "/api/": "api_reference",
      "/guide/": "guides",
      "/tutorial/": "tutorials",
      "/reference/": "reference",
      "/getting-started/": "getting_started"
    }
  }
}
```

**Issue: Enhancement Failed**
```bash
# Solution 1: Restore backup
[ -f "output/skill/SKILL.md.backup" ] && \
  cp output/skill/SKILL.md.backup output/skill/SKILL.md

# Solution 2: Try alternative enhancement method
# If local failed, try API; if API failed, try local

# Solution 3: Manual enhancement
echo "→ Edit SKILL.md manually to add examples and guidance"
```

**Issue: Rate Limit Exceeded**
```json
// Solution: Increase delay in config
{
  "rate_limit": 1.0  // Increase from 0.5 to 1.0 seconds
}
```

**Issue: robots.txt Disallows Scraping**
```bash
# Check robots.txt
curl https://docs.example.com/robots.txt

# If disallowed:
echo "→ Respect robots.txt restrictions"
echo "→ Contact site owner for permission"
echo "→ Look for official API or data export"
```

## Integration with Other Skills

### With `/create-skill`
```bash
# After generating skill, customize it further
/create-skill
# Add custom scripts, modify SKILL.md, enhance references
```

### With `/document-project`
```bash
# Different use case - document YOUR project
/document-project
# This skill is for EXTERNAL documentation → Claude skills
```

### With `/git-ops`
```bash
# Commit generated skills
git add output/skill-name.zip
git commit -m "feat(skills): add skill-name Claude skill"
```

## Performance Tips

### Faster Scraping
- Use parallel scraping for split configurations
- Enable checkpoints for resume capability
- Set appropriate rate_limit (0.3-0.5s minimum)
- Limit max_pages for testing (increase after validation)

### Better Quality
- Always use enhancement (local or API)
- Choose meaningful skill names
- Write clear descriptions
- Test selectors with dry-run (if available)
- Add category hints for better organization

### Resource Usage
- Monitor disk space (scraped data can be large)
- Clean old data periodically: `rm -rf output/*_data/`
- Use caching to rebuild without re-scraping

## Self-Awareness Rule

**CRITICAL**: This skill NEVER generates skills for:
- This Copilot Skills system itself
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
git commit -m "fix(skills): correct vue-docs selectors for proper content extraction"
```

## Related Resources

- **Skill Directory**: `.github/copilot-skills/skills/docs-to-skill/`
- **Skill Prompt**: `.github/prompts/docs-to-skill.prompt.md`
- **Reference Tool**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

---

**Key Principle**: This skill teaches **discovery and adaptation**. Tools evolve, paths change, but the principles remain constant. Always discover first, validate capabilities, then execute with appropriate strategy. 🚀
