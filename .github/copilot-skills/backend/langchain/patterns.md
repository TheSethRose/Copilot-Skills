# Langchain - Common Patterns

Quick reference for common langchain patterns and usage.

## Code Patterns

### 1. IntroductionOn this pageIntroduction LangChain is a framework for developing applications powered by

```
pip install -qU "langchain[google-genai]"
```

### 2. IntroductionOn this pageIntroduction LangChain is a framework for developing applications powered by

```
pip install -qU "langchain[google-genai]"
```

### 3. IntroductionOn this pageIntroduction LangChain is a framework for developing applications powered by

```
pip install -qU "langchain[google-genai]"
```

### 4. IntroductionOn this pageIntroduction LangChain is a framework for developing applications powered by

```
pip install -qU "langchain[google-genai]"
```

### 5. Introduction LangChain is a framework for developing applications powered by large language models (

```
pip install -qU "langchain[google-genai]"
```

### 6. TutorialsBuild a simple LLM application with chat models and prompt templatesOn this pageBuild a sim

```
pip install langchain
```

### 7. TutorialsBuild a simple LLM application with chat models and prompt templatesOn this pageBuild a sim

```
pip install langchain
```

### 8. TutorialsBuild a simple LLM application with chat models and prompt templatesOn this pageBuild a sim

```
pip install langchain
```

## Examples

### Example 1

```bash
pip install -qU "langchain[google-genai]"
```

### Example 2

```python
import getpassimport osif not os.environ.get("GOOGLE_API_KEY"):  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")from langchain.chat_models import init_chat_modelmodel = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
```

### Example 3

```bash
pip install langchain
```

### Example 4

```bash
conda install langchain -c conda-forge
```

### Example 5

```bash
pip install -qU "langchain[google-genai]"
```

### Example 6

```python
import getpassimport osif not os.environ.get("GOOGLE_API_KEY"):  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")from langchain.chat_models import init_chat_modelmodel = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
```

### Example 7

```python
from langchain_openai import OpenAIEmbeddingsembeddings_model = OpenAIEmbeddings()embeddings = embeddings_model.embed_documents(    [        "Hi there!",        "Oh, hello!",        "What's your name?",        "My friends call me World",        "Hello World!"    ])len(embeddings), len(embeddings[0])(5, 1536)
```

### Example 8

```python
query_embedding = embeddings_model.embed_query("What is the meaning of life?")
```

### Example 9

```python
{    "type": "image_url",    "image_url": {"url": image_url},}
```

### Example 10

```python
{    "type": "image",    "source_type": "base64",    "mime_type": "image/jpeg",  # or image/png, etc.    "data": "<base64 data string>",}
```


## Categories

See organized documentation in `references/`:

- `references/agents.md` - Agents
- `references/guides.md` - Guides
- `references/introduction.md` - Introduction
- `references/modules.md` - Modules
- `references/other.md` - Other
