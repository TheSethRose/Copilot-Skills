---
description: "Auto-loaded context for establishing and applying brand guidelines in projects"
applyTo: "**/*{brand,style,design,visual,identity,guidelines,BRAND}*"
---

# Brand Guidelines - Automatic Context Instructions

**Related Prompt:** `/brand-guidelines`  
**Related Skill:** `.github/copilot-skills/brand-guidelines/README.md`

**Triggers:** brand guidelines, establish brand, brand identity, visual identity, style guide, brand documentation, create brand, design system

## Context: Creating and Applying Brand Guidelines

When working with brand-related files or when user queries contain brand establishment keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "create brand" or "establish brand"
1. Suggest `/brand-guidelines` skill prompt
2. Guide through interactive brand setup
3. Ask about colors, typography, voice/tone
4. Generate comprehensive brand guidelines document
5. Save to `.github/brand-guidelines.md` or `BRAND.md`

### When user mentions "brand colors" or "color palette"
1. Help define primary, secondary, and neutral colors
2. Validate accessibility (WCAG contrast ratios)
3. Suggest complementary colors if needed
4. Document hex codes and usage guidelines
5. Provide CSS/design token examples

### When user mentions "brand typography" or "fonts"
1. Help select heading and body fonts
2. Define font hierarchy (H1-H6, body, captions)
3. Specify weights, sizes, line heights
4. Include web-safe fallbacks
5. Create typography scale

### When user mentions "apply brand" or "use brand guidelines"
1. Look for existing brand guidelines file
2. Read `.github/brand-guidelines.md`, `BRAND.md`, or `docs/brand-guidelines.md`
3. Apply documented colors, fonts, spacing
4. Ensure consistency with established guidelines
5. Reference brand file in generated artifacts

## Quality Guidelines

### ✅ Do
- Help users define their own brand colors and fonts
- Validate accessibility (WCAG AA minimum contrast 4.5:1)
- Include fallback fonts for cross-platform compatibility
- Document usage guidelines for each color
- Create reusable design tokens (CSS variables)
- Store guidelines in accessible location (.github/, docs/)
- Reference brand file in copilot-instructions.md
- Update brand guidelines as project evolves

### ❌ Don't
- Apply pre-defined brand colors without user input
- Skip accessibility validation
- Use colors without contrast checking
- Create brand guidelines in hidden/obscure locations
- Forget to document usage examples
- Hardcode colors instead of using variables
- Ignore existing brand assets

## Brand Specification Template

When creating brand guidelines, use this structure:

### Color Palette Template

**Primary Colors:**
- Primary: `#______` - Main brand color, used for key elements
- Secondary: `#______` - Supporting color, used for accents  
- Tertiary: `#______` - Optional third color

**Neutral Colors:**
- Dark: `#______` - Text, dark backgrounds
- Light: `#______` - Light backgrounds, reversed text
- Gray: `#______` - Secondary text, borders

**Accent Colors:**
- Success: `#______` - Positive actions, confirmations
- Warning: `#______` - Warnings, caution
- Error: `#______` - Errors, destructive actions
- Info: `#______` - Informational elements

### Typography Template

**Headings:**
- Font Family: [e.g., "Inter", "Helvetica Neue", sans-serif]
- Weights: [e.g., 700 for H1, 600 for H2-H3, 500 for H4-H6]
- Sizes: [H1: 36px, H2: 28px, H3: 24px, etc.]

**Body Text:**
- Font Family: [e.g., "Inter", system-ui, sans-serif]
- Size: [e.g., 16px base]
- Line Height: [e.g., 1.6]
- Weight: [e.g., 400 normal, 600 bold]

## Common Workflows

### Create Brand Guidelines from Scratch

```bash
# 1. Start interactive brand setup
/brand-guidelines

# 2. Answer questions about brand identity
# 3. Generate brand-guidelines.md file
# 4. Reference in copilot-instructions.md
```

### Apply Brand Styling Example

```css
/* Example CSS using established brand colors */
:root {
  /* User-defined brand colors */
  --brand-primary: #3B82F6;
  --brand-secondary: #8B5CF6;
  --brand-dark: #1F2937;
  --brand-light: #F9FAFB;
  
  /* User-defined typography */
  --font-heading: "Inter", system-ui, sans-serif;
  --font-body: "Inter", system-ui, sans-serif;
}

h1, h2, h3 {
  font-family: var(--font-heading);
  color: var(--brand-dark);
}

body, p {
  font-family: var(--font-body);
  color: var(--brand-dark);
}

.btn-primary {
  background: var(--brand-primary);
  color: white;
}
```

### Validate Brand Compliance

Check that styling includes:
- [ ] User-defined brand colors (not defaults)
- [ ] Proper typography with fallbacks
- [ ] Accessible color contrast (WCAG AA: 4.5:1 minimum)
- [ ] Consistent visual hierarchy
- [ ] Appropriate font sizing
- [ ] CSS variables for reusability

## Next Steps

When applying brand guidelines:
1. Use `/brand-guidelines` prompt for guided workflow
2. Check `.github/copilot-skills/brand-guidelines/README.md` for full specifications
3. Reference official brand documentation
4. Validate accessibility and contrast ratios

## Related Skills

- **Document Skills** - For creating branded documents
- **Visual Design** - For additional design patterns
- **PDF Handling** - For branded PDF output
