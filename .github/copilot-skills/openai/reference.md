# OpenAI - Reference Documentation

Comprehensive OpenAI API documentation organized by topic and use case.

## Overview

This reference guide covers all major OpenAI APIs and features:

### Core APIs
- **Chat Completions** - Conversational AI with GPT models
- **Assistants** - Persistent, stateful AI agents
- **Embeddings** - Text-to-vector conversion for search
- **Images** - DALL-E image generation and editing
- **Audio** - Whisper transcription and Text-to-Speech
- **Vision** - Image understanding with GPT-4V
- **Batch Processing** - Asynchronous bulk requests
- **Files** - Document upload and management

### Advanced Features
- **Function Calling** - Let models invoke tools
- **Structured Output** - Guaranteed JSON responses
- **Fine-tuning** - Customize models with your data
- **Vision Analysis** - Analyze images and documents

## Quick Navigation

### I Want To...

**Build a chatbot**
→ Start with Pattern 2 in `patterns.md`
→ See `chat-completions.md` for system prompts
→ Check `assistants.md` for persistent state

**Extract data from text/images**
→ Pattern 8 (structured output) or Pattern 5 (vision)
→ See `structured-output.md`
→ Reference `vision.md` for image processing

**Search or find similar content**
→ Pattern 4 (embeddings)
→ See `embeddings.md` for similarity search
→ Learn vector storage options

**Process multiple requests efficiently**
→ Pattern 9 (batch processing)
→ See `batch.md` for file formats
→ Understand cost savings

**Create AI agents with tools**
→ Pattern 3 (function calling) or Pattern 10 (assistants)
→ See `function-calling.md` for details
→ Read `assistants.md` for persistent agents

**Analyze images**
→ Pattern 5 (vision)
→ See `vision.md` for all examples
→ Learn about detail levels

**Convert speech to text or vice versa**
→ See `audio.md`
→ Whisper for transcription
→ TTS for speech synthesis

**Fine-tune a model**
→ See `fine-tuning.md`
→ Prepare training data
→ Monitor fine-tuning jobs

## Reference Files

### Getting Started
- **README.md** - Quick reference and API overview
- **patterns.md** - 10 common code patterns

### Core Documentation

**`chat-completions.md`**
- Basic and advanced chat API usage
- System prompts and few-shot learning
- Temperature and sampling parameters
- Streaming and multiple completions
- Token counting and cost estimation

**`assistants.md`**
- Creating and managing assistants
- Threads and persistent conversation
- Tools and code interpreter
- File retrieval and knowledge bases
- Running and monitoring assistants

**`embeddings.md`**
- Text-to-vector conversion
- Embedding models and dimensions
- Similarity search techniques
- Batch embedding for efficiency
- Storage and retrieval patterns

**`vision.md`**
- Image understanding with GPT-4V
- URL-based and base64 images
- Detail levels (low/high/auto)
- Multi-image analysis
- Batch image processing

**`function-calling.md`**
- Defining callable functions
- Model tool selection
- Handling tool responses
- Complex workflows
- Integration patterns

**`audio.md`**
- Whisper speech-to-text
- Text-to-speech (TTS)
- Audio file formats
- Language detection
- Streaming options

**`structured-output.md`**
- JSON schema definition
- Pydantic models
- Guaranteed output format
- Complex nested structures
- Error handling

**`batch.md`**
- Batch request format
- File preparation
- Job monitoring
- Result retrieval
- Cost optimization

**`fine-tuning.md`**
- Training data preparation
- Fine-tuning jobs
- Checkpoint management
- Evaluation and testing
- Deployment

**`models.md`**
- Available models and versions
- Model capabilities matrix
- Context window sizes
- Pricing comparison
- Deprecation timeline

## Models Reference (Updated Oct 2024)

