# Langchain - Modules

**Pages**: 9

---

## Architecture | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/architecture/

**Contents**:
- Architecture
- langchain-core​
- langchain​
- Integration packages​
- langchain-community​
- langgraph​
- langserve​
- LangSmith​

LangChain is a framework that consists of a number of packages.

This package contains base abstractions for different components and ways to compose them together. The interfaces for core components like chat models, vector stores, tools and more are defined here. No third-party integrations are defined here. The dependencies are kept purposefully very lightweight.

The main langchain package contains chains and retrieval strategies that make up an application's cognitive architecture. These are NOT third-party integrations. All chains, agents, and retrieval strategies here are NOT specific to any one integration, but rather generic across all integrations.

Popular integrations have their own packages (e.g. langchain-openai, langchain-anthropic, etc) so that they can be properly versioned and appropriately lightweight.

For more information see:

This package contains third-party integrations that are maintained by the LangChain community. Key integration packages are separated out (see above). This contains integrations for various components (chat models, vector stores, tools, etc). All dependencies in this package are optional to keep the package as lightweight as possible.

langgraph is an extension of langchain aimed at building robust and stateful multi-actor applications with LLMs by modeling steps as edges and nodes in a graph.

LangGraph exposes high level interfaces for creating common types of agents, as well as a low-level API for composing custom flows.

A package to deploy LangChain chains as REST APIs. Makes it easy to get a production ready API up and running.

LangServe is designed to primarily deploy simple Runnables and work with well-known primitives in langchain-core.

If you need a deployment option for LangGraph, you should instead be looking at LangGraph Platform (beta) which will be better suited for deploying LangGraph applications.

For more information, see the LangServe documentation.

A developer platform that lets you debug, test, ev

*[Content truncated - see full docs]*

---

## Build a simple LLM application with chat models and prompt templates | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/tutorials/llm_chain/

**Contents**:
- Build a simple LLM application with chat models and prompt templates
- Setup​
  - Jupyter Notebook​
  - Installation​
  - LangSmith​
- Using Language Models​
  - Streaming​
- Prompt Templates​

In this quickstart we'll show you how to build a simple LLM application with LangChain. This application will translate text from English into another language. This is a relatively simple LLM application - it's just a single LLM call plus some prompting. Still, this is a great way to get started with LangChain - a lot of features can be built with just some prompting and an LLM call!

After reading this tutorial, you'll have a high level overview of:

Using language models

Using prompt templates

Debugging and tracing your application using LangSmith

This and other tutorials are perhaps most conveniently run in a Jupyter notebooks. Going through guides in an interactive environment is a great way to better understand them. See here for instructions on how to install.

To install LangChain run:

For more details, see our Installation guide.

Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with LangSmith.

After you sign up at the link above, make sure to set your environment variables to start logging traces:

Or, if in a notebook, you can set them with:

First up, let's learn how to use a language model by itself. LangChain supports many different language models that you can use interchangeably. For details on getting started with a specific model, refer to supported integrations.

Let's first use the model directly. ChatModels are instances of LangChain Runnables, which means they expose a standard interface for interacting with them. To simply call the model, we can pass in a list of messages to the .invoke method.

