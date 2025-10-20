# Langchain - Agents

**Pages**: 7

---

## Agents | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/agents/

**Contents**:
- Agents
- Legacy agent concept: AgentExecutor​
  - Transitioning from AgentExecutor to LangGraph​

By themselves, language models can't take actions - they just output text. Agents are systems that take a high-level task and use an LLM as a reasoning engine to decide what actions to take and execute those actions.

LangGraph is an extension of LangChain specifically aimed at creating highly controllable and customizable agents. We recommend that you use LangGraph for building agents.

Please see the following resources for more information:

LangChain previously introduced the AgentExecutor as a runtime for agents. While it served as an excellent starting point, its limitations became apparent when dealing with more sophisticated and customized agents. As a result, we're gradually phasing out AgentExecutor in favor of more flexible solutions in LangGraph.

If you're currently using AgentExecutor, don't worry! We've prepared resources to help you:

For those who still need to use AgentExecutor, we offer a comprehensive guide on how to use AgentExecutor.

However, we strongly recommend transitioning to LangGraph for improved flexibility and control. To facilitate this transition, we've created a detailed migration guide to help you move from AgentExecutor to LangGraph seamlessly.

---

## Build an Agent | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/tutorials/agents/

**Contents**:
- Build an Agent
- End-to-end agent​
- Setup​
  - Jupyter Notebook​
  - Installation​
  - LangSmith​
  - Tavily​
- Define tools​

LangChain supports the creation of agents, or systems that use LLMs as reasoning engines to determine which actions to take and the inputs necessary to perform the action. After executing actions, the results can be fed back into the LLM to determine whether more actions are needed, or whether it is okay to finish. This is often achieved via tool-calling.

In this tutorial we will build an agent that can interact with a search engine. You will be able to ask this agent questions, watch it call the search tool, and have conversations with it.

The code snippet below represents a fully functional agent that uses an LLM to decide which tools to use. It is equipped with a generic search tool. It has conversational memory - meaning that it can be used as a multi-turn chatbot.

In the rest of the guide, we will walk through the individual components and what each part does - but if you want to just grab some code and get started, feel free to use this!

This guide (and most of the other guides in the documentation) uses Jupyter notebooks and assumes the reader is as well. Jupyter notebooks are perfect interactive environments for learning how to work with LLM systems because oftentimes things can go wrong (unexpected output, API down, etc), and observing these cases is a great way to better understand building with LLMs.

This and other tutorials are perhaps most conveniently run in a Jupyter notebook. See here for instructions on how to install.

To install LangChain run:

For more details, see our Installation guide.

Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with LangSmith.

After you sign up at the link above, make sure to set your environment variables to start logging traces:

Or, if in a notebook, you can set them with:

We

*[Content truncated - see full docs]*

**Examples**:

```python
# Import relevant functionalityfrom langchain.chat_models import init_chat_modelfrom langchain_tavily import TavilySearchfrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.prebuilt import create_react_agent# Create the agentmemory = MemorySaver()model = init_chat_model("anthropic:claude-3-5-sonnet-latest")search = TavilySearch(max_results=2)tools = [search]agent_executor = create_react_agent(model, tools, checkpointer=memory)
```

```python
# Use the agentconfig = {"configurable": {"thread_id": "abc123"}}input_message = {    "role": "user",    "content": "Hi, I'm Bob and I live in SF.",}for step in agent_executor.stream(    {"messages": [input_message]}, config, stream_mode="values"):    step["messages"][-1].pretty_print()
```

```output
================================[1m Human Message [0m=================================Hi, I'm Bob and I live in SF.==================================[1m Ai Message [0m==================================Hello Bob! I notice you've introduced yourself and mentioned you live in SF (San Francisco), but you haven't asked a specific question or made a request that requires the use of any tools. Is there something specific you'd like to know about San Francisco or any other topic? I'd be happy to hel
...
```

---

## GOAT | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/goat/

**Contents**:
- GOAT
  - How it works​
- Installation and Setup​

GOAT is the finance toolkit for AI agents.

Create agents that can:

GOAT leverages blockchains, cryptocurrencies (such as stablecoins), and wallets as the infrastructure to enable agents to become economic actors:

See everything GOAT supports here.

Lightweight and extendable Different from other toolkits, GOAT is designed to be lightweight and extendable by keeping its core minimal and allowing you to install only the tools you need.

If you don't find what you need on our more than 200 integrations you can easily:

See how to do it here.

Check out our quickstart to see how to set up and install GOAT.

---

## ScraperAPI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/scraperapi/

**Contents**:
- ScraperAPI
- Installation and Setup​
  - Tools​

ScraperAPI enables data collection from any public website with its web scraping API, without worrying about proxies, browsers, or CAPTCHA handling. langchain-scraperapi wraps this service, making it easy for AI agents to browse the web and scrape data from it.

