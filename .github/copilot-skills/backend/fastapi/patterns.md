# Fastapi - Common Patterns

Quick reference for common fastapi patterns and usage.

## Code Patterns

### 1. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
BackgroundTasks
```

### 2. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
BackgroundTasks
```

### 3. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
BackgroundTasks
```

### 4. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
BackgroundTasks
```

### 5. How To - Recipes

```
FastAPI
```

### 6. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
APIRouter
```

### 7. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
APIRouter
```

### 8. FastAPI fastapi/fastapi FastAPI Features Learn Learn Python Types Intro Concurrency and async / awai

```
APIRouter
```

## Examples

### Example 1

```python
from app.routers import items
```

### Example 2

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

### Example 3

```python
from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
```

### Example 4

```python
from typing import Annotated, Union

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: Union[str, None] = None
    googall_tracker: Union[str, None] = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
```

### Example 5

```python
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```

### Example 6

```python
from typing import Annotated, Union

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}
```

### Example 7

```python
from unicorn import UnicornMiddleware

app = SomeASGIApp()

new_app = UnicornMiddleware(app, some_config="rainbow")
```

### Example 8

```python
from fastapi import FastAPI
from unicorn import UnicornMiddleware

app = FastAPI()

app.add_middleware(UnicornMiddleware, some_config="rainbow")
```

### Example 9

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Tomato"}
```

### Example 10

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
def read_items():
    return ["plumbus", "portal gun"]
```


## Categories

See organized documentation in `references/`:

- `references/advanced.md` - Advanced
- `references/deployment.md` - Deployment
- `references/other.md` - Other
- `references/reference.md` - Reference
- `references/tutorial.md` - Tutorial