If we've enabled LangSmith, we can see that this run is logged to LangSmith, and can see the LangSmith trace. The LangSmith trace reports token usage information, latency, standard model parameters (such as tempe

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install langchain
```

```bash
conda install langchain -c conda-forge
```

```shell
export LANGSMITH_TRACING="true"export LANGSMITH_API_KEY="..."export LANGSMITH_PROJECT="default" # or any other project name
```

---

## Chat models | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/

**Contents**:
- Chat models
- Featured Providers​
- All chat models​

Chat models are language models that use a sequence of messages as inputs and return messages as outputs (as opposed to using plain text). These are generally newer models.

If you'd like to write your own chat model, see this how-to. If you'd like to contribute an integration, see Contributing integrations.

While all these LangChain classes support the indicated advanced feature, you may have to open the provider-specific documentation to learn which hosted models or backends support the feature.

**Examples**:

```bash
pip install -qU "langchain[google-genai]"
```

```python
import getpassimport osif not os.environ.get("GOOGLE_API_KEY"):  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")from langchain.chat_models import init_chat_modelmodel = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
```

```python
model.invoke("Hello, world!")
```

---

## Chat models | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/chat_models/

**Contents**:
- Chat models
- Overview​
- Features​
- Integrations​
- Interface​
  - Key methods​
  - Inputs and outputs​
  - Standard parameters​

Large Language Models (LLMs) are advanced machine learning models that excel in a wide range of language-related tasks such as text generation, translation, summarization, question answering, and more, without needing task-specific fine tuning for every scenario.

Modern LLMs are typically accessed through a chat model interface that takes a list of messages as input and returns a message as output.

The newest generation of chat models offer additional capabilities:

LangChain provides a consistent interface for working with chat models from different providers while offering additional features for monitoring, debugging, and optimizing the performance of applications that use LLMs.

LangChain has many chat model integrations that allow you to use a wide variety of models from different providers.

These integrations are one of two types:

LangChain chat models are named with a convention that prefixes "Chat" to their class names (e.g., ChatOllama, ChatAnthropic, ChatOpenAI, etc.).

Please review the chat model integrations for a list of supported models.

Models that do not include the prefix "Chat" in their name or include "LLM" as a suffix in their name typically refer to older models that do not follow the chat model interface and instead use an interface that takes a string as input and returns a string as output.

LangChain chat models implement the BaseChatModel interface. Because BaseChatModel also implements the Runnable Interface, chat models support a standard streaming interface, async programming, optimized batching, and more. Please see the Runnable Interface for more details.

Many of the key methods of chat models operate on messages as input and return messages as output.

Chat models offer a standard set of parameters that can be used to configure the model. These parameters are typically used to control the behavior of the model, such as the temperature of the output, the maximum number of tokens in the response, and the maximum time to wait for 

*[Content truncated - see full docs]*

---

## Embedding models | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/embedding_models/

**Contents**:
- Embedding models
- Key concepts​
- Embedding​
  - Historical context​
  - Interface​
  - Integrations​
- Measure similarity​

This conceptual overview focuses on text-based embedding models.

Embedding models can also be multimodal though such models are not currently supported by LangChain.

Imagine being able to capture the essence of any text - a tweet, document, or book - in a single, compact representation. This is the power of embedding models, which lie at the heart of many retrieval systems. Embedding models transform human language into a format that machines can understand and compare with speed and accuracy. These models take text as input and produce a fixed-length array of numbers, a numerical fingerprint of the text's semantic meaning. Embeddings allow search system to find relevant documents not just based on keyword matches, but on semantic understanding.

(1) Embed text as a vector: Embeddings transform text into a numerical vector representation.

(2) Measure similarity: Embedding vectors can be compared using simple mathematical operations.

The landscape of embedding models has evolved significantly over the years. A pivotal moment came in 2018 when Google introduced BERT (Bidirectional Encoder Representations from Transformers). BERT applied transformer models to embed text as a simple vector representation, which lead to unprecedented performance across various NLP tasks. However, BERT wasn't optimized for generating sentence embeddings efficiently. This limitation spurred the creation of SBERT (Sentence-BERT), which adapted the BERT architecture to generate semantically rich sentence embeddings, easily comparable via similarity metrics like cosine similarity, dramatically reduced the computational overhead for tasks like finding similar sentences. Today, the embedding model ecosystem is diverse, with numerous providers offering their own implementations. To navigate this variety, researchers and practitioners often turn to benchmarks like the Massive Text Embedding Benchmark (MTEB) here for objective comparisons.

LangChain provides a universal interface for working 

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_openai import OpenAIEmbeddingsembeddings_model = OpenAIEmbeddings()embeddings = embeddings_model.embed_documents(    [        "Hi there!",        "Oh, hello!",        "What's your name?",        "My friends call me World",        "Hello World!"    ])len(embeddings), len(embeddings[0])(5, 1536)
```

```python
query_embedding = embeddings_model.embed_query("What is the meaning of life?")
```