The package offers 3 tools to scrape any website, get structured Google search results, and get structured Amazon search results respectively.

For a more detailed walkthrough of how to use these tools, visit the official repository.

**Examples**:

```python
%pip install langchain_scraperapifrom langchain_scraperapi.tools import (    ScraperAPIAmazonSearchTool,    ScraperAPIGoogleSearchTool,    ScraperAPITool,)
```

```python
tool = ScraperAPITool()result = tool.invoke({"url": "https://example.com", "output_format": "markdown"})print(result)
```

---

## Tavily | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/tavily/

**Contents**:
- Tavily
- Installation and Setup​
- Tools​

Tavily is a search engine, specifically designed for AI agents. Tavily provides both a search and extract API, AI developers can effortlessly integrate their applications with realtime online information. Tavily’s primary mission is to provide factual and reliable information from trusted sources, enhancing the accuracy and reliability of AI generated content and reasoning.

See detail on available tools tavily_search and tavily_extract.

**Examples**:

```bash
pip install langchain-tavily
```

---

## Tensorlake | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/tensorlake/

**Contents**:
- Tensorlake
- Tensorlake feature overview​
- Installation​
- Examples​
- Quick Start​
  - 1. Set up your environment​
  - 2. Import necessary packages​
  - 3. Build a Signature Detection Agent​

Tensorlake is the AI Data Cloud that reliably transforms data from unstructured sources into ingestion-ready formats for AI Applications.

The langchain-tensorlake package provides seamless integration between Tensorlake and LangChain, enabling you to build sophisticated document processing agents with enhanced parsing features, like signature detection.

Tensorlake gives you tools to:

Learn more at docs.tensorlake.ai

Follow a full tutorial on how to detect signatures in unstructured documents using the langchain-tensorlake tool.

Or check out this colab notebook for a quick start.

You should configure credentials for Tensorlake and OpenAI by setting the following environment variables:

Get your Tensorlake API key from the Tensorlake Cloud Console. New users get 100 free credits.

Note: We highly recommend using openai as the agent model to ensure the agent sets the right parsing parameters

Reach out to us on Slack or on the package repository on GitHub directly.

**Examples**:

```bash
pip install -U langchain-tensorlake
```

```text
export TENSORLAKE_API_KEY="your-tensorlake-api-key"export OPENAI_API_KEY = "your-openai-api-key"
```

```python
from langchain_tensorlake import document_markdown_toolfrom langgraph.prebuilt import create_react_agentimport asyncioimport os
```

---

## Tools | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/tools/

**Contents**:
- Tools
- Overview​
- Key concepts​
- Tool interface​
- Create tools using the @tool decorator​
- Use the tool directly​
  - Inspect​
- Configuring the schema​

The tool abstraction in LangChain associates a Python function with a schema that defines the function's name, description and expected arguments.

Tools can be passed to chat models that support tool calling allowing the model to request the execution of a specific function with specific inputs.

The tool interface is defined in the BaseTool class which is a subclass of the Runnable Interface.

The key attributes that correspond to the tool's schema:

The key methods to execute the function associated with the tool:

The recommended way to create tools is using the @tool decorator. This decorator is designed to simplify the process of tool creation and should be used in most cases. After defining a function, you can decorate it with @tool to create a tool that implements the Tool Interface.

For more details on how to create tools, see the how to create custom tools guide.

LangChain has a few other ways to create tools; e.g., by sub-classing the BaseTool class or by using StructuredTool. These methods are shown in the how to create custom tools guide, but we generally recommend using the @tool decorator for most cases.

Once you have defined a tool, you can use it directly by calling the function. For example, to use the multiply tool defined above:

You can also inspect the tool's schema and other properties:

If you're using pre-built LangChain or LangGraph components like create_react_agent,you might not need to interact with tools directly. However, understanding how to use them can be valuable for debugging and testing. Additionally, when building custom LangGraph workflows, you may find it necessary to work with tools directly.

The @tool decorator offers additional options to configure the schema of the tool (e.g., modify name, description or parse the function's doc-string to infer the schema).

Please see the API reference for @tool for more details and review the how to create custom tools guide for examples.

Tools are utilities that can be called by a 

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.tools import tool@tooldef multiply(a: int, b: int) -> int:   """Multiply two numbers."""   return a * b
```

```python
multiply.invoke({"a": 2, "b": 3})
```

```python
print(multiply.name) # multiplyprint(multiply.description) # Multiply two numbers.print(multiply.args)# {# 'type': 'object',# 'properties': {'a': {'type': 'integer'}, 'b': {'type': 'integer'}},# 'required': ['a', 'b']# }
```

---
