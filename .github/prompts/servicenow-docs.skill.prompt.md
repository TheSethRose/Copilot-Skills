---
description: "Intelligent access to 200+ ServiceNow documentation bundles for research, implementation guides, and API references"
---

# ServiceNow Documentation Lookup

**Slash Command**: `/servicenow-docs`  
**Status**: Available  
**Transport**: MCP Server (SSE/HTTP)

## When to Use This Skill

Use this skill when you need to:

- 🔍 **Find ServiceNow documentation** – Search across 200+ bundles by product or topic
- 📋 **Browse available content** – Discover what documentation exists for a product area
- 🔗 **Get implementation guides** – Find step-by-step instructions for features
- 💻 **Access API documentation** – Look up API endpoints and code examples
- 🎯 **Explore by version** – Find documentation specific to Yokohama, Xanadu, or Zurich versions
- 📖 **Read page content** – Access full documentation page text without visiting ServiceNow website
- 🏗️ **Understand workflows** – Research how to build workflows, flows, and automations
- 📊 **ITSM research** – Explore incident, change, problem, and request management docs

## The Problem It Solves

- ❌ Manual website navigation through 200+ documentation bundles is time-consuming
- ❌ Searching ServiceNow docs requires knowing the exact product version
- ❌ Documentation URLs are difficult to remember and often change
- ❌ Agents waste context trying to explain how to find information
- ✅ This skill provides **instant, structured access** to all documentation

## Quick Start (5 Minutes)

### Step 1: Understand the Tools

The skill provides 6 MCP tools:

| Tool | Purpose | When to Use |
|------|---------|------------|
| `search_servicenow` | Search actual documentation pages | Finding specific topics or features |
| `search_documentation` | Search bundle metadata | Discovering which bundles cover a topic |
| `list_product_categories` | See all available product areas | Understanding documentation scope |
| `list_bundles` | Browse bundles by category | Exploring what's available |
| `get_bundle_details` | Get complete table of contents | Finding pages within a bundle |
| `get_page_content` | Read full page text | Accessing detailed information |

### Step 2: Choose Your Starting Point

**If you want to find something specific:**
```
Use: search_servicenow(query="your topic")
Example: search_servicenow(query="create incident", limit=5)
```

**If you want to explore what exists:**
```
Use: list_product_categories() → list_bundles() → get_bundle_details()
```

**If you have a direct page URL:**
```
Use: get_page_content(url="https://...")
```

### Step 3: Follow Up

Use the results to get more detailed information:
- URLs from search results → Use `get_page_content()`
- Bundle IDs from listings → Use `get_bundle_details()`
- Page from TOC → Use `get_page_content()`

## Common Workflows

### Workflow 1: Find Implementation Guide (2-3 steps)

**Goal**: "How do I create a custom service catalog item?"

```
1. search_servicenow(query="service catalog item")
   ↓ Get list of relevant pages with URLs
2. get_page_content(url="<most relevant URL>")
   ↓ Read full implementation guide
```

**Result**: Complete step-by-step instructions with examples

---

### Workflow 2: Explore Product Area (3-4 steps)

**Goal**: "What ITSM documentation exists?"

```
1. list_product_categories()
   ↓ See all product areas including "IT Service Management"
2. list_bundles(category="IT Service Management", limit=10)
   ↓ Browse ITSM bundles by version
3. get_bundle_details(bundle_name="yokohama-it-service-management")
   ↓ See all pages in the bundle
4. get_page_content(url="<interesting page>")
   ↓ Read details
```

**Result**: Complete understanding of available ITSM documentation

---

### Workflow 3: Find API Reference (2-3 steps)

**Goal**: "How do I use the ServiceNow REST API for incidents?"

```
1. search_servicenow(query="REST API incident", limit=5)
   ↓ Find API reference pages
2. get_page_content(url="<API reference URL>")
   ↓ Read API documentation with examples
```

**Result**: API endpoints, parameters, and code examples

---

### Workflow 4: Search Within Specific Version (2-3 steps)

**Goal**: "I need Yokohama-specific documentation for Flow Designer"

