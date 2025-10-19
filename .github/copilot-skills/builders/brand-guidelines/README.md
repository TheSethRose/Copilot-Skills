---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any artifact requiring visual identity
version: "1.0.0"
tags: ["branding", "visual-identity", "styling", "typography", "design"]
dependencies: []
license: Adapted from Anthropic's brand-guidelines skill
---

# Brand Guidelines

## Overview

Access Anthropic's official brand identity and style resources for applying consistent visual formatting to artifacts.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Maintains color fidelity across different systems
- Ensures accessible contrast ratios

## Usage Patterns

### CSS Implementation
```css
:root {
  --brand-dark: #141413;
  --brand-light: #faf9f5;
  --brand-accent: #d97757;
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

### HTML Implementation
```html
<h1 style="font-family: Poppins, Arial; color: #141413;">Heading</h1>
<p style="font-family: Lora, Georgia; color: #141413;">Body text</p>
```

## Best Practices

### Color Usage
- Use Dark (#141413) for primary text and important elements
- Use Light (#faf9f5) for backgrounds and inverted text
- Reserve accent colors for highlights and calls-to-action
- Maintain 4.5:1 contrast ratio minimum for accessibility

### Typography
- Headings: Poppins 24pt minimum (with Arial fallback)
- Body: Lora 12pt standard (with Georgia fallback)
- Always include fallback fonts for system compatibility
- Maintain consistent hierarchy across documents

### Visual Consistency
- Apply brand styling to all external-facing artifacts
- Use consistent color palette throughout document
- Follow typography hierarchy (H1 > H2 > H3 > body)
- Test appearance across different systems and platforms

## Progressive Disclosure

For additional details, see:
- **Color Theory**: Advanced color usage and accessibility guidelines
- **Typography Guide**: Complete font specifications and sizing
- **Examples**: Branded artifact templates and samples

## Related Skills

- **Document Skills** - Creating branded documents in multiple formats
- **PDF Handling** - Applying brand styling to PDF outputs
- **Visual Design** - Additional design patterns and principles