| Model | Best For | Context | Speed | Cost | Notes |
|-------|----------|---------|-------|------|-------|
| **gpt-5** | Latest flagship | 128K | Fast | High | Reasoning, structured outputs |
| **o3, o4-mini** | Advanced reasoning | 128K | Medium | High | No `stop` parameter support |
| **gpt-4o** | Multi-modal | 128K | Fast | Medium | Text, vision, audio, tools |
| **gpt-4o-mini** | Cost-effective multi-modal | 128K | Very Fast | Low | Best value |
| **computer-use-preview** | UI automation (Beta) | - | Medium | - | Experimental |
| **gpt-4-turbo** | Complex reasoning | 128K | Medium | High | Production-ready |
| **gpt-4** | Accuracy-critical | 8K | Slow | Very High | Legacy |
| **gpt-3.5-turbo** | General use | 16K | Fast | Low | Budget option |
| **text-embedding-3-large** | Semantic search | - | Fast | Medium | 3072 dims |
| **text-embedding-3-small** | Simple embeddings | - | Fast | Low | 1536 dims |
| **dall-e-3** | Image generation | - | Slow | Medium | HD quality |
| **whisper-1** | Speech-to-text | - | Fast | Low | Multi-language |
| **tts-1** | Speech synthesis | - | Fast | Low | Natural voices |

**New Features:**
- **Reasoning models** (o3, o4-mini) for complex logic
- **verbosity** control (low/medium/high) for response length
- **reasoning_effort** parameter for deeper thinking
- **safety_identifier** replaces deprecated `user` parameter
- **service_tier** options: auto, default, flex, priority

See `models.md` for detailed specifications and latest updates.

## API Endpoints

### Chat
- `POST /chat/completions` - Create chat completion
- `GET /chat/completions/{id}` - Get completion status

### Assistants
- `POST /assistants` - Create assistant
- `POST /threads` - Create thread
- `POST /threads/{thread_id}/messages` - Add message
- `POST /threads/{thread_id}/runs` - Run assistant
- `GET /threads/{thread_id}/runs/{run_id}` - Get run status
- `POST /threads/{thread_id}/runs/{run_id}/submit_tool_outputs` - Submit tool outputs

### Embeddings
- `POST /embeddings` - Create embeddings

### Images
- `POST /images/generations` - Generate images
- `POST /images/edits` - Edit images
- `POST /images/variations` - Create variations

### Audio
- `POST /audio/transcriptions` - Transcribe audio
- `POST /audio/translations` - Translate audio
- `POST /audio/speech` - Text-to-speech

### Files
- `POST /files` - Upload file
- `GET /files/{file_id}` - Get file info
- `GET /files/{file_id}/content` - Download file
- `DELETE /files/{file_id}` - Delete file

### Batch
- `POST /batches` - Create batch job
- `GET /batches/{batch_id}` - Get batch status
- `GET /batches/{batch_id}/results` - Get results

## Common Tasks

### Task: Make your first API call

```python
from openai import OpenAI
client = OpenAI(api_key="sk-...")
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

See `chat-completions.md` for more examples.

### Task: Extract structured data

Use Pattern 8 from `patterns.md` or see `structured-output.md` for complete guide.

### Task: Build a search feature

See Pattern 4 in `patterns.md` or read `embeddings.md` for detailed implementation.

### Task: Analyze an image

Use Pattern 5 from `patterns.md` or see `vision.md` for all image features.

### Task: Process bulk requests

See Pattern 9 in `patterns.md` or read `batch.md` for optimization.

## Best Practices

✅ **Always**
- Store API keys in environment variables
- Implement error handling and retries with exponential backoff
- Monitor token usage and costs with tiktoken
- Test with gpt-3.5-turbo first (cheaper)
- Use streaming for better UX
- Add timeouts to API calls
- Validate input before sending to API
- Use batch API for processing 100+ requests
- Replace newlines in embeddings input (can hurt performance)
- Cache embeddings when possible
- Use vector databases for production RAG systems

❌ **Never**
- Commit API keys to version control
- Use production keys in development
- Ignore rate limit errors without retry logic
- Make unbounded requests in loops
- Skip input validation
- Deploy without testing
- Process large embedding batches without rate limiting
- Forget to handle async operations in streaming

## Production Patterns from OpenAI Cookbook

### RAG Architecture

For production RAG systems:

1. **Pre-process documents**
   - Chunk intelligently (respect sentence/paragraph boundaries)
   - Generate embeddings with `text-embedding-3-small` or `-large`
   - Store in vector database (Pinecone, Weaviate, Qdrant, etc.)

2. **Query flow**
   ```python
   query_embedding = get_embedding(query)
   → vector_db.search(query_embedding, top_k=5)
   → compile_context(results)
   → chat_completion(context + query)
   ```

3. **Optimization**
   - Rerank results for better precision
   - Use hybrid search (vector + keyword)
   - Implement query rewriting
   - Cache frequent queries

### Error Handling Pattern

```python
from tenacity import retry, wait_random_exponential, stop_after_attempt
from openai import RateLimitError, APIError, Timeout

