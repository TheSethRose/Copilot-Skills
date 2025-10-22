# OpenAI - Common Patterns

Quick reference for the most common OpenAI API patterns and code examples.

## Pattern 1: Simple Chat Completion

The most basic pattern - ask a question, get an answer.

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is 2+2?"}]
)
print(response.choices[0].message.content)
```

**Use when**: You need a single, simple response without conversation history.

**See also**: `references/chat-completions.md` for streaming and multi-turn conversations.

---

## Pattern 2: Multi-turn Conversation

Maintain conversation state across multiple exchanges.

```python
messages = [
    {"role": "system", "content": "You are a helpful math tutor."}
]

# Turn 1
messages.append({"role": "user", "content": "What is 5+3?"})
response = client.chat.completions.create(model="gpt-4", messages=messages)
assistant_msg = response.choices[0].message.content
messages.append({"role": "assistant", "content": assistant_msg})

# Turn 2
messages.append({"role": "user", "content": "And if I add 2?"})
response = client.chat.completions.create(model="gpt-4", messages=messages)
print(response.choices[0].message.content)
```

**Use when**: Building chatbots or interactive applications with context.

**See also**: `references/chat-completions.md` for system prompts and few-shot learning.

---

## Pattern 3: Function Calling

Let the model decide when to call tools/functions.

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=tools
)

if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        print(f"Function: {tool_call.function.name}")
        print(f"Args: {tool_call.function.arguments}")
```

**Use when**: Model needs to execute actions or retrieve real-time data.

**See also**: `references/function-calling.md` for complete workflow.

---

## Pattern 4: Embeddings for Search

Convert text to vectors for semantic similarity.

```python
# Get embedding for a query
query_embedding = client.embeddings.create(
    input="machine learning tutorial",
    model="text-embedding-3-small"
).data[0].embedding

# Get embeddings for documents
docs = ["ML basics", "Deep learning guide", "Python programming"]
doc_embeddings = client.embeddings.create(
    input=docs,
    model="text-embedding-3-small"
).data

# Calculate similarity (cosine)
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

for doc, doc_emb in zip(docs, doc_embeddings):
    similarity = cosine_similarity(query_embedding, doc_emb.embedding)
    print(f"{doc}: {similarity:.2f}")
```

**Use when**: Building search, recommendation, or semantic analysis features.

**See also**: `references/embeddings.md` for batch processing and storage.

---

## Pattern 5: Vision - Image Analysis

Analyze images with GPT-4 Vision.

```python
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image in detail"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/image.jpg",
                        "detail": "low"  # low, high, or auto
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

**Use when**: You need to analyze, understand, or extract info from images.

**See also**: `references/vision.md` for base64 images and batch analysis.

---

## Pattern 6: Streaming Responses

Stream responses token-by-token for real-time display.

```python
with client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell a short story"}],
    stream=True
) as stream:
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
```

**Use when**: Building UIs that need real-time response display.

**See also**: `references/chat-completions.md` for async streaming.

---

## Pattern 7: Error Handling & Retries

Robust error handling with exponential backoff.

```python
import time
from openai import RateLimitError, APIError

max_retries = 3
retry_delay = 1

for attempt in range(max_retries):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Hello"}]
        )
        break
    except RateLimitError:
        if attempt < max_retries - 1:
            time.sleep(retry_delay)
            retry_delay *= 2
        else:
            raise
    except APIError as e:
        print(f"API error: {e}")
        raise
```

**Use when**: Building production applications with reliability requirements.

**See also**: `references/chat-completions.md` for timeout handling.

---

## Pattern 8: Structured Output (JSON)

Get guaranteed JSON structure from the model.

```python
from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    name: str
    date: str
    attendees: int
    location: Optional[str] = None

response = client.beta.chat.completions.parse(
    model="gpt-4-turbo",
    messages=[{
        "role": "user",
        "content": "Extract events from: Tech conf on Oct 22 in SF, 500 people"
    }],
    response_format=Event
)

