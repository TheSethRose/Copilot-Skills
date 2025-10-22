# ServiceNow Documentation Lookup Skill

This skill provides intelligent access to 200+ ServiceNow documentation bundles through the ServiceNow MCP server.

## Overview

**Skill Prompt**: `.github/prompts/servicenow-docs.skill.prompt.md`  
**Instructions**: `.github/instructions/servicenow-docs.instructions.md`  
**Status**: v1.0.0  

The skill teaches agents how to:
- Search across 200+ ServiceNow documentation bundles
- Browse by product category (ITSM, HRSD, AI Experiences, etc.)
- Navigate complete table of contents for bundles
- Retrieve full documentation page content
- Filter by ServiceNow version (Yokohama, Xanadu, Zurich)

## MCP Server Integration

This skill requires the **ServiceNow MCP Server** running:

```json
{
  "servers": {
    "servicenow-docs": {
      "url": "https://your-domain.com/mcp"
    }
  }
}
```

The server provides 6 MCP tools:
1. `search_servicenow` - Search page content
2. `search_documentation` - Search bundle metadata
3. `list_product_categories` - Browse product areas
4. `list_bundles` - List documentation bundles
5. `get_bundle_details` - Get complete table of contents
6. `get_page_content` - Retrieve full page text

## When to Use This Skill

✅ Finding ServiceNow documentation quickly  
✅ Researching features and capabilities  
✅ Looking up API references  
✅ Finding implementation guides  
✅ Exploring ITSM workflows and best practices  
✅ Discovering available functionality  
✅ Understanding version-specific features  

## Quick Example

**User Request**: "How do I create an incident in ServiceNow?"

**Skill Response**:
```
1. search_servicenow(query="create incident", limit=5)
   ↓ Get list of relevant pages
2. get_page_content(url="<most relevant>")
   ↓ Read full implementation guide
```

**Result**: Step-by-step instructions with examples

## Skill Architecture

### Progressive Disclosure
- **Layer 1**: Skill prompt (5-minute overview of all workflows)
- **Layer 2**: Tool reference (detailed parameter docs)
- **Layer 3**: Common patterns (real-world scenarios)
- **Layer 4**: Advanced usage (tips and troubleshooting)

### File Organization
```
.github/
├── prompts/servicenow-docs.skill.prompt.md (Main workflow guide)
├── instructions/servicenow-docs.instructions.md (Auto-loaded context)
└── copilot-skills/servicenow-docs/
    ├── README.md (This file)
    ├── tools.md (Tool reference)
    ├── workflows.md (Common patterns)
    ├── api-reference.md (MCP API docs)
    └── best-practices.md (Usage tips)
```

### Dynamic Discovery
- **Keyword triggers**: servicenow, documentation, docs, api, itsm, hrsd, workflow
- **Auto-loaded for**: Files matching `**/*{servicenow,docs}*`
- **Slash command**: `/servicenow-docs`
- **Related to**: MCP Builder, Git Ops, Document Project skills

### Deterministic Execution
- MCP tools return structured JSON responses
- All results include direct URLs
- Pagination built-in for large result sets
- Clear error messages with remediation tips

### Composability
- Works with Git Ops for version control
- References MCP Builder for server deployment
- Integrates with Document Project for content generation
- No overlapping functionality with other skills

## Available Workflows

### 1. Quick Topic Search (2-3 steps)
Find specific documentation quickly.

### 2. Product Exploration (3-4 steps)
Browse available documentation for a product area.

### 3. API Reference Lookup (2-3 steps)
Find and read API documentation with examples.

### 4. Version-Specific Research (2-3 steps)
Find documentation for specific ServiceNow version.

### 5. Deep Dive Research (5+ steps)
Comprehensive multi-source documentation research.

See `.github/prompts/servicenow-docs.skill.prompt.md` for full workflow details.

## Tool Decision Tree

```
What do you need?
│
├─ Find specific docs → search_servicenow()
├─ Explore a topic → search_documentation()
├─ Browse categories → list_product_categories()
├─ Browse bundles → list_bundles()
├─ See bundle contents → get_bundle_details()
└─ Read page content → get_page_content()
```

## Configuration

The skill works with the ServiceNow MCP server configured in `mcp.json`:

```json
{
  "servers": {
    "servicenow-docs": {
      "url": "https://servicenow.seth-rose.dev/mcp"
    }
  }
}
```

**Server Environment Variables**:
- `SERVICENOW_VERSIONS` - Filter to specific versions (yokohama, xanadu, zurich)
- `SERVICENOW_API_KEY` - Optional API key for authentication
- `SERVER_HOST` - Server bind address (default: 0.0.0.0)
- `SERVER_PORT` - Server port (default: 8000)