```python
import numpy as npdef cosine_similarity(vec1, vec2):    dot_product = np.dot(vec1, vec2)    norm_vec1 = np.linalg.norm(vec1)    norm_vec2 = np.linalg.norm(vec2)    return dot_product / (norm_vec1 * norm_vec2)similarity = cosine_similarity(query_result, document_result)print("Cosine Similarity:", similarity)
```

---

## How to pass multimodal data to models | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/how_to/multimodal_inputs/

**Contents**:
- How to pass multimodal data to models
- Images​
  - Images from base64 data​
  - Images from a URL​
- Documents (PDF)​
  - Documents from base64 data​
  - Documents from a URL​
- Audio​

Here we demonstrate how to pass multimodal input directly to models.

LangChain supports multimodal data as input to chat models:

Below, we demonstrate the cross-provider standard. See chat model integrations for detail on native formats for specific providers.

Most chat models that support multimodal image inputs also accept those values in OpenAI's Chat Completions format:

Many providers will accept images passed in-line as base64 data. Some will additionally accept an image from a URL directly.

To pass images in-line, format them as content blocks of the following form:

See LangSmith trace for more detail.

Some providers (including OpenAI, Anthropic, and Google Gemini) will also accept images from URLs directly.

To pass images as URLs, format them as content blocks of the following form:

We can also pass in multiple images:

Some providers (including OpenAI, Anthropic, and Google Gemini) will accept PDF documents.

OpenAI requires file-names be specified for PDF inputs. When using LangChain's format, include the filename key. See example below.

To pass documents in-line, format them as content blocks of the following form:

Some providers (specifically Anthropic) will also accept documents from URLs directly.

To pass documents as URLs, format them as content blocks of the following form:

Some providers (including OpenAI and Google Gemini) will accept audio inputs.

To pass audio in-line, format them as content blocks of the following form:

Some providers will support or require additional fields on content blocks containing multimodal data. For example, Anthropic lets you specify caching of specific content to reduce token consumption.

To use these fields, you can:

We show three examples below.

OpenAI requires that PDF documents be associated with file names:

Some multimodal models support tool calling features as well. To call tools using such models, simply bind tools to them in the usual way, and invoke the model using content blocks of the des

*[Content truncated - see full docs]*

**Examples**:

```python
{    "type": "image_url",    "image_url": {"url": image_url},}
```

```python
{    "type": "image",    "source_type": "base64",    "mime_type": "image/jpeg",  # or image/png, etc.    "data": "<base64 data string>",}
```

```python
import base64import httpxfrom langchain.chat_models import init_chat_model# Fetch image dataimage_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")# Pass to LLMllm = init_chat_model("anthropic:claude-3-5-sonnet-latest")message = {    "role": "user",    "content": [        {            "type": "text",       
...
```

---

## How to use chat models to call tools | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/how_to/tool_calling

**Contents**:
- How to use chat models to call tools
- Defining tool schemas​
  - Python functions​
  - LangChain Tool​
  - Pydantic class​
  - TypedDict class​
- Tool calls​
- Parsing​

This guide assumes familiarity with the following concepts:

Tool calling allows a chat model to respond to a given prompt by "calling a tool".

Remember, while the name "tool calling" implies that the model is directly performing some action, this is actually not the case! The model only generates the arguments to a tool, and actually running the tool (or not) is up to the user.

Tool calling is a general technique that generates structured output from a model, and you can use it even when you don't intend to invoke any tools. An example use-case of that is extraction from unstructured text.

If you want to see how to use the model-generated tool call to actually run a tool check out this guide.

Tool calling is not universal, but is supported by many popular LLM providers. You can find a list of all models that support tool calling here.

LangChain implements standard interfaces for defining tools, passing them to LLMs, and representing tool calls. This guide will cover how to bind tools to an LLM, then invoke the LLM to generate these arguments.

For a model to be able to call tools, we need to pass in tool schemas that describe what the tool does and what its arguments are. Chat models that support tool calling features implement a .bind_tools() method for passing tool schemas to the model. Tool schemas can be passed in as Python functions (with typehints and docstrings), Pydantic models, TypedDict classes, or LangChain Tool objects. Subsequent invocations of the model will pass in these tool schemas along with the prompt.

