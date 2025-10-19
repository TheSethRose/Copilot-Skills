# Brand Guidelines Assistant

---
description: "Apply Anthropic's official brand colors and typography to artifacts requiring visual identity"
---

# Brand Guidelines Skill

Apply Anthropic's official brand identity and style resources to any artifact that benefits from professional visual formatting.

## When to Use This Skill

Use this skill when:
- Creating branded documents, presentations, or visual content
- Applying consistent corporate identity across artifacts
- Needing official brand colors for styling
- Working with typography and visual design standards
- Post-processing artifacts with brand styling

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, visual formatting, visual design

## Workflow

### Step 1: Identify Brand Elements Needed

Determine which brand elements to apply:
- Color palette (dark, light, accent colors)
- Typography (headings, body text)
- Visual formatting guidelines

### Step 2: Load Brand Specifications

Reference the brand guidelines:
- **Main colors**: Dark (`#141413`), Light (`#faf9f5`), Mid Gray (`#b0aea5`), Light Gray (`#e8e6dc`)
- **Accent colors**: Orange (`#d97757`), Blue (`#6a9bcc`), Green (`#788c5d`)
- **Typography**: Poppins for headings (24pt+), Lora for body text
- **Fallbacks**: Arial for headings, Georgia for body

### Step 3: Apply Brand Styling

Apply appropriate brand elements:
```
1. Use dark (#141413) for primary text and dark backgrounds
2. Use light (#faf9f5) for light backgrounds and text on dark
3. Apply Poppins font to headings (24pt and larger)
4. Apply Lora font to body text
5. Use accent colors (orange, blue, green) for highlights
6. Ensure Arial/Georgia fallbacks for compatibility
```

### Step 4: Validate Visual Consistency

Check that styling:
- Maintains readability across all systems
- Uses accessible color contrasts
- Follows brand guidelines consistently
- Has appropriate font fallbacks

## Examples

### Example 1: Styled Document Header
```html
<h1 style="font-family: Poppins, Arial; color: #141413; font-size: 36pt;">
  Document Title
</h1>
<p style="font-family: Lora, Georgia; color: #141413; font-size: 12pt;">
  Body content with appropriate typography
</p>
```

### Example 2: Branded Color Scheme
```css
:root {
  --brand-dark: #141413;
  --brand-light: #faf9f5;
  --brand-accent: #d97757;
  --heading-font: Poppins, Arial, sans-serif;
  --body-font: Lora, Georgia, serif;
}
```

## Detail Files

- **Color reference**: All official brand colors with usage guidelines
- **Typography guide**: Font specifications and hierarchy
- **Examples**: Branded artifact templates

## Notes

- Fonts should be pre-installed for best results
- Always include fallback fonts for system compatibility
- Maintain accessibility standards with color contrast
- Brand guidelines apply to external-facing artifacts

## Related Skills

- **Document Skills** - For creating branded documents
- **Visual Design** - For additional design patterns
