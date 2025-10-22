# FastAPI Instructions

**Auto-loaded when**: Working with files matching: `**/*.py, **/main.py, **/fastapi*`

## Default Behaviors

When working with FastAPI:

1. **Follow Official Patterns**: Use patterns from official FastAPI documentation
2. **Type Hints**: Always use Pydantic models for request/response bodies
3. **Error Handling**: Implement proper exception handlers with HTTPException
4. **Async/Await**: Use async routes for I/O operations
5. **Validation**: Leverage Pydantic for automatic validation
6. **Documentation**: Use docstrings for all route functions
7. **Status Codes**: Return appropriate HTTP status codes

## Common Workflows

### Basic API Endpoint

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/", status_code=201)
async def create_item(item: Item):
    return item
```

### With Database (Prisma/SQLAlchemy)

```python
from prisma import Prisma
from contextlib import asynccontextmanager

db = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return await db.user.find_unique(where={"id": user_id})
```

### With Claude/OpenAI Integration

```python
import anthropic
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
client = anthropic.Anthropic()

class Message(BaseModel):
    content: str

@app.post("/analyze")
async def analyze(msg: Message):
    response = client.messages.create(
        model="claude-3-sonnet-20250219",
        max_tokens=1024,
        messages=[{"role": "user", "content": msg.content}]
    )
    return {"analysis": response.content[0].text}
```

### Dependency Injection

```python
from fastapi import Depends, FastAPI

async def get_query(q: str | None = None):
    return q

@app.get("/search")
async def search(q: str = Depends(get_query)):
    return {"q": q}
```

### Error Handling

```python
from fastapi import FastAPI, HTTPException

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {"item_id": item_id}

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return {"error": str(exc)}
```

## Common Patterns

### Setup & Installation

Check `references/getting_started.md` for:
- Installation steps (`pip install fastapi uvicorn`)
- Configuration options
- Initial project setup

### Development

1. Reference official documentation patterns
2. Use type-safe code with Pydantic validation
3. Follow FastAPI naming conventions
4. Test thoroughly with pytest

### Debugging

Common issues and solutions documented in `references/` files:
- Port already in use: Change `uvicorn` port
- Pydantic validation errors: Check model definitions
- Async/await issues: Ensure route is declared async
- CORS errors: Add CORSMiddleware if needed

## Quality Guidelines

- ✅ Use Pydantic models for type safety
- ✅ Write async route handlers for I/O operations
- ✅ Return appropriate HTTP status codes
- ✅ Document endpoints with docstrings
- ✅ Use FastAPI dependency injection pattern
- ⚠️ Avoid blocking operations in async code
- ⚠️ Don't hardcode API keys (use environment variables)

## Integration Patterns

### With Prisma ORM
```python
@app.get("/users")
async def list_users():
    return await db.user.find_many()
```

### With Supabase
```python
from supabase import create_client

supabase = create_client(url, key)

@app.get("/data")
async def get_data():
    return supabase.table("items").select("*").execute()
```

### With LangChain
```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.7)

@app.post("/generate")
async def generate(prompt: str):
    # Use LangChain for complex LLM interactions
    pass
```

## Resources

- Skill prompt: `.github/prompts/fastapi.skill.prompt.md`
- References: `.github/copilot-skills/backend/fastapi/references/`
- Official docs: https://fastapi.tiangolo.com/
- Uvicorn docs: https://www.uvicorn.org/

## Related Skills

- `/prisma` – Database ORM integration
- `/supabase` – Cloud database alternative
- `/langchain` – LLM chains and agents
- `/claude` – Claude API integration
- `/openai` – OpenAI API integration
- `/better-auth` – Authentication setup
