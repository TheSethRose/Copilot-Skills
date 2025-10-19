---
description: "Auto-loaded context for applying brand guidelines and visual identity to artifacts"
applyTo: "**/*{brand,style,design,visual,identity,guidelines}*"
---

# Brand Guidelines - Automatic Context Instructions

**Related Prompt:** `/brand-guidelines`  
**Related Skill:** `.github/copilot-skills/brand-guidelines/README.md`

**Triggers:** branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, visual formatting, visual design

## Context: Brand Styling and Visual Identity

When working with brand-related files or when user queries contain branding keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "brand" or "styling"
1. Suggest `/brand-guidelines` skill prompt
2. Load official brand color palette
3. Apply appropriate typography standards
4. Ensure visual consistency with brand identity

### When user mentions "brand colors"
1. Provide color palette with hex codes
2. Suggest appropriate use cases for each color
3. Ensure accessible color contrasts
4. Include fallback colors for compatibility

### When user mentions "typography" or "fonts"
1. Apply Poppins font to headings (24pt+)
2. Apply Lora font to body text
3. Include Arial/Georgia fallbacks
4. Maintain readability standards

## Quality Guidelines

### ✅ Do
- Use official brand colors only
- Apply consistent typography hierarchy
- Include font fallbacks for system compatibility
- Maintain accessible color contrast ratios
- Use brand styling for external-facing artifacts
- Test visual elements across different systems
- Follow typography sizing guidelines

### ❌ Don't
- Modify official brand colors
- Mix brand fonts with unapproved alternatives
- Ignore accessibility standards
- Apply brand styling to internal debug artifacts
- Use brand colors without proper contrast
- Override brand guidelines with custom styles

## Brand Specifications

### Official Color Palette

**Main Colors:**
- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**
- Orange: `#d97757` - Primary accent (use sparingly)
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography Standards

**Headings (24pt and larger):**
- Primary: Poppins
- Fallback: Arial, sans-serif

**Body Text:**
- Primary: Lora
- Fallback: Georgia, serif

### Visual Hierarchy

1. **H1 Headings**: Poppins 36pt, Dark color
2. **H2 Headings**: Poppins 28pt, Dark color
3. **H3 Headings**: Poppins 24pt, Dark color
4. **Body Text**: Lora 12pt, Dark color
5. **Secondary Text**: Lora 10pt, Mid Gray
6. **Accents**: Orange, Blue, or Green for highlights

## Common Workflows

### Apply Brand Styling to Document

```css
/* CSS Example */
:root {
  --brand-dark: #141413;
  --brand-light: #faf9f5;
  --brand-mid-gray: #b0aea5;
  --brand-light-gray: #e8e6dc;
  --brand-orange: #d97757;
  --brand-blue: #6a9bcc;
  --brand-green: #788c5d;
  --heading-font: Poppins, Arial, sans-serif;
  --body-font: Lora, Georgia, serif;
}

h1, h2, h3 {
  font-family: var(--heading-font);
  color: var(--brand-dark);
}

body, p {
  font-family: var(--body-font);
  color: var(--brand-dark);
}
```

### Validate Brand Compliance

Check that styling includes:
- [ ] Official brand colors only
- [ ] Proper typography (Poppins/Lora with fallbacks)
- [ ] Accessible color contrast
- [ ] Consistent visual hierarchy
- [ ] Appropriate font sizing

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