```
1. list_product_categories()
   ↓ Confirm category names
2. search_documentation(query="Flow Designer", limit=10)
   ↓ Results filtered to configured version (Yokohama by default)
3. get_bundle_details(bundle_name="yokohama-application-development")
   ↓ Browse all Flow Designer related pages
```

**Result**: Version-specific documentation with all relevant pages

---

### Workflow 5: Deep Dive Research (5+ steps)

**Goal**: "Teach me everything about Workflow design best practices"

```
1. list_product_categories()
   → Understand documentation structure
2. search_servicenow(query="workflow best practices", limit=20)
   → Get multiple relevant pages
3. For each interesting result:
   get_page_content(url="...")
   → Read full content of each page
4. search_documentation(query="workflow design", limit=5)
   → Find related bundles
5. get_bundle_details(bundle_name="<selected>")
   → Browse all workflow-related pages
```

**Result**: Comprehensive understanding from multiple sources

## Tool Details

### search_servicenow (Most Common)

**Purpose**: Search across all ServiceNow documentation pages using native search.

**Parameters**:
- `query` (string): What you're looking for (use 1-2 words for best results)
- `limit` (int): Max results (1-50, default 10)
- `sort` (string): 'relevance' (default), 'updated-desc', or 'updated-asc'
- `category` (string): Optional product filter

**Returns**: List of matching pages with:
- Page title
- Publication name
- Version and product info
- Brief snippet/summary
- Direct URL

**Best for**: Finding specific topics, APIs, implementation guides

**Example**:
```
search_servicenow(
  query="create workflow",
  limit=10,
  sort="relevance"
)
```

---

### search_documentation

**Purpose**: Search across bundle metadata (titles and categories).

**Parameters**:
- `query` (string): Bundle or product name
- `category` (string): Optional product area
- `limit` (int): Results (1-50, default 10)

**Returns**: Matching bundles with product info and URLs

**Best for**: Finding which bundle covers a topic, version discovery

**Example**:
```
search_documentation(
  query="ITSM",
  category="IT Service Management"
)
```

---

### list_product_categories

**Purpose**: Discover all product areas with documentation.

**Parameters**: None

**Returns**: List of unique product categories

**Best for**: Understanding documentation scope, getting valid category filters

**Example**:
```
list_product_categories()
→ Returns: AI Experiences, Building applications, ITSM, HRSD, etc.
```

---

### list_bundles

**Purpose**: Browse documentation bundles by category.

**Parameters**:
- `category` (string): Product area filter
- `limit` (int): Per page (1-100, default 20)
- `offset` (int): Pagination offset (default 0)

**Returns**: Paginated bundle list with metadata

**Best for**: Exploring what bundles exist, finding by version

**Example**:
```
list_bundles(
  category="Building applications",
  limit=10,
  offset=0
)
```

---

### get_bundle_details

**Purpose**: Get complete table of contents for a bundle.

**Parameters**:
- `bundle_name` (string): Bundle ID (e.g., "yokohama-platform-administration")
- `search` (string): Optional filter by page title
- `limit` (int): Results per page (1-500, default 100)
- `offset` (int): Pagination offset

**Returns**: All pages in bundle with titles and URLs

**Best for**: Navigation, finding specific pages, understanding bundle scope

**Example**:
```
get_bundle_details(
  bundle_name="yokohama-platform-administration",
  search="user provisioning"
)
```

---

### get_page_content

**Purpose**: Retrieve full text of a documentation page.

**Parameters**:
- `url` (string): Full page URL

**Returns**: Clean, formatted page text (up to 25,000 characters)

**Best for**: Reading full documentation, extracting code examples

**Example**:
```
get_page_content(
  url="https://servicenow-be-prod.servicenow.com/bundle/yokohama-platform-administration/page/administer/security/concept/c_UserProvisioning.html"
)
```

---

## Decision Tree: Which Tool to Use?

