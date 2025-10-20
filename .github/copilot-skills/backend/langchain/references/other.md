# Langchain - Other

**Pages**: 180

---

## ADS4GPTs | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/ads4gpts/

**Contents**:
- ADS4GPTs
- Installation and Setup​
  - Using pip​
  - From Source​
- Prerequisites​
- Environment Variables​
- Tools​
  - Ads4gptsInlineSponsoredResponseTool​

ADS4GPTs is building the open monetization backbone of the AI-Native internet. It helps AI applications monetize through advertising with a UX and Privacy first approach.

You can install the package directly from PyPI:

Alternatively, install from source:

Set the following environment variables for API authentication:

Alternatively, API keys can be passed directly when initializing classes or stored in a .env file.

ADS4GPTs provides two main tools for monetization:

This tool fetches native, sponsored responses that can be seamlessly integrated within your AI application's outputs.

Generates sponsored prompt suggestions to enhance user engagement and provide monetization opportunities.

Delivers conversational sponsored content that naturally fits within chat interfaces and dialogs.

Provides inline banner advertisements that can be displayed within your AI application's response.

Generates banner advertisement suggestions that can be presented to users as recommended content.

The Ads4gptsToolkit combines these tools for convenient access in LangChain applications.

**Examples**:

```bash
pip install ads4gpts-langchain
```

```bash
git clone https://github.com/ADS4GPTs/ads4gpts.gitcd ads4gpts/libs/python-sdk/ads4gpts-langchainpip install .
```

```bash
export ADS4GPTS_API_KEY='your-ads4gpts-api-key'
```

---

## AI21 Labs | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/ai21/

**Contents**:
- AI21 Labs
- Installation and Setup​
- Chat models​
  - AI21 Chat​
- Deprecated features​
  - AI21 LLM​
  - AI21 Contextual Answer​
- Text splitters​

AI21 Labs is a company specializing in Natural Language Processing (NLP), which develops AI systems that can understand and generate natural language.

This page covers how to use the AI21 ecosystem within LangChain.

**Examples**:

```bash
pip install langchain-ai21
```

```python
from langchain_ai21 import ChatAI21
```

```python
from langchain_ai21 import AI21LLM
```

---

## AI/ML API LLM | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/aimlapi/

**Contents**:
- AI/ML API LLM
- Installation​
- Environment​
- Example: Chat Model​
- Example: Text Completion Model​

AI/ML API provides an API to query 300+ leading AI models (Deepseek, Gemini, ChatGPT, etc.) with enterprise-grade performance.

This example demonstrates how to use LangChain to interact with AI/ML API models.

To use AI/ML API, you'll need an API key which you can generate at: https://aimlapi.com/app/

You can pass it via aimlapi_api_key parameter or set as environment variable AIMLAPI_API_KEY.

**Examples**:

```python
%pip install --upgrade langchain-aimlapi
```

```output
Requirement already satisfied: langchain-aimlapi in c:\users\tuman\appdata\local\programs\python\python312\lib\site-packages (0.1.0)Requirement already satisfied: langchain-core<0.4.0,>=0.3.15 in c:\users\tuman\appdata\local\programs\python\python312\lib\site-packages (from langchain-aimlapi) (0.3.67)Requirement already satisfied: langsmith>=0.3.45 in c:\users\tuman\appdata\local\programs\python\python312\lib\site-packages (from langchain-core<0.4.0,>=0.3.15->langchain-aimlapi) (0.4.4)Requiremen
...
```

```python
import osimport getpassif "AIMLAPI_API_KEY" not in os.environ:    os.environ["AIMLAPI_API_KEY"] = getpass.getpass("Enter your AI/ML API key: ")
```

---

## AWS | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/aws/

**Contents**:
- AWS
- Chat models​
  - Bedrock Chat​
  - Bedrock Converse​
- LLMs​
  - Bedrock​
  - Amazon API Gateway​
  - SageMaker Endpoint​

The LangChain integrations related to Amazon AWS platform.

First-party AWS integrations are available in the langchain_aws package.

And there are also some community integrations available in the langchain_community package with the boto3 optional dependency.

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon via a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top FMs for your use case, privately customize them with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise systems and data sources. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with.

AWS Bedrock maintains a Converse API that provides a unified conversational interface for Bedrock models. This API does not yet support custom models. You can see a list of all models that are supported here.

We recommend the Converse API for users who do not need to use custom models. It can be accessed using ChatBedrockConverse.

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.

