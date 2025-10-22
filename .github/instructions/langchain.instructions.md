# LangChain Instructions

**Auto-loaded when**: Working with files matching: `**/*.py, **/*.ipynb, **/langchain*`

## Default Behaviors

When working with LangChain:

1. **Use LLM Abstractions**: Always use LangChain's LLM interfaces for flexibility
2. **Chain Composition**: Build complex workflows using chains
3. **Memory Management**: Use memory classes for conversation context
4. **Output Parsing**: Parse LLM outputs consistently
5. **Error Handling**: Handle API rate limits and connection errors
6. **Logging**: Enable LangChain debug logging when troubleshooting

## Common Workflows

### Basic Chain Setup

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

chain = prompt | llm

result = chain.invoke({"input": "What is LangChain?"})
```

### With Claude

```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-sonnet-20250219")

chain = prompt | llm
response = chain.invoke({"input": "Explain quantum computing"})
```

### RAG (Retrieval Augmented Generation)

```python
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough

# Setup retriever
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever()

# RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

result = rag_chain.invoke("What is in the documents?")
```

### With Memory (Conversation)

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

response = conversation.predict(input="Hello!")
response = conversation.predict(input="What did I just say?")
```

### Output Parsing

```python
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

parser = JsonOutputParser(pydantic_object=Person)

chain = prompt | llm | parser
result = chain.invoke({"input": "Extract person info from: John is 30"})
```

### With FastAPI

```python
from fastapi import FastAPI
from langchain.chains import LLMChain

app = FastAPI()

@app.post("/chat")
async def chat(message: str):
    response = await chain.ainvoke({"input": message})
    return {"response": response}
```

### Agent with Tools

```python
from langchain import hub
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

tools = [add]
prompt = hub.pull("hwchase17/openai-tools-agent")
agent = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)

result = executor.invoke({"input": "What is 2 + 2?"})
```

## Common Patterns

### Setup & Installation

```bash
pip install langchain langchain-openai  # For OpenAI
pip install langchain langchain-anthropic  # For Claude
pip install langchain-community  # For other integrations
```

### Development Best Practices

1. Use prompts from LangChain Hub for standard workflows
2. Implement streaming for better UX with long responses
3. Add timeout handling for API calls
4. Use `.invoke()` for sync, `.ainvoke()` for async

### Debugging

Common issues:
- API key not found: Check `OPENAI_API_KEY` environment variable
- Rate limited: Implement exponential backoff with retries
- Memory leak: Use `ConversationSummaryMemory` instead of `BufferMemory` for long conversations
- Slow performance: Enable caching and use `.batch()` for multiple inputs

## Quality Guidelines

- ✅ Use abstractions (LLMChain, Chains) over direct API calls
- ✅ Implement memory for context in conversations
- ✅ Parse outputs to structured formats (Pydantic, JSON)
- ✅ Use agents for complex multi-step tasks
- ✅ Handle errors gracefully with retries
- ⚠️ Avoid exposing API keys in code
- ⚠️ Don't use `BufferMemory` for production without summarization

## Integration Patterns

### With Supabase (Vector DB)

```python
from langchain_community.vectorstores.supabase import SupabaseVectorStore

vectorstore = SupabaseVectorStore.from_documents(
    documents, embeddings, client=supabase
)
```

### With FastAPI + Async

```python
async def stream_response(message: str):
    async for chunk in chain.astream({"input": message}):
        yield chunk.get("output", "")
```

## Resources

- Skill prompt: `.github/prompts/langchain.skill.prompt.md`
- References: `.github/copilot-skills/backend/langchain/references/`
- Official docs: https://python.langchain.com/
- LangChain Hub: https://smith.langchain.com/
- Cookbook: https://github.com/langchain-ai/langchain/tree/master/cookbook

## Related Skills

- `/claude` – Claude integration patterns
- `/openai` – OpenAI integration patterns
- `/fastapi` – Backend framework integration
- `/supabase` – Vector database for RAG
- `/prisma` – Traditional database integration
