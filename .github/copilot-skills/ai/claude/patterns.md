# Claude - Common Patterns

Quick reference for common claude patterns and usage.

## Code Patterns

### 1. Get started: For pre-built Agent Skills: See the quickstart tutorial to start using PowerPoint, Exce

```
---
name: PDF Processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

### 2. Get started: For pre-built Agent Skills: See the quickstart tutorial to start using PowerPoint, Exce

```
---
name: PDF Processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

### 3. Copy@dataclass class ResultMessage: subtype: str duration_ms: int duration_api_ms: int is_error: boo

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
    usage: dict[str, Any] | None = None
    result: str | None = None
```

### 4. @dataclass class ResultMessage: subtype: str duration_ms: int duration_api_ms: int is_error: bool nu

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
    usage: dict[str, Any] | None = None
    result: str | None = None
```

### 5. @dataclass class ResultMessage: subtype: str duration_ms: int duration_api_ms: int is_error: bool nu

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
    usage: dict[str, Any] | None = None
    result: str | None = None
```

### 6. Copytype SDKResultMessage = | { type: 'result'; subtype: 'success'; uuid: UUID; session_id: string; 

```
type SDKResultMessage = 
  | {
      type: 'result';
      subtype: 'success';
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      result: string;
      total_cost_usd: number;
      usage: NonN
```

### 7. type SDKResultMessage = | { type: 'result'; subtype: 'success'; uuid: UUID; session_id: string; dura

```
type SDKResultMessage = 
  | {
      type: 'result';
      subtype: 'success';
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      result: string;
      total_cost_usd: number;
      usage: NonN
```

### 8. type SDKResultMessage = | { type: 'result'; subtype: 'success'; uuid: UUID; session_id: string; dura

```
type SDKResultMessage = 
  | {
      type: 'result';
      subtype: 'success';
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      result: string;
      total_cost_usd: number;
      usage: NonN
```

## Examples

### Example 1

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

### Example 2

```python
async def query(
    *,
    prompt: str | AsyncIterable[dict[str, Any]],
    options: ClaudeAgentOptions | None = None
) -> AsyncIterator[Message]
```

### Example 3

```javascript
function query({
  prompt,
  options
}: {
  prompt: string | AsyncIterable<SDKUserMessage>;
  options?: Options;
}): Query
```

### Example 4

```python
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ],
    betas=["beta-feature-name"]
)
```


## Categories

See organized documentation in `references/`:

- `references/agent_skills.md` - Agent Skills
- `references/api.md` - Api
- `references/claude_code.md` - Claude Code
- `references/evaluation.md` - Evaluation
- `references/features.md` - Features
- `references/getting_started.md` - Getting Started
- `references/models.md` - Models
- `references/other.md` - Other
- `references/prompt_engineering.md` - Prompt Engineering