event = response.choices[0].message.parsed
print(f"{event.name} on {event.date}")
```

**Use when**: You need reliable, structured data extraction.

**See also**: `references/structured-output.md` for complex schemas.

---

## Pattern 9: Batch Processing

Process multiple requests efficiently.

```python
# Create batch file
requests = [
    {
        "custom_id": "req-1",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Hello"}]
        }
    },
    {
        "custom_id": "req-2",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Hi"}]
        }
    }
]

# Submit batch
batch = client.batches.create(
    input_file_id="file-abc123",
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# Check status
status = client.batches.retrieve(batch.id)
print(f"Status: {status.status}")
```

**Use when**: Processing 100+ requests (50% cheaper, async).

**See also**: `references/batch.md` for file formats.

---

## Pattern 10: Assistants API

Persistent AI assistants with tools and knowledge.

```python
# Create assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a helpful math tutor who explains concepts.",
    model="gpt-4",
    tools=[
        {"type": "code_interpreter"}
    ]
)

# Create thread
thread = client.beta.threads.create()

# Add message
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What's the derivative of x^2?"
)

# Run assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Get response
messages = client.beta.threads.messages.list(thread_id=thread.id)
print(messages.data[0].content[0].text)
```

**Use when**: Building long-running agents with persistent state.

**See also**: `references/assistants.md` for file handling and retrieval.

---

## Quick Pattern Finder

| Need | Pattern | Time to implement |
|------|---------|-------------------|
| Simple Q&A | Pattern 1 | 5 min |
| Chatbot | Pattern 2 | 15 min |
| Tool use | Pattern 3 | 30 min |
| Search | Pattern 4 | 20 min |
| Image analysis | Pattern 5 | 10 min |
| Real-time UI | Pattern 6 | 15 min |
| Production app | Pattern 7 | 30 min |
| Data extraction | Pattern 8 | 20 min |
| Bulk processing | Pattern 9 | 45 min |
| Agents | Pattern 10 | 60 min |

## Next Steps

1. **Choose a pattern** matching your use case
2. **Copy the code** and adjust for your needs
3. **Check references/** for detailed documentation
4. **Test locally** before deploying

## Integration Tips

- Always use environment variables for API keys
- Set a timeout to avoid hanging requests
- Monitor token usage and costs
- Start with GPT-3.5 Turbo for cost optimization
- Move to GPT-4 only when needed

---

## Advanced Patterns from OpenAI Cookbook

### Pattern 11: RAG (Retrieval-Augmented Generation)

Combine embeddings search with chat completions for context-aware answers.

```python
# 1. Create embeddings for your knowledge base
docs = ["Doc 1 content...", "Doc 2 content...", "Doc 3 content..."]
doc_embeddings = [
    client.embeddings.create(input=doc, model="text-embedding-3-small").data[0].embedding
    for doc in docs
]

# 2. Find relevant docs for a query
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

query = "What is machine learning?"
query_embedding = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
).data[0].embedding

# Find top 3 most relevant docs
similarities = [cosine_similarity(query_embedding, emb) for emb in doc_embeddings]
top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:3]
context = "\n\n".join([docs[i] for i in top_indices])

# 3. Use context in chat completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Answer based on the context provided."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
)
print(response.choices[0].message.content)
```

**Use when**: Building Q&A systems over your own documents.

**See also**: Cookbook examples for vector databases (Pinecone, Weaviate, Qdrant, Redis).

---

### Pattern 12: Retry with Exponential Backoff

Handle rate limits gracefully using tenacity.

```python
from tenacity import retry, wait_random_exponential, stop_after_attempt

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_embedding_with_retry(text):
    return client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    ).data[0].embedding

# Automatically retries with exponential backoff
embedding = get_embedding_with_retry("Some text")
```

**Use when**: Processing large batches or hitting rate limits.

**See also**: `references/embeddings.md` for batch processing.

---

### Pattern 13: Token Counting

Estimate costs before making requests.

```python
import tiktoken