## Search Tips

### Good Queries (1-2 words)
- "incident management"
- "REST API"
- "workflow design"
- "service catalog"

### Poor Queries (Too long)
- "how do I create an incident in servicenow" ❌
- "what is the servicenow platform" ❌

### Search Strategy
1. Use 1-2 words for best results
2. ServiceNow search uses AND operators
3. Try alternative phrasing if needed
4. Use category filters to narrow scope

## Documentation Bundles

The MCP server provides access to 200+ bundles across ServiceNow's product portfolio:

**Product Areas**:
- IT Service Management (ITSM)
- Human Resources Service Delivery (HRSD)
- AI Experiences
- Platform Administration
- Building Applications
- Financial Services
- Customer Service Management
- And many more...

**Versions**:
- Yokohama (current)
- Xanadu (previous)
- Zurich (next generation)

Use `list_product_categories()` to see complete list.

## Common Use Cases

### Use Case 1: Learn ITSM Processes
```
1. list_product_categories()
2. search_documentation(query="ITSM", limit=5)
3. get_bundle_details(bundle_name="yokohama-it-service-management")
4. get_page_content(url="<relevant pages>")
```

### Use Case 2: Find API Examples
```
1. search_servicenow(query="REST API incident", limit=10)
2. get_page_content(url="<API reference page>")
3. Extract code examples
```

### Use Case 3: Understand Workflow Design
```
1. search_servicenow(query="workflow design", limit=5)
2. search_servicenow(query="flow designer best practices", limit=3)
3. get_page_content(url="<comprehensive guide>")
```

## Performance Characteristics

- **Search Speed**: ~500ms-1s per query
- **Page Content**: ~1-2s for retrieval and parsing
- **Bundle TOC**: ~500ms-1s
- **Result Limits**: Up to 50 results per search
- **Content Truncation**: 25,000 characters (with notice)

## Troubleshooting

### No Results
- Try simpler search terms (1-2 words)
- Check category name with `list_product_categories()`
- Try alternative phrasing

### Page Access Fails
- Try searching for content instead
- Check URL is correct
- Page may require authentication

### Bundle Not Found
- Verify bundle name spelling
- Check version prefix (yokohama, xanadu, zurich)
- Use `list_bundles()` to see available bundles

## Integration with Other Tools

The skill works seamlessly with:

| Tool | Integration |
|------|-----------|
| Git Ops | Version control ServiceNow configuration |
| MCP Builder | Deploy and update MCP server |
| Document Project | Generate docs from ServiceNow content |
| Create Skill | Create new skills following same patterns |

## Next Steps

1. **Learn the workflow** - Read `.github/prompts/servicenow-docs.skill.prompt.md`
2. **Understand the tools** - See `.github/copilot-skills/servicenow-docs/tools.md`
3. **Try common patterns** - Use examples from `.github/copilot-skills/servicenow-docs/workflows.md`
4. **Apply best practices** - Read `.github/copilot-skills/servicenow-docs/best-practices.md`

## Reference Files

- **`.github/prompts/servicenow-docs.skill.prompt.md`** - Main skill prompt (5 workflows, 8 tools)
- **`.github/instructions/servicenow-docs.instructions.md`** - Auto-loaded context (default behaviors)
- **`.github/copilot-skills/servicenow-docs/tools.md`** - Complete tool reference
- **`.github/copilot-skills/servicenow-docs/workflows.md`** - Common patterns
- **`.github/copilot-skills/servicenow-docs/api-reference.md`** - MCP API documentation
- **`.github/copilot-skills/servicenow-docs/best-practices.md`** - Tips and tricks

## Constitutional Compliance

This skill satisfies all 5 principles:

✅ **Progressive Disclosure** - Metadata → skill prompt → details → tools  
✅ **File-Based Organization** - Prompt + instructions + bundled reference  
✅ **Dynamic Discovery** - Keywords enable automatic discovery  
✅ **Deterministic Execution** - MCP tools produce consistent JSON output  
✅ **Composability** - Works with Git Ops, MCP Builder, Document Project  

## License

This skill is provided as part of the Copilot Skills Architecture and uses the ServiceNow MCP Server.

## Support

For questions or improvements:
- Review `.github/copilot-instructions.md` for system-wide guidance
- Check `.github/instructions/create-skill.instructions.md` for skill creation principles
- See `.specify/memory/constitution.md` for 5 constitutional principles

---

**Last Updated**: October 21, 2025  
**Skill Version**: 1.0.0  
**Compatible Versions**: Yokohama, Xanadu, Zurich

