# Langchain - Guides

**Pages**: 3

---

## Conceptual guide | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/

**Contents**:
- Conceptual guide
- High level​
- Concepts​
- Glossary​

This guide provides explanations of the key concepts behind the LangChain framework and AI applications more broadly.

We recommend that you go through at least one of the Tutorials before diving into the conceptual guide. This will provide practical context that will make it easier to understand the concepts discussed here.

The conceptual guide does not cover step-by-step instructions or specific implementation examples — those are found in the How-to guides and Tutorials. For detailed reference material, please see the API reference.

---

## How-to guides | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/how_to/

**Contents**:
- How-to guides
- Installation​
- Key features​
- Components​
  - Chat models​
  - Messages​
  - Prompt templates​
  - Example selectors​

Here you’ll find answers to "How do I….?" types of questions. These guides are goal-oriented and concrete; they're meant to help you complete a specific task. For conceptual explanations see the Conceptual guide. For end-to-end walkthroughs see Tutorials. For comprehensive descriptions of every class and function see the API Reference.

This highlights functionality that is core to using LangChain.

These are the core building blocks you can use when building applications.

Chat Models are newer forms of language models that take messages in and output a message. See supported integrations for details on getting started with chat models from a specific provider.

Messages are the input and output of chat models. They have some content and a role, which describes the source of the message.

Prompt Templates are responsible for formatting user input into a format that can be passed to a language model.

Example Selectors are responsible for selecting the correct few-shot examples to pass to the prompt.

What LangChain calls LLMs are older forms of language models that take a string in and output a string.

Output Parsers are responsible for taking the output of an LLM and parsing into more structured format.

Document Loaders are responsible for loading documents from a variety of sources.

Text Splitters take a document and split into chunks that can be used for retrieval.

Embedding Models take a piece of text and create a numerical representation of it. See supported integrations for details on getting started with embedding models from a specific provider.

Vector stores are databases that can efficiently store and retrieve embeddings. See supported integrations for details on getting started with vector stores from a specific provider.

Retrievers are responsible for taking a query and returning relevant documents.

Indexing is the process of keeping your vectorstore in-sync with the underlying data source.

LangChain Tools contain a description of the tool (to p

*[Content truncated - see full docs]*

---

## Tutorials | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/tutorials/

**Contents**:
- Tutorials
- Get started​
- Orchestration​
- LangSmith​
  - Evaluation​

New to LangChain or LLM app development in general? Read this material to quickly get up and running building your first applications.

Familiarize yourself with LangChain's open-source components by building simple applications.

If you're looking to get started with chat models, vector stores, or other LangChain components from a specific provider, check out our supported integrations.

Refer to the how-to guides for more detail on using all LangChain components.

Get started using LangGraph to assemble LangChain components into full-featured applications.

LangSmith allows you to closely trace, monitor and evaluate your LLM application. It seamlessly integrates with LangChain, and you can use it to inspect and debug individual steps of your chains as you build.

LangSmith documentation is hosted on a separate site. You can peruse LangSmith tutorials here.

LangSmith helps you evaluate the performance of your LLM applications. The tutorial below is a great way to get started:

---
