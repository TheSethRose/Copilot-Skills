---
description: Claude AI platform documentation - API, features, models, and best practices
---

# Claude

**Purpose**: Claude AI platform documentation - API, features, models, and best practices

## When to Use This Skill

Use this skill when:
- Working with claude projects
- Implementing claude features
- Debugging claude code
- Learning claude best practices
- Building applications with claude

**Keywords**: claude, getting_started, api, models, features, prompt_engineering, agent_skills, claude_code, evaluation, other

## Quick Reference

### Common Patterns

**1. Copy@dataclass class ResultMessage: subtype: str duration_ms: int duration_api_m**

```
@dataclass
class ResultMessage:
    subtype: str
    duration_ms: int
    duration_api_ms: int
    is_error: bool
    num_turns: int
    session_id: str
    total_cost_usd: float | None = None
    usa
```

**2. @dataclass class ResultMessage: subtype: str duration_ms: int duration_api_ms: i**

```
@dataclass
class ResultMessage:
    subtype: str
    duration_ms: int
    duration_api_ms: int
    is_error: bool
    num_turns: int
    session_id: str
    total_cost_usd: float | None = None
    usa
```

**3. @dataclass class ResultMessage: subtype: str duration_ms: int duration_api_ms: i**

```
@dataclass
class ResultMessage:
    subtype: str
    duration_ms: int
    duration_api_ms: int
    is_error: bool
    num_turns: int
    session_id: str
    total_cost_usd: float | None = None
    usa
```

**4. Copytype SDKResultMessage = | { type: 'result'; subtype: 'success'; uuid: UUID; **

```
type SDKResultMessage = 
  | {
      type: 'result';
      subtype: 'success';
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boo
```

**5. type SDKResultMessage = | { type: 'result'; subtype: 'success'; uuid: UUID; sess**

```
type SDKResultMessage = 
  | {
      type: 'result';
      subtype: 'success';
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boo
```

### Code Examples

**Example 1** (python):
```python
async def query(
    *,
    prompt: str | AsyncIterable[dict[str, Any]],
    options: ClaudeAgentOptions | None = None
) -> AsyncIterator[Message]
```

**Example 2** (javascript):
```javascript
function query({
  prompt,
  options
}: {
  prompt: string | AsyncIterable<SDKUserMessage>;
  options?: Options;
}): Query
```

**Example 3** (python):
```python
# PDF Processing

## Quick start

Use pdfplumber to extract text from PDFs:

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For advanced form filling, see [FORMS.md](FORMS.md).
```

## Reference Documentation

This skill includes comprehensive documentation in `.github/copilot-skills/ai/claude/references/`:

- **agent_skills.md** - Agent Skills documentation
- **api.md** - Api documentation
- **claude_code.md** - Claude Code documentation
- **evaluation.md** - Evaluation documentation
- **features.md** - Features documentation
- **getting_started.md** - Getting Started documentation
- **models.md** - Models documentation
- **other.md** - Other documentation
- **prompt_engineering.md** - Prompt Engineering documentation

## How to Use

### For Quick Answers
Ask directly about claude features, APIs, or patterns.

### For Detailed Information
Reference specific documentation files:
- Check `references/getting_started.md` for setup
- Check `references/api_reference.md` for API details
- Check category files for specific topics

### For Code Examples
Use the Quick Reference patterns above or ask for specific examples.

## Related Skills

- None (standalone skill)

## More Information

- **Base Documentation**: https://docs.claude.com/en/home
- **Generated**: 2025-10-21
- **Total Pages**: 328