```
START: What do you need?
│
├─ "Find documentation about X" → search_servicenow()
│  └─ Result page URL → get_page_content()
│
├─ "What bundles exist for X?" → search_documentation()
│  └─ Bundle ID from results → get_bundle_details()
│
├─ "Show me all product areas" → list_product_categories()
│  └─ Pick category → list_bundles(category="...")
│     └─ Pick bundle → get_bundle_details()
│
├─ "Browse X bundle" → get_bundle_details(bundle_name="...")
│  └─ Find interesting page → get_page_content()
│
└─ "I have a direct URL" → get_page_content(url="...")
```

## Tips for Better Results

### Tip 1: Search Tips
- **Use 1-2 words** for search: "incident", "flow designer", "REST API"
- **Avoid long phrases** – ServiceNow search uses AND operators
- **Be specific** – "create custom table" better than "tables"
- **Try multiple terms** – If first search doesn't help, try different words

### Tip 2: Version Awareness
- Bundles include version prefix: "yokohama-*", "xanadu-*", "zurich-*"
- Server can be configured to filter by version
- Check bundle name to verify you're using the right version

### Tip 3: Navigation Strategy
- Start with `search_servicenow()` for quick answers
- Use `get_bundle_details()` when you need to explore a topic deeply
- Use `list_bundles()` to compare multiple bundles side-by-side

### Tip 4: Handling Large Bundles
- Use `search` parameter in `get_bundle_details()` to filter pages
- Use pagination (`limit` and `offset`) for large result sets
- Get TOC first, then request specific pages

### Tip 5: Reading Efficiently
- Use `get_page_content()` for full understanding
- Page content is truncated at 25,000 chars (indicated in response)
- Focus on the most relevant pages to stay in context budget

## Related Skills

- **Git Ops** – Version control for ServiceNow configuration files
- **Document Project** – Generate docs from ServiceNow code
- **MCP Builder** – Create custom MCP servers for other platforms

## Troubleshooting

### "No results found"
- Try simpler search terms (1-2 words)
- Check if category name is valid using `list_product_categories()`
- Verify version filter is set correctly

### "Failed to retrieve page"
- URL may require authentication – try searching instead
- Page may have been moved – search for the topic
- Try alternative page from search results

### Getting too many results
- Make search more specific: "incident creation" instead of "incident"
- Use category filters to narrow scope
- Increase limit and review top results

### Bundle name not found
- Double-check bundle name spelling and version prefix
- Use `list_bundles()` to see available bundle names
- Try different version (yokohama, xanadu, zurich)

## Example Scenarios

### Scenario 1: "Help me understand ServiceNow workflows"

```
1. search_servicenow(query="workflow design", limit=5)
2. get_page_content(url="<most comprehensive URL>")
3. search_servicenow(query="workflow best practices", limit=3)
4. get_page_content(url="<best practices page>")
5. search_documentation(query="workflow", limit=3)
6. get_bundle_details(bundle_name="<selected bundle>")
```

Result: Multi-source understanding of workflows

---

### Scenario 2: "I need to look up the ServiceNow REST API"

```
1. search_servicenow(query="REST API", limit=10)
2. Review results for "API Reference" pages
3. get_page_content(url="<REST API reference>")
4. If need examples: get_page_content(url="<code examples page>")
```

Result: Complete API reference with examples

---

### Scenario 3: "What documentation exists for our ITSM version?"

```
1. list_product_categories()
2. list_bundles(category="IT Service Management", limit=20)
3. For each bundle: get_bundle_details(bundle_name="...")
4. Explore pages that look relevant
```

Result: Complete inventory of available ITSM documentation

## Success Indicators

You're using this skill effectively when:

✅ You find documentation without leaving the editor  
✅ You avoid manual website navigation  
✅ You stay in your current context/conversation  
✅ You get direct URLs to pages  
✅ You find multiple relevant pages quickly  
✅ You understand which version you're reading  

## Next Steps

1. **Get familiar with the tools** – Read tool details above
2. **Choose a starting workflow** – Pick one of the 5 workflows
3. **Try a search** – Start with `search_servicenow(query="your topic")`
4. **Navigate with results** – Use URLs returned to dive deeper
5. **Explore a bundle** – Use `get_bundle_details()` for comprehensive browsing

---

**Ready to research ServiceNow documentation?** Start with `search_servicenow(query="your topic")` or pick a workflow above.

