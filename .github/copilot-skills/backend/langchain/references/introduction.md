# Langchain - Introduction

**Pages**: 1

---

## Introduction | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/introduction/

**Contents**:
- Introduction
- Architecture​
- Guides​
  - Tutorials​
  - How-to guides​
  - Conceptual guide​
  - Integrations​
  - API reference​

LangChain is a framework for developing applications powered by large language models (LLMs).

LangChain simplifies every stage of the LLM application lifecycle:

LangChain implements a standard interface for large language models and related technologies, such as embedding models and vector stores, and integrates with hundreds of providers. See the integrations page for more.

These docs focus on the Python LangChain library. Head here for docs on the JavaScript LangChain library.

The LangChain framework consists of multiple open-source libraries. Read more in the Architecture page.

If you're looking to build something specific or are more of a hands-on learner, check out our tutorials section. This is the best place to get started.

These are the best ones to get started with:

Explore the full list of LangChain tutorials here, and check out other LangGraph tutorials here. To learn more about LangGraph, check out our first LangChain Academy course, Introduction to LangGraph, available here.

Here you’ll find short answers to “How do I….?” types of questions. These how-to guides don’t cover topics in depth – you’ll find that material in the Tutorials and the API Reference. However, these guides will help you quickly accomplish common tasks using chat models, vector stores, and other common LangChain components.

Check out LangGraph-specific how-tos here.

Introductions to all the key parts of LangChain you’ll need to know! Here you'll find high level explanations of all LangChain concepts.

For a deeper dive into LangGraph concepts, check out this page.

LangChain is part of a rich ecosystem of tools that integrate with our framework and build on top of it. If you're looking to get up and running quickly with chat models, vector stores, or other LangChain components from a specific provider, check out our growing list of integrations.

Head to the reference section for full documentation of all classes and methods in the LangChain Python packages.

Trace and eval

*[Content truncated - see full docs]*

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