API Gateway handles all the tasks involved in a

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install langchain-aws
```

```bash
pip install langchain-community boto3
```

```python
from langchain_aws import ChatBedrock
```

---

## Abso | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/abso/

**Contents**:
- Abso
- Installation and setup​
- Chat Model​

Abso is an open-source LLM proxy that automatically routes requests between fast and slow models based on prompt complexity. It uses various heuristics to chose the proper model. It's very fast and has low latency.

See usage details here

**Examples**:

```bash
pip install langchain-abso
```

---

## AgentQL | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/agentql/

**Contents**:
- AgentQL
- Installation and Setup​
- API Key​
- DocumentLoader​
- Tools and Toolkits​

AgentQL provides web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt. AgentQL can be used across multiple languages and web pages without breaking over time and change.

Install the integration package:

Get an API Key from our Dev Portal and add it to your environment variables:

AgentQL's document loader provides structured data extraction from any web page using an AgentQL query.

See our document loader documentation and usage example.

AgentQL tools provides web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt.

See our tools documentation and usage example.

**Examples**:

```bash
pip install langchain-agentql
```

```text
export AGENTQL_API_KEY="your-api-key-here"
```

```python
from langchain_agentql.document_loaders import AgentQLLoader
```

---

## Alibaba Cloud | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/alibaba_cloud/

**Contents**:
- Alibaba Cloud
- LLMs​
  - Alibaba Cloud PAI EAS​
  - Tongyi Qwen​
- Chat Models​
  - Alibaba Cloud PAI EAS​
  - Tongyi Qwen Chat​
  - Qwen QwQ Chat​

Alibaba Group Holding Limited (Wikipedia), or Alibaba (Chinese: 阿里巴巴), is a Chinese multinational technology company specializing in e-commerce, retail, Internet, and technology.

Alibaba Cloud (Wikipedia), also known as Aliyun (Chinese: 阿里云; pinyin: Ālǐyún; lit. 'Ali Cloud'), is a cloud computing company, a subsidiary of Alibaba Group. Alibaba Cloud provides cloud computing services to online businesses and Alibaba's own e-commerce ecosystem.

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example.

See installation instructions and a usage example.

**Examples**:

```python
from langchain_community.llms.pai_eas_endpoint import PaiEasEndpoint
```

```python
from langchain_community.llms import Tongyi
```

```python
from langchain_community.chat_models import PaiEasChatEndpoint
```

---

## Alibaba Cloud PAI EAS | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/alibaba_cloud_pai_eas

**Contents**:
- Alibaba Cloud PAI EAS
- Setup EAS Service​
- Run Chat Model​
- Related​

Alibaba Cloud PAI (Platform for AI) is a lightweight and cost-efficient machine learning platform that uses cloud-native technologies. It provides you with an end-to-end modelling service. It accelerates model training based on tens of billions of features and hundreds of billions of samples in more than 100 scenarios.

Machine Learning Platform for AI of Alibaba Cloud is a machine learning or deep learning engineering platform intended for enterprises and developers. It provides easy-to-use, cost-effective, high-performance, and easy-to-scale plug-ins that can be applied to various industry scenarios. With over 140 built-in optimization algorithms, Machine Learning Platform for AI provides whole-process AI engineering capabilities including data labelling (PAI-iTAG), model building (PAI-Designer and PAI-DSW), model training (PAI-DLC), compilation optimization, and inference deployment (PAI-EAS).

PAI-EAS supports different types of hardware resources, including CPUs and GPUs, and features high throughput and low latency. It allows you to deploy large-scale complex models with a few clicks and perform elastic scale-ins and scale-outs in real-time. It also provides a comprehensive O&M and monitoring system.

Set up environment variables to init EAS service URL and token. Use this document for more information.

Another option is to use this code:

You can use the default settings to call EAS service as follows:

Or, call EAS service with new inference params:

Or, run a stream call to get a stream response:

**Examples**:

```bash
export EAS_SERVICE_URL=XXXexport EAS_SERVICE_TOKEN=XXX
```

```python
import osfrom langchain_community.chat_models import PaiEasChatEndpointfrom langchain_core.language_models.chat_models import HumanMessageos.environ["EAS_SERVICE_URL"] = "Your_EAS_Service_URL"os.environ["EAS_SERVICE_TOKEN"] = "Your_EAS_Service_Token"chat = PaiEasChatEndpoint(    eas_service_url=os.environ["EAS_SERVICE_URL"],    eas_service_token=os.environ["EAS_SERVICE_TOKEN"],)
```

```python
output = chat.invoke([HumanMessage(content="write a funny joke")])print("output:", output)
```

---

## Anchor Browser | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/anchor_browser/

**Contents**:
- Anchor Browser
- Quickstart​
  - Installation​
  - Usage​
- Additional Resources​

Anchor is the platform for AI Agentic browser automation, which solves the challenge of automating workflows for web applications that lack APIs or have limited API coverage. It simplifies the creation, deployment, and management of browser-based automations, transforming complex web interactions into simple API endpoints.

langchain-anchorbrowser provides 3 main tools:

Import and utilize your intended tool. The full list of Anchor Browser available tools see Tool Features table in Anchor Browser tool page

**Examples**:

```bash
pip install langchain-anchorbrowser
```

```python
from langchain_anchorbrowser import AnchorContentTool# Get Markdown Content for https://www.anchorbrowser.ioAnchorContentTool().invoke(    {"url": "https://www.anchorbrowser.io", "format": "markdown"})
```

---

## Anthropic | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/anthropic/

**Contents**:
- Anthropic
- Installation and Setup​
- Chat Models​
  - ChatAnthropic​
- LLMs​
  - [Legacy] AnthropicLLM​

Anthropic is an AI safety and research company, and is the creator of Claude. This page covers all integrations between Anthropic models and LangChain.

To use Anthropic models, you need to install a python package:

You need to set the ANTHROPIC_API_KEY environment variable. You can get an Anthropic API key here

NOTE: AnthropicLLM only supports legacy Claude 2 models. To use the newest Claude 3 models, please use ChatAnthropic instead.

**Examples**:

```bash
pip install -U langchain-anthropic
```

```python
from langchain_anthropic import ChatAnthropicmodel = ChatAnthropic(model='claude-3-opus-20240229')
```

```python
from langchain_anthropic import AnthropicLLMmodel = AnthropicLLM(model='claude-2.1')
```

---

## Apify | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/apify/

**Contents**:
- Apify
- Installation and Setup​
- Tool​
- Wrapper​
- Document loader​

Apify is a cloud platform for web scraping and data extraction, which provides an ecosystem of more than a thousand ready-made apps called Actors for various scraping, crawling, and extraction use cases.

This integration enables you run Actors on the Apify platform and load their results into LangChain to feed your vector indexes with documents and data from the web, e.g. to generate answers from websites with documentation, blogs, or knowledge bases.

You can use the ApifyActorsTool to use Apify Actors with agents.

See this notebook for example usage and a full example of a tool-calling agent with LangGraph in the Apify LangGraph agent Actor template.

For more information on how to use this tool, visit the Apify integration documentation.

You can use the ApifyWrapper to run Actors on the Apify platform.

For more information on how to use this wrapper, see the Apify integration documentation.

You can also use our ApifyDatasetLoader to get data from Apify dataset.

For a more detailed walkthrough of this loader, see this notebook.

Source code for this integration can be found in the LangChain Apify repository.

**Examples**:

```bash
pip install langchain-apify
```

```python
from langchain_apify import ApifyActorsTool
```

```python
from langchain_apify import ApifyWrapper
```

---

## Astra DB | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/astradb/

**Contents**:
- Astra DB
- Installation and Setup​
- Vector Store​
- Chat message history​
- LLM Cache​
- Semantic LLM Cache​
- Document loader​
- Self-querying retriever​

DataStax Astra DB is a serverless AI-ready database built on Apache Cassandra® and made conveniently available through an easy-to-use JSON API.

See a tutorial provided by DataStax.

Install the following Python package:

Create a database (if needed) and get the connection secrets. Set the following variables:

A few typical initialization patterns are shown here:

Notable features of class AstraDBVectorStore:

Learn more in the example notebook.

See the example provided by DataStax.

See the usage example.

Learn more in the example notebook (scroll to the Astra DB section).

Learn more in the example notebook (scroll to the appropriate section).

Learn more in the example notebook.

Learn more in the example notebook.

See the API Reference for the AstraDBStore.

See the API reference for the AstraDBByteStore.

**Examples**:

```bash
pip install "langchain-astradb>=0.6,<0.7"
```

```python
ASTRA_DB_API_ENDPOINT="API_ENDPOINT"ASTRA_DB_APPLICATION_TOKEN="TOKEN"
```

```python
from langchain_astradb import AstraDBVectorStorevector_store = AstraDBVectorStore(    embedding=my_embedding,    collection_name="my_store",    api_endpoint=ASTRA_DB_API_ENDPOINT,    token=ASTRA_DB_APPLICATION_TOKEN,)from astrapy.info import VectorServiceOptionsvector_store_vectorize = AstraDBVectorStore(    collection_name="my_vectorize_store",    api_endpoint=ASTRA_DB_API_ENDPOINT,    token=ASTRA_DB_APPLICATION_TOKEN,    collection_vector_service_options=VectorServiceOptions(        provider="
...
```

---

## Async programming with LangChain | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/async/

**Contents**:
- Async programming with LangChain
- LangChain asynchronous APIs​
- Delegation to sync methods​
- Performance​
- Compatibility​
- How to use in ipython and jupyter notebooks​

LLM based applications often involve a lot of I/O-bound operations, such as making API calls to language models, databases, or other services. Asynchronous programming (or async programming) is a paradigm that allows a program to perform multiple tasks concurrently without blocking the execution of other tasks, improving efficiency and responsiveness, particularly in I/O-bound operations.

You are expected to be familiar with asynchronous programming in Python before reading this guide. If you are not, please find appropriate resources online to learn how to program asynchronously in Python. This guide specifically focuses on what you need to know to work with LangChain in an asynchronous context, assuming that you are already familiar with asynchronous programming.

Many LangChain APIs are designed to be asynchronous, allowing you to build efficient and responsive applications.

Typically, any method that may perform I/O operations (e.g., making API calls, reading files) will have an asynchronous counterpart.

In LangChain, async implementations are located in the same classes as their synchronous counterparts, with the asynchronous methods having an "a" prefix. For example, the synchronous invoke method has an asynchronous counterpart called ainvoke.

Many components of LangChain implement the Runnable Interface, which includes support for asynchronous execution. This means that you can run Runnables asynchronously using the await keyword in Python.

Other components like Embedding Models and VectorStore that do not implement the Runnable Interface usually still follow the same rule and include the asynchronous version of method in the same class with an "a" prefix.

Runnables created using the LangChain Expression Language (LCEL) can also be run asynchronously as they implement the full Runnable Interface.

For more information, please review the API reference for the specific component you are using.

Most popular LangChain integrations implement asynchronous su

*[Content truncated - see full docs]*

**Examples**:

```python
await some_runnable.ainvoke(some_input)
```

```python
await some_vectorstore.aadd_documents(documents)
```

---

## AzureChatOpenAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/azure_chat_openai/

**Contents**:
- AzureChatOpenAI
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This guide will help you get started with AzureOpenAI chat models. For detailed documentation of all AzureChatOpenAI features and configurations head to the API reference.

Azure OpenAI has several chat models. You can find information about their latest models and their costs, context windows, and supported input types in the Azure docs.

Azure OpenAI refers to OpenAI models hosted on the Microsoft Azure platform. OpenAI also provides its own model APIs. To access OpenAI services directly, use the ChatOpenAI integration.

To access AzureOpenAI models you'll need to create an Azure account, create a deployment of an Azure OpenAI model, get the name and endpoint for your deployment, get an Azure OpenAI API key, and install the langchain-openai integration package.

Head to the Azure docs to create your deployment and generate an API key. Once you've done this set the AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT environment variables:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain AzureOpenAI integration lives in the langchain-openai package:

Now we can instantiate our model object and generate chat completions.

We can chain our model with a prompt template like so:

Azure OpenAI responses contain model_name response metadata property, which is name of the model used to generate the response. However unlike native OpenAI responses, it does not contain the specific version of the model, which is set on the deployment in Azure. E.g. it does not distinguish between gpt-35-turbo-0125 and gpt-35-turbo-0301. This makes it tricky to know which version of the model was used to generate the response, which as result can lead to e.g. wrong total cost calculation with OpenAICallbackHandler.

To solve this problem, you can pass model_version parameter to AzureChatOpenAI class, which will be added to the model name in the llm output. This way you can easily distinguish between different versions of the model.

For detailed document

*[Content truncated - see full docs]*

**Examples**:

```python
import getpassimport osif "AZURE_OPENAI_API_KEY" not in os.environ:    os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass(        "Enter your AzureOpenAI API key: "    )os.environ["AZURE_OPENAI_ENDPOINT"] = "https://YOUR-ENDPOINT.openai.azure.com/"
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-openai
```

---

## Azure AI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/azure_ai/

**Contents**:
- Azure AI
- Chat models​
  - Azure AI Chat Completions Model​
- Embedding models​
  - Azure AI model inference for embeddings​

All functionality related to Azure AI Foundry and its related projects.

Integration packages for Azure AI, Dynamic Sessions, SQL Server are maintained in the langchain-azure repository.

We recommend developers start with the (langchain-azure-ai) to access all the models available in Azure AI Foundry.

Access models like Azure OpenAI, DeepSeek R1, Cohere, Phi and Mistral using the AzureAIChatCompletionsModel class.

Configure your API key and Endpoint.

Configure your API key and Endpoint.

**Examples**:

```bash
pip install -U langchain-azure-ai
```

```bash
export AZURE_INFERENCE_CREDENTIAL=your-api-keyexport AZURE_INFERENCE_ENDPOINT=your-endpoint
```

```python
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModelllm = AzureAIChatCompletionsModel(    model_name="gpt-4o",    api_version="2024-05-01-preview",)llm.invoke('Tell me a joke and include some emojis')
```

---

## Bigtable | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/google-bigtable/

**Contents**:
- Bigtable
- Quick Start​
- Installation​
- Integrations​
  - Vector Store​
  - Key-value Store​
  - Document Loader​
  - Chat Message History​

Bigtable is a scalable, fully managed key-value and wide-column store ideal for fast access to structured, semi-structured, or unstructured data. This page provides an overview of Bigtable's LangChain integrations.

Client Library Documentation: cloud.google.com/python/docs/reference/langchain-google-bigtable/latest

Product Documentation: cloud.google.com/bigtable

To use this library, you first need to:

The main package for this integration is langchain-google-bigtable.

The langchain-google-bigtable package provides the following integrations:

With BigtableVectorStore, you can store documents and their vector embeddings to find the most similar or relevant information in your database.

Learn more in the Vector Store how-to guide.

Use BigtableByteStore as a persistent, scalable key-value store for caching, session management, or other storage needs. It supports both synchronous and asynchronous operations.

Learn more in the Key-value Store how-to guide.

Use the BigtableLoader to load data from a Bigtable table and represent it as LangChain Document objects.

Learn more in the Document Loader how-to guide.

Use BigtableChatMessageHistory to store conversation histories, enabling stateful chains and agents.

Learn more in the Chat Message History how-to guide.

Contributions to this library are welcome. Please see the CONTRIBUTING guide in the package repo for more details

This project is licensed under the Apache 2.0 License - see the LICENSE file in the package repo for details.

This is not an officially supported Google product.

**Examples**:

```bash
pip install -U langchain-google-bigtable
```

```python
from langchain_google_bigtable import BigtableVectorStore# Your embedding service and other configurations# embedding_service = ...engine = await BigtableEngine.async_initialize(project_id="your-project-id")vector_store = await BigtableVectorStore.create(    engine=engine,    instance_id="your-instance-id",    table_id="your-table-id",    embedding_service=embedding_service,    collection="your_collection_name",)await vector_store.aadd_documents([your_documents])results = await vector_store.asim
...
```

```python
from langchain_google_bigtable import BigtableByteStore# Initialize the storestore = await BigtableByteStore.create(    project_id="your-project-id",    instance_id="your-instance-id",    table_id="your-table-id",)# Set and get valuesawait store.amset([("key1", b"value1")])retrieved = await store.amget(["key1"])
```

---

## Box | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/box/

**Contents**:
- Box
  - Installation and setup​
- langchain-box
- Pre-requisites​
- Authentication​
  - BoxAuth helper class​
- Document Loaders​
  - BoxLoader​

Box is the Intelligent Content Cloud, a single platform that enables organizations to fuel collaboration, manage the entire content lifecycle, secure critical content, and transform business workflows with enterprise AI. Founded in 2005, Box simplifies work for leading global organizations, including AstraZeneca, JLL, Morgan Stanley, and Nationwide.

In this package, we make available a number of ways to include Box content in your AI workflows.

This package contains the LangChain integration with Box. For more information about Box, check out our developer documentation.

In order to integrate with Box, you need a few things:

The box-langchain package offers some flexibility to authentication. The most basic authentication method is by using a developer token. This can be found in the Box developer console on the configuration screen. This token is purposely short-lived (1 hour) and is intended for development. With this token, you can add it to your environment as BOX_DEVELOPER_TOKEN, you can pass it directly to the loader, or you can use the BoxAuth authentication helper class.

We will cover passing it directly to the loader in the section below.

BoxAuth supports the following authentication methods:

If using JWT authentication, you will need to download the configuration from the Box developer console after generating your public/private key pair. Place this file in your application directory structure somewhere. You will use the path to this file when using the BoxAuth helper class.

For more information, learn about how to set up a Box application, and check out the Box authentication guide for more about our different authentication options.

JWT with a service account

JWT with a specified user

CCG with a service account

CCG with a specified user

If you wish to use OAuth2 with the authorization_code flow, please use BoxAuthType.TOKEN with the token you have acquired.

**Examples**:

```bash
pip install -U langchain-box
```

```python
from langchain_box.document_loaders import BoxLoaderfrom langchain_box.utilities import BoxAuth, BoxAuthTypeauth = BoxAuth(    auth_type=BoxAuthType.TOKEN,    box_developer_token=box_developer_token)loader = BoxLoader(    box_auth=auth,    ...)
```

```python
from langchain_box.document_loaders import BoxLoaderfrom langchain_box.utilities import BoxAuth, BoxAuthTypeauth = BoxAuth(    auth_type=BoxAuthType.JWT,    box_jwt_path=box_jwt_path)loader = BoxLoader(    box_auth=auth,    ...
```

---

## Bright Data | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/brightdata/

**Contents**:
- Bright Data
- Installation and Setup​
- Tools​

Bright Data is a web data platform that provides tools for web scraping, SERP collection, and accessing geo-restricted content.

Bright Data allows developers to extract structured data from websites, perform search engine queries, and access content that might be otherwise blocked or geo-restricted. The platform is designed to help overcome common web scraping challenges including anti-bot systems, CAPTCHAs, and IP blocks.

You'll need to set up your Bright Data API key:

Or you can pass it directly when initializing tools:

The Bright Data integration provides several tools:

**Examples**:

```bash
pip install langchain-brightdata
```

```python
import osos.environ["BRIGHT_DATA_API_KEY"] = "your-api-key"
```

```python
from langchain_bright_data import BrightDataSERPtool = BrightDataSERP(bright_data_api_key="your-api-key")
```

---

## Build a Chatbot | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/tutorials/chatbot/

**Contents**:
- Build a Chatbot
- Overview​
- Setup​
  - Jupyter Notebook​
  - Installation​
  - LangSmith​
- Quickstart​
- Message persistence​

This tutorial previously used the RunnableWithMessageHistory abstraction. You can access that version of the documentation in the v0.2 docs.

As of the v0.3 release of LangChain, we recommend that LangChain users take advantage of LangGraph persistence to incorporate memory into new LangChain applications.

If your code is already relying on RunnableWithMessageHistory or BaseChatMessageHistory, you do not need to make any changes. We do not plan on deprecating this functionality in the near future as it works for simple chat applications and any code that uses RunnableWithMessageHistory will continue to work as expected.

Please see How to migrate to LangGraph Memory for more details.

We'll go over an example of how to design and implement an LLM-powered chatbot. This chatbot will be able to have a conversation and remember previous interactions with a chat model.

Note that this chatbot that we build will only use the language model to have a conversation. There are several other related concepts that you may be looking for:

This tutorial will cover the basics which will be helpful for those two more advanced topics, but feel free to skip directly to there should you choose.

This guide (and most of the other guides in the documentation) uses Jupyter notebooks and assumes the reader is as well. Jupyter notebooks are perfect for learning how to work with LLM systems because oftentimes things can go wrong (unexpected output, API down, etc) and going through guides in an interactive environment is a great way to better understand them.

This and other tutorials are perhaps most conveniently run in a Jupyter notebook. See here for instructions on how to install.

For this tutorial we will need langchain-core and langgraph. This guide requires langgraph >= 0.2.28.

For more details, see our Installation guide.

Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more c

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install langchain-core langgraph>0.2.27
```

```bash
conda install langchain-core langgraph>0.2.27 -c conda-forge
```

```shell
export LANGSMITH_TRACING="true"export LANGSMITH_API_KEY="..."
```

---

## Callbacks | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/callbacks/

**Contents**:
- Callbacks
- Callback events​
- Callback handlers​
- Passing callbacks​

LangChain provides a callback system that allows you to hook into the various stages of your LLM application. This is useful for logging, monitoring, streaming, and other tasks.

You can subscribe to these events by using the callbacks argument available throughout the API. This argument is a list of handler objects, which are expected to implement one or more of the methods described below in more detail.

Callback handlers can either be sync or async:

During run-time LangChain configures an appropriate callback manager (e.g., CallbackManager or AsyncCallbackManager which will be responsible for calling the appropriate method on each "registered" callback handler when the event is triggered.

The callbacks property is available on most objects throughout the API (Models, Tools, Agents, etc.) in two different places:

Constructor callbacks are scoped only to the object they are defined on. They are not inherited by children of the object.

If you're creating a custom chain or runnable, you need to remember to propagate request time callbacks to any child objects.

Any RunnableLambda, a RunnableGenerator, or Tool that invokes other runnables and is running async in python<=3.10, will have to propagate callbacks to child objects manually. This is because LangChain cannot automatically propagate callbacks to child objects in this case.

This is a common reason why you may fail to see events being emitted from custom runnables or tools.

For specifics on how to use callbacks, see the relevant how-to guides here.

---

## Cerebras | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/cerebras/

**Contents**:
- Cerebras
- Installation and Setup​
- API Key​
- Chat Model​

At Cerebras, we've developed the world's largest and fastest AI processor, the Wafer-Scale Engine-3 (WSE-3). The Cerebras CS-3 system, powered by the WSE-3, represents a new class of AI supercomputer that sets the standard for generative AI training and inference with unparalleled performance and scalability.

With Cerebras as your inference provider, you can:

Our CS-3 systems can be quickly and easily clustered to create the largest AI supercomputers in the world, making it simple to place and run the largest models. Leading corporations, research institutions, and governments are already using Cerebras solutions to develop proprietary models and train popular open-source models.

Want to experience the power of Cerebras? Check out our website for more resources and explore options for accessing our technology through the Cerebras Cloud or on-premise deployments!

For more information about Cerebras Cloud, visit cloud.cerebras.ai. Our API reference is available at inference-docs.cerebras.ai.

Install the integration package:

Get an API Key from cloud.cerebras.ai and add it to your environment variables:

**Examples**:

```bash
pip install langchain-cerebras
```

```text
export CEREBRAS_API_KEY="your-api-key-here"
```

---

## ChatAI21 | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/ai21

**Contents**:
- ChatAI21
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​
- Invocation​

This notebook covers how to get started with AI21 chat models. Note that different chat models support different parameters. See the AI21 documentation to learn more about the parameters in your chosen model. See all AI21's LangChain components.

We'll need to get an AI21 API key and set the AI21_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

!pip install -qU langchain-ai21

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

This example shows how to use tool calling with AI21 models:

For detailed documentation of all ChatAI21 features and configurations head to the API reference: https://python.langchain.com/api_reference/ai21/chat_models/langchain_ai21.chat_models.ChatAI21.html

**Examples**:

```python
import osfrom getpass import getpassif "AI21_API_KEY" not in os.environ:    os.environ["AI21_API_KEY"] = getpass()
```

```python
# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

```python
from langchain_ai21 import ChatAI21llm = ChatAI21(model="jamba-instruct", temperature=0)
```

---

## ChatAbso | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/abso

**Contents**:
- ChatAbso
- Overview​
  - Integration details​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​
- Invocation​

This will help you get started with ChatAbso chat models. For detailed documentation of all ChatAbso features and configurations, head to the API reference.

To access ChatAbso models, you'll need to create an OpenAI account, get an API key, and install the langchain-abso integration package.

Head to (TODO: link) to sign up for ChatAbso and generate an API key. Once you've done this, set the ABSO_API_KEY environment variable:

The LangChain ChatAbso integration lives in the langchain-abso package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

For detailed documentation of all ChatAbso features and configurations head to the API reference: https://python.langchain.com/api_reference/en/latest/chat_models/langchain_abso.chat_models.ChatAbso.html

**Examples**:

```python
import getpassimport osif not os.getenv("OPENAI_API_KEY"):    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
```

```python
%pip install -qU langchain-abso
```

```python
from langchain_abso import ChatAbsollm = ChatAbso(fast_model="gpt-4o", slow_model="o3-mini")
```

---

## ChatAimlapi | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/aimlapi

**Contents**:
- ChatAimlapi
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Installation​
- Instantiation​
- Invocation​

This page will help you get started with AI/ML API chat models. For detailed documentation of all ChatAimlapi features and configurations, head to the API reference.

AI/ML API provides access to 300+ models (Deepseek, Gemini, ChatGPT, etc.) via high-uptime and high-rate API.

To access AI/ML API models, sign up at aimlapi.com, generate an API key, and set the AIMLAPI_API_KEY environment variable:

Install the langchain-aimlapi package:

Now we can instantiate the ChatAimlapi model and generate chat completions:

You can invoke the model with a list of messages:

We can chain the model with a prompt template as follows:

For detailed documentation of all ChatAimlapi features and configurations, visit the API Reference.

**Examples**:

```python
import getpassimport osif "AIMLAPI_API_KEY" not in os.environ:    os.environ["AIMLAPI_API_KEY"] = getpass.getpass("Enter your AI/ML API key: ")
```

```python
%pip install -qU langchain-aimlapi
```

```output
Note: you may need to restart the kernel to use updated packages.
```

---

## ChatAimlapi | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/aimlapi/

**Contents**:
- ChatAimlapi
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Installation​
- Instantiation​
- Invocation​

This page will help you get started with AI/ML API chat models. For detailed documentation of all ChatAimlapi features and configurations, head to the API reference.

AI/ML API provides access to 300+ models (Deepseek, Gemini, ChatGPT, etc.) via high-uptime and high-rate API.

To access AI/ML API models, sign up at aimlapi.com, generate an API key, and set the AIMLAPI_API_KEY environment variable:

Install the langchain-aimlapi package:

Now we can instantiate the ChatAimlapi model and generate chat completions:

You can invoke the model with a list of messages:

We can chain the model with a prompt template as follows:

For detailed documentation of all ChatAimlapi features and configurations, visit the API Reference.

**Examples**:

```python
import getpassimport osif "AIMLAPI_API_KEY" not in os.environ:    os.environ["AIMLAPI_API_KEY"] = getpass.getpass("Enter your AI/ML API key: ")
```

```python
%pip install -qU langchain-aimlapi
```

```output
Note: you may need to restart the kernel to use updated packages.
```

---

## ChatAnthropic | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/anthropic/

**Contents**:
- ChatAnthropic
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This notebook provides a quick overview for getting started with Anthropic chat models. For detailed documentation of all ChatAnthropic features and configurations head to the API reference.

Anthropic has several chat models. You can find information about their latest models and their costs, context windows, and supported input types in the Anthropic docs.

Note that certain Anthropic models can also be accessed via AWS Bedrock and Google VertexAI. See the ChatBedrock and ChatVertexAI integrations to use Anthropic models via these services.

To access Anthropic models you'll need to create an Anthropic account, get an API key, and install the langchain-anthropic integration package.

Head to https://console.anthropic.com/ to sign up for Anthropic and generate an API key. Once you've done this set the ANTHROPIC_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Anthropic integration lives in the langchain-anthropic package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

Content from a single Anthropic AI message can either be a single string or a list of content blocks. For example when an Anthropic model invokes a tool, the tool invocation is part of the message content (as well as being exposed in the standardized AIMessage.tool_calls):

Claude supports image and PDF inputs as content blocks, both in Anthropic's native format (see docs for vision and PDF support) as well as LangChain's standard format.

Claude also supports interactions with files through its managed Files API. See examples below.

The Files API can also be used to upload files to a container for use with Claude's built-in code-execution tools. See the code execution section below, for details.

Claude 3.7 Sonnet supports an extended thinking feature, which will output the step-by-step reasoning process that led to its final answer.

To use it, 

*[Content truncated - see full docs]*

**Examples**:

```python
import getpassimport osif "ANTHROPIC_API_KEY" not in os.environ:    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Anthropic API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-anthropic
```

---

## ChatBedrock | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/bedrock/

**Contents**:
- ChatBedrock
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation ​

This doc will help you get started with AWS Bedrock chat models. Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon via a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top FMs for your use case, privately customize them with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise systems and data sources. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with.

AWS Bedrock maintains a Converse API which provides a unified conversational interface for Bedrock models. This API does not yet support custom models. You can see a list of all models that are supported here.

We recommend the Converse API for users who do not need to use custom models. It can be accessed using ChatBedrockConverse.

For detailed documentation of all Bedrock features and configurations head to the API reference.

The below apply to both ChatBedrock and ChatBedrockConverse.

To access Bedrock models you'll need to create an AWS account, set up the Bedrock API service, get an access key ID and secret key, and install the langchain-aws integration package.

Head to the AWS docs to sign up to AWS and setup your credentials.

Alternatively, ChatBedrockConverse will read from the following environment variables by default:

You'll also need to turn on model access for your account, which you can do by following these instructions.

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Bedrock integratio

*[Content truncated - see full docs]*

**Examples**:

```python
# os.environ["AWS_ACCESS_KEY_ID"] = "..."# os.environ["AWS_SECRET_ACCESS_KEY"] = "..."# Not required unless using temporary credentials.# os.environ["AWS_SESSION_TOKEN"] = "..."
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-aws
```

---

## ChatDatabricks | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/databricks

**Contents**:
- ChatDatabricks
- Overview​
  - Integration details​
  - Model features​
  - Supported Methods​
  - Endpoint Requirement​
- Setup​
  - Credentials (only if you are outside Databricks)​

Databricks Lakehouse Platform unifies data, analytics, and AI on one platform.

This notebook provides a quick overview for getting started with Databricks chat models. For detailed documentation of all ChatDatabricks features and configurations head to the API reference.

ChatDatabricks class wraps a chat model endpoint hosted on Databricks Model Serving. This example notebook shows how to wrap your serving endpoint and use it as a chat model in your LangChain application.

ChatDatabricks supports all methods of ChatModel including async APIs.

The serving endpoint ChatDatabricks wraps must have OpenAI-compatible chat input/output format (reference). As long as the input format is compatible, ChatDatabricks can be used for any endpoint type hosted on Databricks Model Serving:

To access Databricks models you'll need to create a Databricks account, set up credentials (only if you are outside Databricks workspace), and install required packages.

If you are running LangChain app inside Databricks, you can skip this step.

Otherwise, you need manually set the Databricks workspace hostname and personal access token to DATABRICKS_HOST and DATABRICKS_TOKEN environment variables, respectively. See Authentication Documentation for how to get an access token.

The LangChain Databricks integration lives in the databricks-langchain package.

We first demonstrates how to query DBRX-instruct model hosted as Foundation Models endpoint with ChatDatabricks.

For other type of endpoints, there are some difference in how to set up the endpoint itself, however, once the endpoint is ready, there is no difference in how to query it with ChatDatabricks. Please refer to the bottom of this notebook for the examples with other type of endpoints.

Similar to other chat models, ChatDatabricks can be used as a part of a complex chain.

ChatDatabricks supports OpenAI-compatible tool calling API that lets you describe tools and their arguments, and have the model return a JSON object with a too

*[Content truncated - see full docs]*

**Examples**:

```python
import getpassimport osos.environ["DATABRICKS_HOST"] = "https://your-workspace.cloud.databricks.com"if "DATABRICKS_TOKEN" not in os.environ:    os.environ["DATABRICKS_TOKEN"] = getpass.getpass(        "Enter your Databricks access token: "    )
```

```output
Enter your Databricks access token:  ········
```

```python
%pip install -qU databricks-langchain
```

---

## ChatFireworks | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/fireworks/

**Contents**:
- ChatFireworks
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This doc helps you get started with Fireworks AI chat models. For detailed documentation of all ChatFireworks features and configurations head to the API reference.

Fireworks AI is an AI inference platform to run and customize models. For a list of all models served by Fireworks see the Fireworks docs.

To access Fireworks models you'll need to create a Fireworks account, get an API key, and install the langchain-fireworks integration package.

Head to (https://fireworks.ai/login to sign up to Fireworks and generate an API key. Once you've done this set the FIREWORKS_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Fireworks integration lives in the langchain-fireworks package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

For detailed documentation of all ChatFireworks features and configurations head to the API reference: https://python.langchain.com/api_reference/fireworks/chat_models/langchain_fireworks.chat_models.ChatFireworks.html

**Examples**:

```python
import getpassimport osif "FIREWORKS_API_KEY" not in os.environ:    os.environ["FIREWORKS_API_KEY"] = getpass.getpass("Enter your Fireworks API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-fireworks
```

---

## ChatGoogleGenerativeAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/google_generative_ai/

**Contents**:
- ChatGoogleGenerativeAI
  - Integration details​
  - Model features​
  - Setup​
  - Chat Models​
- Instantiation​
- Invocation​
- Chaining​

Access Google's Generative AI models, including the Gemini family, directly via the Gemini API or experiment rapidly using Google AI Studio. The langchain-google-genai package provides the LangChain integration for these models. This is often the best starting point for individual developers.

For information on the latest models, their features, context windows, etc. head to the Google AI docs. All model ids can be found in the Gemini API docs.

To access Google AI models you'll need to create a Google Account, get a Google AI API key, and install the langchain-google-genai integration package.

Head to https://ai.google.dev/gemini-api/docs/api-key (or via Google AI Studio) to generate a Google AI API key.

Use the ChatGoogleGenerativeAI class to interact with Google's chat models. See the API reference for full details.

To enable automated tracing of your model calls, set your LangSmith API key:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

Gemini models can accept multimodal inputs (text, images, audio, video) and, for some models, generate multimodal outputs.

Provide image inputs along with text using a HumanMessage with a list content format. Make sure to use a model that supports image input, such as gemini-2.5-flash.

Other supported image_url formats:

Provide audio file inputs along with text.

Provide video file inputs along with text.

Certain models (such as gemini-2.0-flash-preview-image-generation) can generate text and images inline. You need to specify the desired response_modalities. See more information on the Gemini API docs for details.

You can iterate on an image in a multi-turn conversation, as shown below:

You can also represent an input image and query in a single message by encoding the base64 data in the data URI scheme:

You can also use LangGraph to manage the conversation history for you as in this tutorial.

You can equip the model with tools to call.

*[Content truncated - see full docs]*

**Examples**:

```python
%pip install -U langchain-google-genai
```

```python
import getpassimport osif "GOOGLE_API_KEY" not in os.environ:    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

---

## ChatGroq | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/groq/

**Contents**:
- ChatGroq
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This will help you get started with Groq chat models. For detailed documentation of all ChatGroq features and configurations head to the API reference. For a list of all Groq models, visit this link.

To access Groq models you'll need to create a Groq account, get an API key, and install the langchain-groq integration package.

Head to the Groq console to sign up to Groq and generate an API key. Once you've done this set the GROQ_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Groq integration lives in the langchain-groq package:

Now we can instantiate our model object and generate chat completions.

If you choose to set a reasoning_format, you must ensure that the model you are using supports it. You can find a list of supported models in the Groq documentation.

We can chain our model with a prompt template like so:

For detailed documentation of all ChatGroq features and configurations head to the API reference.

**Examples**:

```python
import getpassimport osif "GROQ_API_KEY" not in os.environ:    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-groq
```

---

## ChatHuggingFace | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/huggingface/

**Contents**:
- ChatHuggingFace
- Overview​
  - Integration details​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​

This will help you get started with langchain_huggingface chat models. For detailed documentation of all ChatHuggingFace features and configurations head to the API reference. For a list of models supported by Hugging Face check out this page.

To access Hugging Face models you'll need to create a Hugging Face account, get an API key, and install the langchain-huggingface integration package.

Generate a Hugging Face Access Token and store it as an environment variable: HUGGINGFACEHUB_API_TOKEN.

To access langchain_huggingface models you'll need to create a Hugging Face account, get an API key, and install the langchain-huggingface integration package.

You'll need to have a Hugging Face Access Token saved as an environment variable: HUGGINGFACEHUB_API_TOKEN.

You can instantiate a ChatHuggingFace model in two different ways, either from a HuggingFaceEndpoint or from a HuggingFacePipeline.

Now let's take advantage of Inference Providers to run the model on specific third-party providers

To run a quantized version of your model, you can specify a bitsandbytes quantization config as follows:

and pass it to the HuggingFacePipeline as a part of its model_kwargs:

For detailed documentation of all ChatHuggingFace features and configurations head to the API reference: https://python.langchain.com/api_reference/huggingface/chat_models/langchain_huggingface.chat_models.huggingface.ChatHuggingFace.html

For detailed documentation of all ChatHuggingFace features and configurations head to the API reference: https://python.langchain.com/api_reference/huggingface/chat_models/langchain_huggingface.chat_models.huggingface.ChatHuggingFace.html

**Examples**:

```python
import getpassimport osif not os.getenv("HUGGINGFACEHUB_API_TOKEN"):    os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass.getpass("Enter your token: ")
```

```python
import getpassimport osos.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass.getpass(    "Enter your Hugging Face API key: ")
```

```python
%pip install --upgrade --quiet  langchain-huggingface text-generation transformers google-search-results numexpr langchainhub sentencepiece jinja2 bitsandbytes accelerate
```

---

## ChatMistralAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/mistralai/

**Contents**:
- ChatMistralAI
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This will help you get started with Mistral chat models. For detailed documentation of all ChatMistralAI features and configurations head to the API reference. The ChatMistralAI class is built on top of the Mistral API. For a list of all the models supported by Mistral, check out this page.

To access ChatMistralAI models you'll need to create a Mistral account, get an API key, and install the langchain-mistralai integration package.

A valid API key is needed to communicate with the API. Once you've done this set the MISTRAL_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Mistral integration lives in the langchain-mistralai package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

Head to the API reference for detailed documentation of all attributes and methods.

**Examples**:

```python
import getpassimport osif "MISTRAL_API_KEY" not in os.environ:    os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter your Mistral API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-mistralai
```

---

## ChatNVIDIA | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints/

**Contents**:
- ChatNVIDIA
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This will help you get started with NVIDIA chat models. For detailed documentation of all ChatNVIDIA features and configurations head to the API reference.

The langchain-nvidia-ai-endpoints package contains LangChain integrations building applications with models on NVIDIA NIM inference microservice. NIM supports models across domains like chat, embedding, and re-ranking models from the community as well as NVIDIA. These models are optimized by NVIDIA to deliver the best performance on NVIDIA accelerated infrastructure and deployed as a NIM, an easy-to-use, prebuilt containers that deploy anywhere using a single command on NVIDIA accelerated infrastructure.

NVIDIA hosted deployments of NIMs are available to test on the NVIDIA API catalog. After testing, NIMs can be exported from NVIDIA’s API catalog using the NVIDIA AI Enterprise license and run on-premises or in the cloud, giving enterprises ownership and full control of their IP and AI application.

NIMs are packaged as container images on a per model basis and are distributed as NGC container images through the NVIDIA NGC Catalog. At their core, NIMs provide easy, consistent, and familiar APIs for running inference on an AI model.

This example goes over how to use LangChain to interact with NVIDIA supported via the ChatNVIDIA class.

For more information on accessing the chat models through this api, check out the ChatNVIDIA documentation.

Create a free account with NVIDIA, which hosts NVIDIA AI Foundation models.

Click on your model of choice.

Under Input select the Python tab, and click Get API Key. Then click Generate Key.

Copy and save the generated key as NVIDIA_API_KEY. From there, you should have access to the endpoints.

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain NVIDIA AI Endpoints integration lives in the langchain-nvidia-ai-endpoints package:

Now we can access models in the NVIDIA API Catalog:

When ready to deploy, you can self-host models with 

*[Content truncated - see full docs]*

**Examples**:

```python
import getpassimport osif not os.getenv("NVIDIA_API_KEY"):    # Note: the API key should start with "nvapi-"    os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
```

```python
# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

```python
%pip install --upgrade --quiet langchain-nvidia-ai-endpoints
```

---

## ChatOCIGenAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/oci_generative_ai

**Contents**:
- ChatOCIGenAI
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This notebook provides a quick overview for getting started with OCIGenAI chat models. For detailed documentation of all ChatOCIGenAI features and configurations head to the API reference.

Oracle Cloud Infrastructure (OCI) Generative AI is a fully managed service that provides a set of state-of-the-art, customizable large language models (LLMs) that cover a wide range of use cases, and which is available through a single API. Using the OCI Generative AI service you can access ready-to-use pretrained models, or create and host your own fine-tuned custom models based on your own data on dedicated AI clusters. Detailed documentation of the service and API is available here and here.

To access OCIGenAI models you'll need to install the oci and langchain-oci packages.

The credentials and authentication methods supported for this integration are equivalent to those used with other OCI services and follow the standard SDK authentication methods, specifically API Key, session token, instance principal, and resource principal.

API key is the default authentication method used in the examples above. The following example demonstrates how to use a different authentication method (session token)

The LangChain OCIGenAI integration lives in the langchain-oci package and you will also need to install the oci package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

For detailed documentation of all ChatOCIGenAI features and configurations head to the API reference: https://pypi.org/project/langchain-oci/

**Examples**:

```python
%pip install -qU langchain-oci
```

```python
from langchain_oci.chat_models import ChatOCIGenAIchat = ChatOCIGenAI(    model_id="cohere.command-r-plus-08-2024",    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",    compartment_id="compartment_id",    model_kwargs={"temperature": 0, "max_tokens": 500},    auth_type="SECURITY_TOKEN",    auth_profile="auth_profile_name",    auth_file_location="auth_file_location",)
```

```python
response = chat.invoke("Tell me one fact about Earth")
```

---

## ChatOllama | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/ollama/

**Contents**:
- ChatOllama
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Installation​
- Instantiation​
- Invocation​

Ollama allows you to run open-source large language models, such as gpt-oss, locally.

ollama bundles model weights, configuration, and data into a single package, defined by a Modelfile.

It optimizes setup and configuration details, including GPU usage.

For a complete list of supported models and model variants, see the Ollama model library.

First, follow these instructions to set up and run a local Ollama instance:

On Mac, the models will be download to ~/.ollama/models

On Linux (or WSL), the models will be stored at /usr/share/ollama/.ollama/models

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Ollama integration lives in the langchain-ollama package:

Make sure you're using the latest Ollama version!

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

We can use tool calling with an LLM that has been fine-tuned for tool use such as gpt-oss:

Details on creating custom tools are available in this guide. Below, we demonstrate how to create a tool using the @tool decorator on a normal python function.

Ollama has limited support for multi-modal LLMs, such as gemma3

Be sure to update Ollama so that you have the most recent version to support multi-modal.

Some models, such as IBM's Granite 3.2, support custom message roles to enable thinking processes.

To access Granite 3.2's thinking features, pass a message with a "control" role with content set to "thinking". Because "control" is a non-standard message role, we can use a ChatMessage object to implement it:

Note that the model exposes its thought process in addition to its final response.

For detailed documentation of all ChatOllama features and configurations head to the API reference.

**Examples**:

```python
# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

```python
%pip install -qU langchain-ollama
```

```python
%pip install -U ollama
```

---

## ChatOpenAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/openai/

**Contents**:
- ChatOpenAI
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This notebook provides a quick overview for getting started with OpenAI chat models. For detailed documentation of all ChatOpenAI features and configurations head to the API reference.

OpenAI has several chat models. You can find information about their latest models and their costs, context windows, and supported input types in the OpenAI docs.

Note that certain OpenAI models can also be accessed via the Microsoft Azure platform. To use the Azure OpenAI service use the AzureChatOpenAI integration.

To access OpenAI models you'll need to create an OpenAI account, get an API key, and install the langchain-openai integration package.

Head to https://platform.openai.com to sign up to OpenAI and generate an API key. Once you've done this set the OPENAI_API_KEY environment variable:

If you want to get automated tracing of your model calls you can also set your LangSmith API key by uncommenting below:

The LangChain OpenAI integration lives in the langchain-openai package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

OpenAI has a tool calling (we use "tool calling" and "function calling" interchangeably here) API that lets you describe tools and their arguments, and have the model return a JSON object with a tool to invoke and the inputs to that tool. tool-calling is extremely useful for building tool-using chains and agents, and for getting structured outputs from models more generally.

With ChatOpenAI.bind_tools, we can easily pass in Pydantic classes, dict schemas, LangChain tools, or even functions as tools to the model. Under the hood these are converted to an OpenAI tool schemas, which looks like:

and passed in every model invocation.

As of Aug 6, 2024, OpenAI supports a strict argument when calling tools that will enforce that the tool argument schema is respected by the model. See more here: https://platform.openai.com/docs/guides/function-calling

Note: If strict=True the t

*[Content truncated - see full docs]*

**Examples**:

```python
import getpassimport osif not os.environ.get("OPENAI_API_KEY"):    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-openai
```

---

## ChatPerplexity | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/perplexity

**Contents**:
- ChatPerplexity
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
- Using Perplexity-specific parameters through ChatPerplexity​
  - Accessing the search results metadata​

This page will help you get started with Perplexity chat models. For detailed documentation of all ChatPerplexity features and configurations head to the API reference.

To access Perplexity models you'll need to create a Perplexity account, get an API key, and install the langchain-perplexity integration package.

Head to this page to sign up for Perplexity and generate an API key. Once you've done this set the PPLX_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The code provided assumes that your PPLX_API_KEY is set in your environment variables. If you would like to manually specify your API key and also choose a different model, you can use the following code:

You can check a list of available models here. For reproducibility, we can set the API key dynamically by taking it as an input in this notebook.

You can format and structure the prompts like you would typically. In the following example, we ask the model to tell us a joke about cats.

You can also use Perplexity-specific parameters through the ChatPerplexity class. For example, parameters like search_domain_filter, return_images, return_related_questions or search_recency_filter using the extra_body parameter as shown below:

Perplexity often provides a list of the web pages it consulted (“search_results”). You don't need to pass any special parameter — the list is placed in response.additional_kwargs["search_results"].

**Examples**:

```python
import getpassimport osif "PPLX_API_KEY" not in os.environ:    os.environ["PPLX_API_KEY"] = getpass.getpass("Enter your Perplexity API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
from langchain_core.prompts import ChatPromptTemplatefrom langchain_perplexity import ChatPerplexity
```

---

## ChatTogether | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/together/

**Contents**:
- ChatTogether
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This page will help you get started with Together AI chat models. For detailed documentation of all ChatTogether features and configurations, head to the API reference.

Together AI offers an API to query 50+ leading open-source models

To access Together models you'll need to create a/an Together account, get an API key, and install the langchain-together integration package.

Head to this page to sign up to Together and generate an API key. Once you've done this, set the TOGETHER_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain Together integration is included in the langchain-together package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template as follows:

For detailed documentation of all ChatTogether features and configurations, head to the API reference: https://python.langchain.com/api_reference/together/chat_models/langchain_together.chat_models.ChatTogether.html

**Examples**:

```python
import getpassimport osif "TOGETHER_API_KEY" not in os.environ:    os.environ["TOGETHER_API_KEY"] = getpass.getpass("Enter your Together API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-together
```

---

## ChatUpstage | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/upstage

**Contents**:
- ChatUpstage
- Installation​
- Environment Setup​
- Usage​
- Chaining​
- Related​

This notebook covers how to get started with Upstage chat models.

Install langchain-upstage package.

Make sure to set the following environment variables:

**Examples**:

```bash
pip install -U langchain-upstage
```

```python
import osos.environ["UPSTAGE_API_KEY"] = "YOUR_API_KEY"
```

```python
from langchain_core.prompts import ChatPromptTemplatefrom langchain_upstage import ChatUpstagechat = ChatUpstage()
```

---

## ChatVertexAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/google_vertex_ai_palm/

**Contents**:
- ChatVertexAI
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This page provides a quick overview for getting started with VertexAI chat models. For detailed documentation of all ChatVertexAI features and configurations head to the API reference.

ChatVertexAI exposes all foundational models available in Google Cloud, like gemini-2.5-pro, gemini-2.5-flash, etc. For a full and updated list of available models visit VertexAI documentation.

The Google Cloud VertexAI integration is separate from the Google PaLM integration. Google has chosen to offer an enterprise version of PaLM through GCP, and this supports the models made available through there.

To access VertexAI models you'll need to create a Google Cloud Platform account, set up credentials, and install the langchain-google-vertexai integration package.

To use the integration you must either:

This codebase uses the google.auth library which first looks for the application credentials variable mentioned above, and then looks for system-level auth.

For more information, see:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain VertexAI integration lives in the langchain-google-vertexai package:

Now we can instantiate our model object and generate chat completions:

Gemini supports a range of tools that are executed server-side.

Gemini can execute a Google search and use the results to ground its responses:

Gemini can generate and execute Python code:

We can chain our model with a prompt template like so:

For detailed documentation of all ChatVertexAI features and configurations, like how to send multimodal inputs and configure safety settings, head to the API reference: https://python.langchain.com/api_reference/google_vertexai/chat_models/langchain_google_vertexai.chat_models.ChatVertexAI.html

**Examples**:

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-google-vertexai
```

```output
Note: you may need to restart the kernel to use updated packages.
```

---

## ChatWatsonx | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/ibm_watsonx

**Contents**:
- ChatWatsonx
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

ChatWatsonx is a wrapper for IBM watsonx.ai foundation models.

The aim of these examples is to show how to communicate with watsonx.ai models using LangChain LLMs API.

To access IBM watsonx.ai models you'll need to create an IBM watsonx.ai account, get an API key, and install the langchain-ibm integration package.

The cell below defines the credentials required to work with watsonx Foundation Model inferencing.

Action: Provide the IBM Cloud user API key. For details, see Managing user API keys.

Additionally you are able to pass additional secrets as an environment variable.

The LangChain IBM integration lives in the langchain-ibm package:

You might need to adjust model parameters for different models or tasks. For details, refer to Available TextChatParameters.

Initialize the WatsonxLLM class with the previously set parameters.

In this example, we’ll use the project_id and Dallas URL.

You need to specify the model_id that will be used for inferencing. You can find the list of all the available models in Supported chat models.

Alternatively, you can use Cloud Pak for Data credentials. For details, see watsonx.ai software setup.

Instead of model_id, you can also pass the deployment_id of the previously deployed model with reference to a Prompt Template.

For certain requirements, there is an option to pass the IBM's APIClient object into the ChatWatsonx class.

To obtain completions, you can call the model directly using a string prompt.

Create ChatPromptTemplate objects which will be responsible for creating a random question.

Provide a inputs and run the chain.

You can stream the model output.

You can batch the model output.

Notice that the AIMessage has a tool_calls attribute. This contains in a standardized ToolCall format that is model-provider agnostic.

For detailed documentation of all ChatWatsonx features and configurations head to the API reference.

**Examples**:

```python
import osfrom getpass import getpasswatsonx_api_key = getpass()os.environ["WATSONX_APIKEY"] = watsonx_api_key
```

```python
import osos.environ["WATSONX_URL"] = "your service instance url"os.environ["WATSONX_TOKEN"] = "your token for accessing the CPD cluster"os.environ["WATSONX_PASSWORD"] = "your password for accessing the CPD cluster"os.environ["WATSONX_USERNAME"] = "your username for accessing the CPD cluster"os.environ["WATSONX_INSTANCE_ID"] = "your instance_id for accessing the CPD cluster"
```

```python
!pip install -qU langchain-ibm
```

---

## ChatXAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/xai

**Contents**:
- ChatXAI
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Credentials​
  - Installation​
- Instantiation​

This page will help you get started with xAI chat models. For detailed documentation of all ChatXAI features and configurations, head to the API reference.

xAI offers an API to interact with Grok models.

To access xAI models, you'll need to create an xAI account, get an API key, and install the langchain-xai integration package.

Head to this page to sign up for xAI and generate an API key. Once you've done this, set the XAI_API_KEY environment variable:

To enable automated tracing of your model calls, set your LangSmith API key:

The LangChain xAI integration lives in the langchain-xai package:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

ChatXAI has a tool calling (we use "tool calling" and "function calling" interchangeably here) API that lets you describe tools and their arguments, and have the model return a JSON object with a tool to invoke and the inputs to that tool. Tool-calling is extremely useful for building tool-using chains and agents, and for getting structured outputs from models more generally.

With ChatXAI.bind_tools, we can easily pass in Pydantic classes, dict schemas, LangChain tools, or even functions as tools to the model. Under the hood, these are converted to an OpenAI tool schema, which looks like:

and passed in every model invocation.

xAI supports a Live Search feature that enables Grok to ground its answers using results from web searches:

See xAI docs for the full set of web search options.

For detailed documentation of all ChatXAI features and configurations, head to the API reference.

**Examples**:

```python
import getpassimport osif "XAI_API_KEY" not in os.environ:    os.environ["XAI_API_KEY"] = getpass.getpass("Enter your xAI API key: ")
```

```python
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")# os.environ["LANGSMITH_TRACING"] = "true"
```

```python
%pip install -qU langchain-xai
```

---

## Chat history | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/chat_history/

**Contents**:
- Chat history
- Conversation patterns​
- Managing chat history​
- Related resources​

Chat history is a record of the conversation between the user and the chat model. It is used to maintain context and state throughout the conversation. The chat history is sequence of messages, each of which is associated with a specific role, such as "user", "assistant", "system", or "tool".

Most conversations start with a system message that sets the context for the conversation. This is followed by a user message containing the user's input, and then an assistant message containing the model's response.

The assistant may respond directly to the user or if configured with tools request that a tool be invoked to perform a specific task.

A full conversation often involves a combination of two patterns of alternating messages:

Since chat models have a maximum limit on input size, it's important to manage chat history and trim it as needed to avoid exceeding the context window.

While processing chat history, it's essential to preserve a correct conversation structure.

Key guidelines for managing chat history:

Understanding correct conversation structure is essential for being able to properly implement memory in chat models.

---

## Chroma | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/chroma/

**Contents**:
- Chroma
- Installation and Setup​
- VectorStore​
- Retriever​

Chroma is a database for building AI applications with embeddings.

There exists a wrapper around Chroma vector databases, allowing you to use it as a vectorstore, whether for semantic search or example selection.

For a more detailed walkthrough of the Chroma wrapper, see this notebook

**Examples**:

```bash
pip install langchain-chroma
```

```python
from langchain_chroma import Chroma
```

```python
from langchain.retrievers import SelfQueryRetriever
```

---

## Cloudflare | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/cloudflare/

**Contents**:
- Cloudflare
- ChatModels​
- VectorStore​
- Embeddings​
- LLMs​

Cloudflare, Inc. (Wikipedia) is an American company that provides content delivery network services, cloud cybersecurity, DDoS mitigation, and ICANN-accredited domain registration services.

Cloudflare Workers AI allows you to run machine learning models, on the Cloudflare network, from your code via REST API.

See installation instructions and usage example.

See installation instructions and usage example.

See installation instructions and usage example.

See installation instructions and usage example.

**Examples**:

```python
from langchain_cloudflare import ChatCloudflareWorkersAI
```

```python
from langchain_cloudflare import CloudflareVectorize
```

```python
from langchain_cloudflare import CloudflareWorkersAIEmbeddings
```

---

## Cognee | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/cognee/

**Contents**:
- Cognee
- Installation and Setup​
- Retrievers​

Cognee implements scalable, modular ECL (Extract, Cognify, Load) pipelines that allow you to interconnect and retrieve past conversations, documents, and audio transcriptions while reducing hallucinations, developer effort, and cost.

Cognee merges graph and vector databases to uncover hidden relationships and new patterns in your data. You can automatically model, load and retrieve entities and objects representing your business domain and analyze their relationships, uncovering insights that neither vector stores nor graph stores alone can provide.

Try it in a Google Colab notebook or have a look at the documentation.

If you have questions, join cognee Discord community.

Have you seen cognee's starter repo? Check it out!

See detail on available retrievers here.

**Examples**:

```bash
pip install langchain-cognee
```

---

## Cohere | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/cohere/

**Contents**:
- Cohere
- Installation and Setup​
- Cohere langchain integrations​
- Quick copy examples​
  - Chat​
  - LLM​
  - Tool calling​
  - ReAct Agent​

Cohere is a Canadian startup that provides natural language processing models that help companies improve human-machine interactions.

Get a Cohere api key and set it as an environment variable (COHERE_API_KEY)

Usage of the Cohere chat model

Usage of the Cohere (legacy) LLM model

Tool calling with Cohere LLM can be done by binding the necessary tools to the llm as seen above. An alternative, is to support multi hop tool calling with the ReAct agent as seen below.

The agent is based on the paper ReAct: Synergizing Reasoning and Acting in Language Models.

The ReAct agent can be used to call multiple tools in sequence.

Usage of the Cohere RAG Retriever

Usage of the Cohere Text Embeddings model

Usage of the Cohere Reranker

**Examples**:

```bash
pip install langchain-cohere
```

```python
from langchain_cohere import ChatCoherefrom langchain_core.messages import HumanMessagechat = ChatCohere()messages = [HumanMessage(content="knock knock")]print(chat.invoke(messages))
```

```python
from langchain_cohere.llms import Coherellm = Cohere()print(llm.invoke("Come up with a pet name"))
```

---

## Cohere | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/cohere/

**Contents**:
- Cohere
- Setup​
- Usage​
- Chaining​
- Tool calling​
- Related​

This notebook covers how to get started with Cohere chat models.

Head to the API reference for detailed documentation of all attributes and methods.

The integration lives in the langchain-cohere package. We can install these with:

We'll also need to get a Cohere API key and set the COHERE_API_KEY environment variable:

It's also helpful (but not needed) to set up LangSmith for best-in-class observability

ChatCohere supports all ChatModel functionality:

You can also easily combine with a prompt template for easy structuring of user input. We can do this using LCEL

Cohere supports tool calling functionalities!

**Examples**:

```bash
pip install -U langchain-cohere
```

```python
import getpassimport osos.environ["COHERE_API_KEY"] = getpass.getpass()
```

```python
# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

---

## Components | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/components/

**Contents**:
- Components
- 🗃️ Chat models
- 🗃️ Retrievers
- 🗃️ Tools/Toolkits
- 🗃️ Document loaders
- 🗃️ Vector stores
- 🗃️ Embedding models
- 🗃️ Other

---

## Contextual AI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/contextual/

**Contents**:
- Contextual AI
- Grounded Language Model (GLM)​
- Instruction-Following Reranker​
- Using Contextual AI with LangChain​
  - Grounded Language Model​
  - Instruction-Following Reranker​

Contextual AI provides state-of-the-art RAG components designed specifically for accurate and reliable enterprise AI applications. Our LangChain integration exposes standalone API endpoints for our specialized models:

Grounded Language Model (GLM): The world's most grounded language model, engineered to minimize hallucinations by prioritizing faithfulness to retrieved knowledge. GLM delivers exceptional factual accuracy with inline attributions, making it ideal for enterprise RAG and agentic applications where reliability is critical.

Instruction-Following Reranker: The first reranker that follows custom instructions to intelligently prioritize documents based on specific criteria like recency, source, or document type. Outperforming competitors on industry benchmarks, our reranker resolves conflicting information challenges in enterprise knowledge bases.

Founded by the inventors of RAG technology, Contextual AI's specialized components help innovative teams accelerate the development of production-ready RAG agents that deliver responses with exceptional accuracy.

The Grounded Language Model (GLM) is engineered specifically to minimize hallucinations in enterprise RAG and agentic applications. The GLM delivers:

GLM serves as a drop-in replacement for general-purpose LLMs in RAG pipelines, dramatically improving reliability for mission-critical enterprise applications.

The world's first Instruction-Following Reranker revolutionizes document ranking with unprecedented control and accuracy. Key capabilities include:

The reranker excels at handling enterprise knowledge bases with potentially contradictory information, allowing you to specify exactly which sources should take precedence in various scenarios.

This integration allows you to easily incorporate Contextual AI's GLM and Instruction-Following Reranker into your LangChain workflows. The GLM ensures your applications deliver strictly grounded responses, while the reranker significantly improves retrieval 

*[Content truncated - see full docs]*

**Examples**:

```python
# Integrating the Grounded Language Modelimport getpassimport osfrom langchain_contextual import ChatContextual# Set credentialsif not os.getenv("CONTEXTUAL_AI_API_KEY"):    os.environ["CONTEXTUAL_AI_API_KEY"] = getpass.getpass(        "Enter your Contextual API key: "    )# initialize Contextual llmllm = ChatContextual(    model="v1",    api_key="",)# include a system prompt (optional)system_prompt = "You are a helpful assistant that uses all of the provided knowledge to answer the user's query
...
```

```output
According to the information available, there are two types of cats in the world:1. Good cats2. Best cats
```

```python
import getpassimport osfrom langchain_contextual import ContextualRerankif not os.getenv("CONTEXTUAL_AI_API_KEY"):    os.environ["CONTEXTUAL_AI_API_KEY"] = getpass.getpass(        "Enter your Contextual API key: "    )api_key = ""model = "ctxl-rerank-en-v1-instruct"compressor = ContextualRerank(    model=model,    api_key=api_key,)from langchain_core.documents import Documentquery = "What is the current enterprise pricing for the RTX 5090 GPU for bulk orders?"instruction = "Prioritize internal s
...
```

---

## Contribute integrations | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/contributing/how_to/integrations/

**Contents**:
- Contribute integrations
- Why contribute an integration to LangChain?​
- Components to integrate​
- How to contribute an integration​
- Co-marketing​
- Further reading​

Integrations are a core component of LangChain. LangChain provides standard interfaces for several different components (language models, vector stores, etc) that are crucial when building LLM applications.

See the Conceptual Guide for an overview of all components supported in LangChain

While any component can be integrated into LangChain, there are specific types of integrations we encourage more:

In order to contribute an integration, you should follow these steps:

With over 20 million monthly downloads, LangChain has a large audience of developers building LLM applications. Beyond just listing integrations, we aim to highlight high-quality, educational examples that inspire developers and advance the ecosystem.

While we occasionally share integrations, we prioritize content that provides meaningful insights and best practices. Our main social channels are Twitter and LinkedIn, where we highlight the best examples.

Here are some heuristics for types of content we are excited to promote:

To get started, let's learn how to implement an integration package for LangChain.

---

## Couchbase | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/couchbase/

**Contents**:
- Couchbase
- Installation and Setup​
- Vector Store​
- Document loader​
- LLM Caches​
  - CouchbaseCache​
  - CouchbaseSemanticCache​
- Chat Message History​

Couchbase is an award-winning distributed NoSQL cloud database that delivers unmatched versatility, performance, scalability, and financial value for all of your cloud, mobile, AI, and edge computing applications.

We have to install the langchain-couchbase package.

API Reference: CouchbaseSearchVectorStore

Use Couchbase as a cache for prompts and responses.

To import this cache:

To use this cache with your LLMs:

API Reference: CouchbaseCache

Semantic caching allows users to retrieve cached prompts based on the semantic similarity between the user input and previously cached inputs. Under the hood it uses Couchbase as both a cache and a vectorstore. The CouchbaseSemanticCache needs a Search Index defined to work. Please look at the usage example on how to set up the index.

To import this cache:

To use this cache with your LLMs:

API Reference: CouchbaseSemanticCache

Use Couchbase as the storage for your chat messages.

To use the chat message history in your applications:

API Reference: CouchbaseChatMessageHistory

**Examples**:

```bash
pip install langchain-couchbase
```

```python
from langchain_couchbase import CouchbaseSearchVectorStoreimport getpass# Constants for the connectionCOUCHBASE_CONNECTION_STRING = getpass.getpass(    "Enter the connection string for the Couchbase cluster: ")DB_USERNAME = getpass.getpass("Enter the username for the Couchbase cluster: ")DB_PASSWORD = getpass.getpass("Enter the password for the Couchbase cluster: ")# Create Couchbase connection objectfrom datetime import timedeltafrom couchbase.auth import PasswordAuthenticatorfrom couchbase.clu
...
```

```python
from langchain_community.document_loaders.couchbase import CouchbaseLoaderconnection_string = "couchbase://localhost"  # valid Couchbase connection stringdb_username = (    "Administrator"  # valid database user with read access to the bucket being queried)db_password = "Password"  # password for the database user# query is a valid SQL++ queryquery = """    SELECT h.* FROM `travel-sample`.inventory.hotel h        WHERE h.country = 'United States'        LIMIT 1        """loader = CouchbaseLoader
...
```

---

## CrateDB | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/cratedb/

**Contents**:
- CrateDB
- Installation and Setup​
  - Setup CrateDB​
    - Start CrateDB on your local machine​
    - Deploy cluster on CrateDB Cloud​
  - Install Client​
- Documentation​
- Features​

CrateDB is a distributed and scalable SQL database for storing and analyzing massive amounts of data in near real-time, even with complex queries. It is PostgreSQL-compatible, based on Lucene, and inheriting from Elasticsearch.

There are two ways to get started with CrateDB quickly. Alternatively, choose other CrateDB installation options.

Example: Run a single-node CrateDB instance with security disabled, using Docker or Podman. This is not recommended for production use.

CrateDB Cloud is a managed CrateDB service. Sign up for a free trial.

Install the most recent version of the langchain-cratedb package and a few others that are needed for this tutorial.

For a more detailed walkthrough of the CrateDB wrapper, see using LangChain with CrateDB. See also all features of CrateDB to learn about other functionality provided by CrateDB.

The CrateDB adapter for LangChain provides APIs to use CrateDB as vector store, document loader, and storage for chat messages.

Use the CrateDB vector store functionality around FLOAT_VECTOR and KNN_MATCH for similarity search and other purposes. See also CrateDBVectorStore Tutorial.

Make sure you've configured a valid OpenAI API key.

Load load documents from a CrateDB database table, using the document loader CrateDBLoader, which is based on SQLAlchemy. See also CrateDBLoader Tutorial.

To use the document loader in your applications:

Use CrateDB as the storage for your chat messages. See also CrateDBChatMessageHistory Tutorial.

To use the chat message history in your applications:

The standard / full cache avoids invoking the LLM when the supplied prompt is exactly the same as one encountered already. See also CrateDBCache Example.

To use the full cache in your applications:

The semantic cache allows users to retrieve cached prompts based on semantic similarity between the user input and previously cached inputs. It also avoids invoking the LLM when not needed. See also CrateDBSemanticCache Example.

To use the semantic ca

*[Content truncated - see full docs]*

**Examples**:

```bash
docker run --name=cratedb --rm \  --publish=4200:4200 --publish=5432:5432 --env=CRATE_HEAP_SIZE=2g \  crate:latest -Cdiscovery.type=single-node
```

```bash
pip install --upgrade langchain-cratedb langchain-openai unstructured
```

```bash
export OPENAI_API_KEY=sk-XJZ...
```

---

## Dappier | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/dappier/

**Contents**:
- Dappier
- Installation and Setup​
- Chat models​
- Retriever​
- Tool​

Dappier connects any LLM or your Agentic AI to real-time, rights-cleared, proprietary data from trusted sources, making your AI an expert in anything. Our specialized models include Real-Time Web Search, News, Sports, Financial Stock Market Data, Crypto Data, and exclusive content from premium publishers. Explore a wide range of data models in our marketplace at marketplace.dappier.com.

Dappier delivers enriched, prompt-ready, and contextually relevant data strings, optimized for seamless integration with LangChain. Whether you're building conversational AI, recommendation engines, or intelligent search, Dappier's LLM-agnostic RAG models ensure your AI has access to verified, up-to-date data—without the complexity of building and managing your own retrieval pipeline.

Install langchain-dappier and set environment variable DAPPIER_API_KEY.

We also need to set our Dappier API credentials, which can be generated at the Dappier site..

We can find the supported data models by heading over to the Dappier marketplace.

**Examples**:

```bash
pip install -U langchain-dappierexport DAPPIER_API_KEY="your-api-key"
```

```python
from langchain_community.chat_models import ChatDappierAI
```

```python
from langchain_dappier import DappierRetriever
```

---

## Databricks | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/databricks/

**Contents**:
- Databricks
- Installation​
- Chat Model​
- LLM​
- Embeddings​
- Vector Search​
- MLflow Integration​
- SQLDatabase​

Databricks Intelligence Platform is the world's first data intelligence platform powered by generative AI. Infuse AI into every facet of your business.

Databricks embraces the LangChain ecosystem in various ways:

First-party Databricks integrations are now available in the databricks-langchain partner package.

The legacy langchain-databricks partner package is still available but will be soon deprecated.

ChatDatabricks is a Chat Model class to access chat endpoints hosted on Databricks, including state-of-the-art models such as Llama3, Mixtral, and DBRX, as well as your own fine-tuned models.

See the usage example for more guidance on how to use it within your LangChain application.

Databricks is an LLM class to access completion endpoints hosted on Databricks.

Text completion models have been deprecated and the latest and most popular models are chat completion models. Use ChatDatabricks chat model instead to use those models and advanced features such as tool calling.

See the usage example for more guidance on how to use it within your LangChain application.

DatabricksEmbeddings is an Embeddings class to access text-embedding endpoints hosted on Databricks, including state-of-the-art models such as BGE, as well as your own fine-tuned models.

See the usage example for more guidance on how to use it within your LangChain application.

Databricks Vector Search is a serverless similarity search engine that allows you to store a vector representation of your data, including metadata, in a vector database. With Vector Search, you can create auto-updating vector search indexes from Delta tables managed by Unity Catalog and query them with a simple API to return the most similar vectors.

See the usage example for how to set up vector indices and integrate them with LangChain.

In the context of LangChain integration, MLflow provides the following capabilities:

See MLflow LangChain Integration to learn about the full capabilities of using MLflow with LangChain 

*[Content truncated - see full docs]*

**Examples**:

```text
pip install databricks-langchain
```

```text
from databricks_langchain import ChatDatabrickschat_model = ChatDatabricks(endpoint="databricks-meta-llama-3-70b-instruct")
```

```text
from langchain_community.llm.databricks import Databricksllm = Databricks(endpoint="your-completion-endpoint")
```

---

## DeepSeek | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/deepseek/

**Contents**:
- DeepSeek

DeepSeek is a Chinese artificial intelligence company that develops LLMs.

**Examples**:

```python
from langchain_deepseek import ChatDeepSeek
```

---

## Deeplake | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/deeplake/

**Contents**:
- Deeplake
- Installation and Setup​
- Vector stores​

Deeplake is a database optimized for AI and deep learning applications.

See detail on available vector stores here.

**Examples**:

```bash
pip install langchain-deeplake
```

---

## Dell | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/dell/

**Contents**:
- Dell
- PowerScale​
  - Installation and Setup​
  - Document loaders​

Dell is a global technology company that provides a range of hardware, software, and services, including AI solutions. Their AI portfolio includes purpose-built infrastructure for AI workloads, including Dell PowerScale storage systems optimized for AI data management.

Dell PowerScale is an enterprise scale out storage system that hosts industry leading OneFS filesystem that can be hosted on-prem or deployed in the cloud.

See detail on available loaders here.

**Examples**:

```bash
pip install powerscale-rag-connector
```

---

## DigitalOcean Gradient | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/gradientai/

**Contents**:
- DigitalOcean Gradient
- Setup​
  - Credentials​
  - Installation​
- Instantiation​
- Invocation​
- Chaining​

This will help you getting started with DigitalOcean Gradient chat models.

langchain-gradient uses DigitalOcean's Gradient™ AI Platform.

Create an account on DigitalOcean, acquire a DIGITALOCEAN_INFERENCE_KEY API key from the Gradient Platform, and install the langchain-gradient integration package.

Head to DigitalOcean Gradient

Once you've done this set the DIGITALOCEAN_INFERENCE_KEY environment variable:

The LangChain Gradient integration is in the langchain-gradient package:

**Examples**:

```python
import osos.environ["DIGITALOCEAN_INFERENCE_KEY"] = "your-api-key"
```

```bash
pip install -qU langchain-gradient
```

```python
from langchain_gradient import ChatGradientllm = ChatGradient(    model="llama3.3-70b-instruct",    api_key=os.environ.get("DIGITALOCEAN_INFERENCE_KEY"))
```

---

## Discord | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/discord-shikenso/

**Contents**:
- Discord
- Installation and Setup​
- Tools​
- Toolkit​
- Future Integrations​

Discord is an instant messaging, voice, and video communication platform widely used by communities of all types.

Install the langchain-discord-shikenso package:

You must provide a bot token via environment variable so the tools can authenticate with the Discord API:

If DISCORD_BOT_TOKEN is not set, the tools will raise a ValueError when instantiated.

Below is a snippet showing how you can read and send messages in Discord. For more details, see the documentation for Discord tools.

DiscordToolkit groups multiple Discord-related tools into a single interface. For a usage example, see the Discord toolkit docs.

Additional integrations (e.g., document loaders, chat loaders) could be added for Discord. Check the Discord Developer Docs for more information, and watch for updates or advanced usage examples in the langchain_discord GitHub repo.

**Examples**:

```bash
pip install langchain-discord-shikenso
```

```bash
export DISCORD_BOT_TOKEN="your-discord-bot-token"
```

```python
from langchain_discord.tools.discord_read_messages import DiscordReadMessagesfrom langchain_discord.tools.discord_send_messages import DiscordSendMessage# Create tool instancesread_tool = DiscordReadMessages()send_tool = DiscordSendMessage()# Example: Read the last 3 messages from channel 1234567890read_result = read_tool({"channel_id": "1234567890", "limit": 3})print(read_result)# Example: Send a message to channel 1234567890send_result = send_tool({"channel_id": "1234567890", "message": "Hello
...
```

---

## Docling | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/docling/

**Contents**:
- Docling
- Installation and Setup​
- Document Loader​
- Additional Resources​

Docling parses PDF, DOCX, PPTX, HTML, and other formats into a rich unified representation including document layout, tables etc., making them ready for generative AI workflows like RAG.

This integration provides Docling's capabilities via the DoclingLoader document loader.

Simply install langchain-docling from your package manager, e.g. pip:

The DoclingLoader class in langchain-docling seamlessly integrates Docling into LangChain, enabling you to:

Basic usage looks as follows:

For end-to-end usage check out this example.

**Examples**:

```shell
pip install langchain-docling
```

```python
from langchain_docling import DoclingLoaderFILE_PATH = ["https://arxiv.org/pdf/2408.09869"]  # Docling Technical Reportloader = DoclingLoader(file_path=FILE_PATH)docs = loader.load()
```

---

## Document loaders | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/document_loaders/

**Contents**:
- Document loaders
- Integrations​
- Interface​
- Related resources​

Document loaders are designed to load document objects. LangChain has hundreds of integrations with various data sources to load data from: Slack, Notion, Google Drive, etc.

You can find available integrations on the Document loaders integrations page.

Documents loaders implement the BaseLoader interface.

Each DocumentLoader has its own specific parameters, but they can all be invoked in the same way with the .load method or .lazy_load.

Here's a simple example:

When working with large datasets, you can use the .lazy_load method:

Please see the following resources for more information:

**Examples**:

```python
from langchain_community.document_loaders.csv_loader import CSVLoaderloader = CSVLoader(    ...  # <-- Integration specific parameters here)data = loader.load()
```

```python
for document in loader.lazy_load():    print(document)
```

---

## Elasticsearch | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/elasticsearch/

**Contents**:
- Elasticsearch
- Installation and Setup​
  - Setup Elasticsearch​
    - Install Elasticsearch on your local machine via Docker​
    - Deploy Elasticsearch on Elastic Cloud​
  - Install Client​
- Embedding models​
- Vector store​

Elasticsearch is a distributed, RESTful search and analytics engine. It provides a distributed, multi-tenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.

There are two ways to get started with Elasticsearch:

Example: Run a single-node Elasticsearch instance with security disabled. This is not recommended for production use.

Elastic Cloud is a managed Elasticsearch service. Signup for a free trial.

The ElasticsearchRetriever enables flexible access to all Elasticsearch features through the Query DSL.

It is a chain for interacting with Elasticsearch Database.

**Examples**:

```bash
docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.security.http.ssl.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.9.0
```

```bash
pip install elasticsearchpip install langchain-elasticsearch
```

```python
from langchain_elasticsearch import ElasticsearchEmbeddings
```

---

## Evaluation | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/evaluation/

**Contents**:
- Evaluation

Evaluation is the process of assessing the performance and effectiveness of your LLM-powered applications. It involves testing the model's responses against a set of predefined criteria or benchmarks to ensure it meets the desired quality standards and fulfills the intended purpose. This process is vital for building reliable applications.

LangSmith helps with this process in a few ways:

To learn more, check out this LangSmith guide.

---

## Exa | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/exa_search/

**Contents**:
- Exa
- Installation and Setup​
- Retriever​
- Tools​
  - ExaFindSimilarResults​
  - ExaSearchResults​

Exa is a knowledge API for AI and developers.

Exa integration exists in its own partner package. You can install it with:

In order to use the package, you will also need to set the EXA_API_KEY environment variable to your Exa API key.

You can use the ExaSearchRetriever in a standard retrieval pipeline. You can import it as follows.

You can use Exa as an agent tool as described in the Exa tool calling docs.

A tool that queries the Metaphor Search API and gets back JSON.

**Examples**:

```python
%pip install -qU langchain-exa
```

```python
from langchain_exa import ExaSearchRetriever
```

```python
from langchain_exa.tools import ExaFindSimilarResults
```

---

## Example selectors | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/example_selectors/

**Contents**:
- Example selectors
- Overview​
- Related resources​

One common prompting technique for achieving better performance is to include examples as part of the prompt. This is known as few-shot prompting.

This gives the language model concrete examples of how it should behave. Sometimes these examples are hardcoded into the prompt, but for more advanced situations it may be nice to dynamically select them.

Example Selectors are classes responsible for selecting and then formatting examples into prompts.

---

## FMP Data (Financial Data Prep) | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/fmp-data/

**Contents**:
- FMP Data (Financial Data Prep)
- Installation and Setup​
- Tools​

FMP-Data is a python package for connecting to Financial Data Prep API. It simplifies how you can access production quality data.

Get an FMP Data API key by visiting this page. and set it as an environment variable (FMP_API_KEY).

Then, install langchain-fmp-data.

**Examples**:

```python
from langchain_fmp_data import FMPDataTool, FMPDataToolkit
```

---

## FalkorDB | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/falkordb/

**Contents**:
- FalkorDB
- Installation and Setup​
- VectorStore​
- Memory​

Get started with FalkorDB by visiting their website.

The FalkorDB vector index is used as a vectorstore, whether for semantic search or example selection.

**Examples**:

```python
from langchain_community.vectorstores.falkordb_vector import FalkorDBVector
```

```python
from langchain_falkordb.vectorstore import FalkorDBVector
```

```python
from langchain_falkordb.message_history import (    FalkorDBChatMessageHistory,)
```

---

## Featherless AI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/featherless-ai/

**Contents**:
- Featherless AI
- Installation and Setup
- Model catalog

Featherless AI is a serverless AI inference platform that offers access to over 4300+ open-source models. Our goal is to make all AI models available for serverless inference. We provide inference via API to a continually expanding library of open-weight models.

pip install langchain-featherless-ai

Visit our model catalog for an overview of all our models: https://featherless.ai/models

---

## Few-shot prompting | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/few_shot_prompting/

**Contents**:
- Few-shot prompting
- Overview​
- 1. Generating examples​
- 2. Number of examples​
- 3. Selecting examples​
- 4. Formatting examples​

One of the most effective ways to improve model performance is to give a model examples of what you want it to do. The technique of adding example inputs and expected outputs to a model prompt is known as "few-shot prompting". The technique is based on the Language Models are Few-Shot Learners paper. There are a few things to think about when doing few-shot prompting:

Here are the considerations for each.

The first and most important step of few-shot prompting is coming up with a good dataset of examples. Good examples should be relevant at runtime, clear, informative, and provide information that was not already known to the model.

At a high-level, the basic ways to generate examples are:

Which approach is best depends on your task. For tasks where a small number of core principles need to be understood really well, it can be valuable hand-craft a few really good examples. For tasks where the space of correct behaviors is broader and more nuanced, it can be useful to generate many examples in a more automated fashion so that there's a higher likelihood of there being some highly relevant examples for any runtime input.

Single-turn v.s. multi-turn examples

Another dimension to think about when generating examples is what the example is actually showing.

The simplest types of examples just have a user input and an expected model output. These are single-turn examples.

One more complex type of example is where the example is an entire conversation, usually in which a model initially responds incorrectly and a user then tells the model how to correct its answer. This is called a multi-turn example. Multi-turn examples can be useful for more nuanced tasks where it's useful to show common errors and spell out exactly why they're wrong and what should be done instead.

Once we have a dataset of examples, we need to think about how many examples should be in each prompt. The key tradeoff is that more examples generally improve performance, but larger prompts increa

*[Content truncated - see full docs]*

---

## Fireworks AI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/fireworks/

**Contents**:
- Fireworks AI
- Installation and setup​
  - Authentication​
- Chat models​
- LLMs​
- Embedding models​

Fireworks AI is a generative AI inference platform to run and customize models with industry-leading speed and production-readiness.

Install the Fireworks integration package.

Get a Fireworks API key by signing up at fireworks.ai.

Authenticate by setting the FIREWORKS_API_KEY environment variable.

There are two ways to authenticate using your Fireworks API key:

Setting the FIREWORKS_API_KEY environment variable.

Setting api_key field in the Fireworks LLM module.

**Examples**:

```bash
pip install langchain-fireworks
```

```python
os.environ["FIREWORKS_API_KEY"] = "<KEY>"
```

```python
llm = Fireworks(api_key="<KEY>")
```

---

## Gel | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/gel/

**Contents**:
- Gel
- Installation​
- Setup​
- Usage​

Gel is a powerful data platform built on top of PostgreSQL.

Note: this is the minimal setup. Feel free to add as many types, properties and links as you want! Learn more about taking advantage of Gel's schema by reading the docs.

See the full usage example here.

**Examples**:

```bash
pip install langchain-gel
```

```gel
using extension pgvector;module default {    scalar type EmbeddingVector extending ext::pgvector::vector<1536>;    type Record {        required collection: str;        text: str;        embedding: EmbeddingVector;        external_id: str {            constraint exclusive;        };        metadata: json;        index ext::pgvector::hnsw_cosine(m := 16, ef_construction := 128)            on (.embedding)    }}
```

```python
from langchain_gel import GelVectorStorevector_store = GelVectorStore(    embeddings=embeddings,)
```

---

## Goodfire | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/goodfire/

**Contents**:
- Goodfire
- Installation and Setup​
- Chat models​

Goodfire is a research lab focused on AI safety and interpretability.

See detail on available chat models here.

**Examples**:

```bash
pip install langchain-goodfire
```

---

## Google | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/google/

**Contents**:
- Google
- Google Generative AI (Gemini API & AI Studio)​
  - Chat Models​
  - Embedding Models​
  - LLMs​
- Google Cloud​
  - Chat Models​
    - Vertex AI​

All functionality related to Google Cloud, Google Gemini and other Google products.

See Google's guide on migrating from the Gemini API to Vertex AI for more details on the differences.

Integration packages for Gemini models and the Vertex AI platform are maintained in the langchain-google repository. You can find a host of LangChain integrations with other Google APIs and services in the googleapis Github organization and the langchain-google-community package.

Access Google Gemini models directly using the Gemini API, best suited for rapid development and experimentation. Gemini models are available in Google AI Studio.

Start for free and get your API key from Google AI Studio.

Use the ChatGoogleGenerativeAI class to interact with Gemini models. See details in this guide.

The image_url can be a public URL, a GCS URI (gs://...), a local file path, a base64 encoded image string (data:image/png;base64,...), or a PIL Image object.

Generate text embeddings using models like gemini-embedding-001 with the GoogleGenerativeAIEmbeddings class.

Access the same Gemini models using the (legacy) LLM interface with the GoogleGenerativeAI class.

Access Gemini models, Vertex AI Model Garden and other Google Cloud services via Vertex AI and specific cloud integrations.

Vertex AI models require the langchain-google-vertexai package. Other services might require additional packages like langchain-google-community, langchain-google-cloud-sql-pg, etc.

Google Cloud integrations typically use Application Default Credentials (ADC). Refer to the Google Cloud authentication documentation for setup instructions (e.g., using gcloud auth application-default login).

Access chat models like Gemini via the Vertex AI platform.

Local Gemma model loaded from HuggingFace. Requires langchain-google-vertexai.

Local Gemma model loaded from Kaggle. Requires langchain-google-vertexai.

Requires langchain-google-vertexai.

Implementation of the Image Captioning model as a chat. Requires langc

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install -U langchain-google-genai
```

```bash
export GOOGLE_API_KEY="YOUR_API_KEY"
```

```python
from langchain_google_genai import ChatGoogleGenerativeAIfrom langchain_core.messages import HumanMessagellm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")# Simple text invocationresult = llm.invoke("Sing a ballad of LangChain.")print(result.content)# Multimodal invocation with gemini-pro-visionmessage = HumanMessage(    content=[        {            "type": "text",            "text": "What's in this image?",        },        {"type": "image_url", "image_url": "https://picsum.photos/seed/pic
...
```

---

## Graph RAG | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/graph_rag/

**Contents**:
- Graph RAG
- Overview​
- Installation and setup​
- Retrievers​

Graph RAG provides a retriever interface that combines unstructured similarity search on vectors with structured traversal of metadata properties. This enables graph-based retrieval over existing vector stores.

For more information, see the Graph RAG Integration Guide.

**Examples**:

```bash
pip install langchain-graph-retriever
```

```python
from langchain_graph_retriever import GraphRetriever
```

---

## GreenNode | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/greennode/

**Contents**:
- GreenNode
- Installation and Setup​
  - API Key​
- Chat models​
- Embedding models​
- Rerank​

GreenNode is a global AI solutions provider and a NVIDIA Preferred Partner, delivering full-stack AI capabilities—from infrastructure to application—for enterprises across the US, MENA, and APAC regions. Operating on world-class infrastructure (LEED Gold, TIA‑942, Uptime Tier III), GreenNode empowers enterprises, startups, and researchers with a comprehensive suite of AI services:

The GreenNode integration can be installed via pip:

To use GreenNode Serverless AI, you'll need an API key which you can obtain from GreenNode Serverless AI. The API key can be passed as an initialization parameter api_key or set as the environment variable GREENNODE_API_KEY.

Usage of the GreenNode Chat Model

Usage of the GreenNode Embedding Model

Usage of the GreenNode Rerank Model

**Examples**:

```python
%pip install -qU langchain-greennode
```

```output
Note: you may need to restart the kernel to use updated packages.
```

```python
import getpassimport osif not os.getenv("GREENNODE_API_KEY"):    os.environ["GREENNODE_API_KEY"] = getpass.getpass("Enter your GreenNode API key: ")
```

---

## Groq | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/groq/

**Contents**:
- Groq
- Installation and Setup​
- Chat models​

Groq developed the world's first Language Processing Unit™, or LPU. The Groq LPU has a deterministic, single core streaming architecture that sets the standard for GenAI inference speed with predictable and repeatable performance for any given workload.

Beyond the architecture, Groq software is designed to empower developers like you with the tools you need to create innovative, powerful AI applications.

With Groq as your engine, you can:

Install the integration package:

Request an API key and set it as an environment variable:

**Examples**:

```bash
pip install langchain-groq
```

```bash
export GROQ_API_KEY=gsk_...
```

```python
from langchain_groq import ChatGroq
```

---

## How to create a custom chat model class | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/how_to/custom_chat_model/

**Contents**:
- How to create a custom chat model class
- Inputs and outputs​
  - Messages​
  - Streaming Variant​
- Base Chat Model​
  - Implementation​
  - Let's test it 🧪​
- Contributing​

This guide assumes familiarity with the following concepts:

In this guide, we'll learn how to create a custom chat model using LangChain abstractions.

Wrapping your LLM with the standard BaseChatModel interface allow you to use your LLM in existing LangChain programs with minimal code modifications!

As a bonus, your LLM will automatically become a LangChain Runnable and will benefit from some optimizations out of the box (e.g., batch via a threadpool), async support, the astream_events API, etc.

First, we need to talk about messages, which are the inputs and outputs of chat models.

Chat models take messages as inputs and return a message as output.

LangChain has a few built-in message types:

ToolMessage and FunctionMessage closely follow OpenAI's function and tool roles.

This is a rapidly developing field and as more models add function calling capabilities. Expect that there will be additions to this schema.

All the chat messages have a streaming variant that contains Chunk in the name.

These chunks are used when streaming output from chat models, and they all define an additive property!

Let's implement a chat model that echoes back the first n characters of the last message in the prompt!

To do so, we will inherit from BaseChatModel and we'll need to implement the following:

The _astream implementation uses run_in_executor to launch the sync _stream in a separate thread if _stream is implemented, otherwise it fallsback to use _agenerate.

You can use this trick if you want to reuse the _stream implementation, but if you're able to implement code that's natively async that's a better solution since that code will run with less overhead.

The chat model will implement the standard Runnable interface of LangChain which many of the LangChain abstractions support!

Please see the implementation of _astream in the model! If you do not implement it, then no output will stream.!

Let's try to use the astream events API which will also help double check that 

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.messages import (    AIMessage,    BaseMessage,    FunctionMessage,    HumanMessage,    SystemMessage,    ToolMessage,)
```

```python
from langchain_core.messages import (    AIMessageChunk,    FunctionMessageChunk,    HumanMessageChunk,    SystemMessageChunk,    ToolMessageChunk,)
```

```python
AIMessageChunk(content="Hello") + AIMessageChunk(content=" World!")
```

---

## How to create and query vector stores | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/how_to/vectorstores/

**Contents**:
- How to create and query vector stores
- Get started​
- Similarity search​
  - Similarity search by vector​
- Async Operations​

Head to Integrations for documentation on built-in integrations with 3rd-party vector stores.

One of the most common ways to store and search over unstructured data is to embed it and store the resulting embedding vectors, and then at query time to embed the unstructured query and retrieve the embedding vectors that are 'most similar' to the embedded query. A vector store takes care of storing embedded data and performing vector search for you.

This guide showcases basic functionality related to vector stores. A key part of working with vector stores is creating the vector to put in them, which is usually created via embeddings. Therefore, it is recommended that you familiarize yourself with the text embedding model interfaces before diving into this.

Before using the vectorstore at all, we need to load some data and initialize an embedding model.

We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.

There are many great vector store options, here are a few that are free, open-source, and run entirely on your local machine. Review all integrations for many great hosted offerings.

This walkthrough uses the chroma vector database, which runs on your local machine as a library.

This walkthrough uses the FAISS vector database, which makes use of the Facebook AI Similarity Search (FAISS) library.

This notebook shows how to use functionality related to the LanceDB vector database based on the Lance data format.

All vectorstores expose a similarity_search method. This will take incoming documents, create an embedding of them, and then find all documents with the most similar embedding.

It is also possible to do a search for documents similar to a given embedding vector using similarity_search_by_vector which accepts an embedding vector as a parameter instead of a string.

Vector stores are usually run as a separate service that requires some IO operations, and therefore they might be called asynchronously. That gives performance benefits as you do

*[Content truncated - see full docs]*

**Examples**:

```python
import osimport getpassos.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
```

```python
from langchain_community.document_loaders import TextLoaderfrom langchain_openai import OpenAIEmbeddingsfrom langchain_text_splitters import CharacterTextSplitter# Load the document, split it into chunks, embed each chunk and load it into the vector store.raw_documents = TextLoader('state_of_the_union.txt').load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)documents = text_splitter.split_documents(raw_documents)
```

```bash
pip install langchain-chroma
```

---

## How to return structured data from a model | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/how_to/structured_output/

**Contents**:
- How to return structured data from a model
- The .with_structured_output() method​
  - Pydantic class​
  - TypedDict or JSON Schema​
  - Choosing between multiple schemas​
    - Using Pydantic​
    - Using TypedDict​
  - Streaming​

This guide assumes familiarity with the following concepts:

It is often useful to have a model return output that matches a specific schema. One common use-case is extracting data from text to insert into a database or use with some other downstream system. This guide covers a few strategies for getting structured outputs from a model.

You can find a list of models that support this method here.

This is the easiest and most reliable way to get structured outputs. with_structured_output() is implemented for models that provide native APIs for structuring outputs, like tool/function calling or JSON mode, and makes use of these capabilities under the hood.

This method takes a schema as input which specifies the names, types, and descriptions of the desired output attributes. The method returns a model-like Runnable, except that instead of outputting strings or messages it outputs objects corresponding to the given schema. The schema can be specified as a TypedDict class, JSON Schema or a Pydantic class. If TypedDict or JSON Schema are used then a dictionary will be returned by the Runnable, and if a Pydantic class is used then a Pydantic object will be returned.

As an example, let's get a model to generate a joke and separate the setup from the punchline:

If we want the model to return a Pydantic object, we just need to pass in the desired Pydantic class. The key advantage of using Pydantic is that the model-generated output will be validated. Pydantic will raise an error if any required fields are missing or if any fields are of the wrong type.

Beyond just the structure of the Pydantic class, the name of the Pydantic class, the docstring, and the names and provided descriptions of parameters are very important. Most of the time with_structured_output is using a model's function/tool calling API, and you can effectively think of all of this information as being added to the model prompt.

If you don't want to use Pydantic, explicitly don't want validation of the

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install -qU "langchain[google-genai]"
```

```python
import getpassimport osif not os.environ.get("GOOGLE_API_KEY"):  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
```

```python
from typing import Optionalfrom pydantic import BaseModel, Field# Pydanticclass Joke(BaseModel):    """Joke to tell user."""    setup: str = Field(description="The setup of the joke")    punchline: str = Field(description="The punchline to the joke")    rating: Optional[int] = Field(        default=None, description="How funny the joke is, from 1 to 10"    )structured_llm = llm.with_structured_output(Joke)structured_llm.invoke("Tell me a joke about cats")
```

---

## Hugging Face | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/huggingface/

**Contents**:
- Hugging Face
- Installation​
- Chat models​
  - ChatHuggingFace​
- LLMs​
  - HuggingFaceEndpoint​
  - HuggingFacePipeline​
- Embedding Models​

All functionality related to Hugging Face Hub and libraries like transformers, sentence transformers, and datasets.

Hugging Face is an AI platform with all major open source models, datasets, MCPs, and demos. It supplies model inference locally and via serverless Inference Providers.

You can use Inference Providers to run open source models like DeepSeek R1 on scalable serverless infrastructure.

Most of the Hugging Face integrations are available in the langchain-huggingface package.

We can use the Hugging Face LLM classes or directly use the ChatHuggingFace class.

We can use the HuggingFaceEndpoint class to run open source models via serverless Inference Providers or via dedicated Inference Endpoints.

We can use the HuggingFacePipeline class to run open source models locally.

We can use the HuggingFaceEmbeddings class to run open source embedding models locally.

We can use the HuggingFaceEndpointEmbeddings class to run open source embedding models via a dedicated Inference Endpoint.

We can use the HuggingFaceInferenceAPIEmbeddings class to run open source embedding models via Inference Providers.

We can use the HuggingFaceInstructEmbeddings class to run open source embedding models locally.

BGE models on the HuggingFace are one of the best open-source embedding models. BGE model is created by the Beijing Academy of Artificial Intelligence (BAAI). BAAI is a private non-profit organization engaged in AI research and development.

Hugging Face Hub is home to over 75,000 datasets in more than 100 languages that can be used for a broad range of tasks across NLP, Computer Vision, and Audio. They used for a diverse range of tasks such as translation, automatic speech recognition, and image classification.

We need to install datasets python package.

Load model information from Hugging Face Hub, including README content.

This loader interfaces with the Hugging Face Models API to fetch and load model metadata and README files. The API allows you to search and f

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install langchain-huggingface
```

```python
from langchain_huggingface import ChatHuggingFace
```

```python
from langchain_huggingface import HuggingFaceEndpoint
```

---

## Hyperbrowser | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/hyperbrowser/

**Contents**:
- Hyperbrowser
- Installation and Setup​
- Available Tools​
  - Browser Agent Tools​
    - Browser Use Tool​
    - OpenAI CUA Tool​
    - Claude Computer Use Tool​
  - Web Scraping Tools​

Hyperbrowser is a platform for running and scaling headless browsers. It lets you launch and manage browser sessions at scale and provides easy to use solutions for any webscraping needs, such as scraping a single page or crawling an entire site.

For more information about Hyperbrowser, please visit the Hyperbrowser website or if you want to check out the docs, you can visit the Hyperbrowser docs.

To get started with langchain-hyperbrowser, you can install the package using pip:

And you should configure credentials by setting the following environment variables:

HYPERBROWSER_API_KEY=<your-api-key>

Make sure to get your API Key from https://app.hyperbrowser.ai/

Hyperbrowser provides two main categories of tools that are particularly useful for:

Hyperbrowser provides a number of Browser Agents tools. Currently we supported

You can see more details here

A general-purpose browser automation tool that can handle various web tasks through natural language instructions.

Leverages OpenAI's Computer Use Agent capabilities for advanced web interactions and information gathering.

Utilizes Anthropic's Claude for sophisticated web browsing and information processing tasks.

Here is a brief description of the Web Scraping Tools available with Hyperbrowser. You can see more details here

The Scrape Tool allows you to extract content from a single webpage in markdown, HTML, or link format.

The Crawl Tool enables you to traverse entire websites, starting from a given URL, with configurable page limits.

The Extract Tool uses AI to pull structured data from web pages based on predefined schemas, making it perfect for data extraction tasks.

The HyperbrowserLoader class in langchain-hyperbrowser can easily be used to load content from any single page or multiple pages as well as crawl an entire site. The content can be loaded as markdown or html.

You can specify the operation to be performed by the loader. The default operation is scrape. For scrape, you can provide a sin

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install langchain-hyperbrowser
```

```python
from langchain_hyperbrowser import HyperbrowserBrowserUseTooltool = HyperbrowserBrowserUseTool()result = tool.run({    "task": "Go to npmjs.com, find the React package, and tell me when it was last updated"})print(result)
```

```python
from langchain_hyperbrowser import HyperbrowserOpenAICUATooltool = HyperbrowserOpenAICUATool()result = tool.run({    "task": "Go to Hacker News and summarize the top 5 posts right now"})print(result)
```

---

## Jenkins | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/jenkins/

**Contents**:
- Jenkins
- Installation and Setup​
- Tools​

Jenkins is an open-source automation platform that enables software teams to streamline their development workflows. It's widely adopted in the DevOps community as a tool for automating the building, testing, and deployment of applications through CI/CD pipelines.

See detail on available tools here.

**Examples**:

```bash
pip install langchain-jenkins
```

---

## Kùzu | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/kuzu/

**Contents**:
- Kùzu
- Installation and Setup​
- Usage​
- Graphs​
- Chains​

Kùzu is an embeddable, scalable, extremely fast graph database. It is permissively licensed with an MIT license, and you can see its source code here.

Key characteristics of Kùzu:

Get started with Kùzu by visiting their documentation.

Install the Python SDK as follows:

**Examples**:

```bash
pip install -U langchain-kuzu
```

```python
from langchain_kuzu.graphs.kuzu_graph import KuzuGraph
```

```python
from langchain_kuzu.chains.graph_qa.kuzu import KuzuQAChain
```

---

## LangChain Expression Language (LCEL) | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/lcel/

**Contents**:
- LangChain Expression Language (LCEL)
- Benefits of LCEL​
- Should I use LCEL?​
- Composition Primitives​
  - RunnableSequence​
  - RunnableParallel​
- Composition Syntax​
  - The | operator​

The LangChain Expression Language (LCEL) takes a declarative approach to building new Runnables from existing Runnables.

This means that you describe what should happen, rather than how it should happen, allowing LangChain to optimize the run-time execution of the chains.

We often refer to a Runnable created using LCEL as a "chain". It's important to remember that a "chain" is Runnable and it implements the full Runnable Interface.

LangChain optimizes the run-time execution of chains built with LCEL in a number of ways:

Other benefits include:

LCEL is an orchestration solution -- it allows LangChain to handle run-time execution of chains in an optimized way.

While we have seen users run chains with hundreds of steps in production, we generally recommend using LCEL for simpler orchestration tasks. When the application requires complex state management, branching, cycles or multiple agents, we recommend that users take advantage of LangGraph.

In LangGraph, users define graphs that specify the application's flow. This allows users to keep using LCEL within individual nodes when LCEL is needed, while making it easy to define complex orchestration logic that is more readable and maintainable.

Here are some guidelines:

LCEL chains are built by composing existing Runnables together. The two main composition primitives are RunnableSequence and RunnableParallel.

Many other composition primitives (e.g., RunnableAssign) can be thought of as variations of these two primitives.

You can find a list of all composition primitives in the LangChain Core API Reference.

RunnableSequence is a composition primitive that allows you "chain" multiple runnables sequentially, with the output of one runnable serving as the input to the next.

Invoking the chain with some input:

corresponds to the following:

runnable1 and runnable2 are placeholders for any Runnable that you want to chain together.

RunnableParallel is a composition primitive that allows you to run multiple runnabl

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.runnables import RunnableSequencechain = RunnableSequence([runnable1, runnable2])
```

```python
final_output = chain.invoke(some_input)
```

```python
output1 = runnable1.invoke(some_input)final_output = runnable2.invoke(output1)
```

---

## LangChain v0.3 | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/versions/v0_3/

**Contents**:
- LangChain v0.3
- What's changed​
- What's new​
- How to update your code​
  - Base packages​
  - Downstream packages​
  - Integration packages​
- Common issues when transitioning to Pydantic 2​

Last updated: 09.16.24

These are the only breaking changes.

The following features have been added during the development of 0.2.x:

If you're using langchain / langchain-community / langchain-core 0.0 or 0.1, we recommend that you first upgrade to 0.2.

If you're using langgraph, upgrade to langgraph>=0.2.20,<0.3. This will work with either 0.2 or 0.3 versions of all the base packages.

Here is a complete list of all packages that have been released and what we recommend upgrading your version constraints to. Any package that now requires langchain-core 0.3 had a minor version bump. Any package that is now compatible with both langchain-core 0.2 and 0.3 had a patch version bump.

You can use the langchain-cli to update deprecated imports automatically. The CLI will handle updating deprecated imports that were introduced in LangChain 0.0.x and LangChain 0.1, as well as updating the langchain_core.pydantic_v1 and langchain.pydantic_v1 imports.

Once you've updated to recent versions of the packages, you may need to address the following issues stemming from the internal switch from Pydantic v1 to Pydantic v2:

Replace any usage of langchain_core.pydantic_v1 or langchain.pydantic_v1 with direct imports from pydantic.

This may require you to make additional updates to your Pydantic code given that there are a number of breaking changes in Pydantic 2. See the Pydantic Migration for how to upgrade your code from Pydantic 1 to 2.

Users using the following APIs:

should ensure that they are passing Pydantic 2 objects to these APIs rather than Pydantic 1 objects (created via the pydantic.v1 namespace of pydantic 2).

While v1 objects may be accepted by some of these APIs, users are advised to use Pydantic 2 objects to avoid future issues.

Any sub-classing from existing LangChain models (e.g., BaseTool, BaseChatModel, LLM) should upgrade to use Pydantic 2 features.

For example, any user code that's relying on Pydantic 1 features (e.g., validator) should be updated to t

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.pydantic_v1 import BaseModel
```

```python
from pydantic import BaseModel
```

```python
from pydantic.v1 import validator, Field # if pydantic 2 is installed# from pydantic import validator, Field # if pydantic 1 is installed# from langchain_core.pydantic_v1 import validator, Field# from langchain.pydantic_v1 import validator, Fieldclass CustomTool(BaseTool): # BaseTool is v1 code    x: int = Field(default=1)    def _run(*args, **kwargs):        return "hello"    @validator('x') # v1 code    @classmethod    def validate_x(cls, x: int) -> int:        return 1
```

---

## LangFair: Use-Case Level LLM Bias and Fairness Assessments | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/langfair/

**Contents**:
- LangFair: Use-Case Level LLM Bias and Fairness Assessments
- ⚡ Quickstart Guide​
  - (Optional) Create a virtual environment for using LangFair​
  - Installing LangFair​
  - Usage Examples​
      - Generate LLM responses​
      - Compute toxicity metrics​
      - Compute stereotype metrics​

LangFair is a comprehensive Python library designed for conducting bias and fairness assessments of large language model (LLM) use cases. The LangFair repository includes a comprehensive framework for choosing bias and fairness metrics, along with demo notebooks and a technical playbook that discusses LLM bias and fairness risks, evaluation metrics, and best practices.

Explore our documentation site for detailed instructions on using LangFair.

We recommend creating a new virtual environment using venv before installing LangFair. To do so, please follow instructions here.

The latest version can be installed from PyPI:

Below are code samples illustrating how to use LangFair to assess bias and fairness risks in text generation and summarization use cases. The below examples assume the user has already defined a list of prompts from their use case, prompts.

To generate responses, we can use LangFair's ResponseGenerator class. First, we must create a langchain LLM object. Below we use ChatVertexAI, but any of LangChain’s LLM classes may be used instead. Note that InMemoryRateLimiter is to used to avoid rate limit errors.

We can use ResponseGenerator.generate_responses to generate 25 responses for each prompt, as is convention for toxicity evaluation.

Toxicity metrics can be computed with ToxicityMetrics. Note that use of torch.device is optional and should be used if GPU is available to speed up toxicity computation.

Stereotype metrics can be computed with StereotypeMetrics.

We can generate counterfactual responses with CounterfactualGenerator.

Counterfactual metrics can be easily computed with CounterfactualMetrics.

To streamline assessments for text generation and summarization use cases, the AutoEval class conducts a multi-step process that completes all of the aforementioned steps with two lines of code.

**Examples**:

```bash
pip install langfair
```

```python
from langchain_google_vertexai import ChatVertexAIfrom langchain_core.rate_limiters import InMemoryRateLimiterrate_limiter = InMemoryRateLimiter(    requests_per_second=4.5, check_every_n_seconds=0.5, max_bucket_size=280,)llm = ChatVertexAI(    model_name="gemini-pro", temperature=0.3, rate_limiter=rate_limiter)
```

```python
from langfair.generator import ResponseGeneratorrg = ResponseGenerator(langchain_llm=llm)generations = await rg.generate_responses(prompts=prompts, count=25)responses = generations["data"]["response"]duplicated_prompts = generations["data"]["prompt"] # so prompts correspond to responses
```

---

## Lindorm | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/lindorm/

**Contents**:
- Lindorm
- Embeddings​
- Rerank​
- Vector Store​
- ByteStore​

Lindorm is a cloud-native multimodal database from Alibaba-Cloud, It supports unified access and integrated processing of various types of data, including wide tables, time-series, text, objects, streams, and spatial data. It is compatible with multiple standard interfaces such as SQL, HBase/Cassandra/S3, TSDB, HDFS, Solr, and Kafka, and seamlessly integrates with third-party ecosystem tools. This makes it suitable for scenarios such as logging, monitoring, billing, advertising, social networking, travel, and risk control. Lindorm is also one of the databases that support Alibaba's core businesses.

To use the AI and vector capabilities of Lindorm, you should get the service and install langchain-lindorm-integration package.

To use the embedding model deployed in Lindorm AI Service, import the LindormAIEmbeddings.

The Lindorm AI Service also supports reranking.

Lindorm also supports vector store.

Use ByteStore from Lindorm

**Examples**:

```python
!pip install -U langchain-lindorm-integration
```

```python
from langchain_lindorm_integration import LindormAIEmbeddings
```

```python
from langchain_lindorm_integration.reranker import LindormAIRerank
```

---

## Linkup | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/linkup/

**Contents**:
- Linkup
- Installation and Setup​
- Retriever​
- Tools​

Linkup provides an API to connect LLMs to the web and the Linkup Premium Partner sources.

To use the Linkup provider, you first need a valid API key, which you can find by signing-up here. You will also need the langchain-linkup package, which you can install using pip:

**Examples**:

```bash
pip install langchain-linkup
```

```python
from langchain_linkup import LinkupSearchRetrieverretriever = LinkupSearchRetriever(    depth="deep",  # "standard" or "deep"    linkup_api_key=None,  # API key can be passed here or set as the LINKUP_API_KEY environment variable)
```

```python
from langchain_linkup import LinkupSearchTooltool = LinkupSearchTool(    depth="deep",  # "standard" or "deep"    output_type="searchResults",  # "searchResults", "sourcedAnswer" or "structured"    linkup_api_key=None,  # API key can be passed here or set as the LINKUP_API_KEY environment variable)
```

---

## LiteLLM | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/litellm/

**Contents**:
- LiteLLM
- Installation and setup​
- Chat Models​
- API reference​

LiteLLM is a library that simplifies calling Anthropic, Azure, Huggingface, Replicate, etc.

See more detail in the guide here.

For detailed documentation of all ChatLiteLLM and ChatLiteLLMRouter features and configurations head to the API reference: https://github.com/Akshay-Dongare/langchain-litellm

**Examples**:

```bash
pip install langchain-litellm
```

```python
from langchain_litellm import ChatLiteLLM
```

```python
from langchain_litellm import ChatLiteLLMRouter
```

---

## Llama.cpp | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/chat/llamacpp

**Contents**:
- Llama.cpp
- Overview​
  - Integration details​
  - Model features​
- Setup​
  - Installation​
- Instantiation​
- Invocation​

llama.cpp python library is a simple Python bindings for @ggerganov llama.cpp.

This package provides:

To get started and use all the features shown below, we recommend using a model that has been fine-tuned for tool-calling.

We will use Hermes-2-Pro-Llama-3-8B-GGUF from NousResearch.

Hermes 2 Pro is an upgraded version of Nous Hermes 2, consisting of an updated and cleaned version of the OpenHermes 2.5 Dataset, as well as a newly introduced Function Calling and JSON Mode dataset developed in-house. This new version of Hermes maintains its excellent general task and conversation capabilities - but also excels at Function Calling

See our guides on local models to go deeper:

The LangChain LlamaCpp integration lives in the langchain-community and llama-cpp-python packages:

Now we can instantiate our model object and generate chat completions:

We can chain our model with a prompt template like so:

Firstly, it works mostly the same as OpenAI Function Calling

OpenAI has a tool calling (we use "tool calling" and "function calling" interchangeably here) API that lets you describe tools and their arguments, and have the model return a JSON object with a tool to invoke and the inputs to that tool. tool-calling is extremely useful for building tool-using chains and agents, and for getting structured outputs from models more generally.

With ChatLlamaCpp.bind_tools, we can easily pass in Pydantic classes, dict schemas, LangChain tools, or even functions as tools to the model. Under the hood, these are converted to an OpenAI tool schema, which looks like:

and passed in every model invocation.

However, it cannot automatically trigger a function/tool, we need to force it by specifying the 'tool choice' parameter. This parameter is typically formatted as described below.

{"type": "function", "function": {"name": <<tool_name>>}}.

For detailed documentation of all ChatLlamaCpp features and configurations, head to the API reference: https://python.langchain.com/api_refere

*[Content truncated - see full docs]*

**Examples**:

```python
%pip install -qU langchain-community llama-cpp-python
```

```python
# Path to your model weightslocal_model = "local/path/to/Hermes-2-Pro-Llama-3-8B-Q8_0.gguf"
```

```python
import multiprocessingfrom langchain_community.chat_models import ChatLlamaCppllm = ChatLlamaCpp(    temperature=0.5,    model_path=local_model,    n_ctx=10000,    n_gpu_layers=8,    n_batch=300,  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.    max_tokens=512,    n_threads=multiprocessing.cpu_count() - 1,    repeat_penalty=1.5,    top_p=0.5,    verbose=True,)
```

---

## LocalAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/localai/

**Contents**:
- LocalAI
- Installation and Setup​
- Embedding models​

LocalAI is the free, Open Source OpenAI alternative. LocalAI act as a drop-in replacement REST API that’s compatible with OpenAI API specifications for local inferencing. It allows you to run LLMs, generate images, audio (and not only) locally or on-prem with consumer grade hardware, supporting multiple model families and architectures.

For proper compatibility, please ensure you are using the openai SDK at version 0.x.

langchain-localai is a 3rd party integration package for LocalAI. It provides a simple way to use LocalAI services in Langchain. The source code is available on Github

We have to install several python packages:

**Examples**:

```bash
pip install tenacity openai
```

```python
from langchain_localai import LocalAIEmbeddings
```

---

## MCP Toolbox | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/toolbox-langchain/

**Contents**:
- MCP Toolbox
- What is it?​
- Installation​
- Tutorial​

The MCP Toolbox in LangChain allows you to equip an agent with a set of tools. When the agent receives a query, it can intelligently select and use the most appropriate tool provided by MCP Toolbox to fulfill the request.

MCP Toolbox is essentially a container for your tools. Think of it as a multi-tool device for your agent; it can hold any tools you create. The agent then decides which specific tool to use based on the user's input.

This is particularly useful when you have an agent that needs to perform a variety of tasks that require different capabilities.

To get started, you'll need to install the necessary package:

For a complete, step-by-step guide on how to create, configure, and use MCP Toolbox with your agents, please refer to our detailed Jupyter notebook tutorial.

➡️ View the full tutorial here.

**Examples**:

```bash
pip install toolbox-langchain
```

---

## MariaDB | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/mariadb/

**Contents**:
- MariaDB
- Installation​
- Setup​
- Wrappers​
  - VectorStore​
  - Usage​

This page covers how to use the MariaDB ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific PGVector wrappers.

on CentOS, RHEL, Rocky Linux

The first step is to have a MariaDB 11.7.1 or later installed.

The docker image is the easiest way to get started.

There exists a wrapper around MariaDB vector databases, allowing you to use it as a vectorstore, whether for semantic search or example selection.

To import this vectorstore:

For a more detailed walkthrough of the MariaDB wrapper, see this notebook

**Examples**:

```bash
sudo apt install libmariadb3 libmariadb-dev
```

```bash
sudo yum install MariaDB-shared MariaDB-devel
```

```python
from langchain_mariadb import MariaDBStore
```

---

## Memgraph | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/memgraph/

**Contents**:
- Memgraph
- Installation and Setup​
- MemgraphQAChain​
- Constructing a Knowledge Graph from unstructured data​
- Memgraph Tools and Toolkit​

Memgraph is a high-performance, in-memory graph database that is optimized for real-time queries and analytics. Get started with Memgraph by visiting their website.

There exists a wrapper around Memgraph graph database that allows you to generate Cypher statements based on the user input and use them to retrieve relevant information from the database.

You can use the integration to construct a knowledge graph from unstructured data.

Memgraph also provides a toolkit that allows you to interact with the Memgraph database. See a usage example.

**Examples**:

```python
from langchain_memgraph.chains.graph_qa import MemgraphQAChainfrom langchain_memgraph.graphs.memgraph import MemgraphLangChain
```

```python
from langchain_memgraph.graphs.memgraph import MemgraphLangChainfrom langchain_experimental.graph_transformers import LLMGraphTransformer
```

```python
from langchain_memgraph import MemgraphToolkit
```

---

## Messages | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/messages/

**Contents**:
- Messages
- Overview​
- What is inside a message?​
  - Role​
  - Content​
  - Other Message Data​
- Conversation Structure​
- LangChain Messages​

Messages are the unit of communication in chat models. They are used to represent the input and output of a chat model, as well as any additional context or metadata that may be associated with a conversation.

Each message has a role (e.g., "user", "assistant") and content (e.g., text, multimodal data) with additional metadata that varies depending on the chat model provider.

LangChain provides a unified message format that can be used across chat models, allowing users to work with different chat models without worrying about the specific details of the message format used by each model provider.

A message typically consists of the following pieces of information:

Roles are used to distinguish between different types of messages in a conversation and help the chat model understand how to respond to a given sequence of messages.

The content of a message text or a list of dictionaries representing multimodal data (e.g., images, audio, video). The exact format of the content can vary between different chat model providers.

Currently, most chat models support text as the primary content type, with some models also supporting multimodal data. However, support for multimodal data is still limited across most chat model providers.

For more information see:

Depending on the chat model provider, messages can include other data such as:

The sequence of messages into a chat model should follow a specific structure to ensure that the chat model can generate a valid response.

For example, a typical conversation structure might look like this:

Please read the chat history guide for more information on managing chat history and ensuring that the conversation structure is correct.

LangChain provides a unified message format that can be used across all chat models, allowing users to work with different chat models without worrying about the specific details of the message format used by each model provider.

LangChain messages are Python objects that subclass from a Bas

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.messages import HumanMessagemodel.invoke([HumanMessage(content="Hello, how are you?")])
```

```python
model.invoke("Hello, how are you?")
```

```python
from langchain_core.messages import HumanMessageai_message = model.invoke([HumanMessage("Tell me a joke")])ai_message # <-- AIMessage
```

---

## Microsoft | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/microsoft/

**Contents**:
- Microsoft
- Chat Models​
  - Azure OpenAI​
  - Azure AI​
  - Azure ML Chat Online Endpoint​
- LLMs​
  - Azure ML​
  - Azure OpenAI​

All functionality related to Microsoft Azure and other Microsoft products.

Microsoft offers three main options for accessing chat models through Azure:

Microsoft Azure, often referred to as Azure is a cloud computing platform run by Microsoft, which offers access, management, and development of applications and services through global data centers. It provides a range of capabilities, including software as a service (SaaS), platform as a service (PaaS), and infrastructure as a service (IaaS). Microsoft Azure supports many programming languages, tools, and frameworks, including Microsoft-specific and third-party software and systems.

Azure OpenAI is an Azure service with powerful language models from OpenAI including the GPT-3, Codex and Embeddings model series for content generation, summarization, semantic search, and natural language to code translation.

Set the environment variables to get access to the Azure OpenAI service.

Azure AI Foundry provides access to a wide range of models from various providers including Azure OpenAI, DeepSeek R1, Cohere, Phi and Mistral through the AzureAIChatCompletionsModel class.

Configure your API key and Endpoint.

See the documentation here for accessing chat models hosted with Azure Machine Learning.

Microsoft offers two main options for accessing embedding models through Azure:

Configure your API key and Endpoint.

Azure AI Studio provides the capability to upload data assets to cloud storage and register existing data assets from the following sources:

First, you need to install several python packages.

Azure AI Document Intelligence (formerly known as Azure Form Recognizer) is machine-learning based service that extracts texts (including handwriting), tables, document structures, and key-value-pairs from digital or scanned PDFs, images, Office and HTML files.

Document Intelligence supports PDF, JPEG/JPG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX and HTML.

First, you need to install a python package.

Azure Blob Stor

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install langchain-openai
```

```python
import osos.environ["AZURE_OPENAI_ENDPOINT"] = "https://<your-endpoint.openai.azure.com/"os.environ["AZURE_OPENAI_API_KEY"] = "your AzureOpenAI key"
```

```python
from langchain_openai import AzureChatOpenAI
```

---

## Milvus | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/milvus/

**Contents**:
- Milvus
- Installation and Setup​
- Vector Store​

Milvus is a database that stores, indexes, and manages massive embedding vectors generated by deep neural networks and other machine learning (ML) models.

Install the Python SDK:

To import this vectorstore:

**Examples**:

```bash
pip install langchain-milvus
```

```python
from langchain_milvus import Milvus
```

---

## MistralAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/mistralai/

**Contents**:
- MistralAI
- Installation and Setup​
- Chat models​
  - ChatMistralAI​
- Embedding models​
  - MistralAIEmbeddings​

Mistral AI is a platform that offers hosting for their powerful open source models.

A valid API key is needed to communicate with the API.

You will also need the langchain-mistralai package:

**Examples**:

```bash
pip install langchain-mistralai
```

```python
from langchain_mistralai.chat_models import ChatMistralAI
```

```python
from langchain_mistralai import MistralAIEmbeddings
```

---

## MongoDB Atlas | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/mongodb_atlas/

**Contents**:
- MongoDB Atlas
- Installation and Setup​
- Vector Store​
- Retrievers​
  - Full Text Search Retriever​
  - Hybrid Search Retriever​
- Model Caches​
  - MongoDBCache​

MongoDB Atlas is a fully-managed cloud database available in AWS, Azure, and GCP. It now has support for native Vector Search on the MongoDB document data.

See detail configuration instructions.

We need to install langchain-mongodb python package.

Hybrid Search Retriever performs full-text searches using Lucene’s standard (BM25) analyzer.

Hybrid Search Retriever combines vector and full-text searches weighting them the via Reciprocal Rank Fusion (RRF) algorithm.

An abstraction to store a simple cache in MongoDB. This does not use Semantic Caching, nor does it require an index to be made on the collection before generation.

To import this cache:

To use this cache with your LLMs:

Semantic caching allows users to retrieve cached prompts based on semantic similarity between the user input and previously cached results. Under the hood it blends MongoDBAtlas as both a cache and a vectorstore. The MongoDBAtlasSemanticCache inherits from MongoDBAtlasVectorSearch and needs an Atlas Vector Search Index defined to work. Please look at the usage example on how to set up the index.

To import this cache:

To use this cache with your LLMs:

**Examples**:

```bash
pip install langchain-mongodb
```

```python
from langchain_mongodb import MongoDBAtlasVectorSearch
```

```python
from langchain_mongodb.retrievers import MongoDBAtlasFullTextSearchRetriever
```

---

## More | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/all/

**Contents**:
- More
- 📄️ Providers
- 📄️ Abso
- 📄️ Acreom
- 📄️ Activeloop Deep Lake
- 📄️ ADS4GPTs
- 📄️ AgentQL
- 📄️ AI21 Labs

If you'd like to write your own integration, see Extending LangChain.

Abso is an open-source LLM proxy that automatically routes requests between fast and slow models based on prompt complexity. It uses various heuristics to chose the proper model. It's very fast and has low latency.

acreom is a dev-first knowledge base with tasks running on local markdown files.

Activeloop Deep Lake is a data lake for Deep Learning applications, allowing you to use it

ADS4GPTs is building the open monetization backbone of the AI-Native internet. It helps AI applications monetize through advertising with a UX and Privacy first approach.

AgentQL provides web interaction and structured data extraction from any web page using an AgentQL query or a Natural Language prompt. AgentQL can be used across multiple languages and web pages without breaking over time and change.

AI21 Labs is a company specializing in Natural

Aim makes it super easy to visualize and debug LangChain executions. Aim tracks inputs and outputs of LLMs and tools, as well as actions of agents.

AI/ML API provides an API to query 300+ leading AI models (Deepseek, Gemini, ChatGPT, etc.) with enterprise-grade performance.

AI Network is a layer 1 blockchain designed to accommodate

Airbyte is a data integration platform for ELT pipelines from APIs,

Airtable is a cloud collaboration service.

Alchemy is the platform to build blockchain applications.

Aleph Alpha was founded in 2019 with the mission to research and build the foundational technology for an era of strong AI. The team of international scientists, engineers, and innovators researches, develops, and deploys transformative AI like large language and multimodal models and runs the fastest European commercial AI cluster.

Alibaba Group Holding Limited (Wikipedia), or Alibaba

AnalyticDB for PostgreSQL

Anchor is the platform for AI Agentic browser automation, which solves the challenge of automating workflows for web applications that lack APIs or have limi

*[Content truncated - see full docs]*

---

## Multimodality | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/multimodality/

**Contents**:
- Multimodality
- Overview​
- Multimodality in chat models​
  - How to use multimodal models​
  - What kind of multimodality is supported?​
    - Inputs​
    - Outputs​
    - Tools​

Multimodality refers to the ability to work with data that comes in different forms, such as text, audio, images, and video. Multimodality can appear in various components, allowing models and systems to handle and process a mix of these data types seamlessly.

LangChain supports multimodal data as input to chat models:

Some models can accept multimodal inputs, such as images, audio, video, or files. The types of multimodal inputs supported depend on the model provider. For instance, OpenAI, Anthropic, and Google Gemini support documents like PDFs as inputs.

The gist of passing multimodal inputs to a chat model is to use content blocks that specify a type and corresponding data. For example, to pass an image to a chat model as URL:

We can also pass the image as in-line data:

To pass a PDF file as in-line data (or URL, as supported by providers such as Anthropic), just change "type" to "file" and "mime_type" to "application/pdf".

See the how-to guides for more detail.

Most chat models that support multimodal image inputs also accept those values in OpenAI's Chat Completions format:

Otherwise, chat models will typically accept the native, provider-specific content block format. See chat model integrations for detail on specific providers.

Some chat models support multimodal outputs, such as images and audio. Multimodal outputs will appear as part of the AIMessage response object. See for example:

Currently, no chat model is designed to work directly with multimodal data in a tool call request or ToolMessage result.

However, a chat model can easily interact with multimodal data by invoking tools with references (e.g., a URL) to the multimodal data, rather than the data itself. For example, any model capable of tool calling can be equipped with tools to download and process images, audio, or video.

Embeddings are vector representations of data used for tasks like similarity search and retrieval.

The current embedding interface used in LangChain is optimized 

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.messages import HumanMessagemessage = HumanMessage(    content=[        {"type": "text", "text": "Describe the weather in this image:"},        {            "type": "image",            "source_type": "url",            "url": "https://...",        },    ],)response = model.invoke([message])
```

```python
from langchain_core.messages import HumanMessagemessage = HumanMessage(    content=[        {"type": "text", "text": "Describe the weather in this image:"},        {            "type": "image",            "source_type": "base64",            "data": "<base64 string>",            "mime_type": "image/jpeg",        },    ],)response = model.invoke([message])
```

```python
from langchain_core.messages import HumanMessagemessage = HumanMessage(    content=[        {"type": "text", "text": "Describe the weather in this image:"},        {"type": "image_url", "image_url": {"url": image_url}},    ],)response = model.invoke([message])
```

---

## NAVER | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/naver/

**Contents**:
- NAVER
- Installation and Setup​
- Chat models​
  - ChatClovaX​
- Embedding models​
  - ClovaXEmbeddings​
- Tools​
  - Naver Search​

All functionality related to Naver, including HyperCLOVA X models, particularly those accessible through Naver Cloud CLOVA Studio.

Naver is a global technology company with cutting-edge technologies and a diverse business portfolio including search, commerce, fintech, content, cloud, and AI.

Naver Cloud is the cloud computing arm of Naver, a leading cloud service provider offering a comprehensive suite of cloud services to businesses through its Naver Cloud Platform (NCP).

Please refer to NCP User Guide for more detailed instructions (also in Korean).

Naver integrations live in two packages:

(Note) Naver integration via langchain-community, a collection of third-party integrations, is outdated.

The Naver Search integration allows your LangChain applications to retrieve information from Naver's search engine. This is particularly useful for Korean language queries and getting up-to-date information about Korean topics.

To use the Naver Search tools, you need to:

See a usage example for more details.

The package also provides specialized search tools for different types of content:

Each of these can be used within LangChain agents to provide more targeted search capabilities.

**Examples**:

```bash
pip install -U langchain-naver# pip install -U langchain-naver-community // Install to use Naver Search tool.
```

```python
from langchain_naver import ChatClovaX
```

```python
from langchain_naver import ClovaXEmbeddings
```

---

## NVIDIA | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/nvidia/

**Contents**:
- NVIDIA
- Installation​
- Setup​
- Working with NVIDIA API Catalog​
- Working with NVIDIA NIMs​
- Using NVIDIA AI Foundation Endpoints​

The langchain-nvidia-ai-endpoints package contains LangChain integrations building applications with models on NVIDIA NIM inference microservice. NIM supports models across domains like chat, embedding, and re-ranking models from the community as well as NVIDIA. These models are optimized by NVIDIA to deliver the best performance on NVIDIA accelerated infrastructure and deployed as a NIM, an easy-to-use, prebuilt containers that deploy anywhere using a single command on NVIDIA accelerated infrastructure.

NVIDIA hosted deployments of NIMs are available to test on the NVIDIA API catalog. After testing, NIMs can be exported from NVIDIA’s API catalog using the NVIDIA AI Enterprise license and run on-premises or in the cloud, giving enterprises ownership and full control of their IP and AI application.

NIMs are packaged as container images on a per model basis and are distributed as NGC container images through the NVIDIA NGC Catalog. At their core, NIMs provide easy, consistent, and familiar APIs for running inference on an AI model.

Below is an example on how to use some common functionality surrounding text-generative and embedding models.

Create a free account with NVIDIA, which hosts NVIDIA AI Foundation models.

Click on your model of choice.

Under Input select the Python tab, and click Get API Key. Then click Generate Key.

Copy and save the generated key as NVIDIA_API_KEY. From there, you should have access to the endpoints.

Using the API, you can query live endpoints available on the NVIDIA API Catalog to get quick results from a DGX-hosted cloud compute environment. All models are source-accessible and can be deployed on your own compute cluster using NVIDIA NIM which is part of NVIDIA AI Enterprise, shown in the next section Working with NVIDIA NIMs.

When ready to deploy, you can self-host models with NVIDIA NIM—which is included with the NVIDIA AI Enterprise software license—and run them anywhere, giving you ownership of your customizations and full co

*[Content truncated - see full docs]*

**Examples**:

```python
pip install -U --quiet langchain-nvidia-ai-endpoints
```

```python
import getpassimport osif not os.environ.get("NVIDIA_API_KEY", "").startswith("nvapi-"):    nvidia_api_key = getpass.getpass("Enter your NVIDIA API key: ")    assert nvidia_api_key.startswith("nvapi-"), f"{nvidia_api_key[:5]}... is not a valid key"    os.environ["NVIDIA_API_KEY"] = nvidia_api_key
```

```python
from langchain_nvidia_ai_endpoints import ChatNVIDIAllm = ChatNVIDIA(model="mistralai/mixtral-8x22b-instruct-v0.1")result = llm.invoke("Write a ballad about LangChain.")print(result.content)
```

---

## Nebius | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/nebius/

**Contents**:
- Nebius
- Installation and Setup​
  - Available Models​
- Chat models​
  - ChatNebius​
- Embedding models​
  - NebiusEmbeddings​
- Retrievers​

All functionality related to Nebius AI Studio

Nebius AI Studio provides API access to a wide range of state-of-the-art large language models and embedding models for various use cases.

The Nebius integration can be installed via pip:

To use Nebius AI Studio, you'll need an API key which you can obtain from Nebius AI Studio. The API key can be passed as an initialization parameter api_key or set as the environment variable NEBIUS_API_KEY.

The full list of supported models can be found in the Nebius AI Studio Documentation.

The ChatNebius class allows you to interact with Nebius AI Studio's chat models.

The NebiusEmbeddings class allows you to generate vector embeddings using Nebius AI Studio's embedding models.

The NebiusRetriever enables efficient similarity search using embeddings from Nebius AI Studio. It leverages high-quality embedding models to enable semantic search over documents.

The NebiusRetrievalTool allows you to create a tool for agents based on the NebiusRetriever.

**Examples**:

```bash
pip install langchain-nebius
```

```python
import osos.environ["NEBIUS_API_KEY"] = "YOUR-NEBIUS-API-KEY"
```

```python
from langchain_nebius import ChatNebius# Initialize the chat modelchat = ChatNebius(    model="Qwen/Qwen3-30B-A3B-fast",  # Choose from available models    temperature=0.6,    top_p=0.95)
```

---

## Neo4j | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/neo4j/

**Contents**:
- Neo4j
- Installation and Setup​
- VectorStore​
- GraphCypherQAChain​
- Constructing a knowledge graph from text​
- Memory​

Get started with Neo4j by visiting their website.

The Neo4j vector index is used as a vectorstore, whether for semantic search or example selection.

There exists a wrapper around Neo4j graph database that allows you to generate Cypher statements based on the user input and use them to retrieve relevant information from the database.

Text data often contain rich relationships and insights that can be useful for various analytics, recommendation engines, or knowledge management applications. Diffbot's NLP API allows for the extraction of entities, relationships, and semantic meaning from unstructured text data. By coupling Diffbot's NLP API with Neo4j, a graph database, you can create powerful, dynamic graph structures based on the information extracted from text. These graph structures are fully queryable and can be integrated into various applications.

**Examples**:

```python
from langchain_neo4j import Neo4jVector
```

```python
from langchain_neo4j import GraphCypherQAChain, Neo4jGraph
```

```python
from langchain_neo4j import Neo4jGraphfrom langchain_experimental.graph_transformers.diffbot import DiffbotGraphTransformer
```

---

## Netmind | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/netmind/

**Contents**:
- Netmind
- Installation and Setup​
- Chat Models​
- Embedding Model​

Netmind AI Build AI Faster, Smarter, and More Affordably. Train, Fine-tune, Run Inference, and Scale with our Global GPU Network—Your all-in-one AI Engine.

This example goes over how to use LangChain to interact with Netmind AI models.

Get an Netmind api key and set it as an environment variable (NETMIND_API_KEY). Head to https://www.netmind.ai/ to sign up to Netmind and generate an API key.

For more on Netmind chat models, visit the guide here

For more on Netmind embedding models, visit the guide

**Examples**:

```bash
pip install langchain-netmind
```

---

## Nimble | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/nimble/

**Contents**:
- Nimble
- Retrievers:​
  - NimbleSearchRetriever​

Nimble is the first business external data platform, making data decision-making easier than ever, with our award-winning AI-powered data structuring technology Nimble connects business users with the public web knowledge. We empower businesses with mission-critical real-time external data to unlock advanced business intelligence, price comparison, and other public data for sales and marketing. We translate data into immediate business value.

If you'd like to learn more about Nimble, visit us at nimbleway.com.

Enables developers to build RAG applications and AI Agents that can search, access, and retrieve online information from anywhere on the web.

We need to install the langchain-nimble python package.

Note that authentication is required, please refer to the Setup section in the documentation.

**Examples**:

```python
%pip install -U langchain-nimble
```

```python
from langchain_nimble import NimbeSearchRetriever
```

---

## Nomic | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/nomic/

**Contents**:
- Nomic
- Installation​
- LLMs​
  - GPT4All​
- Embedding models​
  - NomicEmbeddings​
  - GPT4All​
- Vector store​

Nomic builds tools that enable everyone to interact with AI scale datasets and run AI models on consumer computers.

Nomic currently offers two products:

The Nomic integration exists in two partner packages: langchain-nomic and in langchain-community.

You can install them with:

See a usage example and installation instructions.

**Examples**:

```bash
pip install -U langchain-nomicpip install -U langchain-community
```

```python
from langchain_community.llms import GPT4All
```

```python
from langchain_nomic import NomicEmbeddings
```

---

## OceanBase | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/oceanbase/

**Contents**:
- OceanBase
- Installation​
  - Usage​

OceanBase Database is a distributed relational database. It is developed entirely by Ant Group. The OceanBase Database is built on a common server cluster. Based on the Paxos protocol and its distributed structure, the OceanBase Database provides high availability and linear scalability.

OceanBase currently has the ability to store vectors. Users can easily perform the following operations with SQL:

We recommend using Docker to deploy OceanBase:

More methods to deploy OceanBase cluster

For a more detailed walkthrough of the OceanBase Wrapper, see this notebook

**Examples**:

```bash
pip install -U langchain-oceanbase
```

```shell
docker run --name=ob433 -e MODE=slim -p 2881:2881 -d oceanbase/oceanbase-ce:4.3.3.0-100000132024100711
```

---

## Ollama | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/ollama/

**Contents**:
- Ollama
- Installation and Setup​
  - Ollama installation​
  - Ollama LangChain partner package install​
- LLM​
- Chat Models​
  - Chat Ollama​
  - Ollama tool calling​

Ollama allows you to run open-source large language models, such as gpt-oss, locally.

Ollama bundles model weights, configuration, and data into a single package, defined by a Modelfile. It optimizes setup and configuration details, including GPU usage. For a complete list of supported models and model variants, see the Ollama model library.

See this guide for more details on how to use ollama with LangChain.

Follow these instructions to set up and run a local Ollama instance.

Ollama will start as a background service automatically, if this is disabled, run:

After starting ollama, run ollama pull <name-of-model> to download a model from the Ollama model library:

We're now ready to install the langchain-ollama partner package and run a model.

Install the integration package with:

See the notebook example here.

See the notebook example here.

Ollama tool calling uses the OpenAI compatible web server specification, and can be used with the default BaseChatModel.bind_tools() methods as described here. Make sure to select an ollama model that supports tool calling.

See the notebook example here.

**Examples**:

```bash
# export OLLAMA_HOST=127.0.0.1 # environment variable to set ollama host# export OLLAMA_PORT=11434 # environment variable to set the ollama portollama serve
```

```bash
ollama pull gpt-oss:20b
```

```bash
pip install langchain-ollama
```

---

## OpenAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/openai/

**Contents**:
- OpenAI
- Installation and Setup​
- Chat model​
- LLM​
- Embedding Model​
- Document Loader​
- Retriever​
- Tools​

All functionality related to OpenAI

OpenAI is American artificial intelligence (AI) research laboratory consisting of the non-profit OpenAI Incorporated and its for-profit subsidiary corporation OpenAI Limited Partnership. OpenAI conducts AI research with the declared intention of promoting and developing a friendly AI. OpenAI systems run on an Azure-based supercomputing platform from Microsoft.

The OpenAI API is powered by a diverse set of models with different capabilities and price points.

ChatGPT is the Artificial Intelligence (AI) chatbot developed by OpenAI.

Install the integration package with

Get an OpenAI api key and set it as an environment variable (OPENAI_API_KEY)

If you are using a model hosted on Azure, you should use different wrapper for that:

For a more detailed walkthrough of the Azure wrapper, see here.

If you are using a model hosted on Azure, you should use different wrapper for that:

For a more detailed walkthrough of the Azure wrapper, see here.

OpenAI Dall-E are text-to-image models developed by OpenAI using deep learning methodologies to generate digital images from natural language descriptions, called "prompts".

There are several places you can use the tiktoken tokenizer. By default, it is used to count tokens for OpenAI LLMs.

You can also use it to count tokens when splitting documents with

For a more detailed walkthrough of this, see this notebook

**Examples**:

```bash
pip install langchain-openai
```

```python
from langchain_openai import ChatOpenAI
```

```python
from langchain_openai import AzureChatOpenAI
```

---

## OpenGradient | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/opengradient/

**Contents**:
- OpenGradient
- Installation and Setup​
- OpenGradient Toolkit​
  - Key Benefits​

OpenGradient is a decentralized AI computing network enabling globally accessible, permissionless, and verifiable ML model inference.

The OpenGradient langchain package currently offers a toolkit that allows developers to build their own custom ML inference tools for models on the OpenGradient network. This was previously a challenge because of the context-window polluting nature of large model parameters -- imagine having to give your agent a 200x200 array of floating-point data!

The toolkit solves this problem by encapsulating all data processing logic within the tool definition itself. This approach keeps the agent's context window clean while giving developers complete flexibility to implement custom data processing and live-data retrieval for their ML models.

Ensure that you have an OpenGradient API key in order to access the OpenGradient network. If you already have an API key, simply set the environment variable:

If you need to set up a new API key, download the opengradient SDK and follow the instructions to initialize a new configuration.

Once you have set up your API key, install the langchain-opengradient package.

The OpenGradientToolkit empowers developers to create specialized tools based on ML models and workflows deployed on the OpenGradient decentralized network. This integration enables LangChain agents to access powerful ML capabilities while maintaining efficient context usage.

🔄 Real-time data integration - Process live data feeds within your tools

🎯 Dynamic processing - Custom data pipelines that adapt to specific agent inputs

🧠 Context efficiency - Handle complex ML operations without flooding your context window

🔌 Seamless deployment - Easy integration with models already on the OpenGradient network

🔧 Full customization - Create and deploy your own specific models through the OpenGradient SDK, then build custom tools from them

🔐 Verifiable inference - All inferences run on the decentralized OpenGradient network, allowing users to c

*[Content truncated - see full docs]*

**Examples**:

```python
!export OPENGRADIENT_PRIVATE_KEY="your-api-key"
```

```python
!pip install opengradient!opengradient config init
```

```python
pip install -U langchain-opengradient
```

---

## Oracle Cloud Infrastructure (OCI) | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/oci/

**Contents**:
- Oracle Cloud Infrastructure (OCI)
- OCI Generative AI​
- OCI Data Science Model Deployment Endpoint​

The LangChain integrations related to Oracle Cloud Infrastructure.

Oracle Cloud Infrastructure (OCI) Generative AI is a fully managed service that provides a set of state-of-the-art, customizable large language models (LLMs) that cover a wide range of use cases, and which are available through a single API. Using the OCI Generative AI service you can access ready-to-use pretrained models, or create and host your own fine-tuned custom models based on your own data on dedicated AI clusters.

To use, you should have the latest oci python SDK and the langchain_community package installed.

See chat, complete, and embedding usage examples.

OCI Data Science is a fully managed and serverless platform for data science teams. Using the OCI Data Science platform you can build, train, and manage machine learning models, and then deploy them as an OCI Model Deployment Endpoint using the OCI Data Science Model Deployment Service.

To use, you should have the latest oracle-ads python SDK installed.

See chat and complete usage examples.

**Examples**:

```bash
python -m pip install -U langchain-oci
```

```python
from langchain_oci.chat_models import ChatOCIGenAIfrom langchain_oci.embeddings import OCIGenAIEmbeddings
```

```bash
pip install -U oracle-ads
```

---

## Output parsers | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/output_parsers/

**Contents**:
- Output parsers

The information here refers to parsers that take a text output from a model try to parse it into a more structured representation. More and more models are supporting function (or tool) calling, which handles this automatically. It is recommended to use function/tool calling rather than output parsing. See documentation for that here.

Output parser is responsible for taking the output of a model and transforming it to a more suitable format for downstream tasks. Useful when you are using LLMs to generate structured data, or to normalize output from chat models and LLMs.

LangChain has lots of different types of output parsers. This is a list of output parsers LangChain supports. The table below has various pieces of information:

For specifics on how to use output parsers, see the relevant how-to guides here.

---

## Oxylabs | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/oxylabs/

**Contents**:
- Oxylabs
- Installation and Setup​
- Tools​

Oxylabs is a market-leading web intelligence collection platform, driven by the highest business, ethics, and compliance standards, enabling companies worldwide to unlock data-driven insights.

langchain-oxylabs implements tools enabling LLMs to interact with Oxylabs Web Scraper API.

See details on available tools here.

**Examples**:

```bash
pip install langchain-oxylabs
```

---

## PGVector | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/pgvector/

**Contents**:
- PGVector
- Installation​
- Setup​
- Wrappers​
  - VectorStore​
  - Usage​

This page covers how to use the Postgres PGVector ecosystem within LangChain It is broken into two parts: installation and setup, and then references to specific PGVector wrappers.

The first step is to create a database with the pgvector extension installed.

Follow the steps at PGVector Installation Steps to install the database and the extension. The docker image is the easiest way to get started.

There exists a wrapper around Postgres vector databases, allowing you to use it as a vectorstore, whether for semantic search or example selection.

To import this vectorstore:

For a more detailed walkthrough of the PGVector Wrapper, see this notebook

**Examples**:

```python
from langchain_community.vectorstores.pgvector import PGVector
```

---

## PaymanAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/payman-tool/

**Contents**:
- PaymanAI
- Overview​
  - Integration details​
- Setup​
- Instantiation​
- Invocation​
  - Invoke directly with args​
  - Invoke with ToolCall​

PaymanAI provides functionality to send and receive payments (fiat and crypto) on behalf of an AI Agent. To get started:

This notebook gives a quick overview of integrating PaymanAI into LangChain as a tool. For complete reference, see the API documentation.

The PaymanAI integration is part of the langchain-community (or your custom) package. It allows you to:

These can be wrapped as LangChain Tools for an LLM-based agent to call them automatically.

If you're simply calling the PaymanAI SDK, you can do it directly or via the Tool interface in LangChain.

Your PAYMAN_API_SECRET should be the secret key from app.paymanai.com. The PAYMAN_ENVIRONMENT can be sandbox or production depending on your usage.

Here is an example of instantiating a PaymanAI tool. If you have multiple Payman methods, you can create multiple tools.

You can call tool.invoke(...) and pass a dictionary matching the tool's expected fields. For example:

When used inside an AI workflow, the LLM might produce a ToolCall dict. You can simulate it as follows:

You can bind a PaymanAI tool to a LangChain agent or chain that supports tool-calling.

**Examples**:

```bash
pip install langchain-payman-tool
```

```bash
pip install paymanai
```

```bash
export PAYMAN_API_SECRET="YOUR_SECRET_KEY"export PAYMAN_ENVIRONMENT="sandbox"
```

---

## Permit | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/permit/

**Contents**:
- Permit
- Installation and Setup​
- Tools​
- Retrievers​

Permit.io offers fine-grained access control and policy enforcement. With LangChain, you can integrate Permit checks to ensure only authorized users can access or retrieve data in your LLM applications.

Set environment variables for your Permit PDP and credentials:

Make sure your PDP is running and configured. See Permit Docs for policy setup.

See detail on available tools here.

See detail on available retrievers here.

**Examples**:

```bash
pip install langchain-permitpip install permit
```

```python
export PERMIT_API_KEY="your_permit_api_key"export PERMIT_PDP_URL="http://localhost:7766"   # or your real PDP endpoint
```

---

## Perplexity | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/perplexity/

**Contents**:
- Perplexity
- Installation and Setup​
- Chat models​

Perplexity is the most powerful way to search the internet with unlimited Pro Search, upgraded AI models, unlimited file upload, image generation, and API credits.

You can check a list of available models.

Install the Perplexity x LangChain integration package:

Get your API key from here.

See a variety of usage examples here.

**Examples**:

```bash
pip install langchain-perplexity
```

```python
from langchain_perplexity import ChatPerplexity
```

---

## Pinecone | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/pinecone/

**Contents**:
- Pinecone
- Installation and Setup​
- Vector store​
  - Sparse Vector store​
  - Sparse Embedding​
- Retrievers​
  - Pinecone Hybrid Search​
  - Self Query retriever​

Pinecone is a vector database with broad functionality.

Install the Python SDK:

There exists a wrapper around Pinecone indexes, allowing you to use it as a vectorstore, whether for semantic search or example selection.

For a more detailed walkthrough of the Pinecone vectorstore, see this notebook

LangChain's PineconeSparseVectorStore enables sparse retrieval using Pinecone's sparse English model. It maps text to sparse vectors and supports adding documents and similarity search.

For a more detailed walkthrough, see the Pinecone Sparse Vector Store notebook.

LangChain's PineconeSparseEmbeddings provides sparse embedding generation using Pinecone's pinecone-sparse-english-v0 model.

For more detailed usage, see the Pinecone Sparse Embeddings notebook.

For more detailed information, see this notebook.

Pinecone vector store can be used as a retriever for self-querying.

For more detailed information, see this notebook.

**Examples**:

```bash
pip install langchain-pinecone
```

```python
from langchain_pinecone import PineconeVectorStore
```

```python
from langchain_pinecone import PineconeSparseVectorStore# Initialize sparse vector storevector_store = PineconeSparseVectorStore(    index=my_index,    embedding_model="pinecone-sparse-english-v0")# Add documentsvector_store.add_documents(documents)# Queryresults = vector_store.similarity_search("your query", k=3)
```

---

## Pipeshift | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/pipeshift/

**Contents**:
- Pipeshift
- Installation and Setup​
  - Authentication​
- Chat models​
- LLMs​

Pipeshift is a fine-tuning and inference platform for open-source LLMs

Install the Pipeshift integration package.

Get your Pipeshift API key by signing up at Pipeshift.

You can perform authentication using your Pipeshift API key in any of the following ways:

Adding API key to the environment variable as PIPESHIFT_API_KEY.

By passing api_key to the pipeshift LLM module or chat module

**Examples**:

```bash
pip install langchain-pipeshift
```

```python
os.environ["PIPESHIFT_API_KEY"] = "<your_api_key>"
```

```python
llm = Pipeshift(api_key="<your_api_key>", model="meta-llama/Meta-Llama-3.1-8B-Instruct", max_tokens=512)                    ORchat = ChatPipeshift(api_key="<your_api_key>", model="meta-llama/Meta-Llama-3.1-8B-Instruct", max_tokens=512)
```

---

## Prediction Guard | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/predictionguard/

**Contents**:
- Prediction Guard
- Installation and Setup​
- Prediction Guard Langchain Integrations​
- Getting Started​
- Chat Models​
  - Prediction Guard Chat​
    - Usage​
- Embedding Models​

This page covers how to use the Prediction Guard ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific Prediction Guard wrappers.

This integration is maintained in the langchain-predictionguard package.

**Examples**:

```text
pip install langchain-predictionguard
```

```python
from langchain_predictionguard import ChatPredictionGuard
```

```python
# If predictionguard_api_key is not passed, default behavior is to use the `PREDICTIONGUARD_API_KEY` environment variable.chat = ChatPredictionGuard(model="Hermes-3-Llama-3.1-8B")chat.invoke("Tell me a joke")
```

---

## Prompt Templates | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/prompt_templates/

**Contents**:
- Prompt Templates
- String PromptTemplates​
- ChatPromptTemplates​
- MessagesPlaceholder​

Prompt templates help to translate user input and parameters into instructions for a language model. This can be used to guide a model's response, helping it understand the context and generate relevant and coherent language-based output.

Prompt Templates take as input a dictionary, where each key represents a variable in the prompt template to fill in.

Prompt Templates output a PromptValue. This PromptValue can be passed to an LLM or a ChatModel, and can also be cast to a string or a list of messages. The reason this PromptValue exists is to make it easy to switch between strings and messages.

There are a few different types of prompt templates:

These prompt templates are used to format a single string, and generally are used for simpler inputs. For example, a common way to construct and use a PromptTemplate is as follows:

These prompt templates are used to format a list of messages. These "templates" consist of a list of templates themselves. For example, a common way to construct and use a ChatPromptTemplate is as follows:

In the above example, this ChatPromptTemplate will construct two messages when called. The first is a system message, that has no variables to format. The second is a HumanMessage, and will be formatted by the topic variable the user passes in.

This prompt template is responsible for adding a list of messages in a particular place. In the above ChatPromptTemplate, we saw how we could format two messages, each one a string. But what if we wanted the user to pass in a list of messages that we would slot into a particular spot? This is how you use MessagesPlaceholder.

This will produce a list of four messages total: the system message plus the three messages we passed in (two HumanMessages and one AIMessage). If we had passed in 5 messages, then it would have produced 6 messages in total (the system message plus the 5 passed in). This is useful for letting a list of messages be slotted into a particular spot.

An alternative way to accompl

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.prompts import PromptTemplateprompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")prompt_template.invoke({"topic": "cats"})
```

```python
from langchain_core.prompts import ChatPromptTemplateprompt_template = ChatPromptTemplate([    ("system", "You are a helpful assistant"),    ("user", "Tell me a joke about {topic}")])prompt_template.invoke({"topic": "cats"})
```

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderfrom langchain_core.messages import HumanMessage, AIMessageprompt_template = ChatPromptTemplate([    ("system", "You are a helpful assistant"),    MessagesPlaceholder("msgs")])# Simple example with one messageprompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})# More complex example with conversation historymessages_to_pass = [    HumanMessage(content="What's the capital of France?"),    AIMessage(content="The c
...
```

---

## Providers | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/

**Contents**:
- Providers
- Integration Packages​
- All Providers​

If you'd like to write your own integration, see Extending LangChain. If you'd like to contribute an integration, see Contributing integrations.

These providers have standalone langchain-{provider} packages for improved versioning, dependency management and testing.

Click here to see all providers. Or search for a provider using the Search field in the top-right corner of the screen.

---

## PullMd Loader | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/pull-md/

**Contents**:
- PullMd Loader
- Installation and Setup​
- Document Loader​
- API Reference​
- Additional Resources​

PullMd is a service that converts web pages into Markdown format. The langchain-pull-md package utilizes this service to convert URLs, especially those rendered with JavaScript frameworks like React, Angular, or Vue.js, into Markdown without the need for local rendering.

To get started with langchain-pull-md, you need to install the package via pip:

See the usage example for detailed integration and usage instructions.

The PullMdLoader class in langchain-pull-md provides an easy way to convert URLs to Markdown. It's particularly useful for loading content from modern web applications for use within LangChain's processing capabilities.

This loader supports any URL and is particularly adept at handling sites built with dynamic JavaScript, making it a versatile tool for markdown extraction in data processing workflows.

For a comprehensive guide to all available functions and their parameters, visit the API reference.

**Examples**:

```bash
pip install langchain-pull-md
```

```python
from langchain_pull_md import PullMdLoader# Initialize the loader with a URL of a JavaScript-rendered webpageloader = PullMdLoader(url='https://example.com')# Load the content as a Documentdocuments = loader.load()# Access the Markdown contentfor document in documents:    print(document.page_content)
```

---

## PyMuPDF4LLM | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/pymupdf4llm/

**Contents**:
- PyMuPDF4LLM

PyMuPDF4LLM is aimed to make it easier to extract PDF content in Markdown format, needed for LLM & RAG applications.

langchain-pymupdf4llm integrates PyMuPDF4LLM to LangChain as a Document Loader.

**Examples**:

```python
%pip install -qU langchain-pymupdf4llm
```

```python
from langchain_pymupdf4llm import PyMuPDF4LLMLoader, PyMuPDF4LLMParser
```

---

## Qdrant | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/qdrant/

**Contents**:
- Qdrant
- Installation and Setup​
- Embedding models​
  - FastEmbedSparse​
  - SparseEmbeddings​
- Vector Store​

Qdrant (read: quadrant) is a vector similarity search engine. It provides a production-ready service with a convenient API to store, search, and manage points - vectors with an additional payload. Qdrant is tailored to extended filtering support.

Install the Python partner package:

There exists a wrapper around Qdrant indexes, allowing you to use it as a vectorstore, whether for semantic search or example selection.

To import this vectorstore:

For a more detailed walkthrough of the Qdrant wrapper, see this notebook

**Examples**:

```bash
pip install langchain-qdrant
```

```python
from langchain_qdrant import FastEmbedSparse
```

```python
from langchain_qdrant import SparseEmbeddings
```

---

## Recallio | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/recallio/

**Contents**:
- Recallio
- Installation​

Recallio is a powerfull API allowing to store, index, and retrieve application “memories” with built-in fact extraction, dynamic summaries, reranked recall, and a full knowledge-graph layer.

**Examples**:

```bash
pip install langchain-recallio
```

```python
from langchain_recallio.memory import RecallioMemory
```

---

## Redis | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/redis/

**Contents**:
- Redis
- Installation and Setup​
  - Connections​
    - Redis Standalone connection url​
    - Redis Sentinel connection url​
    - Redis Cluster connection url​
- Cache​
  - Standard Cache​

Redis (Remote Dictionary Server) is an open-source in-memory storage, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Because it holds all data in memory and because of its design, Redis offers low-latency reads and writes, making it particularly suitable for use cases that require a cache. Redis is the most popular NoSQL database, and one of the most popular databases overall.

This page covers how to use the Redis ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific Redis wrappers.

Install the Python SDK:

To run Redis locally, you can use Docker:

To stop the container:

And to start it again:

We need a redis url connection string to connect to the database support either a stand alone Redis server or a High-Availability setup with Replication and Redis Sentinels.

For standalone Redis server, the official redis connection url formats can be used as describe in the python redis modules "from_url()" method Redis.from_url

Example: redis_url = "redis://:secret-pass@localhost:6379/0"

For Redis sentinel setups the connection scheme is "redis+sentinel". This is an unofficial extensions to the official IANA registered protocol schemes as long as there is no connection url for Sentinels available.

Example: redis_url = "redis+sentinel://:secret-pass@sentinel-host:26379/mymaster/0"

The format is redis+sentinel://[[username]:[password]]@[host-or-ip]:[port]/[service-name]/[db-number] with the default values of "service-name = mymaster" and "db-number = 0" if not set explicit. The service-name is the redis server monitoring group name as configured within the Sentinel.

The current url format limits the connection string to one sentinel host only (no list can be given) and both Redis server and sentinel must have the same password set (if used).

Redis cluster is not supported right now for all methods requiring a "redis_url" parameter. The only way to us

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install redis
```

```bash
docker run --name langchain-redis -d -p 6379:6379 redis redis-server --save 60 1 --loglevel warning
```

```bash
docker stop langchain-redis
```

---

## Retrieval | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/retrieval/

**Contents**:
- Retrieval
- Overview​
- Key concepts​
- Query analysis​
  - Query re-writing​
  - Query construction​
- Information retrieval​
  - Common retrieval systems​

Some of the concepts reviewed here utilize models to generate queries (e.g., for SQL or graph databases). There are inherent risks in doing this. Make sure that your database connection permissions are scoped as narrowly as possible for your application's needs. This will mitigate, though not eliminate, the risks of building a model-driven system capable of querying databases. For more on general security best practices, see our security guide.

Retrieval systems are fundamental to many AI applications, efficiently identifying relevant information from large datasets. These systems accommodate various data formats:

Despite the growing diversity in data formats, modern AI applications increasingly aim to make all types of data accessible through natural language interfaces. Models play a crucial role in this process by translating natural language queries into formats compatible with the underlying search index or database. This translation enables more intuitive and flexible interactions with complex data structures.

(1) Query analysis: A process where models transform or construct search queries to optimize retrieval.

(2) Information retrieval: Search queries are used to fetch information from various retrieval systems.

While users typically prefer to interact with retrieval systems using natural language, these systems may require specific query syntax or benefit from certain keywords. Query analysis serves as a bridge between raw user input and optimized search queries. Some common applications of query analysis include:

Query analysis employs models to transform or construct optimized search queries from raw user input.

Retrieval systems should ideally handle a wide spectrum of user inputs, from simple and poorly worded queries to complex, multi-faceted questions. To achieve this versatility, a popular approach is to use models to transform raw user queries into more effective search queries. This transformation can range from simple keyword extraction to 

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Listfrom pydantic import BaseModel, Fieldfrom langchain_openai import ChatOpenAIfrom langchain_core.messages import SystemMessage, HumanMessage# Define a pydantic model to enforce the output structureclass Questions(BaseModel):    questions: List[str] = Field(        description="A list of sub-questions related to the input query."    )# Create an instance of the model and enforce the output structuremodel = ChatOpenAI(model="gpt-4o", temperature=0)structured_model = model.wit
...
```

```python
metadata_field_info = schema_for_metadatadocument_content_description = "Brief summary of a movie"llm = ChatOpenAI(temperature=0)retriever = SelfQueryRetriever.from_llm(    llm,    vectorstore,    document_content_description,    metadata_field_info,)
```

```python
docs = retriever.invoke(query)
```

---

## Retrieval augmented generation (RAG) | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/rag/

**Contents**:
- Retrieval augmented generation (RAG)
- Overview​
- Key concepts​
- Retrieval system​
- Adding external knowledge​

Retrieval Augmented Generation (RAG) is a powerful technique that enhances language models by combining them with external knowledge bases. RAG addresses a key limitation of models: models rely on fixed training datasets, which can lead to outdated or incomplete information. When given a query, RAG systems first search a knowledge base for relevant information. The system then incorporates this retrieved information into the model's prompt. The model uses the provided context to generate a response to the query. By bridging the gap between vast language models and dynamic, targeted information retrieval, RAG is a powerful technique for building more capable and reliable AI systems.

(1) Retrieval system: Retrieve relevant information from a knowledge base.

(2) Adding external knowledge: Pass retrieved information to a model.

Model's have internal knowledge that is often fixed, or at least not updated frequently due to the high cost of training. This limits their ability to answer questions about current events, or to provide specific domain knowledge. To address this, there are various knowledge injection techniques like fine-tuning or continued pre-training. Both are costly and often poorly suited for factual retrieval. Using a retrieval system offers several advantages:

See our conceptual guide on retrieval.

With a retrieval system in place, we need to pass knowledge from this system to the model. A RAG pipeline typically achieves this following these steps:

As an example, here's a simple RAG workflow that passes information from a retriever to a chat model:

RAG a deep area with many possible optimization and design choices:

**Examples**:

```python
from langchain_openai import ChatOpenAIfrom langchain_core.messages import SystemMessage, HumanMessage# Define a system prompt that tells the model how to use the retrieved contextsystem_prompt = """You are an assistant for question-answering tasks.Use the following pieces of retrieved context to answer the question.If you don't know the answer, just say that you don't know.Use three sentences maximum and keep the answer concise.Context: {context}:"""# Define a questionquestion = """What are the
...
```

---

## Retrievers | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/retrievers/

**Contents**:
- Retrievers
- Overview​
- Key concept​
- Interface​
- Common types​
  - Search apis​
  - Relational or graph database​
  - Lexical search​

Many different types of retrieval systems exist, including vectorstores, graph databases, and relational databases. With the rise on popularity of large language models, retrieval systems have become an important component in AI application (e.g., RAG). Because of their importance and variability, LangChain provides a uniform interface for interacting with different types of retrieval systems. The LangChain retriever interface is straightforward:

All retrievers implement a simple interface for retrieving documents using natural language queries.

The only requirement for a retriever is the ability to accepts a query and return documents. In particular, LangChain's retriever class only requires that the _get_relevant_documents method is implemented, which takes a query: str and returns a list of Document objects that are most relevant to the query. The underlying logic used to get relevant documents is specified by the retriever and can be whatever is most useful for the application.

A LangChain retriever is a runnable, which is a standard interface for LangChain components. This means that it has a few common methods, including invoke, that are used to interact with it. A retriever can be invoked with a query:

Retrievers return a list of Document objects, which have two attributes:

Despite the flexibility of the retriever interface, a few common types of retrieval systems are frequently used.

It's important to note that retrievers don't need to actually store documents. For example, we can build retrievers on top of search APIs that simply return search results! See our retriever integrations with Amazon Kendra or Wikipedia Search.

Retrievers can be built on top of relational or graph databases. In these cases, query analysis techniques to construct a structured query from natural language is critical. For example, you can build a retriever for a SQL database using text-to-SQL conversion. This allows a natural language query (string) retriever to be transforme

*[Content truncated - see full docs]*

**Examples**:

```python
docs = retriever.invoke(query)
```

```python
vectorstore = MyVectorStore()retriever = vectorstore.as_retriever()
```

```python
# Initialize the ensemble retrieverensemble_retriever = EnsembleRetriever(    retrievers=[bm25_retriever, vector_store_retriever], weights=[0.5, 0.5])
```

---

## Runnable interface | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/runnables/

**Contents**:
- Runnable interface
- Overview of runnable interface​
  - Optimized parallel execution (batch)​
  - Asynchronous support​
- Streaming APIs​
- Input and output types​
  - Inspecting schemas​
    - With_types​

The Runnable interface is the foundation for working with LangChain components, and it's implemented across many of them, such as language models, output parsers, retrievers, compiled LangGraph graphs and more.

This guide covers the main concepts and methods of the Runnable interface, which allows developers to interact with various LangChain components in a consistent and predictable manner.

The Runnable way defines a standard interface that allows a Runnable component to be:

Please review the LCEL Cheatsheet for some common patterns that involve the Runnable interface and LCEL expressions.

LangChain Runnables offer a built-in batch (and batch_as_completed) API that allow you to process multiple inputs in parallel.

Using these methods can significantly improve performance when needing to process multiple independent inputs, as the processing can be done in parallel instead of sequentially.

The two batching options are:

The default implementation of batch and batch_as_completed use a thread pool executor to run the invoke method in parallel. This allows for efficient parallel execution without the need for users to manage threads, and speeds up code that is I/O-bound (e.g., making API requests, reading files, etc.). It will not be as effective for CPU-bound operations, as the GIL (Global Interpreter Lock) in Python will prevent true parallel execution.

Some Runnables may provide their own implementations of batch and batch_as_completed that are optimized for their specific use case (e.g., rely on a batch API provided by a model provider).

The async versions of abatch and abatch_as_completed relies on asyncio's gather and as_completed functions to run the ainvoke method in parallel.

When processing a large number of inputs using batch or batch_as_completed, users may want to control the maximum number of parallel calls. This can be done by setting the max_concurrency attribute in the RunnableConfig dictionary. See the RunnableConfig for more information.

C

*[Content truncated - see full docs]*

**Examples**:

```python
some_runnable.invoke(   some_input,   config={      'run_name': 'my_run',      'tags': ['tag1', 'tag2'],      'metadata': {'key': 'value'}   })
```

```python
chain = prompt | chat_model | output_parser
```

```python
def foo(input):    # Note that .invoke() is used directly here    return bar_runnable.invoke(input)foo_runnable = RunnableLambda(foo)
```

---

## Runpod | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/runpod/

**Contents**:
- Runpod
- Intstallation​
- Setup​
  - 1. Deploy an Endpoint on RunPod​
  - 2. Set API Credentials​
- Components​
  - 1. LLM​
  - 2. Chat Model​

RunPod provides GPU cloud infrastructure, including Serverless endpoints optimized for deploying and scaling AI models.

This guide covers how to use the langchain-runpod integration package to connect LangChain applications to models hosted on RunPod Serverless.

The integration offers interfaces for both standard Language Models (LLMs) and Chat Models.

Install the dedicated partner package:

The integration needs your RunPod API Key and the Endpoint ID. Set them as environment variables for secure access:

(Optional) If using different endpoints for LLM and Chat models, you might need to set RUNPOD_CHAT_ENDPOINT_ID or pass the ID directly during initialization.

This package provides two main components:

For interacting with standard text completion models.

See the RunPod LLM Integration Guide for detailed usage

For interacting with conversational models.

See the RunPod Chat Model Integration Guide for detailed usage and feature support.

**Examples**:

```python
%pip install -qU langchain-runpod
```

```python
import getpassimport osos.environ["RUNPOD_API_KEY"] = getpass.getpass("Enter your RunPod API Key: ")os.environ["RUNPOD_ENDPOINT_ID"] = input("Enter your RunPod Endpoint ID: ")
```

```python
from langchain_runpod import RunPod# Example initialization (uses environment variables)llm = RunPod(model_kwargs={"max_new_tokens": 100})  # Add generation params here# Example Invocationtry:    response = llm.invoke("Write a short poem about the cloud.")    print(response)except Exception as e:    print(        f"Error invoking LLM: {e}. Ensure endpoint ID and API key are correct and endpoint is active."    )
```

---

## SAP | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/sap/

**Contents**:
- SAP
- Installation and Setup​
- Vectorstore​

SAP SE(Wikipedia) is a German multinational software company. It develops enterprise software to manage business operation and customer relations. The company is the world's leading enterprise resource planning (ERP) software vendor.

We need to install the langchain-hana python package.

SAP HANA Cloud Vector Engine is a vector store fully integrated into the SAP HANA Cloud database.

**Examples**:

```bash
pip install langchain-hana
```

```python
from langchain_hana import HanaDB
```

---

## SWI-Prolog | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/prolog/

**Contents**:
- SWI-Prolog
- Installation and Setup​
- Tools​

SWI-Prolog offers a comprehensive free Prolog environment.

Once SWI-Prolog has been installed, install lanchain-prolog using pip:

The PrologTool class allows the generation of langchain tools that use Prolog rules to generate answers.

See the same guide for usage examples of PrologRunnable, which allows the generation of LangChain runnables that use Prolog rules to generate answers.

**Examples**:

```bash
pip install langchain-prolog
```

```python
from langchain_prolog import PrologConfig, PrologTool
```

---

## Salesforce | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/salesforce/

**Contents**:
- Salesforce
- Installation and Setup​
- Tools​

Salesforce is a cloud-based software company that provides customer relationship management (CRM) solutions and a suite of enterprise applications focused on sales, customer service, marketing automation, and analytics.

langchain-salesforce implements tools enabling LLMs to interact with Salesforce data.

See detail on available tools here.

**Examples**:

```bash
pip install langchain-salesforce
```

---

## SambaNova | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/sambanova/

**Contents**:
- SambaNova
  - SambaNovaCloud​
  - SambaStudio​
- Installation and Setup​
- Chat models​
- Embedding Models​

Customers are turning to SambaNova to quickly deploy state-of-the-art AI capabilities to gain competitive advantage. Our purpose-built enterprise-scale AI platform is the technology backbone for the next generation of AI computing. We power the foundation models that unlock the valuable business insights trapped in data.

Designed for AI, the SambaNova RDU was built with a revolutionary dataflow architecture. This design makes the RDU significantly more efficient for these workloads than GPUs as it eliminates redundant calls to memory, which are an inherent limitation of how GPUs function. This built-in efficiency is one of the features that makes the RDU capable of much higher performance than GPUs in a fraction of the footprint.

On top of our architecture We have developed some platforms that allow companies and developers to get full advantage of the RDU processors and open source models.

SambaNova's SambaNova Cloud is a platform for performing inference with open-source models

You can obtain a free SambaNovaCloud API key here

SambaNova's SambaStudio is a rich, GUI-based platform that provides the functionality to train, deploy, and manage models in SambaNova DataScale systems.

Install the integration package:

set your API key it as an environment variable:

If you are a SambaNovaCloud user:

or if you are SambaStudio User

For a more detailed walkthrough of the ChatSambaNovaCloud component, see this notebook

For a more detailed walkthrough of the ChatSambaStudio component, see this notebook

For a more detailed walkthrough of the SambaNovaCloudEmbeddings component, see this notebook

For a more detailed walkthrough of the SambaStudioEmbeddings component, see this notebook

API Reference langchain-sambanova

**Examples**:

```bash
pip install langchain-sambanova
```

```bash
export SAMBANOVA_API_KEY="your-sambanova-cloud-api-key-here"
```

```bash
export SAMBASTUDIO_API_KEY="your-sambastudio-api-key-here"
```

---

## ScrapeGraph AI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/scrapegraph/

**Contents**:
- ScrapeGraph AI
- Installation and Setup​
- Tools​

ScrapeGraph AI is a service that provides AI-powered web scraping capabilities. It offers tools for extracting structured data, converting webpages to markdown, and processing local HTML content using natural language prompts.

Install the required packages:

There are four tools available:

Each tool serves a specific purpose:

**Examples**:

```bash
pip install langchain-scrapegraph
```

```bash
export SGAI_API_KEY="your-scrapegraph-api-key"
```

```python
from langchain_scrapegraph.tools import (    SmartScraperTool,    # Extract structured data from websites    SmartCrawlerTool,    # Extract data from multiple pages with crawling    MarkdownifyTool,     # Convert webpages to markdown    GetCreditsTool,      # Check remaining API credits)
```

---

## Scrapeless | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/scrapeless/

**Contents**:
- Scrapeless
- Installation and Setup​
- Tools​

Scrapeless offers flexible and feature-rich data acquisition services with extensive parameter customization and multi-format export support.

You'll need to set up your Scrapeless API key:

The Scrapeless integration provides several tools:

**Examples**:

```bash
pip install langchain-scrapeless
```

```python
import osos.environ["SCRAPELESS_API_KEY"] = "your-api-key"
```

---

## Security Policy | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/security/

**Contents**:
- Security Policy
- Best practices​
- Reporting OSS Vulnerabilities​
  - In-Scope Targets​
  - Out of Scope Targets​
- Reporting LangSmith Vulnerabilities​
  - Other Security Concerns​

LangChain has a large ecosystem of integrations with various external resources like local and remote file systems, APIs and databases. These integrations allow developers to create versatile applications that combine the power of LLMs with the ability to access, interact with and manipulate external resources.

When building such applications, developers should remember to follow good security practices:

Risks of not doing so include, but are not limited to:

Example scenarios with mitigation strategies:

If you're building applications that access external resources like file systems, APIs or databases, consider speaking with your company's security team to determine how to best design and secure your applications.

LangChain is partnered with huntr by Protect AI to provide a bounty program for our open source projects.

Please report security vulnerabilities associated with the LangChain open source projects at huntr.

Before reporting a vulnerability, please review:

The following packages and repositories are eligible for bug bounties:

All out of scope targets defined by huntr as well as:

Please report security vulnerabilities associated with LangSmith by email to security@langchain.dev.

For any other security concerns, please contact us at security@langchain.dev.

---

## Sema4 (fka Robocorp) | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/robocorp/

**Contents**:
- Sema4 (fka Robocorp)
- Installation and Setup​
- Tool​
- Toolkit​

Robocorp helps build and operate Python workers that run seamlessly anywhere at any scale

You need to install langchain-robocorp python package:

You will need a running instance of Action Server to communicate with from your agent application. See the Robocorp Quickstart on how to setup Action Server and create your Actions.

You can bootstrap a new project using Action Server new command.

**Examples**:

```bash
pip install langchain-robocorp
```

```bash
action-server newcd ./your-project-nameaction-server start
```

```python
from langchain_robocorp.toolkits import ActionServerRequestTool
```

---

## SingleStore Integration | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/singlestore/

**Contents**:
- SingleStore Integration

SingleStore is a high-performance, distributed SQL database designed to excel in both cloud and on-premises environments. It offers a versatile feature set, seamless deployment options, and exceptional performance.

This integration provides the following components to leverage SingleStore's capabilities:

These components enable efficient document storage, embedding management, and advanced search capabilities, combining full-text and vector-based search for fast and accurate queries.

**Examples**:

```python
from langchain_singlestore import (    SingleStoreChatMessageHistory,    SingleStoreLoader,    SingleStoreSemanticCache,    SingleStoreVectorStore,)
```

---

## Smabbler | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/galaxia/

**Contents**:
- Smabbler
- Galaxia
- Installation​
- Usage​

Smabbler’s graph-powered platform boosts AI development by transforming data into a structured knowledge foundation.

Galaxia Knowledge Base is an integrated knowledge base and retrieval mechanism for RAG. In contrast to standard solution, it is based on Knowledge Graphs built using symbolic NLP and Knowledge Representation solutions. Provided texts are analysed and transformed into Graphs containing text, language and semantic information. This rich structure allows for retrieval that is based on semantic information, not on vector similarity/distance.

Implementing RAG using Galaxia involves first uploading your files to Galaxia, analyzing them there and then building a model (knowledge graph). When the model is built, you can use GalaxiaRetriever to connect to the API and start retrieving.

More information: docs

**Examples**:

```text
pip install langchain-galaxia-retriever
```

```text
from langchain_galaxia_retriever.retriever import GalaxiaRetrievergr = GalaxiaRetriever(    api_url="beta.api.smabbler.com",    api_key="<key>",    knowledge_base_id="<knowledge_base_id>",    n_retries=10,    wait_time=5,)result = gr.invoke('<test question>')print(result)
```

---

## Snowflake | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/snowflake/

**Contents**:
- Snowflake
- Embedding models​
- Document loader​

Snowflake is a cloud-based data-warehousing platform that allows you to store and query large amounts of data.

This page covers how to use the Snowflake ecosystem within LangChain.

Snowflake offers their open-weight arctic line of embedding models for free on Hugging Face. The most recent model, snowflake-arctic-embed-m-v1.5 feature matryoshka embedding which allows for effective vector truncation. You can use these models via the HuggingFaceEmbeddings connector:

You can use the SnowflakeLoader to load data from Snowflake:

**Examples**:

```shell
pip install langchain-community sentence-transformers
```

```python
from langchain_huggingface import HuggingFaceEmbeddingsmodel = HuggingFaceEmbeddings(model_name="snowflake/arctic-embed-m-v1.5")
```

```python
from langchain_community.document_loaders import SnowflakeLoader
```

---

## Streaming | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/streaming/

**Contents**:
- Streaming
- Overview​
- What to stream in LLM applications​
  - 1. Streaming LLM outputs​
  - 2. Streaming pipeline or workflow progress​
  - 3. Streaming custom data​
- Streaming APIs​
  - stream() and astream()​

Streaming is crucial for enhancing the responsiveness of applications built on LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves user experience (UX), particularly when dealing with the latency of LLMs.

Generating full responses from LLMs often incurs a delay of several seconds, which becomes more noticeable in complex applications with multiple model calls. Fortunately, LLMs generate responses iteratively, allowing for intermediate results to be displayed as they are produced. By streaming these intermediate outputs, LangChain enables smoother UX in LLM-powered apps and offers built-in support for streaming at the core of its design.

In this guide, we'll discuss streaming in LLM applications and explore how LangChain's streaming APIs facilitate real-time output from various components in your application.

In applications involving LLMs, several types of data can be streamed to improve user experience by reducing perceived latency and increasing transparency. These include:

The most common and critical data to stream is the output generated by the LLM itself. LLMs often take time to generate full responses, and by streaming the output in real-time, users can see partial results as they are produced. This provides immediate feedback and helps reduce the wait time for users.

Beyond just streaming LLM output, it’s useful to stream progress through more complex workflows or pipelines, giving users a sense of how the application is progressing overall. This could include:

In LangGraph Workflows: With LangGraph, workflows are composed of nodes and edges that represent various steps. Streaming here involves tracking changes to the graph state as individual nodes request updates. This allows for more granular monitoring of which node in the workflow is currently active, giving real-time updates about the status of the workflow as it progresses through different stages.

In LCEL Pipelines: Streaming upd

*[Content truncated - see full docs]*

**Examples**:

```python
for chunk in component.stream(some_input):    # IMPORTANT: Keep the processing of each chunk as efficient as possible.    # While you're processing the current chunk, the upstream component is    # waiting to produce the next one. For example, if working with LangGraph,    # graph execution is paused while the current chunk is being processed.    # In extreme cases, this could even result in timeouts (e.g., when llm outputs are    # streamed from an API that has a timeout).    print(chunk)
```

```python
from langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_anthropic import ChatAnthropicmodel = ChatAnthropic(model="claude-3-7-sonnet-20250219")prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")parser = StrOutputParser()chain = prompt | model | parserasync for event in chain.astream_events({"topic": "parrot"}):    kind = event["event"]    if kind == "on_chat_model_stream":        print(event, end="|", flus
...
```

```python
def node(state):    ...    # The code below uses the invoke method, but LangChain will    # automatically switch to streaming mode    # when it detects that the overall    # application is being streamed.    ai_message = model.invoke(state["messages"])    ...for chunk in compiled_graph.stream(..., mode="messages"):    ...
```

---

## String-in, string-out llms | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/text_llms/

**Contents**:
- String-in, string-out llms

You are probably looking for the Chat Model Concept Guide page for more information.

LangChain has implementations for older language models that take a string as input and return a string as output. These models are typically named without the "Chat" prefix (e.g., Ollama, Anthropic, OpenAI, etc.), and may include the "LLM" suffix (e.g., OllamaLLM, AnthropicLLM, OpenAILLM, etc.). These models implement the BaseLLM interface.

Users should be using almost exclusively the newer Chat Models as most model providers have adopted a chat like interface for interacting with language models.

---

## Structured outputs | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/structured_outputs/

**Contents**:
- Structured outputs
- Overview​
- Key concepts​
- Recommended usage​
- Schema definition​
- Returning structured output​
  - Using tool calling​
  - JSON mode​

For many applications, such as chatbots, models need to respond to users directly in natural language. However, there are scenarios where we need models to output in a structured format. For example, we might want to store the model output in a database and ensure that the output conforms to the database schema. This need motivates the concept of structured output, where models can be instructed to respond with a particular output structure.

This pseudocode illustrates the recommended workflow when using structured output. LangChain provides a method, with_structured_output(), that automates the process of binding the schema to the model and parsing the output. This helper function is available for all model providers that support structured output.

When combining structured output with additional tools, bind tools first, then apply structured output:

The central concept is that the output structure of model responses needs to be represented in some way. While types of objects you can use depend on the model you're working with, there are common types of objects that are typically allowed or recommended for structured output in Python.

The simplest and most common format for structured output is a JSON-like structure, which in Python can be represented as a dictionary (dict) or list (list). JSON objects (or dicts in Python) are often used directly when the tool requires raw, flexible, and minimal-overhead structured data.

As a second example, Pydantic is particularly useful for defining structured output schemas because it offers type hints and validation. Here's an example of a Pydantic schema:

With a schema defined, we need a way to instruct the model to use it. While one approach is to include this schema in the prompt and ask nicely for the model to use it, this is not recommended. Several more powerful methods that utilizes native features in the model provider's API are available.

Many model providers support tool calling, a concept discussed in more de

*[Content truncated - see full docs]*

**Examples**:

```python
# Define schemaschema = {"foo": "bar"}# Bind schema to modelmodel_with_structure = model.with_structured_output(schema)# Invoke the model to produce structured output that matches the schemastructured_output = model_with_structure.invoke(user_input)
```

```python
# Correctmodel_with_tools = model.bind_tools([tool1, tool2])structured_model = model_with_tools.with_structured_output(schema)# Incorrect - will cause tool resolution errorsstructured_model = model.with_structured_output(schema)broken_model = structured_model.bind_tools([tool1, tool2])
```

```json
{  "answer": "The answer to the user's question",  "followup_question": "A followup question the user could ask"}
```

---

## SurrealDB | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/surrealdb/

**Contents**:
- SurrealDB
- Installation and Setup​
- Vector Store​

SurrealDB is a unified, multi-model database purpose-built for AI systems. It combines structured and unstructured data (including vector search, graph traversal, relational queries, full-text search, document storage, and time-series data) into a single ACID-compliant engine, scaling from a 3 MB edge binary to petabyte-scale clusters in the cloud. By eliminating the need for multiple specialized stores, SurrealDB simplifies architectures, reduces latency, and ensures consistency for AI workloads.

Why SurrealDB Matters for GenAI Systems

This notebook covers how to get started with the SurrealDB vector store.

Find more examples in the repository.

**Examples**:

```bash
pip install langchain-surrealdb
```

---

## Tableau | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/tableau/

**Contents**:
- Tableau
- Installation and Setup​
- Tools​

Tableau is an analytics platform that enables anyone to see and understand data.

See detail on available tools here.

**Examples**:

```bash
pip install langchain-tableau
```

---

## Taiga | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/taiga/

**Contents**:
- Taiga
- Installation and Setup​
- Tools​
- Toolkit​
- Future Integrations​

Taiga is an open-source project management platform designed for agile teams, offering features like Kanban, Scrum, and issue tracking.

Install the langchain-taiga package:

You must provide a logins via environment variable so the tools can authenticate.

TaigaToolkit groups multiple Taiga-related tools into a single interface.

Check the Taiga Developer Docs for more information, and watch for updates or advanced usage examples in the langchain_taiga GitHub repo.

**Examples**:

```bash
pip install langchain-taiga
```

```bash
export TAIGA_URL="https://taiga.xyz.org/"export TAIGA_API_URL="https://taiga.xyz.org/"export TAIGA_USERNAME="username"export TAIGA_PASSWORD="pw"export OPENAI_API_KEY="OPENAI_API_KEY"
```

```python
from langchain_taiga.toolkits import TaigaToolkittoolkit = TaigaToolkit()tools = toolkit.get_tools()
```

---

## Testing | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/testing/

**Contents**:
- Testing
- Unit Tests​
- Integration Tests​
- Standard Tests​

Testing is a critical part of the development process that ensures your code works as expected and meets the desired quality standards.

In the LangChain ecosystem, we have 2 main types of tests: unit tests and integration tests.

For integrations that implement standard LangChain abstractions, we have a set of standard tests (both unit and integration) that help maintain compatibility between different components and ensure reliability of high-usage ones.

Definition: Unit tests are designed to validate the smallest parts of your code—individual functions or methods—ensuring they work as expected in isolation. They do not rely on external systems or integrations.

Example: Testing the convert_langchain_aimessage_to_dict function to confirm it correctly converts an AI message to a dictionary format:

Definition: Integration tests validate that multiple components or systems work together as expected. For tools or integrations relying on external services, these tests often ensure end-to-end functionality.

Example: Testing ParrotMultiplyTool with access to an API service that multiplies two numbers and adds 80:

Definition: Standard tests are pre-defined tests provided by LangChain to ensure consistency and reliability across all tools and integrations. They include both unit and integration test templates tailored for LangChain components.

Example: Subclassing LangChain's ToolsUnitTests or ToolsIntegrationTests to automatically run standard tests:

To learn more, check out our guide on how to add standard tests to an integration.

**Examples**:

```python
from langchain_core.messages import AIMessage, ToolCall, convert_to_openai_messagesdef test_convert_to_openai_messages():    ai_message = AIMessage(        content="Let me call that tool for you!",        tool_calls=[            ToolCall(name='parrot_multiply_tool', id='1', args={'a': 2, 'b': 3}),        ]    )    result = convert_to_openai_messages(ai_message)    expected = {        "role": "assistant",        "tool_calls": [            {                "type": "function",                "id": 
...
```

```python
def test_integration_with_service():    tool = ParrotMultiplyTool()    result = tool.invoke({"a": 2, "b": 3})    assert result == 86
```

```python
from langchain_tests.unit_tests import ToolsUnitTestsclass TestParrotMultiplyToolUnit(ToolsUnitTests):    @property    def tool_constructor(self):        return ParrotMultiplyTool    def tool_invoke_params_example(self):        return {"a": 2, "b": 3}
```

---

## Text splitters | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/text_splitters/

**Contents**:
- Text splitters
- Overview​
- Key concepts​
- Why split documents?​
- Approaches​
  - Length-based​
  - Text-structured based​
  - Document-structured based​

Document splitting is often a crucial preprocessing step for many applications. It involves breaking down large texts into smaller, manageable chunks. This process offers several benefits, such as ensuring consistent processing of varying document lengths, overcoming input size limitations of models, and improving the quality of text representations used in retrieval systems. There are several strategies for splitting documents, each with its own advantages.

Text splitters split documents into smaller chunks for use in downstream applications.

There are several reasons to split documents:

Now, the next question is how to split the documents into chunks! There are several strategies, each with its own advantages.

The most intuitive strategy is to split documents based on their length. This simple yet effective approach ensures that each chunk doesn't exceed a specified size limit. Key benefits of length-based splitting:

Types of length-based splitting:

Example implementation using LangChain's CharacterTextSplitter with token-based splitting:

Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain's RecursiveCharacterTextSplitter implements this concept:

Here is example usage:

Some documents have an inherent structure, such as HTML, Markdown, or JSON files. In these cases, it's beneficial to split the document based on its structure, as it often naturally groups semantically related text. Key benefits of structure-based splitting:

Examples of structure-based splitting:

Unlike the previous methods, semantic-based splitting actually considers the content of the text. While other approaches use document or text structure as proxies for semantic meaning, this method directly analyzes the text's seman

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_text_splitters import CharacterTextSplittertext_splitter = CharacterTextSplitter.from_tiktoken_encoder(    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0)texts = text_splitter.split_text(document)
```

```python
from langchain_text_splitters import RecursiveCharacterTextSplittertext_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)texts = text_splitter.split_text(document)
```

---

## Tilores | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/tilores/

**Contents**:
- Tilores
- Installation and Setup​
- Toolkits​

Tilores is a platform that provides advanced entity resolution solutions for data integration and management. Using cutting-edge algorithms, machine learning, and a user-friendly interfaces, Tilores helps organizations match, resolve, and consolidate data from disparate sources, ensuring high-quality, consistent information.

To access Tilores, you need to create and configure an instance. If you prefer to test out Tilores first, you can use the read-only demo credentials.

Please refer to the Tilores documentation on how to create your own instance.

You can use the TiloresTools to query data from Tilores:

**Examples**:

```python
%pip install --upgrade tilores-langchain
```

```python
import osfrom tilores import TiloresAPIos.environ["TILORES_API_URL"] = "<api-url>"os.environ["TILORES_TOKEN_URL"] = "<token-url>"os.environ["TILORES_CLIENT_ID"] = "<client-id>"os.environ["TILORES_CLIENT_SECRET"] = "<client-secret>"tilores = TiloresAPI.from_environ()
```

```python
from tilores_langchain import TiloresTools
```

---

## Timbr | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/timbr/

**Contents**:
- Timbr
- Quickstart​
  - Installation​
    - Install the package​
    - Optional: Install with selected LLM provider​
- Configuration​
  - Timbr Connection Parameters​
  - LLM Configuration Parameters​

Timbr integrates natural language inputs with Timbr's ontology-driven semantic layer. Leveraging Timbr's robust ontology capabilities, the SDK integrates with Timbr data models and leverages semantic relationships and annotations, enabling users to query data using business-friendly language.

Timbr provides a pre-built SQL agent, TimbrSqlAgent, which can be used for end-to-end purposes from user prompt, through semantic SQL query generation and validation, to query execution and result analysis.

For customizations and partial usage, you can use LangChain chains and LangGraph nodes with our 5 main tools:

Additionally, langchain-timbr provides TimbrLlmConnector for manual integration with Timbr's semantic layer using LLM providers. This connector includes the following methods:

Choose one of: openai, anthropic, google, azure_openai, snowflake, databricks (or 'all')

Starting from langchain-timbr v2.0.0, all chains, agents, and nodes support optional environment-based configuration. You can set the following environment variables to provide default values and simplify setup for the provided tools:

When these environment variables are set, the corresponding parameters (url, token, ontology) become optional in all chain and agent constructors and will use the environment values as defaults.

When LLM environment variables are set, the llm parameter becomes optional and will use the LlmWrapper with environment configuration.

Example environment setup:

Import and utilize your intended chain/node, or use TimbrLlmConnector to manually integrate with Timbr's semantic layer. For a complete agent working example, see the Timbr tool page.

**Examples**:

```bash
pip install langchain-timbr
```

```bash
pip install 'langchain-timbr[<your selected providers, separated by comma without spaces>]'
```

```bash
# Timbr connectionexport TIMBR_URL="https://your-timbr-app.com/"export TIMBR_TOKEN="tk_XXXXXXXXXXXXXXXXXXXXXXXX"export TIMBR_ONTOLOGY="timbr_knowledge_graph"# LLM configurationexport LLM_TYPE="openai-chat"export LLM_API_KEY="your-openai-api-key"export LLM_MODEL="gpt-4o"export LLM_TEMPERATURE="0.1"export LLM_ADDITIONAL_PARAMS='{"max_tokens": 1000}'
```

---

## Together AI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/together/

**Contents**:
- Together AI
- Installation​
- Environment​
- Example​

Together AI offers an API to query 50+ leading open-source models in a couple lines of code.

This example goes over how to use LangChain to interact with Together AI models.

To use Together AI, you'll need an API key which you can find here: https://api.together.ai/settings/api-keys. This can be passed in as an init param together_api_key or set as environment variable TOGETHER_API_KEY.

**Examples**:

```python
%pip install --upgrade langchain-together
```

```python
# Querying chat models with Together AIfrom langchain_together import ChatTogether# choose from our 50+ models here: https://docs.together.ai/docs/inference-modelschat = ChatTogether(    # together_api_key="YOUR_API_KEY",    model="meta-llama/Llama-3-70b-chat-hf",)# stream the response back from the modelfor m in chat.stream("Tell me fun things to do in NYC"):    print(m.content, end="", flush=True)# if you don't want to do streaming, you can use the invoke method# chat.invoke("Tell me fun thing
...
```

```python
# Querying code and language models with Together AIfrom langchain_together import Togetherllm = Together(    model="codellama/CodeLlama-70b-Python-hf",    # together_api_key="...")print(llm.invoke("def bubble_sort(): "))
```

---

## Tokens | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/tokens/

**Contents**:
- Tokens
- What is a token?​
- How tokens work in language models​
- Tokens don’t have to be text​
- Why not use characters?​
- How tokens correspond to text​

Modern large language models (LLMs) are typically based on a transformer architecture that processes a sequence of units known as tokens. Tokens are the fundamental elements that models use to break down input and generate output. In this section, we'll discuss what tokens are and how they are used by language models.

A token is the basic unit that a language model reads, processes, and generates. These units can vary based on how the model provider defines them, but in general, they could represent:

The way the model tokenizes the input depends on its tokenizer algorithm, which converts the input into tokens. Similarly, the model’s output comes as a stream of tokens, which is then decoded back into human-readable text.

The reason language models use tokens is tied to how they understand and predict language. Rather than processing characters or entire sentences directly, language models focus on tokens, which represent meaningful linguistic units. Here's how the process works:

Input Tokenization: When you provide a model with a prompt (e.g., "LangChain is cool!"), the tokenizer algorithm splits the text into tokens. For example, the sentence could be tokenized into parts like ["Lang", "Chain", " is", " cool", "!"]. Note that token boundaries don’t always align with word boundaries.

Processing: The transformer architecture behind these models processes tokens sequentially to predict the next token in a sentence. It does this by analyzing the relationships between tokens, capturing context and meaning from the input.

Output Generation: The model generates new tokens one by one. These output tokens are then decoded back into human-readable text.

Using tokens instead of raw characters allows the model to focus on linguistically meaningful units, which helps it capture grammar, structure, and context more effectively.

Although tokens are most commonly used to represent text, they don’t have to be limited to textual data. Tokens can also serve as abstract represe

*[Content truncated - see full docs]*

---

## Tool calling | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/tool_calling/

**Contents**:
- Tool calling
- Overview​
- Key concepts​
- Recommended usage​
- Tool creation​
- Tool binding​
- Tool calling​
- Tool execution​

Many AI applications interact directly with humans. In these cases, it is appropriate for models to respond in natural language. But what about cases where we want a model to also interact directly with systems, such as databases or an API? These systems often have a particular input schema; for example, APIs frequently have a required payload structure. This need motivates the concept of tool calling. You can use tool calling to request model responses that match a particular schema.

You will sometimes hear the term function calling. We use this term interchangeably with tool calling.

This pseudocode illustrates the recommended workflow for using tool calling. Created tools are passed to .bind_tools() method as a list. This model can be called, as usual. If a tool call is made, model's response will contain the tool call arguments. The tool call arguments can be passed directly to the tool.

The recommended way to create a tool is using the @tool decorator.

Many model providers support tool calling.

See our model integration page for a list of providers that support tool calling.

The central concept to understand is that LangChain provides a standardized interface for connecting tools to models. The .bind_tools() method can be used to specify which tools are available for a model to call.

As a specific example, let's take a function multiply and bind it as a tool to a model that supports tool calling.

A key principle of tool calling is that the model decides when to use a tool based on the input's relevance. The model doesn't always need to call a tool. For example, given an unrelated input, the model would not call the tool:

The result would be an AIMessage containing the model's response in natural language (e.g., "Hello!"). However, if we pass an input relevant to the tool, the model should choose to call it:

As before, the output result will be an AIMessage. But, if the tool was called, result will have a tool_calls attribute. This attribute includes e

*[Content truncated - see full docs]*

**Examples**:

```python
# Tool creationtools = [my_tool]# Tool bindingmodel_with_tools = model.bind_tools(tools)# Tool callingresponse = model_with_tools.invoke(user_input)
```

```python
from langchain_core.tools import tool@tooldef multiply(a: int, b: int) -> int:    """Multiply a and b."""    return a * b
```

```python
model_with_tools = model.bind_tools(tools_list)
```

---

## Tracing | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/tracing/

**Contents**:
- Tracing

A trace is essentially a series of steps that your application takes to go from input to output. Traces contain individual steps called runs. These can be individual calls from a model, retriever, tool, or sub-chains. Tracing gives you observability inside your chains and agents, and is vital in diagnosing issues.

For a deeper dive, check out this LangSmith conceptual guide.

---

## Unstructured | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/unstructured/

**Contents**:
- Unstructured
- Installation and Setup​
- Data Loaders​
  - UnstructuredLoader​
  - UnstructuredCHMLoader​
  - UnstructuredCSVLoader​
  - UnstructuredEmailLoader​
  - UnstructuredEPubLoader​

The unstructured package from Unstructured.IO extracts clean text from raw source documents like PDFs and Word documents. This page covers how to use the unstructured ecosystem within LangChain.

If you are using a loader that runs locally, use the following steps to get unstructured and its dependencies running.

For the smallest installation footprint and to take advantage of features not available in the open-source unstructured package, install the Python SDK with pip install unstructured-client along with pip install langchain-unstructured to use the UnstructuredLoader and partition remotely against the Unstructured API. This loader lives in a LangChain partner repo instead of the langchain-community repo and you will need an api_key, which you can generate a free key here.

To run everything locally, install the open-source python package with pip install unstructured along with pip install langchain-community and use the same UnstructuredLoader as mentioned above.

Install the following system dependencies if they are not already available on your system with e.g. brew install for Mac. Depending on what document types you're parsing, you may not need all of these.

When running locally, Unstructured also recommends using Docker by following this guide to ensure all system dependencies are installed correctly.

The Unstructured API requires API keys to make requests. You can request an API key here and start using it today! Checkout the README here here to get started making API calls. We'd love to hear your feedback, let us know how it goes in our community slack. And stay tuned for improvements to both quality and performance! Check out the instructions here if you'd like to self-host the Unstructured API or run it locally.

The primary usage of Unstructured is in data loaders.

See a usage example to see how you can use this loader for both partitioning locally and remotely with the serverless Unstructured API.

CHM means Microsoft Compiled HTML Help.

A co

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_unstructured import UnstructuredLoader
```

```python
from langchain_community.document_loaders import UnstructuredCHMLoader
```

```python
from langchain_community.document_loaders import UnstructuredCSVLoader
```

---

## Upstage | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/upstage/

**Contents**:
- Upstage
  - Upstage LangChain integrations​
- Installation and Setup​
- Chat models​
  - Solar LLM​
- Embedding models​
- Document loader​
  - Document Parse​

Upstage is a leading artificial intelligence (AI) company specializing in delivering above-human-grade performance LLM components.

Solar Pro is an enterprise-grade LLM optimized for single-GPU deployment, excelling in instruction-following and processing structured formats like HTML and Markdown. It supports English, Korean, and Japanese with top multilingual performance and offers domain expertise in finance, healthcare, and legal.

Other than Solar, Upstage also offers features for real-world RAG (retrieval-augmented generation), such as Document Parse and Groundedness Check.

See documentations for more details about the models and features.

Install langchain-upstage package:

Get API Keys and set environment variable UPSTAGE_API_KEY.

**Examples**:

```bash
pip install -qU langchain-core langchain-upstage
```

```python
import osos.environ["UPSTAGE_API_KEY"] = "YOUR_API_KEY"
```

```python
from langchain_upstage import ChatUpstagechat = ChatUpstage()response = chat.invoke("Hello, how are you?")print(response)
```

---

## VDMS | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/vdms/

**Contents**:
- VDMS
- Installation and Setup​
  - Install Client​
  - Install Database​
- VectorStore​

VDMS is a storage solution for efficient access of big-”visual”-data that aims to achieve cloud scale by searching for relevant visual data via visual metadata stored as a graph and enabling machine friendly enhancements to visual data for faster access.

There are two ways to get started with VDMS:

Install VDMS on your local machine via docker

Install VDMS directly on your local machine. Please see installation instructions.

To import this vectorstore:

To import the VDMS Client connector:

For a more detailed walkthrough of the VDMS wrapper, see this guide.

**Examples**:

```bash
pip install langchain-vdms
```

```bash
docker run -d -p 55555:55555 intellabs/vdms:latest
```

```python
from langchain_vdms import VDMSfrom langchain_vdms.vectorstores import VDMS
```

---

## Valthera | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/valthera/

**Contents**:
- Valthera
- Installation and Setup​
  - Install langchain-valthera​
  - Example: Initializing the ValtheraTool for LangChain​

Valthera is an open-source framework that empowers LLM Agents to drive meaningful, context-aware user engagement. It evaluates user motivation and ability in real time, ensuring that notifications and actions are triggered only when users are most receptive.

langchain-valthera integrates Valthera with LangChain, enabling developers to build smarter, behavior-driven engagement systems that deliver personalized interactions.

Install the LangChain Valthera package via pip:

Import the ValtheraTool:

This example shows how to initialize the ValtheraTool using a DataAggregator and configuration for motivation and ability scoring.

The langchain-valthera integration allows you to assess user behavior and decide on the best course of action for engagement, ensuring that interactions are both timely and relevant within your LangChain applications.

**Examples**:

```bash
pip install -U langchain-valthera
```

```python
from langchain_valthera.tools import ValtheraTool
```

```python
import osfrom langchain_openai import ChatOpenAIfrom valthera.aggregator import DataAggregatorfrom mocks import hubspot, posthog, snowflake  # Replace these with your actual connector implementationsfrom langchain_valthera.tools import ValtheraTool# Initialize the DataAggregator with your data connectorsdata_aggregator = DataAggregator(    connectors={        "hubspot": hubspot(),        "posthog": posthog(),        "app_db": snowflake()    })# Initialize the ValtheraTool with your scoring confi
...
```

---

## Valyu Deep Search | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/valyu/

**Contents**:
- Valyu Deep Search
- Setup​
- Context Retriever​
- Context Search Tool​

Valyu allows AI applications and agents to search the internet and proprietary data sources for relevant LLM ready information.

This notebook goes over how to use Valyu in LangChain.

First, get an Valyu API key and add it as an environment variable. Get $10 free credit by signing up here.

The integration lives in the langchain-valyu package.

In order to use the package, you will also need to set the VALYU_API_KEY environment variable to your Valyu API key.

You can use the ValyuContextRetriever in a standard retrieval pipeline.

You can use the ValyuSearchTool for advanced search queries.

**Examples**:

```python
%pip install -qU langchain-valyu
```

```python
from langchain_valyu import ValyuRetrievervalyu_api_key = "YOUR API KEY"# Create a new instance of the ValyuRetrievervalyu_retriever = ValyuRetriever(    k=5,    search_type="all",    relevance_threshold=0.5,    max_price=20.0,    start_date="2024-01-01",    end_date="2024-12-31",    valyu_api_key=valyu_api_key,)# Search for a query and save the resultsdocs = valyu_retriever.invoke("What are the benefits of renewable energy?")# Print the resultsfor doc in docs:    print(doc.page_content)    prin
...
```

```python
from langchain_valyu import ValyuSearchTool# Initialize the ValyuSearchToolsearch_tool = ValyuSearchTool(valyu_api_key="YOUR API KEY")# Perform a search querysearch_results = search_tool._run(    query="What are agentic search-enhanced large reasoning models?",    search_type="all",    max_num_results=5,    relevance_threshold=0.5,    max_price=20.0,    start_date="2024-01-01",    end_date="2024-12-31",)print("Search Results:", search_results)
```

---

## Vectara | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/vectara/

**Contents**:
- Vectara
- Setup​
- Getting Started
- Vectara RAG (retrieval augmented generation)​
- Vectara Chat​
- Vectara as self-querying retriever​
- Vectara tools​

Vectara is the trusted AI Assistant and Agent platform which focuses on enterprise readiness for mission-critical applications. Vectara serverless RAG-as-a-service provides all the components of RAG behind an easy-to-use API, including:

For more information:

This notebook shows how to use the basic retrieval functionality, when utilizing Vectara just as a Vector Store (without summarization), incuding: similarity_search and similarity_search_with_score as well as using the LangChain as_retriever functionality.

To use the VectaraVectorStore you first need to install the partner package.

To get started, use the following steps:

To use LangChain with Vectara, you'll need to have these two values: corpus_key and api_key. You can provide VECTARA_API_KEY to LangChain in two ways:

Include in your environment these two variables: VECTARA_API_KEY.

For example, you can set these variables using os.environ and getpass as follows:

In this notebook we assume they are provided in the environment.

First we load the state-of-the-union text into Vectara.

Note that we use the add_files interface which does not require any local processing or chunking - Vectara receives the file content and performs all the necessary pre-processing, chunking and embedding of the file into its knowledge store.

In this case it uses a .txt file but the same works for many other file types.

We now create a VectaraQueryConfig object to control the retrieval and summarization options:

Using this configuration, let's create a LangChain Runnable object that encpasulates the full Vectara RAG pipeline, using the as_rag method:

We can also use the streaming interface like this:

For more details about Vectara as VectorStore go to this notebook.

In most uses of LangChain to create chatbots, one must integrate a special memory component that maintains the history of chat sessions and then uses that history to ensure the chatbot is aware of conversation history.

With Vectara Chat - all of that is pe

*[Content truncated - see full docs]*

**Examples**:

```python
!uv pip install -U pip && uv pip install -qU langchain-vectara
```

```python
import osimport getpassos.environ["VECTARA_API_KEY"] = getpass.getpass("Vectara API Key:")
```

```python
vectara = Vectara(    vectara_api_key=vectara_api_key)
```

---

## Vector stores | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/vectorstores/

**Contents**:
- Vector stores
- All Vectorstores​

A vector store stores embedded data and performs similarity search.

Select embedding model:

**Examples**:

```bash
pip install -qU langchain-openai
```

```python
import getpassimport osif not os.environ.get("OPENAI_API_KEY"):  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")from langchain_openai import OpenAIEmbeddingsembeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

```bash
pip install -qU langchain-core
```

---

## Vector stores | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/vectorstores/

**Contents**:
- Vector stores
- Overview​
- Integrations​
- Interface​
- Initialization​
- Adding documents​
- Delete​
- Search​

This conceptual overview focuses on text-based indexing and retrieval for simplicity. However, embedding models can be multi-modal and vector stores can be used to store and retrieve a variety of data types beyond text.

Vector stores are specialized data stores that enable indexing and retrieving information based on vector representations.

These vectors, called embeddings, capture the semantic meaning of data that has been embedded.

Vector stores are frequently used to search over unstructured data, such as text, images, and audio, to retrieve relevant information based on semantic similarity rather than exact keyword matches.

LangChain has a large number of vectorstore integrations, allowing users to easily switch between different vectorstore implementations.

Please see the full list of LangChain vectorstore integrations.

LangChain provides a standard interface for working with vector stores, allowing users to easily switch between different vectorstore implementations.

The interface consists of basic methods for writing, deleting and searching for documents in the vector store.

Most vectors in LangChain accept an embedding model as an argument when initializing the vector store.

We will use LangChain's InMemoryVectorStore implementation to illustrate the API.

To add documents, use the add_documents method.

This API works with a list of Document objects. Document objects all have page_content and metadata attributes, making them a universal way to store unstructured text and associated metadata.

You should usually provide IDs for the documents you add to the vector store, so that instead of adding the same document multiple times, you can update the existing document.

To delete documents, use the delete method which takes a list of document IDs to delete.

Vector stores embed and store the documents that added. If we pass in a query, the vectorstore will embed the query, perform a similarity search over the embedded documents, and return the most sim

*[Content truncated - see full docs]*

**Examples**:

```python
from langchain_core.vectorstores import InMemoryVectorStore# Initialize with an embedding modelvector_store = InMemoryVectorStore(embedding=SomeEmbeddingModel())
```

```python
from langchain_core.documents import Documentdocument_1 = Document(    page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",    metadata={"source": "tweet"},)document_2 = Document(    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",    metadata={"source": "news"},)documents = [document_1, document_2]vector_store.add_documents(documents=documents)
```

```python
vector_store.add_documents(documents=documents, ids=["doc1", "doc2"])
```

---

## VoyageAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/voyageai/

**Contents**:
- VoyageAI
- Installation and Setup​
- Text Embedding Model​
- Reranking​

All functionality related to VoyageAI

VoyageAI Voyage AI builds embedding models, customized for your domain and company, for better retrieval quality.

Install the integration package with

Get a VoyageAI API key and set it as an environment variable (VOYAGE_API_KEY)

**Examples**:

```bash
pip install langchain-voyageai
```

```python
from langchain_voyageai import VoyageAIEmbeddings
```

```python
from langchain_voyageai import VoyageAIRerank
```

---

## Weaviate | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/weaviate/

**Contents**:
- Weaviate
- Installation and Setup​
- Vector Store​

Weaviate is an open-source vector database. It allows you to store data objects and vector embeddings from your favorite ML models, and scale seamlessly into billions of data objects.

Weaviate is a low-latency vector search engine with out-of-the-box support for different media types (text, images, etc.). It offers Semantic Search, Question-Answer Extraction, Classification, Customizable Models (PyTorch/TensorFlow/Keras), etc. Built from scratch in Go, Weaviate stores both objects and vectors, allowing for combining vector search with structured filtering and the fault tolerance of a cloud-native database. It is all accessible through GraphQL, REST, and various client-side programming languages.

Install the Python SDK:

There exists a wrapper around Weaviate indexes, allowing you to use it as a vectorstore, whether for semantic search or example selection.

To import this vectorstore:

For a more detailed walkthrough of the Weaviate wrapper, see this notebook

**Examples**:

```bash
pip install langchain-weaviate
```

```python
from langchain_weaviate import WeaviateVectorStore
```

---

## Welcome Contributors | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/contributing/

**Contents**:
- Welcome Contributors
- Tutorials​
- How-to guides​
- Reference​
- Community​
  - 💭 Forum​
  - 🚩 GitHub Issues​
  - 📢 Community Slack​

Hi there! Thank you for your interest in contributing to LangChain. As an open-source project in a fast developing field, we are extremely open to contributions, whether they involve new features, improved infrastructure, better documentation, or bug fixes.

More coming soon! We are working on tutorials to help you make your first contribution to the project.

We have a LangChain Forum where users can ask usage questions, discuss design decisions, and propose new features.

If you are able to help answer questions, please do so! This will allow the maintainers to spend more time focused on development and bug fixing.

Our issues page is kept up to date with bugs, docs improvements, and triaged feature requests that are being worked on.

There is a taxonomy of labels to help with sorting and discovery of issues of interest. Please use these to help organize issues. Check out the Help Wanted and Good First Issue tags for recommendations.

If you start working on an issue, please assign it to yourself.

If you are adding an issue, please try to keep it focused on a single, modular bug/improvement/feature. If two issues are related, or blocking, please link them rather than combining them.

We will try to keep these issues as up-to-date as possible, though with the rapid rate of development in this field some may get out of date. If you notice this happening, please let us know.

We have a community slack where you can ask questions, get help, and discuss the project with other contributors and users.

Our goal is to have the simplest developer setup possible. Should you experience any difficulty getting setup, please ask in community slack or open a forum post.

In a similar vein, we do enforce certain linting, formatting, and documentation standards in the codebase. If you are finding these difficult (or even just annoying) to work with, feel free to ask in community slack!

---

## Why LangChain? | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/concepts/why_langchain/

**Contents**:
- Why LangChain?
- Features​
- Standardized component interfaces​
  - Example: chat models​
  - Example: retrievers​
- Orchestration​
- Observability and evaluation​
- Conclusion​

The goal of langchain the Python package and LangChain the company is to make it as easy as possible for developers to build applications that reason. While LangChain originally started as a single open source package, it has evolved into a company and a whole ecosystem. This page will talk about the LangChain ecosystem as a whole. Most of the components within the LangChain ecosystem can be used by themselves - so if you feel particularly drawn to certain components but not others, that is totally fine! Pick and choose whichever components you like best for your own use case!

There are several primary needs that LangChain aims to address:

Standardized component interfaces: The growing number of models and related components for AI applications has resulted in a wide variety of different APIs that developers need to learn and use. This diversity can make it challenging for developers to switch between providers or combine components when building applications. LangChain exposes a standard interface for key components, making it easy to switch between providers.

Orchestration: As applications become more complex, combining multiple components and models, there's a growing need to efficiently connect these elements into control flows that can accomplish diverse tasks. Orchestration is crucial for building such applications.

Observability and evaluation: As applications become more complex, it becomes increasingly difficult to understand what is happening within them. Furthermore, the pace of development can become rate-limited by the paradox of choice. For example, developers often wonder how to engineer their prompt or which LLM best balances accuracy, latency, and cost. Observability and evaluations can help developers monitor their applications and rapidly answer these types of questions with confidence.

LangChain provides common interfaces for components that are central to many AI applications. As an example, all chat models implement the BaseChatModel inter

*[Content truncated - see full docs]*

**Examples**:

```python
# Tool creationtools = [my_tool]# Tool bindingmodel_with_tools = model.bind_tools(tools)
```

```python
# Define schemaschema = ...# Bind schema to modelmodel_with_structure = model.with_structured_output(schema)
```

```python
documents = my_retriever.invoke("What is the meaning of life?")
```

---

## Writer, Inc. | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/writer/

**Contents**:
- Writer, Inc.
- Installation and Setup​
- Chat model​
- PDF Parser​
- Text splitter​
- Tools calling​
  - Functions​
  - Graphs​

All functionality related to Writer

This page covers how to use the Writer ecosystem within LangChain. For further information see Writer docs. Palmyra is a Large Language Model (LLM) developed by Writer, Inc.

The Writer API is powered by a diverse set of Palmyra sub-models with different capabilities and price points.

Install the integration package with

Get an Writer API key and set it as an environment variable (WRITER_API_KEY)

Support of basic function calls defined via dicts, Pydantic, python functions etc.

Writer-specific remotely invoking tool

**Examples**:

```bash
pip install langchain-writer
```

```python
from langchain_writer import ChatWriter
```

```python
from langchain_writer.pdf_parser import PDFParser
```

---

## Xorbits Inference (Xinference) | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/xinference/

**Contents**:
- Xorbits Inference (Xinference)
- Installation and Setup​
- LLM​
  - Wrapper for Xinference​
  - Usage​
  - Embeddings​
  - Xinference LangChain partner package install​
- Chat Models​

This page demonstrates how to use Xinference with LangChain.

Xinference is a powerful and versatile library designed to serve LLMs, speech recognition models, and multimodal models, even on your laptop. With Xorbits Inference, you can effortlessly deploy and serve your or state-of-the-art built-in models using just a single command.

Xinference can be installed via pip from PyPI:

Xinference supports various models compatible with GGML, including chatglm, baichuan, whisper, vicuna, and orca. To view the builtin models, run the command:

You can start a local instance of Xinference by running:

You can also deploy Xinference in a distributed cluster. To do so, first start an Xinference supervisor on the server you want to run it:

Then, start the Xinference workers on each of the other servers where you want to run them on:

You can also start a local instance of Xinference by running:

Once Xinference is running, an endpoint will be accessible for model management via CLI or Xinference client.

For local deployment, the endpoint will be http://localhost:9997.

For cluster deployment, the endpoint will be http://${supervisor_host}:9997.

Then, you need to launch a model. You can specify the model names and other attributes including model_size_in_billions and quantization. You can use command line interface (CLI) to do it. For example,

A model uid will be returned.

For more information and detailed examples, refer to the example for xinference LLMs

Xinference also supports embedding queries and documents. See example for xinference embeddings for a more detailed demo.

Install the integration package with:

**Examples**:

```bash
pip install "xinference[all]"
```

```bash
xinference list --all
```

```bash
xinference-supervisor -H "${supervisor_host}"
```

---

## YDB | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/ydb/

**Contents**:
- YDB
- Installation and Setup​
- Vector Store​

All functionality related to YDB.

YDB is a versatile open source Distributed SQL Database that combines high availability and scalability with strong consistency and ACID transactions. It accommodates transactional (OLTP), analytical (OLAP), and streaming workloads simultaneously.

To import YDB vector store:

For a more detailed walkthrough of the YDB vector store, see this notebook.

**Examples**:

```bash
pip install langchain-ydb
```

```python
from langchain_ydb.vectorstores import YDB
```

---

## ZenRows | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/zenrows/

**Contents**:
- ZenRows
- Installation and Setup​
- Tools​
  - ZenRowsUniversalScraper​

ZenRows is an enterprise-grade web scraping tool that provides advanced web data extraction capabilities at scale. ZenRows specializes in scraping modern websites, bypassing anti-bot systems, extracting structured data from any website, rendering JavaScript-heavy content, accessing geo-restricted websites, and more.

langchain-zenrows provides tools that allow LLMs to access web data using ZenRows' powerful scraping infrastructure.

You'll need to set up your ZenRows API key:

Or you can pass it directly when initializing tools:

The ZenRows integration provides comprehensive web scraping features:

See more in the ZenRows tool documentation.

**Examples**:

```bash
pip install langchain-zenrows
```

```python
import osos.environ["ZENROWS_API_KEY"] = "your-api-key"
```

```python
from langchain_zenrows import ZenRowsUniversalScraperzenrows_scraper_tool = ZenRowsUniversalScraper(zenrows_api_key="your-api-key")
```

---

## Zotero | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/zotero/

**Contents**:
- Zotero
- Installation​
- Retriever​

Zotero is an open source reference management system intended for managing bibliographic data and related research materials. You can connect to your personal library, as well as shared group libraries, via the API. This retriever implementation utilizes PyZotero to access libraries.

**Examples**:

```bash
pip install pyzotero
```

```python
from langchain_zotero_retriever.retrievers import ZoteroRetriever
```

---

## xAI | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/xai/

**Contents**:
- xAI
- Installation​
- Environment​
- Example​

xAI offers an API to interact with Grok models.

This example goes over how to use LangChain to interact with xAI models.

To use xAI, you'll need to create an API key. The API key can be passed in as an init param xai_api_key or set as environment variable XAI_API_KEY.

See ChatXAI docs for detail and supported features.

**Examples**:

```python
%pip install --upgrade langchain-xai
```

```python
# Querying chat models with xAIfrom langchain_xai import ChatXAIchat = ChatXAI(    # xai_api_key="YOUR_API_KEY",    model="grok-4",)# stream the response back from the modelfor m in chat.stream("Tell me fun things to do in NYC"):    print(m.content, end="", flush=True)# if you don't want to do streaming, you can use the invoke method# chat.invoke("Tell me fun things to do in NYC")
```

---

## zeusdb | 🦜️🔗 LangChain

**URL**: https://python.langchain.com/docs/integrations/providers/zeusdb/

**Contents**:
- zeusdb
- LangChain ZeusDB Integration
- Features​
- Quick Start​
  - Installation​
  - Getting Started​
  - Basic Usage​
  - Factory Methods​

A high-performance LangChain integration for ZeusDB, bringing enterprise-grade vector search capabilities to your LangChain applications.

This example uses OpenAIEmbeddings, which requires an OpenAI API key - Get your OpenAI API key here

If you prefer, you can also use this package with any other embedding provider (Hugging Face, Cohere, custom functions, etc.).

For convenience, you can create and populate a vector store in a single step:

Example 1: - Create from texts (creates index and adds texts in one step)

Example 2: - Create from documents (creates index and adds documents in one step)

ZeusDB's enterprise-grade capabilities are fully integrated into the LangChain ecosystem, providing quantization, persistence, advanced search features and many other enterprise capabilities.

For large datasets, use Product Quantization to reduce memory usage:

Please refer to our documentation for helpful configuration guidelines and recommendations for setting up quantization.

ZeusDB persistence lets you save a fully populated index to disk and load it later with complete state restoration. This includes vectors, metadata, HNSW graph, and (if enabled) Product Quantization models.

How to Save your vector store

How to Load your vector store

For further details (including file structure, and further comprehensive examples), see the documentation.

Use these to control scoring, diversity, metadata filtering, and retriever integration for your searches.

Returns (Document, raw_distance) pairs from ZeusDB — lower distance = more similar. If you prefer normalized relevance in [0, 1], use similarity_search_with_relevance_scores.

MMR (Maximal Marginal Relevance) balances two forces: relevance to the query and diversity among selected results, reducing near-duplicate answers. Control the trade-off with lambda_mult (1.0 = all relevance, 0.0 = all diversity).

Filter results using document metadata you stored when adding docs

For supported metadata query types and operators, 

*[Content truncated - see full docs]*

**Examples**:

```bash
pip install -qU langchain-zeusdb
```

```bash
pip install langchain-openai
```

```python
import osimport getpassos.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
```

---