Our tool schemas can be Python functions:

LangChain also implements a @tool decorator that allows for further control of the tool schema, such as tool names and argument descriptions. See the how-to guide here for details.

You can equivalently define the schemas without the accompanying functions using Pydantic.

Note that all fields are required unless provided a default value.

Or using TypedDicts and annotations:

To actually bind those 

*[Content truncated - see full docs]*

**Examples**:

```python
# The function name, type hints, and docstring are all part of the tool# schema that's passed to the model. Defining good, descriptive schemas# is an extension of prompt engineering and is an important part of# getting models to perform well.def add(a: int, b: int) -> int:    """Add two integers.    Args:        a: First integer        b: Second integer    """    return a + bdef multiply(a: int, b: int) -> int:    """Multiply two integers.    Args:        a: First integer        b: Second intege
...
```

```python
from pydantic import BaseModel, Fieldclass add(BaseModel):    """Add two integers."""    a: int = Field(..., description="First integer")    b: int = Field(..., description="Second integer")class multiply(BaseModel):    """Multiply two integers."""    a: int = Field(..., description="First integer")    b: int = Field(..., description="Second integer")
```

```python
from typing_extensions import Annotated, TypedDictclass add(TypedDict):    """Add two integers."""    # Annotations must have the type and can optionally include a default value and description (in that order).    a: Annotated[int, ..., "First integer"]    b: Annotated[int, ..., "Second integer"]class multiply(TypedDict):    """Multiply two integers."""    a: Annotated[int, ..., "First integer"]    b: Annotated[int, ..., "Second integer"]tools = [add, multiply]
```

---

## IBM | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/ibm/

**Contents**:
- IBM
- Watsonx AI​
  - Installation and Setup​
  - Chat Model​
    - ChatWatsonx​
  - LLMs​
    - WatsonxLLM​
  - Embedding Models​

LangChain integrations related to IBM technologies, including the IBM watsonx.ai platform and DB2 database.

IBM® watsonx.ai™ AI studio is part of the IBM watsonx™ AI and data platform, bringing together new generative AI capabilities powered by foundation models and traditional machine learning (ML) into a powerful studio spanning the AI lifecycle. Tune and guide models with your enterprise data to meet your needs with easy-to-use tools for building and refining performant prompts. With watsonx.ai, you can build AI applications in a fraction of the time and with a fraction of the data. Watsonx.ai offers:

Install the integration package with

Get an IBM watsonx.ai api key and set it as an environment variable (WATSONX_APIKEY)

The IBM DB2 relational database v12.1.2 and above offers the abilities of vector store and vector search. Installation of langchain-db2 package will give Langchain users the support of DB2 vector store and vector search.

See detailed usage examples in the guide here.

Installation: This is a separate package for vector store feature only and can be run without the langchain-ibm package.

**Examples**:

```bash
pip install -qU langchain-ibm
```

```python
import osos.environ["WATSONX_APIKEY"] = "your IBM watsonx.ai api key"
```

```python
from langchain_ibm import ChatWatsonx
```

---

## ModelScope | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/modelscope/

**Contents**:
- ModelScope
- Installation​
- Chat Models​
- Embeddings​
- LLMs​

ModelScope is a big repository of the models and datasets.

This page covers how to use the modelscope ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific modelscope wrappers.

Head to ModelScope to sign up to ModelScope and generate an SDK token. Once you've done this set the MODELSCOPE_SDK_TOKEN environment variable:

ModelScopeChatEndpoint class exposes chat models from ModelScope. See available models here.

ModelScopeEmbeddings class exposes embeddings from ModelScope.

ModelScopeEndpoint class exposes LLMs from ModelScope.

**Examples**:

```bash
pip install -U langchain-modelscope-integration
```

```bash
export MODELSCOPE_SDK_TOKEN=<your_sdk_token>
```

```python
from langchain_modelscope import ModelScopeChatEndpointllm = ModelScopeChatEndpoint(model="Qwen/Qwen2.5-Coder-32B-Instruct")llm.invoke("Sing a ballad of LangChain.")
```

---