@retry(
    wait=wait_random_exponential(min=1, max=60),
    stop=stop_after_attempt(6),
    reraise=True
)
def call_openai_with_retry(func):
    try:
        return func()
    except RateLimitError:
        raise  # Retry
    except Timeout:
        raise  # Retry
    except APIError as e:
        if e.status_code >= 500:
            raise  # Retry server errors
        raise  # Don't retry client errors
```

### Batch Processing Pattern

For processing many requests efficiently:

```python
import concurrent.futures
from tqdm import tqdm

def process_batch(texts, max_workers=10):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(get_embedding_with_retry, text) for text in texts]
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(texts)):
            results.append(future.result())
    return results

# Process 1000 texts with concurrency
embeddings = process_batch(texts, max_workers=10)
```

### Token Management

```python
import tiktoken

def truncate_to_token_limit(text, max_tokens=8000, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    
    if len(tokens) <= max_tokens:
        return text
    
    # Truncate and add notice
    truncated_tokens = tokens[:max_tokens-50]  # Leave room for notice
    truncated_text = encoding.decode(truncated_tokens)
    return truncated_text + "\n\n[Content truncated due to length]"
```

### Vision + RAG Pattern

Combine image analysis with document retrieval:

```python
# 1. Extract text from images using GPT-4V
image_response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Extract all text from this image"},
            {"type": "image_url", "image_url": {"url": image_url}}
        ]
    }]
)

extracted_text = image_response.choices[0].message.content

# 2. Use extracted text for RAG
embedding = get_embedding(extracted_text)
relevant_docs = vector_db.search(embedding, top_k=3)
context = compile_context(relevant_docs)

# 3. Answer questions with context
answer = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": f"Context:\n{context}"},
        {"role": "user", "content": "What does the image show?"}
    ]
)
```

## Troubleshooting

**"Invalid API key"**
- Check OPENAI_API_KEY env var
- Verify key at https://platform.openai.com/account/api-keys
- Ensure key has appropriate permissions

**"Rate limit exceeded"**
- Implement exponential backoff retry
- Use batch API for bulk processing
- Check rate limits: https://platform.openai.com/account/rate-limits

**"Context length exceeded"**
- Reduce message history or summarize
- Use higher context model (gpt-4-turbo has 128K)
- Split into multiple requests

**"Timeout"**
- Increase timeout duration
- Use batch API for long-running tasks
- Check network connectivity

See individual reference files for more troubleshooting.

## Learning Path

1. **Start here**: Read this file and `README.md`
2. **Learn basics**: Review Pattern 1-2 in `patterns.md`
3. **Try it**: Run Pattern 1 code with your API key
4. **Go deeper**: Read `chat-completions.md` for advanced features
5. **Build more**: Try other patterns based on your needs
6. **Reference**: Use this guide when stuck

## Resources

- **Official API Docs**: https://platform.openai.com/docs/api-reference
- **Python SDK**: https://github.com/openai/openai-python
- **Node.js SDK**: https://github.com/openai/openai-node
- **Cookbook**: https://cookbook.openai.com/
- **Community**: https://community.openai.com/
- **Status**: https://status.openai.com/

## Document Map

```
.github/copilot-skills/openai/
├── README.md              ← Start here
├── patterns.md            ← 10 common patterns
├── reference.md           ← This file
└── [individual guides]    ← Detailed documentation
    ├── chat-completions.md
    ├── assistants.md
    ├── embeddings.md
    ├── vision.md
    ├── function-calling.md
    ├── audio.md
    ├── structured-output.md
    ├── batch.md
    ├── fine-tuning.md
    └── models.md
```

## Updates & Versions

Last updated: October 2024
Models included: GPT-4 Turbo, GPT-3.5 Turbo, Embeddings 3, DALL-E 3, Whisper, TTS-1

For latest updates, see https://openai.com/blog
