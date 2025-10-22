---
description: "Auto-loaded context for ServiceNow documentation lookup and research"
applyTo: "**/*{servicenow,ServiceNow,SERVICENOW,documentation,docs}*"
---

# ServiceNow Documentation - Automatic Context Instructions

**Related Prompt:** `/servicenow-docs`  
**Related Skill:** `.github/copilot-skills/documentation/servicenow-docs/README.md`

**Triggers:** servicenow, documentation lookup, docs search, servicenow api, incident management, change management, itsm, hrsd, workflow, flow designer, service catalog, rest api

## Context: ServiceNow Documentation Research

When working with ServiceNow-related files or when user queries contain ServiceNow documentation keywords, this context is automatically activated.

## Default Behaviors

### When user mentions "servicenow docs" or "servicenow documentation"
1. Suggest `/servicenow-docs` skill prompt
2. Load MCP tool reference
3. Provide guided workflow based on user goal
4. Help construct appropriate search queries

### When user mentions "search servicenow" or "find servicenow docs"
1. Start with `search_servicenow()` (searches actual page content)
2. Provide relevant URLs from search results
3. Offer to get full page content if needed
4. Suggest related searches based on results

### When user mentions "incident", "change", "request", "itsm"
1. Load ITSM-specific documentation patterns
2. Reference incident/change/problem management bundles
3. Provide process documentation links
4. Suggest workflow automation resources

### When user mentions "workflow", "flow design", or "flow designer"
1. Load workflow design patterns and best practices
2. Reference platform development bundles
3. Link to code examples and templates
4. Suggest Flow Designer documentation

### When user mentions "rest api" or "servicenow api"
1. Load API reference patterns
2. Search for API documentation
3. Provide endpoint examples
4. Link to authentication and integration guides

### When user mentions "service catalog" or "catalog item"
1. Load service catalog configuration patterns
2. Reference catalog management documentation
3. Provide item creation guides
4. Suggest catalog portal customization resources

## Quality Guidelines

### ✅ Do
- Use `search_servicenow()` first for precise topic searches
- Prefer 1-2 word search queries for best results
- Always verify version (Yokohama, Xanadu, Zurich) when relevant
- Provide direct URLs from search results
- Get full page content for implementation guides
- Guide users through the tool decision tree
- Suggest related searches based on initial results
- Check for version-specific differences when applicable

### ❌ Don't
- Search with long phrases (use AND logic instead)
- Ignore version filters when working with version-specific code
- Assume user has access to all documentation
- Return only URLs without explaining context
- Mix different versions without indicating which is which
- Assume the user knows the correct bundle names

## Common Patterns

### Documentation Research Workflow

```
User Query: "How do I..."
    ↓
1. Parse intent and topic
2. Identify appropriate search terms (1-2 words)
3. search_servicenow(query=..., limit=5-10)
    ↓
4. Review results for relevance
5. get_page_content(url="<most relevant>")
    ↓
6. Provide answer with source attribution
7. Offer to search for related topics
```

### Version-Aware Lookup

```
User Query: "...for Yokohama..."
    ↓
1. Verify version prefix in search
2. search_documentation(query=...) returns version-filtered results
    ↓
3. Confirm bundle has correct version (e.g., "yokohama-*")
4. get_bundle_details(bundle_name="yokohama-...")
    ↓
5. Provide version-specific guidance
```

### Bundle Exploration

```
User Query: "What docs exist for ITSM?"
    ↓
1. list_product_categories()
2. Locate "IT Service Management" category
3. list_bundles(category="IT Service Management", limit=20)
4. For interesting bundles: get_bundle_details(bundle_name="...")
    ↓
5. Provide summary of available documentation
6. Guide to specific topics
```

## Tool Selection Guide

| User Goal | Best Tool | Why |
|-----------|-----------|-----|
| "Find docs about X" | `search_servicenow` | Searches page content, most precise |
| "What bundles exist?" | `list_bundles` + `search_documentation` | Browse available resources |
| "Explore ITSM docs" | `list_product_categories` → `list_bundles` | Discovery workflow |
| "Get all pages in bundle" | `get_bundle_details` | Complete table of contents |
| "Read this page" | `get_page_content` | Full documentation content |

