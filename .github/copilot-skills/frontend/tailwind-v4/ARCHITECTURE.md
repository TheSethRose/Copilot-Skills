# Tailwind CSS v4 Skill Architecture

This document shows how the Tailwind v4 skill is organized and how the progressive disclosure works.

## File Structure

```
.github/
├── prompts/
│   └── tailwind.skill.prompt.md          [TIER 1: Callable Prompt]
│       ├── When to use
│       ├── Quick reference
│       ├── Installation methods
│       ├── Core concepts with examples
│       └── Resources & related skills
│
├── instructions/
│   └── tailwind.instructions.md          [TIER 1: Auto-Triggered Context]
│       ├── Core principles (mobile-first, variants, CSS variables)
│       ├── Default behaviors (styling workflow)
│       ├── Quality guidelines (do's and don'ts)
│       ├── Common patterns (flex, grid, cards, forms)
│       └── v3→v4 migration notes
│
└── copilot-skills/frontend/tailwind-v4/
    ├── README.md                         [META: Skill Overview]
    │   ├── What's included
    │   ├── Quick start
    │   ├── Key concepts
    │   ├── Best practices
    │   └── Related skills
    │
    ├── patterns.md                       [TIER 2: Real-World Examples]
    │   ├── Layout patterns (flex, grid, centering)
    │   ├── Typography patterns (scaling, states)
    │   ├── Component patterns (card, button, form)
    │   ├── State patterns (hover, active, disabled)
    │   ├── Spacing patterns
    │   ├── Dark mode patterns
    │   └── Animation & transition patterns
    │
    └── reference.md                      [TIER 3: Complete Reference]
        ├── Navigation & setup
        ├── Installation methods
        ├── Layout utilities (display, flexbox, grid)
        ├── Spacing (margin, padding, gap with scales)
        ├── Typography (sizes, weights, colors, alignment)
        ├── Colors (full palette with shades)
        ├── Backgrounds (colors, gradients, images)
        ├── Borders (width, radius, colors)
        ├── Effects (shadows, opacity, filters, backdrop)
        ├── Sizing (width, height, min/max)
        ├── Responsive prefixes (breakpoints table)
        ├── Interactive states (hover, focus, active, disabled)
        ├── Dark mode (configuration, usage)
        ├── Customization (@theme variables)
        ├── v3→v4 migration comparison
        └── Resources & links
```

## Progressive Disclosure Strategy

### Tier 1: First Contact (< 3 minutes)
**Entry points**: `/tailwind` command or auto-load on CSS file edit

**Provides**:
- When to use this skill
- Key concepts
- Quick code examples
- Installation overview
- Resources

**User Actions**:
- ✅ Learn what Tailwind v4 is
- ✅ Quick lookup of common utilities
- ✅ Get started with installation
- ❌ Not: comprehensive utility reference (use reference.md)

### Tier 2: Going Deeper (3-10 minutes)
**Trigger**: User asks for patterns or examples

**Provides**:
- Layout patterns (responsive, mobile-first)
- Component patterns (card, button, form)
- Typography patterns (scaling, hierarchy)
- State management (interactive)
- Dark mode implementation
- Animations

**User Actions**:
- ✅ Copy working code examples
- ✅ Understand common workflows
- ✅ See best practices in action
- ✅ Learn component structure
- ❌ Not: look up specific utilities (use reference.md)

### Tier 3: Mastery (10+ minutes)
**Trigger**: User asks for deep reference or specific utility

**Provides**:
- All utilities organized by category
- Full spacing scale
- Complete color palette
- Responsive breakpoint table
- Migration guide (v3→v4)
- Customization details
- All interactive states

**User Actions**:
- ✅ Find any utility quickly
- ✅ Understand all variants
- ✅ Migrate from v3
- ✅ Customize theme
- ✅ Advanced patterns

## How Users Interact

### Scenario 1: First Time User
```
User: "Show me how to style a button with Tailwind"
↓ Load: tailwind.skill.prompt.md (Tier 1)
Response: Quick reference + component intro
User: "Show me a complete button example"
↓ Load: patterns.md (Tier 2)
Response: Button variants (primary, secondary, disabled)
```