def count_tokens(text, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

text = "Hello, how are you?"
tokens = count_tokens(text)
print(f"Tokens: {tokens}")

# Estimate cost
input_cost_per_1k = 0.03  # GPT-4
output_cost_per_1k = 0.06
estimated_cost = (tokens / 1000) * input_cost_per_1k
print(f"Estimated input cost: ${estimated_cost:.4f}")
```

**Use when**: Budgeting or optimizing prompts.

**See also**: tiktoken documentation for encoding details.

---

### Pattern 14: Chunking Long Documents

Split text that exceeds token limits.

```python
import tiktoken

def chunk_text(text, max_tokens=8000, encoding_name="cl100k_base"):
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)
    
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunks.append(encoding.decode(chunk_tokens))
    
    return chunks

# Split long document
long_text = "..." * 10000
chunks = chunk_text(long_text)

# Process each chunk
for chunk in chunks:
    embedding = client.embeddings.create(
        input=chunk,
        model="text-embedding-3-small"
    ).data[0].embedding
```

**Use when**: Processing documents larger than model context windows.

**See also**: Cookbook's "Embedding Long Inputs" notebook.

---

### Pattern 15: Hybrid Search (Vector + Keyword)

Combine semantic search with traditional keyword matching.

```python
# Pseudo-code for hybrid approach
def hybrid_search(query, docs, alpha=0.5):
    # 1. Vector search
    query_emb = get_embedding(query)
    vector_scores = [cosine_similarity(query_emb, doc.embedding) for doc in docs]
    
    # 2. Keyword search (BM25 or simple TF-IDF)
    keyword_scores = bm25_search(query, docs)
    
    # 3. Combine scores
    combined_scores = [
        alpha * v + (1 - alpha) * k
        for v, k in zip(vector_scores, keyword_scores)
    ]
    
    # 4. Return top results
    top_indices = sorted(range(len(combined_scores)), 
                        key=lambda i: combined_scores[i], 
                        reverse=True)[:10]
    return [docs[i] for i in top_indices]
```

**Use when**: Vector search alone isn't precise enough (e.g., exact product names).

**See also**: Azure AI Search, Elasticsearch cookbook examples.

---

## New Features (Oct 2024)

### Pattern 16: Reasoning Models with Controlled Verbosity

Use advanced reasoning models with verbosity and effort controls.

```python
# New reasoning models: o3, o4-mini, gpt-5
response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": "Solve this complex logic puzzle: ..."}
    ],
    verbosity="low",  # Options: low, medium, high
    reasoning_effort="medium",  # Control thinking depth
    temperature=1.0
    # Note: 'stop' parameter NOT supported on o3, o4-mini
)

print(response.choices[0].message.content)
```

**Key Parameters:**
- `verbosity` - Controls response length (low/medium/high)
- `reasoning_effort` - How much the model "thinks" before responding
- `safety_identifier` - Replaces deprecated `user` parameter

**Use when**: Complex reasoning, math problems, multi-step logic.

**See also**: Reasoning guide for unsupported parameters.

---

### Pattern 17: Service Tier Selection

Control processing priority and cost with service tiers.

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Urgent query"}],
    service_tier="priority"  # Options: auto, default, flex, priority
)

# Check which tier was used
print(f"Served with: {response.service_tier}")
```

**Tiers:**
- `auto` - Uses project default setting
- `default` - Standard pricing/performance
- `flex` - Dynamic pricing (may be cheaper)
- `priority` - Guaranteed fast processing

**Use when**: Production systems with SLA requirements.

---

### Pattern 18: Enhanced Safety & Caching

Use new safety identifiers and caching optimization.

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Question from user"}],
    safety_identifier="hashed_user_email_abc123",  # For abuse detection
    prompt_cache_key="user_context_bucket_1",      # Optimize caching
    store=True  # Store for model improvement (default: false)
)
```

**Benefits:**
- Better abuse detection with `safety_identifier`
- Improved cache hit rates with `prompt_cache_key`
- Opt-in to model improvement with `store`

**Use when**: Multi-user applications requiring safety monitoring.