## Response Formatting

### Quick Answer (Search Results)
```
Based on ServiceNow docs:

**[Title]** (Version: [X])
- Summary: [snippet]
- Documentation: [URL]

**[Title 2]** (Version: [X])
- Summary: [snippet]
- Documentation: [URL]

Would you like me to get the full page content for any of these?
```

### Detailed Answer (Page Content)
```
From ServiceNow Documentation:
[Full page content with relevant sections]

Source: [URL]
Version: [X]
Category: [Product Area]

Related topics: [suggestions for follow-up searches]
```

### Navigation Suggestion
```
ServiceNow Documentation Bundles:
- [Bundle 1]: [description]
- [Bundle 2]: [description]

Recommended navigation:
1. Start with: [most relevant bundle]
2. Then explore: [related bundle]
3. Reference: [API or code examples]
```

## Search Query Construction

### Good Queries (1-2 words, specific)
- "incident management" ✅
- "create workflow" ✅
- "REST API" ✅
- "service catalog" ✅
- "flow designer" ✅

### Poor Queries (Too long, too general)
- "how do I create an incident in servicenow" ❌
- "servicenow documentation" ❌
- "what is the platform" ❌

### Query Strategy
1. Identify main topic (incident, change, workflow, etc.)
2. Add specificity if needed (create, configure, manage, etc.)
3. Avoid generic terms
4. Use 1-2 words maximum
5. Try alternative phrasing if first search doesn't help

## Error Handling

### When search returns no results
```
No results found for "X". Try:
- Broader search term
- Alternative phrasing
- Related topic search
- Browse by category with list_bundles()
```

### When page access fails
```
The page may require authentication. Try:
- Searching for the content instead
- Finding alternative documentation pages
- Checking bundle table of contents
```

### When unsure about bundle name
```
Use list_bundles() to verify available bundles:
- list_bundles(category="[your area]", limit=20)
- Then use get_bundle_details(bundle_name="[exact name]")
```

## Version Awareness

### Supported Versions
- **Yokohama** – Current stable (default filter)
- **Xanadu** – Previous version
- **Zurich** – Next generation
- **All versions** – If no filter configured

### Version Indicators
- Bundles prefixed with version: "yokohama-*", "xanadu-*", "zurich-*"
- Publication info includes version: "Yokohama, Xanadu, Zurich"
- Search results labeled with version
- Specify version in user responses

### When Versions Matter
- API changes between versions
- Feature availability differs
- Configuration steps vary
- User's instance version matters

## Integration with User Context

### If user is working with ServiceNow code
- Auto-load this context automatically
- Suggest appropriate documentation lookups
- Provide implementation guidance

### If user mentions ServiceNow in conversation
- Recognize need for documentation
- Proactively suggest relevant skill
- Prepare to search and retrieve docs

### If user has version-specific requirements
- Adjust search and filter behavior
- Verify returned docs match version
- Highlight version-specific differences

## Reference Documentation

For detailed tool documentation, see:
- **Tool Reference**: `.github/copilot-skills/documentation/servicenow-docs/tools.md`
- **Workflows**: `.github/copilot-skills/documentation/servicenow-docs/workflows.md`
- **API Guide**: `.github/copilot-skills/documentation/servicenow-docs/api-reference.md`
- **Best Practices**: `.github/copilot-skills/documentation/servicenow-docs/best-practices.md`

## Next Steps

When user needs ServiceNow documentation:
1. Suggest `/servicenow-docs` prompt
2. Identify user's specific goal
3. Choose appropriate tool from decision tree
4. Construct 1-2 word search query
5. Execute tool and get results
6. Provide full page content if needed
7. Offer follow-up searches or related resources

## Related Skills

- **Git Ops** – Version control for ServiceNow instance files
- **MCP Builder** – Create custom MCP servers for other platforms
- **Document Project** – Generate documentation from ServiceNow code
- **Create Skill** – Build new skills for specialized domains

## Quick Reference

```
// Quick lookup
search_servicenow(query="topic", limit=5)

// Explore category
list_product_categories()
list_bundles(category="...", limit=10)

// Browse bundle
get_bundle_details(bundle_name="yokohama-...")

// Read page
get_page_content(url="...")
```

