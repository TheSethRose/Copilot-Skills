# Brand Guidelines Assistant

---
description: "Help establish and document brand guidelines so AI agents consistently apply your visual identity"
---

# Brand Guidelines Skill

Create, document, and apply your project's brand guidelines so AI agents understand and follow your visual identity consistently across all generated artifacts.

## When to Use This Skill

Use this skill when:
- Establishing brand identity for a new project
- Documenting existing brand colors, fonts, and styling
- Creating a brand reference for AI agents to follow
- Ensuring visual consistency across generated artifacts
- Setting up typography and color standards
- Defining voice, tone, and messaging guidelines

**Keywords**: brand guidelines, establish brand, brand identity, visual identity, style guide, brand documentation, corporate identity, design system

## Workflow

### Step 1: Gather Brand Information

Ask the user about their brand identity:
- **Project/Company Name**: What is this brand for?
- **Target Audience**: Who will see this brand?
- **Brand Personality**: Professional, playful, technical, creative, etc.
- **Existing Assets**: Do they have a logo, website, or existing materials?

### Step 2: Define Color Palette

Help establish a color scheme:
```
1. Primary Color: Main brand color (used for key elements)
2. Secondary Color: Supporting color (accents, highlights)
3. Neutral Colors: Background, text (usually grays or off-whites)
4. Accent Colors: Call-to-action, alerts (optional)

For each color, document:
- Hex code (e.g., #3B82F6)
- Usage guidelines (where/when to use)
- Accessibility considerations (contrast ratios)
```

### Step 3: Establish Typography

Define font hierarchy:
```
Headings:
- Font family: (e.g., "Inter", "Helvetica", "Georgia")
- Weights: (e.g., Bold 700 for H1, SemiBold 600 for H2)
- Fallbacks: Always include web-safe fallbacks

Body Text:
- Font family: (usually same or complementary to headings)
- Size: Base size (typically 16px or 1rem)
- Line height: (1.5-1.6 for readability)
- Fallbacks: Generic family (sans-serif, serif)
```

### Step 4: Document Visual Guidelines

Create guidelines for:
- **Spacing**: Margins, padding standards
- **Borders**: Radius, width, style
- **Shadows**: Drop shadows, elevation
- **Icons**: Style (outline, filled, custom)
- **Images**: Style (photography, illustrations, treatment)

### Step 5: Define Voice & Tone

Establish messaging guidelines:
- **Voice**: Consistent personality (friendly, authoritative, casual)
- **Tone**: Adaptive to context (supportive, urgent, celebratory)
- **Language**: Technical level, jargon usage, formality
- **Examples**: Sample phrases that match/don't match brand

### Step 6: Create Brand Document

Generate a comprehensive brand guidelines file:
```markdown
# Brand Guidelines: [Project Name]

## Color Palette
- Primary: #[hex] - [Usage]
- Secondary: #[hex] - [Usage]
- Neutral: #[hex] - [Usage]

## Typography
- Headings: [Font], [Weight], [Sizes]
- Body: [Font], [Size], [Line Height]

## Visual Style
- Border Radius: [value]
- Spacing Scale: [values]
- Shadow: [CSS values]

## Voice & Tone
- Voice: [Description]
- Tone: [Guidelines]
- Examples: [Do/Don't]

## Usage Examples
[Code snippets showing proper usage]
```

### Step 7: Save and Reference

Store guidelines where agents can access them:
- Primary: `.github/brand-guidelines.md`
- Alternative: `BRAND.md`, `docs/brand-guidelines.md`
- Reference in `.github/copilot-instructions.md`

## Examples

### Example 1: Interactive Brand Setup
```
User: Help me create brand guidelines

Agent: I'll help you establish your brand guidelines. Let's start:

1. What's your project/company name?
User: "Acme Analytics"

2. What's your brand personality?
User: "Professional but approachable, data-focused"

3. Do you have existing brand colors?
User: "Blue and white, but not formalized"

Agent: Great! Let me suggest a color palette:
- Primary: #2563EB (Professional blue)
- Secondary: #60A5FA (Lighter blue for accents)
- Neutral Dark: #1F2937 (Text)
- Neutral Light: #F9FAFB (Backgrounds)

[Generates complete brand guidelines document]
```

### Example 2: Document Existing Brand
```
User: I have a logo with colors #FF6B6B and #4ECDC4, help me document this

Agent: I'll create comprehensive guidelines based on those colors:

Primary Color: #FF6B6B (Coral Red)
- Use for: CTAs, primary buttons, key highlights
- Contrast: Passes WCAG AA on white backgrounds

Secondary Color: #4ECDC4 (Turquoise)
- Use for: Secondary actions, informational elements
- Pairs well with neutral grays

[Creates full brand document with typography, spacing, etc.]
```

### Example 3: Apply Existing Guidelines
```
User: Apply our brand guidelines from BRAND.md to this document

Agent: [Reads .github/brand-guidelines.md or BRAND.md]
[Applies documented colors, fonts, spacing]
[Ensures consistency with established guidelines]
```

## Detail Files

- **Template**: Brand guidelines document template
- **Examples**: Sample brand guidelines for different industries
- **Color Tools**: Accessibility checkers, palette generators
- **Typography**: Font pairing recommendations

## Notes

- Store guidelines in `.github/brand-guidelines.md` for agent access
- Reference brand file in `.github/copilot-instructions.md`
- Validate color contrast for accessibility (WCAG AA minimum)
- Include fallback fonts for cross-platform compatibility
- Update guidelines as brand evolves

## Related Skills

- **Generate Instructions** - Reference brand guidelines in copilot-instructions.md
- **Document Skills** - Apply brand to generated documents
- **New Project** - Set up brand guidelines for new projects
