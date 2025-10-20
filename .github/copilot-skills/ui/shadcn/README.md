# ShadCN UI Components Skill

**Status**: ✅ Active  
**Version**: 1.0.0  
**Generated**: October 19, 2025  
**Source**: https://ui.shadcn.com/

## Overview

Comprehensive documentation and patterns for shadcn/ui - a beautiful and accessible component library built with Radix UI and Tailwind CSS. This skill provides instant access to component APIs, installation instructions, theming guides, and usage patterns.

## What This Skill Provides

### 📦 Components Documentation (66 components)
- **UI Components**: Accordion, Alert, Avatar, Badge, Button, Card, Checkbox, Dialog, Dropdown, Form, Input, Select, Sheet, Table, Tabs, Toast, Tooltip, and 49+ more
- **Layout Components**: Separator, Scroll Area, Resizable, Sidebar
- **Data Display**: Data Table, Empty State, Typography
- **Form Components**: Calendar, Date Picker, Combobox, Input OTP, Radio Group
- **Overlay Components**: Popover, Hover Card, Context Menu, Sheet, Dialog

### 🛠 Installation & Setup (14 frameworks)
- Next.js, Vite, Astro, Remix
- Laravel, Gatsby, React Router
- TanStack Start, TanStack Router
- Manual installation

### 🎨 Theming & Customization
- Dark mode integration (Next.js, Vite, Astro, Remix)
- Custom color schemes
- Tailwind v4 support
- CSS variables and theming

### 🔧 CLI Tools
- Component installation
- Monorepo setup
- Registry management

### 📝 Forms Integration
- React Hook Form
- TanStack Form

## File Structure

```
.github/copilot-skills/shadcn/
├── README.md                    # This file - Skill overview
├── patterns.md                  # Common code patterns (quick reference)
├── reference.md                 # Documentation index
├── references/                  # Organized documentation
│   ├── components.md            # 66 UI components (95KB)
│   ├── installation.md          # Framework setup guides (18KB)
│   ├── cli.md                   # CLI commands (8.8KB)
│   ├── theming.md              # Theming and dark mode (7.8KB)
│   └── other.md                # Registry, forms, changelog (19KB)
├── assets/                      # (Empty - for future templates)
└── scripts/                     # (Empty - for custom tools)

.github/prompts/
└── shadcn.skill.prompt.md      # Skill execution workflow

.github/instructions/
└── shadcn.instructions.md      # Auto-loaded context rules
```

## How to Use This Skill

### Automatic Context Loading

The skill auto-loads when working with these file patterns:
- `**/*.tsx` - TypeScript React components
- `**/*.jsx` - JavaScript React components
- `**/components.json` - shadcn configuration
- `**/tailwind.config.*` - Tailwind config files

### Manual Skill Activation

Use the slash command in Copilot Chat:
```
/shadcn
```

### Keywords for Skill Suggestion

The skill is suggested when your query contains:
- shadcn, shadcn/ui, radix ui
- ui components, component library
- tailwind components, accessible components
- Component names: button, card, dialog, form, input, select, sheet, table, tabs, toast, tooltip

## Quick Reference

### Common Tasks

**Install a component:**
```bash
npx shadcn@latest add button
```

**Install multiple components:**
```bash
npx shadcn@latest add button card dialog
```

**Initialize shadcn in a project:**
```bash
npx shadcn@latest init
```

### Component Usage Pattern

```tsx
import { Button } from "@/components/ui/button"

export function MyComponent() {
  return (
    <Button variant="outline" size="lg">
      Click me
    </Button>
  )
}
```

### Form Integration Pattern

```tsx
import { useForm } from "react-hook-form"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"

export function MyForm() {
  const form = useForm()
  
  return (
    <Form {...form}>
      <FormField
        control={form.control}
        name="username"
        render={({ field }) => (
          <FormItem>
            <FormLabel>Username</FormLabel>
            <FormControl>
              <Input placeholder="shadcn" {...field} />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
    </Form>
  )
}
```

## Documentation Categories

### Components (66 pages, 95KB)
Detailed documentation for all UI components including:
- Installation commands
- Import statements
- Usage examples
- Props and variants
- Accessibility features

**File**: `references/components.md`

### Installation (14 pages, 18KB)
Framework-specific setup guides:
- Next.js, Vite, Astro, Remix
- Laravel, Gatsby
- React Router, TanStack
- Manual installation

**File**: `references/installation.md`

### Theming (6 pages, 7.8KB)
Theme customization and dark mode:
- Dark mode setup per framework
- CSS variables
- Color schemes
- Tailwind v4 support

**File**: `references/theming.md`

### CLI (4 pages, 8.8KB)
Command-line tools:
- Component installation
- Monorepo configuration
- Registry management

**File**: `references/cli.md`

### Other (11 pages, 19KB)
Additional documentation:
- Registry setup
- Authentication patterns
- Forms integration
- Changelog
- Figma integration
- JavaScript support
- Legacy documentation

**File**: `references/other.md`

## Skill Dependencies

This skill is **standalone** with no dependencies on other skills.

### Complementary Skills

- `/create-skill` - For customizing this skill further
- `/document-project` - For documenting your shadcn implementation

## Data Source

- **Official Documentation**: https://ui.shadcn.com/
- **Scraped Pages**: 101 pages
- **Last Updated**: October 19, 2025
- **Scraper Config**: `.github/copilot-skills/docs-to-skill/configs/shadcn.json`

## Regenerating This Skill

To update with the latest shadcn documentation:

```bash
# Activate Python environment
source .venv/bin/activate

# Run scraper (15-20 minutes)
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/shadcn.json

# Or resume if interrupted
python3 .github/copilot-skills/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/docs-to-skill/configs/shadcn.json \
  --resume
```

## Quality Guidelines

When working with shadcn/ui:

- ✅ Use official component APIs from documentation
- ✅ Follow Radix UI accessibility patterns
- ✅ Leverage Tailwind CSS for styling
- ✅ Use TypeScript for type safety
- ✅ Implement proper form validation
- ⚠️ Don't bypass accessibility features
- ⚠️ Don't modify core component files directly
- ⚠️ Avoid deprecated patterns

## Examples in Documentation

Each component page includes:
- Installation command
- Import statement
- Basic usage example
- Variants and options
- Composition patterns

See `references/components.md` for comprehensive examples.

## Contributing

To improve this skill:

1. Update scraper config: `.github/copilot-skills/docs-to-skill/configs/shadcn.json`
2. Regenerate skill files
3. Add custom patterns to `patterns.md`
4. Add helper scripts to `scripts/` directory
5. Add templates to `assets/` directory

## License

Documentation content © shadcn/ui  
Skill implementation: MIT License

## Related Resources

- **Official Docs**: https://ui.shadcn.com/
- **GitHub**: https://github.com/shadcn-ui/ui
- **Radix UI**: https://www.radix-ui.com/
- **Tailwind CSS**: https://tailwindcss.com/