### Scenario 2: Responsive Layout
```
User: "I need a responsive grid that's 1 column on mobile, 2 on tablet, 3 on desktop"
↓ Load: tailwind.instructions.md auto-loaded
Response: Mobile-first principle + example code
User: "Show me more grid patterns"
↓ Load: patterns.md (Tier 2)
Response: Multiple responsive grid examples
```

### Scenario 3: Dark Mode
```
User: "How do I add dark mode?"
↓ Load: tailwind.instructions.md auto-loaded
Response: Dark mode guidance (shows dark: prefix)
User: "Show me a complete dark mode component"
↓ Load: patterns.md (Tier 2)
Response: Dark mode pattern with all colors
User: "I need to customize dark mode colors"
↓ Load: reference.md (Tier 3)
Response: @theme variables with dark color customization
```

### Scenario 4: Migrating from v3
```
User: "How do I upgrade to Tailwind v4?"
↓ Load: tailwind.instructions.md + prompt
Response: Quick v3→v4 breaking changes
User: "What changed specifically?"
↓ Load: reference.md (Tier 3)
Response: Complete migration table with all changes
```

## Integration Points

### With copilot-instructions.md
```markdown
#### Tailwind CSS v4
**Keywords:** tailwind, css, utilities, responsive, dark mode, styling
**Suggest:** `/tailwind`
**Auto-context:** `.github/instructions/tailwind.instructions.md`
**Skill:** `.github/copilot-skills/frontend/tailwind-v4/`
```

### With Other Skills
- **React** (`/react`): Use Tailwind utilities in React components
- **Next.js** (`/nextjs`): Tailwind with Next.js App Router
- **Vue** (`/vue`): Tailwind utilities in Vue SFCs
- **shadcn/ui** (`/shadcn`): Component library built on Tailwind

### With Framework Guides
When editing in these contexts, Tailwind instructions auto-load:
- React JSX files
- Next.js app/page components
- Vue `.vue` files
- Plain CSS/HTML
- Tailwind config files

## Design Decisions

### Why This Organization?

1. **Prompt File (Tier 1)**
   - Quick reference without loading big files
   - Fast load time for interactive chat
   - Core concepts in 3 minutes
   - Clear navigation to detail files

2. **Instructions File (Auto-Load)**
   - Immediate context when editing CSS/JSX/TSX
   - Principles-based guidance, not just examples
   - Quality guidelines prevent common mistakes
   - Pattern snippets for quick workflow

3. **Patterns File (Tier 2)**
   - Real working code (copy-paste ready)
   - Shows best practices in context
   - Organized by use case, not utility name
   - Progressive: simple → complex

4. **Reference File (Tier 3)**
   - Comprehensive utility documentation
   - Organized by category, then alphabetical
   - Complete scale information
   - One source of truth

### Why Tier 3 as Single File?

**Advantages**:
- Single search/reference point
- Complete picture of utilities
- Organized hierarchy (category → type → variants)
- Better for "find everything about X" queries

**Alternatives considered**:
- Multiple reference files (faster load, harder to search)
- Embedded in README (makes README huge)
- Separate file per category (fragmentation)

## Future Extensibility

### Could Add (Tier 2 Extensions)
- `animations.md` - Animation patterns
- `forms.md` - Form component patterns
- `accessibility.md` - A11y best practices
- `performance.md` - Performance tips
- `plugin-examples.md` - Custom plugin patterns

### Could Add (Tier 3 Extensions)
- Plugin API reference
- CSS custom properties complete list
- PostCSS configuration deep dive
- Performance tuning guide

### Could Add (Scripts)
- `validate-tailwind.sh` - Check for unused utilities
- `generate-theme.sh` - Theme generator from colors
- `migrate-v3-to-v4.js` - Automated migration helper

## Maintenance Notes

- **Update Frequency**: With each Tailwind v4.x release
- **Breaking Changes**: Track and update migration section
- **New Utilities**: Add to reference and patterns
- **Examples**: Refresh if syntax changes
- **Browser Support**: Update if Tailwind changes support matrix

## Compliance with Constitutional Principles

| Principle | ✓ | How |
|-----------|---|-----|
| Progressive Disclosure | ✓ | Tier 1 → 2 → 3, each independent |
| File-Based | ✓ | Organized in .github/copilot-skills structure |
| Dynamic Discovery | ✓ | Auto-load + keyword routing + /skill command |
| Deterministic | ✓ | Reference docs only, no code generation |
| Composability | ✓ | Clear boundaries, references other skills |

