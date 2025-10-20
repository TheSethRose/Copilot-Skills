# Fastapi - Tutorial

**Pages**: 54

---

## Background Tasks - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/background-tasks/

**Contents**:
- Background Tasks¶
- Using BackgroundTasks¶
- Create a task function¶
- Add the background task¶
- Dependency Injection¶
- Technical Details¶
- Caveat¶
- Recap¶

You can define background tasks to be run after returning a response.

This is useful for operations that need to happen after a request, but that the client doesn't really have to be waiting for the operation to complete before receiving the response.

This includes, for example:

First, import BackgroundTasks and define a parameter in your path operation function with a type declaration of BackgroundTasks:

FastAPI will create the object of type BackgroundTasks for you and pass it as that parameter.

Create a function to be run as the background task.

It is just a standard function that can receive parameters.

It can be an async def or normal def function, FastAPI will know how to handle it correctly.

In this case, the task function will write to a file (simulating sending an email).

And as the write operation doesn't use async and await, we define the function with normal def:

Inside of your path operation function, pass your task function to the background tasks object with the method .add_task():

.add_task() receives as arguments:

Using BackgroundTasks also works with the dependency injection system, you can declare a parameter of type BackgroundTasks at multiple levels: in a path operation function, in a dependency (dependable), in a sub-dependency, etc.

FastAPI knows what to do in each case and how to reuse the same object, so that all the background tasks are merged together and are run in the background afterwards:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

In this example, the messages will be written to the log.txt file after the response is sent.

If there was a query in the request, it will be written to the log in a background task.

And then another background task generated at the path operation function will write a message using the email path parameter.

The class BackgroundTasks comes directly from starlette.background.

It is imported/included directly into FastAPI so that you can

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent i
...
```

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent i
...
```

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent i
...
```

---

## Bigger Applications - Multiple Files - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/bigger-applications/

**Contents**:
- Bigger Applications - Multiple Files¶
- An example file structure¶
- APIRouter¶
  - Import APIRouter¶
  - Path operations with APIRouter¶
- Dependencies¶
- Another module with APIRouter¶
  - Import the dependencies¶

If you are building an application or a web API, it's rarely the case that you can put everything in a single file.

FastAPI provides a convenience tool to structure your application while keeping all the flexibility.

If you come from Flask, this would be the equivalent of Flask's Blueprints.

Let's say you have a file structure like this:

There are several __init__.py files: one in each directory or subdirectory.

This is what allows importing code from one file into another.

For example, in app/main.py you could have a line like:

The same file structure with comments:

Let's say the file dedicated to handling just users is the submodule at /app/routers/users.py.

You want to have the path operations related to your users separated from the rest of the code, to keep it organized.

But it's still part of the same FastAPI application/web API (it's part of the same "Python Package").

You can create the path operations for that module using APIRouter.

You import it and create an "instance" the same way you would with the class FastAPI:

And then you use it to declare your path operations.

Use it the same way you would use the FastAPI class:

You can think of APIRouter as a "mini FastAPI" class.

All the same options are supported.

All the same parameters, responses, dependencies, tags, etc.

In this example, the variable is called router, but you can name it however you want.

We are going to include this APIRouter in the main FastAPI app, but first, let's check the dependencies and another APIRouter.

We see that we are going to need some dependencies used in several places of the application.

So we put them in their own dependencies module (app/dependencies.py).

We will now use a simple dependency to read a custom X-Token header:

Prefer to use the Annotated version if possible.

We are using an invented header to simplify this example.

But in real cases you will get better results using the integrated Security utilities.

Let's say you also have the endpo

*[Content truncated - see full docs]*

**Examples**:

```text
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

```python
from app.routers import items
```

```text
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "user
...
```

---

## Body - Fields - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/body-fields/

**Contents**:
- Body - Fields¶
- Import Field¶
- Declare model attributes¶
- Add extra information¶
- Recap¶

The same way you can declare additional validation and metadata in path operation function parameters with Query, Path and Body, you can declare validation and metadata inside of Pydantic models using Pydantic's Field.

First, you have to import it:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Notice that Field is imported directly from pydantic, not from fastapi as are all the rest (Query, Path, Body, etc).

You can then use Field with model attributes:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Field works the same way as Query, Path and Body, it has all the same parameters, etc.

Actually, Query, Path and others you'll see next create objects of subclasses of a common Param class, which is itself a subclass of Pydantic's FieldInfo class.

And Pydantic's Field returns an instance of FieldInfo as well.

Body also returns objects of a subclass of FieldInfo directly. And there are others you will see later that are subclasses of the Body class.

Remember that when you import Query, Path, and others from fastapi, those are actually functions that return special classes.

Notice how each model's attribute with a type, default value and Field has the same structure as a path operation function's parameter, with Field instead of Path, Query and Body.

You can declare extra information in Field, Query, Body, etc. And it will be included in the generated JSON Schema.

You will learn more about adding extra information later in the docs, when learning to declare examples.

Extra keys passed to Field will also be present in the resulting OpenAPI schema for your application. As these keys may not necessarily be part of the OpenAPI specification, some OpenAPI tools, for example the OpenAPI validator, may not work with your generated schema.

You can use Pydantic's Field to declare extra validations and metadata for model attributes.

You can also use the extra keyw

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    r
...
```

```python
from typing import Annotated, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(e
...
```

```python
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int,
...
```

---

## Body - Multiple Parameters - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/body-multiple-params/

**Contents**:
- Body - Multiple Parameters¶
- Mix Path, Query and body parameters¶
- Multiple body parameters¶
- Singular values in body¶
- Multiple body params and query¶
- Embed a single body parameter¶
- Recap¶

Now that we have seen how to use Path and Query, let's see more advanced uses of request body declarations.

First, of course, you can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.

And you can also declare body parameters as optional, by setting the default to None:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Notice that, in this case, the item that would be taken from the body is optional. As it has a None default value.

In the previous example, the path operations would expect a JSON body with the attributes of an Item, like:

But you can also declare multiple body parameters, e.g. item and user:

In this case, FastAPI will notice that there is more than one body parameter in the function (there are two parameters that are Pydantic models).

So, it will then use the parameter names as keys (field names) in the body, and expect a body like:

Notice that even though the item was declared the same way as before, it is now expected to be inside of the body with a key item.

FastAPI will do the automatic conversion from the request, so that the parameter item receives its specific content and the same for user.

It will perform the validation of the compound data, and will document it like that for the OpenAPI schema and automatic docs.

The same way there is a Query and Path to define extra data for query and path parameters, FastAPI provides an equivalent Body.

For example, extending the previous model, you could decide that you want to have another key importance in the same body, besides the item and user.

If you declare it as is, because it is a singular value, FastAPI will assume that it is a query parameter.

But you can instruct FastAPI to treat it as another body key using Body:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

In this case, FastAPI will expect a body like:

Again, it will convert th

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"
...
```

```python
from typing import Annotated, Union

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    
...
```

```python
from typing import Union

from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    result
...
```

---

## Body - Nested Models - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/body-nested-models/

**Contents**:
- Body - Nested Models¶
- List fields¶
- List fields with type parameter¶
  - Import typing's List¶
  - Declare a list with a type parameter¶
- Set types¶
- Nested Models¶
  - Define a submodel¶

With FastAPI, you can define, validate, document, and use arbitrarily deeply nested models (thanks to Pydantic).

You can define an attribute to be a subtype. For example, a Python list:

This will make tags be a list, although it doesn't declare the type of the elements of the list.

But Python has a specific way to declare lists with internal types, or "type parameters":

In Python 3.9 and above you can use the standard list to declare these type annotations as we'll see below. 💡

But in Python versions before 3.9 (3.6 and above), you first need to import List from standard Python's typing module:

To declare types that have type parameters (internal types), like list, dict, tuple:

In Python 3.9 it would be:

In versions of Python before 3.9, it would be:

That's all standard Python syntax for type declarations.

Use that same standard syntax for model attributes with internal types.

So, in our example, we can make tags be specifically a "list of strings":

But then we think about it, and realize that tags shouldn't repeat, they would probably be unique strings.

And Python has a special data type for sets of unique items, the set.

Then we can declare tags as a set of strings:

With this, even if you receive a request with duplicate data, it will be converted to a set of unique items.

And whenever you output that data, even if the source had duplicates, it will be output as a set of unique items.

And it will be annotated / documented accordingly too.

Each attribute of a Pydantic model has a type.

But that type can itself be another Pydantic model.

So, you can declare deeply nested JSON "objects" with specific attribute names, types and validations.

All that, arbitrarily nested.

For example, we can define an Image model:

And then we can use it as the type of an attribute:

This would mean that FastAPI would expect a body similar to:

Again, doing just that declaration, with FastAPI you get:

Apart from normal singular types like str, int, float, etc. you

*[Content truncated - see full docs]*

**Examples**:

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

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

```python
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
```

---

## Body - Updates - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/body-updates/

**Contents**:
- Body - Updates¶
- Update replacing with PUT¶
  - Warning about replacing¶
- Partial updates with PATCH¶
  - Using Pydantic's exclude_unset parameter¶
  - Using Pydantic's update parameter¶
  - Partial updates recap¶

To update an item you can use the HTTP PUT operation.

You can use the jsonable_encoder to convert the input data to data that can be stored as JSON (e.g. with a NoSQL database). For example, converting datetime to str.

PUT is used to receive data that should replace the existing data.

That means that if you want to update the item bar using PUT with a body containing:

because it doesn't include the already stored attribute "tax": 20.2, the input model would take the default value of "tax": 10.5.

And the data would be saved with that "new" tax of 10.5.

You can also use the HTTP PATCH operation to partially update data.

This means that you can send only the data that you want to update, leaving the rest intact.

PATCH is less commonly used and known than PUT.

And many teams use only PUT, even for partial updates.

You are free to use them however you want, FastAPI doesn't impose any restrictions.

But this guide shows you, more or less, how they are intended to be used.

If you want to receive partial updates, it's very useful to use the parameter exclude_unset in Pydantic's model's .model_dump().

Like item.model_dump(exclude_unset=True).

In Pydantic v1 the method was called .dict(), it was deprecated (but still supported) in Pydantic v2, and renamed to .model_dump().

The examples here use .dict() for compatibility with Pydantic v1, but you should use .model_dump() instead if you can use Pydantic v2.

That would generate a dict with only the data that was set when creating the item model, excluding default values.

Then you can use this to generate a dict with only the data that was set (sent in the request), omitting default values:

Now, you can create a copy of the existing model using .model_copy(), and pass the update parameter with a dict containing the data to update.

In Pydantic v1 the method was called .copy(), it was deprecated (but still supported) in Pydantic v2, and renamed to .model_copy().

The examples here use .copy() for compatibility wit

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 
...
```

```python
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz",
...
```

```python
from typing import List, Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": 
...
```

---

## CORS (Cross-Origin Resource Sharing) - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/cors/

**Contents**:
- CORS (Cross-Origin Resource Sharing)¶
- Origin¶
- Steps¶
- Wildcards¶
- Use CORSMiddleware¶
  - CORS preflight requests¶
  - Simple requests¶
- More info¶

CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a different "origin" than the frontend.

An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), and port (80, 443, 8080).

So, all these are different origins:

Even if they are all in localhost, they use different protocols or ports, so, they are different "origins".

So, let's say you have a frontend running in your browser at http://localhost:8080, and its JavaScript is trying to communicate with a backend running at http://localhost (because we don't specify a port, the browser will assume the default port 80).

Then, the browser will send an HTTP OPTIONS request to the :80-backend, and if the backend sends the appropriate headers authorizing the communication from this different origin (http://localhost:8080) then the :8080-browser will let the JavaScript in the frontend send its request to the :80-backend.

To achieve this, the :80-backend must have a list of "allowed origins".

In this case, the list would have to include http://localhost:8080 for the :8080-frontend to work correctly.

It's also possible to declare the list as "*" (a "wildcard") to say that all are allowed.

But that will only allow certain types of communication, excluding everything that involves credentials: Cookies, Authorization headers like those used with Bearer Tokens, etc.

So, for everything to work correctly, it's better to specify explicitly the allowed origins.

You can configure it in your FastAPI application using the CORSMiddleware.

You can also specify whether your backend allows:

The default parameters used by the CORSMiddleware implementation are restrictive by default, so you'll need to explicitly enable particular origins, methods, or headers, in order for browsers to be permitted to use them in a Cross-Domain context.

The following argume

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
```

---

## Classes as Dependencies - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/

**Contents**:
- Classes as Dependencies¶
- A dict from the previous example¶
- What makes a dependency¶
- Classes as dependencies¶
- Use it¶
- Type annotation vs Depends¶
- Shortcut¶

Before diving deeper into the Dependency Injection system, let's upgrade the previous example.

In the previous example, we were returning a dict from our dependency ("dependable"):

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

But then we get a dict in the parameter commons of the path operation function.

And we know that editors can't provide a lot of support (like completion) for dicts, because they can't know their keys and value types.

Up to now you have seen dependencies declared as functions.

But that's not the only way to declare dependencies (although it would probably be the more common).

The key factor is that a dependency should be a "callable".

A "callable" in Python is anything that Python can "call" like a function.

So, if you have an object something (that might not be a function) and you can "call" it (execute it) like:

then it is a "callable".

You might notice that to create an instance of a Python class, you use that same syntax.

In this case, fluffy is an instance of the class Cat.

And to create fluffy, you are "calling" Cat.

So, a Python class is also a callable.

Then, in FastAPI, you could use a Python class as a dependency.

What FastAPI actually checks is that it is a "callable" (function, class or anything else) and the parameters defined.

If you pass a "callable" as a dependency in FastAPI, it will analyze the parameters for that "callable", and process them in the same way as the parameters for a path operation function. Including sub-dependencies.

That also applies to callables with no parameters at all. The same as it would be for path operation functions with no parameters.

Then, we can change the dependency "dependable" common_parameters from above to the class CommonQueryParams:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Pay attention to the __init__ method used to create the instance of the class:

Prefer to

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

```python
from typing import Annotated, Union

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

```python
from typing import Union

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return common
...
```

---

## Cookie Parameter Models - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/cookie-param-models/

**Contents**:
- Cookie Parameter Models¶
- Cookies with a Pydantic Model¶
- Check the Docs¶
- Forbid Extra Cookies¶
- Summary¶

If you have a group of cookies that are related, you can create a Pydantic model to declare them. 🍪

This would allow you to re-use the model in multiple places and also to declare validations and metadata for all the parameters at once. 😎

This is supported since FastAPI version 0.115.0. 🤓

This same technique applies to Query, Cookie, and Header. 😎

Declare the cookie parameters that you need in a Pydantic model, and then declare the parameter as Cookie:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

FastAPI will extract the data for each field from the cookies received in the request and give you the Pydantic model you defined.

You can see the defined cookies in the docs UI at /docs:

Have in mind that, as browsers handle cookies in special ways and behind the scenes, they don't easily allow JavaScript to touch them.

If you go to the API docs UI at /docs you will be able to see the documentation for cookies for your path operations.

But even if you fill the data and click "Execute", because the docs UI works with JavaScript, the cookies won't be sent, and you will see an error message as if you didn't write any values.

In some special use cases (probably not very common), you might want to restrict the cookies that you want to receive.

Your API now has the power to control its own cookie consent. 🤪🍪

You can use Pydantic's model configuration to forbid any extra fields:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

If a client tries to send some extra cookies, they will receive an error response.

Poor cookie banners with all their effort to get your consent for the API to reject it. 🍪

For example, if the client tries to send a santa_tracker cookie with a value of good-list-please, the client will receive an error response telling them that the santa_tracker cookie is not allowed:

You can use Pydantic models to declare cookies in FastAPI. 😎

**Examples**:

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

```python
from typing import Union

from fastapi import Cookie, FastAPI
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: Union[str, None] = None
    googall_tracker: Union[str, None] = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
```

---

## Cookie Parameters - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/cookie-params/

**Contents**:
- Cookie Parameters¶
- Import Cookie¶
- Declare Cookie parameters¶
- Recap¶

You can define Cookie parameters the same way you define Query and Path parameters.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Then declare the cookie parameters using the same structure as with Path and Query.

You can define the default value as well as all the extra validation or annotation parameters:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Cookie is a "sister" class of Path and Query. It also inherits from the same common Param class.

But remember that when you import Query, Path, Cookie and others from fastapi, those are actually functions that return special classes.

To declare cookies, you need to use Cookie, because otherwise the parameters would be interpreted as query parameters.

Have in mind that, as browsers handle cookies in special ways and behind the scenes, they don't easily allow JavaScript to touch them.

If you go to the API docs UI at /docs you will be able to see the documentation for cookies for your path operations.

But even if you fill the data and click "Execute", because the docs UI works with JavaScript, the cookies won't be sent, and you will see an error message as if you didn't write any values.

Declare cookies with Cookie, using the same common pattern as Query and Path.

**Examples**:

```python
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```

```python
from typing import Annotated, Union

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}
```

```python
from typing import Union

from fastapi import Cookie, FastAPI
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}
```

---

## Debugging - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/debugging/

**Contents**:
- Debugging¶
- Call uvicorn¶
  - About __name__ == "__main__"¶
    - More details¶
- Run your code with your debugger¶

You can connect the debugger in your editor, for example with Visual Studio Code or PyCharm.

In your FastAPI application, import and run uvicorn directly:

The main purpose of the __name__ == "__main__" is to have some code that is executed when your file is called with:

but is not called when another file imports it, like in:

Let's say your file is named myapp.py.

then the internal variable __name__ in your file, created automatically by Python, will have as value the string "__main__".

This won't happen if you import that module (file).

So, if you have another file importer.py with:

in that case, the automatically created variable __name__ inside of myapp.py will not have the value "__main__".

will not be executed.

For more information, check the official Python docs.

Because you are running the Uvicorn server directly from your code, you can call your Python program (your FastAPI application) directly from the debugger.

For example, in Visual Studio Code, you can:

It will then start the server with your FastAPI code, stop at your breakpoints, etc.

Here's how it might look:

If you use Pycharm, you can:

It will then start the server with your FastAPI code, stop at your breakpoints, etc.

Here's how it might look:

**Examples**:

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```text
$ python myapp.py
```

```python
from myapp import app
```

---

## Declare Request Example Data - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/schema-extra-example/

**Contents**:
- Declare Request Example Data¶
- Extra JSON Schema data in Pydantic models¶
- Field additional arguments¶
- examples in JSON Schema - OpenAPI¶
  - Body with examples¶
  - Example in the docs UI¶
  - Body with multiple examples¶
  - OpenAPI-specific examples¶

You can declare examples of the data your app can receive.

Here are several ways to do it.

You can declare examples for a Pydantic model that will be added to the generated JSON Schema.

That extra info will be added as-is to the output JSON Schema for that model, and it will be used in the API docs.

In Pydantic version 2, you would use the attribute model_config, that takes a dict as described in Pydantic's docs: Configuration.

You can set "json_schema_extra" with a dict containing any additional data you would like to show up in the generated JSON Schema, including examples.

In Pydantic version 1, you would use an internal class Config and schema_extra, as described in Pydantic's docs: Schema customization.

You can set schema_extra with a dict containing any additional data you would like to show up in the generated JSON Schema, including examples.

You could use the same technique to extend the JSON Schema and add your own custom extra info.

For example you could use it to add metadata for a frontend user interface, etc.

OpenAPI 3.1.0 (used since FastAPI 0.99.0) added support for examples, which is part of the JSON Schema standard.

Before that, it only supported the keyword example with a single example. That is still supported by OpenAPI 3.1.0, but is deprecated and is not part of the JSON Schema standard. So you are encouraged to migrate example to examples. 🤓

You can read more at the end of this page.

When using Field() with Pydantic models, you can also declare additional examples:

you can also declare a group of examples with additional information that will be added to their JSON Schemas inside of OpenAPI.

Here we pass examples containing one example of the data expected in Body():

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

With any of the methods above it would look like this in the /docs:

You can of course also pass multiple examples:

Prefer to use the Annotated version if possible.


*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }



...
```

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
            
...
```

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Config:
        schema_extra = {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }


@app.put("/item
...
```

---

## Dependencies - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/dependencies/

**Contents**:
- Dependencies¶
- What is "Dependency Injection"¶
- First Steps¶
  - Create a dependency, or "dependable"¶
  - Import Depends¶
  - Declare the dependency, in the "dependant"¶
- Share Annotated dependencies¶
- To async or not to async¶

FastAPI has a very powerful but intuitive Dependency Injection system.

It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with FastAPI.

"Dependency Injection" means, in programming, that there is a way for your code (in this case, your path operation functions) to declare things that it requires to work and use: "dependencies".

And then, that system (in this case FastAPI) will take care of doing whatever is needed to provide your code with those needed dependencies ("inject" the dependencies).

This is very useful when you need to:

All these, while minimizing code repetition.

Let's see a very simple example. It will be so simple that it is not very useful, for now.

But this way we can focus on how the Dependency Injection system works.

Let's first focus on the dependency.

It is just a function that can take all the same parameters that a path operation function can take:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

And it has the same shape and structure that all your path operation functions have.

You can think of it as a path operation function without the "decorator" (without the @app.get("/some-path")).

And it can return anything you want.

In this case, this dependency expects:

And then it just returns a dict containing those values.

FastAPI added support for Annotated (and started recommending it) in version 0.95.0.

If you have an older version, you would get errors when trying to use Annotated.

Make sure you Upgrade the FastAPI version to at least 0.95.1 before using Annotated.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

The same way you use Body, Query, etc. with your path operation function parameters, use Depends with a new parameter:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Although you use Depends in the para

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

```python
from typing import Annotated, Union

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

```python
from typing import Union

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return common
...
```

---

## Dependencies in path operation decorators - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/

**Contents**:
- Dependencies in path operation decorators¶
- Add dependencies to the path operation decorator¶
- Dependencies errors and return values¶
  - Dependency requirements¶
  - Raise exceptions¶
  - Return values¶
- Dependencies for a group of path operations¶
- Global Dependencies¶

In some cases you don't really need the return value of a dependency inside your path operation function.

Or the dependency doesn't return a value.

But you still need it to be executed/solved.

For those cases, instead of declaring a path operation function parameter with Depends, you can add a list of dependencies to the path operation decorator.

The path operation decorator receives an optional argument dependencies.

It should be a list of Depends():

Prefer to use the Annotated version if possible.

These dependencies will be executed/solved the same way as normal dependencies. But their value (if they return any) won't be passed to your path operation function.

Some editors check for unused function parameters, and show them as errors.

Using these dependencies in the path operation decorator you can make sure they are executed while avoiding editor/tooling errors.

It might also help avoid confusion for new developers that see an unused parameter in your code and could think it's unnecessary.

In this example we use invented custom headers X-Key and X-Token.

But in real cases, when implementing security, you would get more benefits from using the integrated Security utilities (the next chapter).

You can use the same dependency functions you use normally.

They can declare request requirements (like headers) or other sub-dependencies:

Prefer to use the Annotated version if possible.

These dependencies can raise exceptions, the same as normal dependencies:

Prefer to use the Annotated version if possible.

And they can return values or not, the values won't be used.

So, you can reuse a normal dependency (that returns a value) you already use somewhere else, and even though the value won't be used, the dependency will be executed:

Prefer to use the Annotated version if possible.

Later, when reading about how to structure bigger applications (Bigger Applications - Multiple Files), possibly with multiple files, you will learn how to declare a single depe

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items
...
```

```python
from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated

app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.g
...
```

```python
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(v
...
```

---

## Dependencies with yield - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/

**Contents**:
- Dependencies with yield¶
- A database dependency with yield¶
- A dependency with yield and try¶
- Sub-dependencies with yield¶
- Dependencies with yield and HTTPException¶
- Dependencies with yield and except¶
  - Always raise in Dependencies with yield and except¶
- Execution of dependencies with yield¶

FastAPI supports dependencies that do some extra steps after finishing.

To do this, use yield instead of return, and write the extra steps (code) after.

Make sure to use yield one single time per dependency.

Any function that is valid to use with:

would be valid to use as a FastAPI dependency.

In fact, FastAPI uses those two decorators internally.

For example, you could use this to create a database session and close it after finishing.

Only the code prior to and including the yield statement is executed before creating a response:

The yielded value is what is injected into path operations and other dependencies:

The code following the yield statement is executed after the response:

You can use async or regular functions.

FastAPI will do the right thing with each, the same as with normal dependencies.

If you use a try block in a dependency with yield, you'll receive any exception that was thrown when using the dependency.

For example, if some code at some point in the middle, in another dependency or in a path operation, made a database transaction "rollback" or created any other exception, you would receive the exception in your dependency.

So, you can look for that specific exception inside the dependency with except SomeException.

In the same way, you can use finally to make sure the exit steps are executed, no matter if there was an exception or not.

You can have sub-dependencies and "trees" of sub-dependencies of any size and shape, and any or all of them can use yield.

FastAPI will make sure that the "exit code" in each dependency with yield is run in the correct order.

For example, dependency_c can have a dependency on dependency_b, and dependency_b on dependency_a:

Prefer to use the Annotated version if possible.

And all of them can use yield.

In this case dependency_c, to execute its exit code, needs the value from dependency_b (here named dep_b) to still be available.

And, in turn, dependency_b needs the value from dependency_a (here 

*[Content truncated - see full docs]*

**Examples**:

```python
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

```python
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

```python
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

---

## Extra Data Types - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/extra-data-types/

**Contents**:
- Extra Data Types¶
- Other data types¶
- Example¶

Up to now, you have been using common data types, like:

But you can also use more complex data types.

And you will still have the same features as seen up to now:

Here are some of the additional data types you can use:

Here's an example path operation with parameters using some of the above types.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Note that the parameters inside the function have their natural data type, and you can, for example, perform normal date manipulations, like:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

**Examples**:

```python
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_dateti
...
```

```python
from datetime import datetime, time, timedelta
from typing import Annotated, Union
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[Union[time, None], Body()] = None,
):
    start_process = start_datetime + process_after
    duration
...
```

```python
from datetime import datetime, time, timedelta
from typing import Union
from uuid import UUID

from fastapi import Body, FastAPI
from typing_extensions import Annotated

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[Union[time, None], Body()] = None,
):
    start_process = start_datetime
...
```

---

## Extra Models - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/extra-models/

**Contents**:
- Extra Models¶
- Multiple models¶
  - About **user_in.dict()¶
    - Pydantic's .dict()¶
    - Unpacking a dict¶
    - A Pydantic model from the contents of another¶
    - Unpacking a dict and extra keywords¶
- Reduce duplication¶

Continuing with the previous example, it will be common to have more than one related model.

This is especially the case for user models, because:

Never store user's plaintext passwords. Always store a "secure hash" that you can then verify.

If you don't know, you will learn what a "password hash" is in the security chapters.

Here's a general idea of how the models could look like with their password fields and the places where they are used:

In Pydantic v1 the method was called .dict(), it was deprecated (but still supported) in Pydantic v2, and renamed to .model_dump().

The examples here use .dict() for compatibility with Pydantic v1, but you should use .model_dump() instead if you can use Pydantic v2.

user_in is a Pydantic model of class UserIn.

Pydantic models have a .dict() method that returns a dict with the model's data.

So, if we create a Pydantic object user_in like:

we now have a dict with the data in the variable user_dict (it's a dict instead of a Pydantic model object).

we would get a Python dict with:

If we take a dict like user_dict and pass it to a function (or class) with **user_dict, Python will "unpack" it. It will pass the keys and values of the user_dict directly as key-value arguments.

So, continuing with the user_dict from above, writing:

would result in something equivalent to:

Or more exactly, using user_dict directly, with whatever contents it might have in the future:

As in the example above we got user_dict from user_in.dict(), this code:

would be equivalent to:

...because user_in.dict() is a dict, and then we make Python "unpack" it by passing it to UserInDB prefixed with **.

So, we get a Pydantic model from the data in another Pydantic model.

And then adding the extra keyword argument hashed_password=hashed_password, like in:

...ends up being like:

The supporting additional functions fake_password_hasher and fake_save_user are just to demo a possible flow of the data, but they of course are not providing any real s

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + 
...
```

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None


def fake_password_hasher(raw
...
```

```text
user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
```

---

## First Steps - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/first-steps/

**Contents**:
- First Steps¶
  - Check it¶
  - Interactive API docs¶
  - Alternative API docs¶
  - OpenAPI¶
    - "Schema"¶
    - API "schema"¶
    - Data "schema"¶

The simplest FastAPI file could look like this:

Copy that to a file main.py.

In the output, there's a line with something like:

That line shows the URL where your app is being served, in your local machine.

Open your browser at http://127.0.0.1:8000.

You will see the JSON response as:

Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

And now, go to http://127.0.0.1:8000/redoc.

You will see the alternative automatic documentation (provided by ReDoc):

FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs.

A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

In this case, OpenAPI is a specification that dictates how to define a schema of your API.

This schema definition includes your API paths, the possible parameters they take, etc.

The term "schema" might also refer to the shape of some data, like a JSON content.

In that case, it would mean the JSON attributes, and data types they have, etc.

OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using JSON Schema, the standard for JSON data schemas.

If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.

You can see it directly at: http://127.0.0.1:8000/openapi.json.

It will show a JSON starting with something like:

The OpenAPI schema is what powers the two interactive documentation systems included.

And there are dozens of alternatives, all based on OpenAPI. You could easily add any of those alternatives to your application built with FastAPI.

You could also use it to generate code automatically, for clients that communicate with your API. For example, frontend, mobile or IoT applications.

FastAPI is a Python class that provides all the functi

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

```python
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166
...
```

```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## Form Data - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/request-forms/

**Contents**:
- Form Data¶
- Import Form¶
- Define Form parameters¶
- About "Form Fields"¶
- Recap¶

When you need to receive form fields instead of JSON, you can use Form.

To use forms, first install python-multipart.

Make sure you create a virtual environment, activate it, and then install it, for example:

Import Form from fastapi:

Prefer to use the Annotated version if possible.

Create form parameters the same way you would for Body or Query:

Prefer to use the Annotated version if possible.

For example, in one of the ways the OAuth2 specification can be used (called "password flow") it is required to send a username and password as form fields.

The spec requires the fields to be exactly named username and password, and to be sent as form fields, not JSON.

With Form you can declare the same configurations as with Body (and Query, Path, Cookie), including validation, examples, an alias (e.g. user-name instead of username), etc.

Form is a class that inherits directly from Body.

To declare form bodies, you need to use Form explicitly, because without it the parameters would be interpreted as query parameters or body (JSON) parameters.

The way HTML forms (<form></form>) sends the data to the server normally uses a "special" encoding for that data, it's different from JSON.

FastAPI will make sure to read that data from the right place instead of JSON.

Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.

But when the form includes files, it is encoded as multipart/form-data. You'll read about handling files in the next chapter.

If you want to read more about these encodings and form fields, head to the MDN web docs for POST.

You can declare multiple Form parameters in a path operation, but you can't also declare Body fields that you expect to receive as JSON, as the request will have the body encoded using application/x-www-form-urlencoded instead of application/json.

This is not a limitation of FastAPI, it's part of the HTTP protocol.

Use Form to declare form data input parameters.

**Examples**:

```text
$ pip install python-multipart
```

```python
from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```

```python
from fastapi import FastAPI, Form
from typing_extensions import Annotated

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
```

---

## Form Models - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/request-form-models/

**Contents**:
- Form Models¶
- Pydantic Models for Forms¶
- Check the Docs¶
- Forbid Extra Form Fields¶
- Summary¶

You can use Pydantic models to declare form fields in FastAPI.

To use forms, first install python-multipart.

Make sure you create a virtual environment, activate it, and then install it, for example:

This is supported since FastAPI version 0.113.0. 🤓

You just need to declare a Pydantic model with the fields you want to receive as form fields, and then declare the parameter as Form:

Prefer to use the Annotated version if possible.

FastAPI will extract the data for each field from the form data in the request and give you the Pydantic model you defined.

You can verify it in the docs UI at /docs:

In some special use cases (probably not very common), you might want to restrict the form fields to only those declared in the Pydantic model. And forbid any extra fields.

This is supported since FastAPI version 0.114.0. 🤓

You can use Pydantic's model configuration to forbid any extra fields:

Prefer to use the Annotated version if possible.

If a client tries to send some extra data, they will receive an error response.

For example, if the client tries to send the form fields:

They will receive an error response telling them that the field extra is not allowed:

You can use Pydantic models to declare form fields in FastAPI. 😎

**Examples**:

```text
$ pip install python-multipart
```

```python
from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
```

```python
from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
```

---

## Get Current User - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/security/get-current-user/

**Contents**:
- Get Current User¶
- Create a user model¶
- Create a get_current_user dependency¶
- Get the user¶
- Inject the current user¶
- Other models¶
- Code size¶
- Recap¶

In the previous chapter the security system (which is based on the dependency injection system) was giving the path operation function a token as a str:

Prefer to use the Annotated version if possible.

But that is still not that useful.

Let's make it give us the current user.

First, let's create a Pydantic user model.

The same way we use Pydantic to declare bodies, we can use it anywhere else:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Let's create a dependency get_current_user.

Remember that dependencies can have sub-dependencies?

get_current_user will have a dependency with the same oauth2_scheme we created before.

The same as we were doing before in the path operation directly, our new dependency get_current_user will receive a token as a str from the sub-dependency oauth2_scheme:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

get_current_user will use a (fake) utility function we created, that takes a token as a str and returns our Pydantic User model:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

So now we can use the same Depends with our get_current_user in the path operation:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Notice that we declare the type of current_user as the Pydantic model User.

This will help us inside of the function with all the completion and type checks.

You might remember that request bodies are also declared with Pydantic models.

Here FastAPI won't get confused because you are using Depends.

The way this dependency system is designed allows us to have different dependencies (different "dependables") that all return a User model.

We are not restricted to having only one dependency that can return that type of data.

You can now get the current user directly in the path operation functions and deal with th

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

---

## Global Dependencies - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/

**Contents**:
- Global Dependencies¶
- Dependencies for groups of path operations¶

For some types of applications you might want to add dependencies to the whole application.

Similar to the way you can add dependencies to the path operation decorators, you can add them to the FastAPI application.

In that case, they will be applied to all the path operations in the application:

Prefer to use the Annotated version if possible.

And all the ideas in the section about adding dependencies to the path operation decorators still apply, but in this case, to all of the path operations in the app.

Later, when reading about how to structure bigger applications (Bigger Applications - Multiple Files), possibly with multiple files, you will learn how to declare a single dependencies parameter for a group of path operations.

**Examples**:

```python
from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependenc
...
```

```python
from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependenc
...
```

```python
from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get
...
```

---

## Handling Errors - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/handling-errors/

**Contents**:
- Handling Errors¶
- Use HTTPException¶
  - Import HTTPException¶
  - Raise an HTTPException in your code¶
  - The resulting response¶
- Add custom headers¶
- Install custom exception handlers¶
- Override the default exception handlers¶

There are many situations in which you need to notify an error to a client that is using your API.

This client could be a browser with a frontend, a code from someone else, an IoT device, etc.

You could need to tell the client that:

In these cases, you would normally return an HTTP status code in the range of 400 (from 400 to 499).

This is similar to the 200 HTTP status codes (from 200 to 299). Those "200" status codes mean that somehow there was a "success" in the request.

The status codes in the 400 range mean that there was an error from the client.

Remember all those "404 Not Found" errors (and jokes)?

To return HTTP responses with errors to the client you use HTTPException.

HTTPException is a normal Python exception with additional data relevant for APIs.

Because it's a Python exception, you don't return it, you raise it.

This also means that if you are inside a utility function that you are calling inside of your path operation function, and you raise the HTTPException from inside of that utility function, it won't run the rest of the code in the path operation function, it will terminate that request right away and send the HTTP error from the HTTPException to the client.

The benefit of raising an exception over returning a value will be more evident in the section about Dependencies and Security.

In this example, when the client requests an item by an ID that doesn't exist, raise an exception with a status code of 404:

If the client requests http://example.com/items/foo (an item_id "foo"), that client will receive an HTTP status code of 200, and a JSON response of:

But if the client requests http://example.com/items/bar (a non-existent item_id "bar"), that client will receive an HTTP status code of 404 (the "not found" error), and a JSON response of:

When raising an HTTPException, you can pass any value that can be converted to JSON as the parameter detail, not only str.

You could pass a dict, a list, etc.

They are handled automatically by F

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

```text
{
  "item": "The Foo Wrestlers"
}
```

---

## Header Parameter Models - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/header-param-models/

**Contents**:
- Header Parameter Models¶
- Header Parameters with a Pydantic Model¶
- Check the Docs¶
- Forbid Extra Headers¶
- Disable Convert Underscores¶
- Summary¶

If you have a group of related header parameters, you can create a Pydantic model to declare them.

This would allow you to re-use the model in multiple places and also to declare validations and metadata for all the parameters at once. 😎

This is supported since FastAPI version 0.115.0. 🤓

Declare the header parameters that you need in a Pydantic model, and then declare the parameter as Header:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

FastAPI will extract the data for each field from the headers in the request and give you the Pydantic model you defined.

You can see the required headers in the docs UI at /docs:

In some special use cases (probably not very common), you might want to restrict the headers that you want to receive.

You can use Pydantic's model configuration to forbid any extra fields:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

If a client tries to send some extra headers, they will receive an error response.

For example, if the client tries to send a tool header with a value of plumbus, they will receive an error response telling them that the header parameter tool is not allowed:

The same way as with regular header parameters, when you have underscore characters in the parameter names, they are automatically converted to hyphens.

For example, if you have a header parameter save_data in the code, the expected HTTP header will be save-data, and it will show up like that in the docs.

If for some reason you need to disable this automatic conversion, you can do it as well for Pydantic models for header parameters.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Before setting convert_underscores to False, bear in mind that some HTTP p

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
```

```python
from typing import Annotated, Union

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: Union[str, None] = None
    traceparent: Union[str, None] = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
```

```python
from typing import List, Union

from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: Union[str, None] = None
    traceparent: Union[str, None] = None
    x_tag: List[str] = []


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
```

---

## Header Parameters - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/header-params/

**Contents**:
- Header Parameters¶
- Import Header¶
- Declare Header parameters¶
- Automatic conversion¶
- Duplicate headers¶
- Recap¶

You can define Header parameters the same way you define Query, Path and Cookie parameters.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Then declare the header parameters using the same structure as with Path, Query and Cookie.

You can define the default value as well as all the extra validation or annotation parameters:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Header is a "sister" class of Path, Query and Cookie. It also inherits from the same common Param class.

But remember that when you import Query, Path, Header, and others from fastapi, those are actually functions that return special classes.

To declare headers, you need to use Header, because otherwise the parameters would be interpreted as query parameters.

Header has a little extra functionality on top of what Path, Query and Cookie provide.

Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-).

But a variable like user-agent is invalid in Python.

So, by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.

Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case").

So, you can use user_agent as you normally would in Python code, instead of needing to capitalize the first letters as User_Agent or something similar.

If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter convert_underscores of Header to False:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Before setting convert_underscores to False, bear in mind that some HTTP proxies and servers disallow the usage of headers with underscores.

It is possible to receive duplicate headers. That means, the same header with multiple values.

You 

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```

```python
from typing import Annotated, Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}
```

```python
from typing import Union

from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}
```

---

## JSON Compatible Encoder - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/encoder/

**Contents**:
- JSON Compatible Encoder¶
- Using the jsonable_encoder¶

There are some cases where you might need to convert a data type (like a Pydantic model) to something compatible with JSON (like a dict, list, etc).

For example, if you need to store it in a database.

For that, FastAPI provides a jsonable_encoder() function.

Let's imagine that you have a database fake_db that only receives JSON compatible data.

For example, it doesn't receive datetime objects, as those are not compatible with JSON.

So, a datetime object would have to be converted to a str containing the data in ISO format.

The same way, this database wouldn't receive a Pydantic model (an object with attributes), only a dict.

You can use jsonable_encoder for that.

It receives an object, like a Pydantic model, and returns a JSON compatible version:

In this example, it would convert the Pydantic model to a dict, and the datetime to a str.

The result of calling it is something that can be encoded with the Python standard json.dumps().

It doesn't return a large str containing the data in JSON format (as a string). It returns a Python standard data structure (e.g. a dict) with values and sub-values that are all compatible with JSON.

jsonable_encoder is actually used by FastAPI internally to convert data. But it is useful in many other scenarios.

**Examples**:

```python
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
```

```python
from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
```

---

## Metadata and Docs URLs - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/metadata/

**Contents**:
- Metadata and Docs URLs¶
- Metadata for API¶
- License identifier¶
- Metadata for tags¶
  - Create metadata for tags¶
  - Use your tags¶
  - Check the docs¶
  - Order of tags¶

You can customize several metadata configurations in your FastAPI application.

You can set the following fields that are used in the OpenAPI specification and the automatic API docs UIs:

You can set them as follows:

You can write Markdown in the description field and it will be rendered in the output.

With this configuration, the automatic API docs would look like:

Since OpenAPI 3.1.0 and FastAPI 0.99.0, you can also set the license_info with an identifier instead of a url.

You can also add additional metadata for the different tags used to group your path operations with the parameter openapi_tags.

It takes a list containing one dictionary for each tag.

Each dictionary can contain:

Let's try that in an example with tags for users and items.

Create metadata for your tags and pass it to the openapi_tags parameter:

Notice that you can use Markdown inside of the descriptions, for example "login" will be shown in bold (login) and "fancy" will be shown in italics (fancy).

You don't have to add metadata for all the tags that you use.

Use the tags parameter with your path operations (and APIRouters) to assign them to different tags:

Read more about tags in Path Operation Configuration.

Now, if you check the docs, they will show all the additional metadata:

The order of each tag metadata dictionary also defines the order shown in the docs UI.

For example, even though users would go after items in alphabetical order, it is shown before them, because we added their metadata as the first dictionary in the list.

By default, the OpenAPI schema is served at /openapi.json.

But you can configure it with the parameter openapi_url.

For example, to set it to be served at /api/v1/openapi.json:

If you want to disable the OpenAPI schema completely you can set openapi_url=None, that will also disable the documentation user interfaces that use it.

You can configure the two documentation user interfaces included:

For example, to set Swagger UI to be served at /documen

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="ChimichangApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
     
...
```

```python
from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="ChimichangApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
     
...
```

```python
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/users/", tags=["user
...
```

---

## Middleware - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/middleware/

**Contents**:
- Middleware¶
- Create a middleware¶
  - Before and after the response¶
- Multiple middleware execution order¶
- Other middlewares¶

You can add middleware to FastAPI applications.

A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.

If you have dependencies with yield, the exit code will run after the middleware.

If there were any background tasks (covered in the Background Tasks section, you will see it later), they will run after all the middleware.

To create a middleware you use the decorator @app.middleware("http") on top of a function.

The middleware function receives:

Keep in mind that custom proprietary headers can be added using the X- prefix.

But if you have custom headers that you want a client in a browser to be able to see, you need to add them to your CORS configurations (CORS (Cross-Origin Resource Sharing)) using the parameter expose_headers documented in Starlette's CORS docs.

You could also use from starlette.requests import Request.

FastAPI provides it as a convenience for you, the developer. But it comes directly from Starlette.

You can add code to be run with the request, before any path operation receives it.

And also after the response is generated, before returning it.

For example, you could add a custom header X-Process-Time containing the time in seconds that it took to process the request and generate a response:

Here we use time.perf_counter() instead of time.time() because it can be more precise for these use cases. 🤓

When you add multiple middlewares using either @app.middleware() decorator or app.add_middleware() method, each new middleware wraps the application, forming a stack. The last middleware added is the outermost, and the first is the innermost.

On the request path, the outermost middleware runs first.

On the response path, it runs last.

This results in the following execution order:

Request: MiddlewareB → MiddlewareA → route

Response: route → MiddlewareA → MiddlewareB

This stacking behavior ensures that middlewares are executed

*[Content truncated - see full docs]*

**Examples**:

```python
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

```python
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

```text
app.add_middleware(MiddlewareA)
app.add_middleware(MiddlewareB)
```

---

## OAuth2 with Password (and hashing), Bearer with JWT tokens - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

**Contents**:
- OAuth2 with Password (and hashing), Bearer with JWT tokens¶
- About JWT¶
- Install PyJWT¶
- Password hashing¶
  - Why use password hashing¶
- Install pwdlib¶
- Hash and verify the passwords¶
- Handle JWT tokens¶

Now that we have all the security flow, let's make the application actually secure, using JWT tokens and secure password hashing.

This code is something you can actually use in your application, save the password hashes in your database, etc.

We are going to start from where we left in the previous chapter and increment it.

JWT means "JSON Web Tokens".

It's a standard to codify a JSON object in a long dense string without spaces. It looks like this:

It is not encrypted, so, anyone could recover the information from the contents.

But it's signed. So, when you receive a token that you emitted, you can verify that you actually emitted it.

That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.

After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.

If you want to play with JWT tokens and see how they work, check https://jwt.io.

We need to install PyJWT to generate and verify the JWT tokens in Python.

Make sure you create a virtual environment, activate it, and then install pyjwt:

If you are planning to use digital signature algorithms like RSA or ECDSA, you should install the cryptography library dependency pyjwt[crypto].

You can read more about it in the PyJWT Installation docs.

"Hashing" means converting some content (a password in this case) into a sequence of bytes (just a string) that looks like gibberish.

Whenever you pass exactly the same content (exactly the same password) you get exactly the same gibberish.

But you cannot convert from the gibberish back to the password.

If your database is stolen, the thief won't have your users' plaintext passwords, only the hashes.

So, the thief 

*[Content truncated - see full docs]*

**Examples**:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

```text
$ pip install pyjwt

---> 100%
```

```text
$ pip install "pwdlib[argon2]"

---> 100%
```

---

## Path Operation Configuration - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/

**Contents**:
- Path Operation Configuration¶
- Response Status Code¶
- Tags¶
  - Tags with Enums¶
- Summary and description¶
- Description from docstring¶
- Response description¶
- Deprecate a path operation¶

There are several parameters that you can pass to your path operation decorator to configure it.

Notice that these parameters are passed directly to the path operation decorator, not to your path operation function.

You can define the (HTTP) status_code to be used in the response of your path operation.

You can pass directly the int code, like 404.

But if you don't remember what each number code is for, you can use the shortcut constants in status:

That status code will be used in the response and will be added to the OpenAPI schema.

You could also use from starlette import status.

FastAPI provides the same starlette.status as fastapi.status just as a convenience for you, the developer. But it comes directly from Starlette.

You can add tags to your path operation, pass the parameter tags with a list of str (commonly just one str):

They will be added to the OpenAPI schema and used by the automatic documentation interfaces:

If you have a big application, you might end up accumulating several tags, and you would want to make sure you always use the same tag for related path operations.

In these cases, it could make sense to store the tags in an Enum.

FastAPI supports that the same way as with plain strings:

You can add a summary and description:

As descriptions tend to be long and cover multiple lines, you can declare the path operation description in the function docstring and FastAPI will read it from there.

You can write Markdown in the docstring, it will be interpreted and displayed correctly (taking into account docstring indentation).

It will be used in the interactive docs:

You can specify the response description with the parameter response_description:

Notice that response_description refers specifically to the response, the description refers to the path operation in general.

OpenAPI specifies that each path operation requires a response description.

So, if you don't provide one, FastAPI will automatically generate one of "Successful respo

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item
```

```python
from typing import Union

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item
```

```python
from typing import Set, Union

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item
```

---

## Path Parameters - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/path-params/

**Contents**:
- Path Parameters¶
- Path parameters with types¶
- Data conversion¶
- Data validation¶
- Documentation¶
- Standards-based benefits, alternative documentation¶
- Pydantic¶
- Order matters¶

You can declare path "parameters" or "variables" with the same syntax used by Python format strings:

The value of the path parameter item_id will be passed to your function as the argument item_id.

So, if you run this example and go to http://127.0.0.1:8000/items/foo, you will see a response of:

You can declare the type of a path parameter in the function, using standard Python type annotations:

In this case, item_id is declared to be an int.

This will give you editor support inside of your function, with error checks, completion, etc.

If you run this example and open your browser at http://127.0.0.1:8000/items/3, you will see a response of:

Notice that the value your function received (and returned) is 3, as a Python int, not a string "3".

So, with that type declaration, FastAPI gives you automatic request "parsing".

But if you go to the browser at http://127.0.0.1:8000/items/foo, you will see a nice HTTP error of:

because the path parameter item_id had a value of "foo", which is not an int.

The same error would appear if you provided a float instead of an int, as in: http://127.0.0.1:8000/items/4.2

So, with the same Python type declaration, FastAPI gives you data validation.

Notice that the error also clearly states exactly the point where the validation didn't pass.

This is incredibly helpful while developing and debugging code that interacts with your API.

And when you open your browser at http://127.0.0.1:8000/docs, you will see an automatic, interactive, API documentation like:

Again, just with that same Python type declaration, FastAPI gives you automatic, interactive documentation (integrating Swagger UI).

Notice that the path parameter is declared to be an integer.

And because the generated schema is from the OpenAPI standard, there are many compatible tools.

Because of this, FastAPI itself provides an alternative API documentation (using ReDoc), which you can access at http://127.0.0.1:8000/redoc:

The same way, there are many compatible

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

```text
{"item_id":"foo"}
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

---

## Path Parameters and Numeric Validations - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/

**Contents**:
- Path Parameters and Numeric Validations¶
- Import Path¶
- Declare metadata¶
- Order the parameters as you need¶
- Order the parameters as you need, tricks¶
  - Better with Annotated¶
- Number validations: greater than or equal¶
- Number validations: greater than and less than or equal¶

In the same way that you can declare more validations and metadata for query parameters with Query, you can declare the same type of validations and metadata for path parameters with Path.

First, import Path from fastapi, and import Annotated:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

FastAPI added support for Annotated (and started recommending it) in version 0.95.0.

If you have an older version, you would get errors when trying to use Annotated.

Make sure you Upgrade the FastAPI version to at least 0.95.1 before using Annotated.

You can declare all the same parameters as for Query.

For example, to declare a title metadata value for the path parameter item_id you can type:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

A path parameter is always required as it has to be part of the path. Even if you declared it with None or set a default value, it would not affect anything, it would still be always required.

This is probably not as important or necessary if you use Annotated.

Let's say that you want to declare the query parameter q as a required str.

And you don't need to declare anything else for that parameter, so you don't really need to use Query.

But you still need to use Path for the item_id path parameter. And you don't want to use Annotated for some reason.

Python will complain if you put a value with a "default" before a value that doesn't have a "default".

But you can re-order them, and have the value without a default (the query parameter q) first.

It doesn't matter for FastAPI. It will detect the parameters by their names, types and default declarations (Query, Path, etc), it doesn't care about the order.

So, you can declare your function as:

But keep in mind that if you use Annotated, you won't have this problem, it won't matter as you're not using the function parameter default values for Query() or Path().

Prefer to use the 

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Annotated, Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

---

## Query Parameter Models - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/query-param-models/

**Contents**:
- Query Parameter Models¶
- Query Parameters with a Pydantic Model¶
- Check the Docs¶
- Forbid Extra Query Parameters¶
- Summary¶

If you have a group of query parameters that are related, you can create a Pydantic model to declare them.

This would allow you to re-use the model in multiple places and also to declare validations and metadata for all the parameters at once. 😎

This is supported since FastAPI version 0.115.0. 🤓

Declare the query parameters that you need in a Pydantic model, and then declare the parameter as Query:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

FastAPI will extract the data for each field from the query parameters in the request and give you the Pydantic model you defined.

You can see the query parameters in the docs UI at /docs:

In some special use cases (probably not very common), you might want to restrict the query parameters that you want to receive.

You can use Pydantic's model configuration to forbid any extra fields:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

If a client tries to send some extra data in the query parameters, they will receive an error response.

For example, if the client tries to send a tool query parameter with a value of plumbus, like:

They will receive an error response telling them that the query parameter tool is not allowed:

You can use Pydantic models to declare query parameters in FastAPI. 😎

Spoiler alert: you can also use Pydantic models to declare cookies and headers, but you will read about that later in the tutorial. 🤫

**Examples**:

```python
from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
```

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated, Literal

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
```

```python
from typing import List

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated, Literal

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: List[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
```

---

## Query Parameters - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/query-params/

**Contents**:
- Query Parameters¶
- Defaults¶
- Optional parameters¶
- Query parameter type conversion¶
- Multiple path and query parameters¶
- Required query parameters¶

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.

For example, in the URL:

...the query parameters are:

As they are part of the URL, they are "naturally" strings.

But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

All the same process that applied for path parameters also applies for query parameters:

As query parameters are not a fixed part of a path, they can be optional and can have default values.

In the example above they have default values of skip=0 and limit=10.

So, going to the URL:

would be the same as going to:

But if you go to, for example:

The parameter values in your function will be:

The same way, you can declare optional query parameters, by setting their default to None:

In this case, the function parameter q will be optional, and will be None by default.

Also notice that FastAPI is smart enough to notice that the path parameter item_id is a path parameter and q is not, so, it's a query parameter.

You can also declare bool types, and they will be converted:

In this case, if you go to:

or any other case variation (uppercase, first letter in uppercase, etc), your function will see the parameter short with a bool value of True. Otherwise as False.

You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.

And you don't have to declare them in any specific order.

They will be detected by name:

When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.

If you don't want to add a specific value but just make it optional, set the default as None.

But when you want to make a query parameter required, you can just not declare any default value:

He

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

```text
http://127.0.0.1:8000/items/?skip=0&limit=10
```

```text
http://127.0.0.1:8000/items/
```

---

## Query Parameters and String Validations - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

**Contents**:
- Query Parameters and String Validations¶
- Additional validation¶
  - Import Query and Annotated¶
- Use Annotated in the type for the q parameter¶
- Add Query to Annotated in the q parameter¶
- Alternative (old): Query as the default value¶
  - Query as the default value or in Annotated¶
  - Advantages of Annotated¶

FastAPI allows you to declare additional information and validation for your parameters.

Let's take this application as example:

The query parameter q is of type str | None, that means that it's of type str but could also be None, and indeed, the default value is None, so FastAPI will know it's not required.

FastAPI will know that the value of q is not required because of the default value = None.

Having str | None will allow your editor to give you better support and detect errors.

We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

To achieve that, first import:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

FastAPI added support for Annotated (and started recommending it) in version 0.95.0.

If you have an older version, you would get errors when trying to use Annotated.

Make sure you Upgrade the FastAPI version to at least 0.95.1 before using Annotated.

Remember I told you before that Annotated can be used to add metadata to your parameters in the Python Types Intro?

Now it's the time to use it with FastAPI. 🚀

We had this type annotation:

What we will do is wrap that with Annotated, so it becomes:

Both of those versions mean the same thing, q is a parameter that can be a str or None, and by default, it is None.

Now let's jump to the fun stuff. 🎉

Now that we have this Annotated where we can put more information (in this case some additional validation), add Query inside of Annotated, and set the parameter max_length to 50:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Notice that the default value is still None, so the parameter is still optional.

But now, having Query(max_length=50) inside of Annotated, we are telling FastAPI that we want it to have additional validation for this value, we want it to have maximum 50 characters. 😎

Here we are using Query() because this is

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

---

## Request Body - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/body/

**Contents**:
- Request Body¶
- Import Pydantic's BaseModel¶
- Create your data model¶
- Declare it as a parameter¶
- Results¶
- Automatic docs¶
- Editor support¶
- Use the model¶

When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.

A request body is data sent by the client to your API. A response body is the data your API sends to the client.

Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time, sometimes they only request a path, maybe with some query parameters, but don't send a body.

To declare a request body, you use Pydantic models with all their power and benefits.

To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.

Sending a body with a GET request has an undefined behavior in the specifications, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.

As it is discouraged, the interactive docs with Swagger UI won't show the documentation for the body when using GET, and proxies in the middle might not support it.

First, you need to import BaseModel from pydantic:

Then you declare your data model as a class that inherits from BaseModel.

Use standard Python types for all the attributes:

The same as when declaring query parameters, when a model attribute has a default value, it is not required. Otherwise, it is required. Use None to make it just optional.

For example, this model above declares a JSON "object" (or Python dict) like:

...as description and tax are optional (with a default value of None), this JSON "object" would also be valid:

To add it to your path operation, declare it the same way you declared path and query parameters:

...and declare its type as the model you created, Item.

With just that Python type declaration, FastAPI will:

The JSON Schemas of your models will be part of your OpenAPI generated schema, and will be shown in the interactive API docs:

And will also be used in the API docs inside each path operation that needs them:

In your editor, inside your function you will get type hints and completion everywhere (this 

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

---

## Request Files - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/request-files/

**Contents**:
- Request Files¶
- Import File¶
- Define File Parameters¶
- File Parameters with UploadFile¶
  - UploadFile¶
- What is "Form Data"¶
- Optional File Upload¶
- UploadFile with Additional Metadata¶

You can define files to be uploaded by the client using File.

To receive uploaded files, first install python-multipart.

Make sure you create a virtual environment, activate it, and then install it, for example:

This is because uploaded files are sent as "form data".

Import File and UploadFile from fastapi:

Prefer to use the Annotated version if possible.

Create file parameters the same way you would for Body or Form:

Prefer to use the Annotated version if possible.

File is a class that inherits directly from Form.

But remember that when you import Query, Path, File and others from fastapi, those are actually functions that return special classes.

To declare File bodies, you need to use File, because otherwise the parameters would be interpreted as query parameters or body (JSON) parameters.

The files will be uploaded as "form data".

If you declare the type of your path operation function parameter as bytes, FastAPI will read the file for you and you will receive the contents as bytes.

Keep in mind that this means that the whole contents will be stored in memory. This will work well for small files.

But there are several cases in which you might benefit from using UploadFile.

Define a file parameter with a type of UploadFile:

Prefer to use the Annotated version if possible.

Using UploadFile has several advantages over bytes:

UploadFile has the following attributes:

UploadFile has the following async methods. They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

As all these methods are async methods, you need to "await" them.

For example, inside of an async path operation function you can get the contents with:

If you are inside of a normal def path operation function, you can access the UploadFile.file directly, for example:

async Technical Details

When you use the async methods, FastAPI runs the file methods in a threadpool and awaits for them.

Starlette Technical Details

FastAPI's UploadFile i

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install python-multipart
```

```python
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

```python
from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

---

## Request Forms and Files - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/request-forms-and-files/

**Contents**:
- Request Forms and Files¶
- Import File and Form¶
- Define File and Form parameters¶
- Recap¶

You can define files and form fields at the same time using File and Form.

To receive uploaded files and/or form data, first install python-multipart.

Make sure you create a virtual environment, activate it, and then install it, for example:

Prefer to use the Annotated version if possible.

Create file and form parameters the same way you would for Body or Query:

Prefer to use the Annotated version if possible.

The files and form fields will be uploaded as form data and you will receive the files and form fields.

And you can declare some of the files as bytes and some as UploadFile.

You can declare multiple File and Form parameters in a path operation, but you can't also declare Body fields that you expect to receive as JSON, as the request will have the body encoded using multipart/form-data instead of application/json.

This is not a limitation of FastAPI, it's part of the HTTP protocol.

Use File and Form together when you need to receive data and files in the same request.

**Examples**:

```text
$ pip install python-multipart
```

```python
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```

```python
from fastapi import FastAPI, File, Form, UploadFile
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
```

---

## Response Model - Return Type - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/response-model/

**Contents**:
- Response Model - Return Type¶
- response_model Parameter¶
  - response_model Priority¶
- Return the same input data¶
- Add an output model¶
  - response_model or Return Type¶
- Return Type and Data Filtering¶
  - Type Annotations and Tooling¶

You can declare the type used for the response by annotating the path operation function return type.

You can use type annotations the same way you would for input data in function parameters, you can use Pydantic models, lists, dictionaries, scalar values like integers, booleans, etc.

FastAPI will use this return type to:

But most importantly:

There are some cases where you need or want to return some data that is not exactly what the type declares.

For example, you could want to return a dictionary or a database object, but declare it as a Pydantic model. This way the Pydantic model would do all the data documentation, validation, etc. for the object that you returned (e.g. a dictionary or database object).

If you added the return type annotation, tools and editors would complain with a (correct) error telling you that your function is returning a type (e.g. a dict) that is different from what you declared (e.g. a Pydantic model).

In those cases, you can use the path operation decorator parameter response_model instead of the return type.

You can use the response_model parameter in any of the path operations:

Notice that response_model is a parameter of the "decorator" method (get, post, etc). Not of your path operation function, like all the parameters and body.

response_model receives the same type you would declare for a Pydantic model field, so, it can be a Pydantic model, but it can also be, e.g. a list of Pydantic models, like List[Item].

FastAPI will use this response_model to do all the data documentation, validation, etc. and also to convert and filter the output data to its type declaration.

If you have strict type checks in your editor, mypy, etc, you can declare the function return type as Any.

That way you tell the editor that you are intentionally returning anything. But FastAPI will still do the data documentation, validation, filtering, etc. with the response_model.

If you declare both a return type and a response_model, the response_

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
```

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
...
```

```python
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> List[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=
...
```

---

## Response Status Code - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/response-status-code/

**Contents**:
- Response Status Code¶
- About HTTP status codes¶
- Shortcut to remember the names¶
- Changing the default¶

The same way you can specify a response model, you can also declare the HTTP status code used for the response with the parameter status_code in any of the path operations:

Notice that status_code is a parameter of the "decorator" method (get, post, etc). Not of your path operation function, like all the parameters and body.

The status_code parameter receives a number with the HTTP status code.

status_code can alternatively also receive an IntEnum, such as Python's http.HTTPStatus.

Some response codes (see the next section) indicate that the response does not have a body.

FastAPI knows this, and will produce OpenAPI docs that state there is no response body.

If you already know what HTTP status codes are, skip to the next section.

In HTTP, you send a numeric status code of 3 digits as part of the response.

These status codes have a name associated to recognize them, but the important part is the number.

To know more about each status code and which code is for what, check the MDN documentation about HTTP status codes.

Let's see the previous example again:

201 is the status code for "Created".

But you don't have to memorize what each of these codes mean.

You can use the convenience variables from fastapi.status.

They are just a convenience, they hold the same number, but that way you can use the editor's autocomplete to find them:

You could also use from starlette import status.

FastAPI provides the same starlette.status as fastapi.status just as a convenience for you, the developer. But it comes directly from Starlette.

Later, in the Advanced User Guide, you will see how to return a different status code than the default you are declaring here.

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

```python
from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
```

---

## SQL (Relational) Databases - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/sql-databases/

**Contents**:
- SQL (Relational) Databases¶
- Install SQLModel¶
- Create the App with a Single Model¶
  - Create Models¶
  - Create an Engine¶
  - Create the Tables¶
  - Create a Session Dependency¶
  - Create Database Tables on Startup¶

FastAPI doesn't require you to use a SQL (relational) database. But you can use any database that you want.

Here we'll see an example using SQLModel.

SQLModel is built on top of SQLAlchemy and Pydantic. It was made by the same author of FastAPI to be the perfect match for FastAPI applications that need to use SQL databases.

You could use any other SQL or NoSQL database library you want (in some cases called "ORMs"), FastAPI doesn't force you to use anything. 😎

As SQLModel is based on SQLAlchemy, you can easily use any database supported by SQLAlchemy (which makes them also supported by SQLModel), like:

In this example, we'll use SQLite, because it uses a single file and Python has integrated support. So, you can copy this example and run it as is.

Later, for your production application, you might want to use a database server like PostgreSQL.

There is an official project generator with FastAPI and PostgreSQL including a frontend and more tools: https://github.com/fastapi/full-stack-fastapi-template

This is a very simple and short tutorial, if you want to learn about databases in general, about SQL, or more advanced features, go to the SQLModel docs.

First, make sure you create your virtual environment, activate it, and then install sqlmodel:

We'll create the simplest first version of the app with a single SQLModel model first.

Later we'll improve it increasing security and versatility with multiple models below. 🤓

Import SQLModel and create a database model:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

The Hero class is very similar to a Pydantic model (in fact, underneath, it actually is a Pydantic model).

There are a few differences:

table=True tells SQLModel that this is a table model, it should represent a table in the SQL database, it's not just a data model (as would be any other regular Pydantic class).

Field(primary_key=True) tells SQLMode

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install sqlmodel
---> 100%
```

```python
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

# Code below omitted 👇
```

```python
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = crea
...
```

---

## Security - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/security/

**Contents**:
- Security¶
- In a hurry?¶
- OAuth2¶
  - OAuth 1¶
- OpenID Connect¶
  - OpenID (not "OpenID Connect")¶
- OpenAPI¶
- FastAPI utilities¶

There are many ways to handle security, authentication and authorization.

And it normally is a complex and "difficult" topic.

In many frameworks and systems just handling security and authentication takes a big amount of effort and code (in many cases it can be 50% or more of all the code written).

FastAPI provides several tools to help you deal with Security easily, rapidly, in a standard way, without having to study and learn all the security specifications.

But first, let's check some small concepts.

If you don't care about any of these terms and you just need to add security with authentication based on username and password right now, skip to the next chapters.

OAuth2 is a specification that defines several ways to handle authentication and authorization.

It is quite an extensive specification and covers several complex use cases.

It includes ways to authenticate using a "third party".

That's what all the systems with "login with Facebook, Google, X (Twitter), GitHub" use underneath.

There was an OAuth 1, which is very different from OAuth2, and more complex, as it included direct specifications on how to encrypt the communication.

It is not very popular or used nowadays.

OAuth2 doesn't specify how to encrypt the communication, it expects you to have your application served with HTTPS.

In the section about deployment you will see how to set up HTTPS for free, using Traefik and Let's Encrypt.

OpenID Connect is another specification, based on OAuth2.

It just extends OAuth2 specifying some things that are relatively ambiguous in OAuth2, to try to make it more interoperable.

For example, Google login uses OpenID Connect (which underneath uses OAuth2).

But Facebook login doesn't support OpenID Connect. It has its own flavor of OAuth2.

There was also an "OpenID" specification. That tried to solve the same thing as OpenID Connect, but was not based on OAuth2.

So, it was a complete additional system.

It is not very popular or used nowadays.

OpenAPI

*[Content truncated - see full docs]*

---

## Security - First Steps - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/security/first-steps/

**Contents**:
- Security - First Steps¶
- How it looks¶
- Create main.py¶
- Run it¶
- Check it¶
- The password flow¶
- FastAPI's OAuth2PasswordBearer¶
  - Use it¶

Let's imagine that you have your backend API in some domain.

And you have a frontend in another domain or in a different path of the same domain (or in a mobile application).

And you want to have a way for the frontend to authenticate with the backend, using a username and password.

We can use OAuth2 to build that with FastAPI.

But let's save you the time of reading the full long specification just to find those little pieces of information you need.

Let's use the tools provided by FastAPI to handle security.

Let's first just use the code and see how it works, and then we'll come back to understand what's happening.

Copy the example in a file main.py:

Prefer to use the Annotated version if possible.

The python-multipart package is automatically installed with FastAPI when you run the pip install "fastapi[standard]" command.

However, if you use the pip install fastapi command, the python-multipart package is not included by default.

To install it manually, make sure you create a virtual environment, activate it, and then install it with:

This is because OAuth2 uses "form data" for sending the username and password.

Run the example with:

Go to the interactive docs at: http://127.0.0.1:8000/docs.

You will see something like this:

You already have a shiny new "Authorize" button.

And your path operation has a little lock in the top-right corner that you can click.

And if you click it, you have a little authorization form to type a username and password (and other optional fields):

It doesn't matter what you type in the form, it won't work yet. But we'll get there.

This is of course not the frontend for the final users, but it's a great automatic tool to document interactively all your API.

It can be used by the frontend team (that can also be yourself).

It can be used by third party applications and systems.

And it can also be used by yourself, to debug, check and test the same application.

Now let's go back a bit and understand what is all that.


*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

---

## Simple OAuth2 with Password and Bearer - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/

**Contents**:
- Simple OAuth2 with Password and Bearer¶
- Get the username and password¶
  - scope¶
- Code to get the username and password¶
  - OAuth2PasswordRequestForm¶
  - Use the form data¶
  - Check the password¶
    - Password hashing¶

Now let's build from the previous chapter and add the missing parts to have a complete security flow.

We are going to use FastAPI security utilities to get the username and password.

OAuth2 specifies that when using the "password flow" (that we are using) the client/user must send a username and password fields as form data.

And the spec says that the fields have to be named like that. So user-name or email wouldn't work.

But don't worry, you can show it as you wish to your final users in the frontend.

And your database models can use any other names you want.

But for the login path operation, we need to use these names to be compatible with the spec (and be able to, for example, use the integrated API documentation system).

The spec also states that the username and password must be sent as form data (so, no JSON here).

The spec also says that the client can send another form field "scope".

The form field name is scope (in singular), but it is actually a long string with "scopes" separated by spaces.

Each "scope" is just a string (without spaces).

They are normally used to declare specific security permissions, for example:

In OAuth2 a "scope" is just a string that declares a specific permission required.

It doesn't matter if it has other characters like : or if it is a URL.

Those details are implementation specific.

For OAuth2 they are just strings.

Now let's use the utilities provided by FastAPI to handle this.

First, import OAuth2PasswordRequestForm, and use it as a dependency with Depends in the path operation for /token:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

OAuth2PasswordRequestForm is a class dependency that declares a form body with:

The OAuth2 spec actually requires a field grant_type with a fixed value of password, but OAuth2PasswordRequestForm doesn't enforce it.

If you need to enforce it, use OAuth2PasswordRequestFormStrict instead of OAuth2PasswordRequestForm.

The OAuth2

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson
...
```

```python
from typing import Annotated, Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wo
...
```

```python
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing_extensions import Annotated

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
 
...
```

---

## Static Files - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/static-files/

**Contents**:
- Static Files¶
- Use StaticFiles¶
  - What is "Mounting"¶
- Details¶
- More info¶

You can serve static files automatically from a directory using StaticFiles.

You could also use from starlette.staticfiles import StaticFiles.

FastAPI provides the same starlette.staticfiles as fastapi.staticfiles just as a convenience for you, the developer. But it actually comes directly from Starlette.

"Mounting" means adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths.

This is different from using an APIRouter as a mounted application is completely independent. The OpenAPI and docs from your main application won't include anything from the mounted application, etc.

You can read more about this in the Advanced User Guide.

The first "/static" refers to the sub-path this "sub-application" will be "mounted" on. So, any path that starts with "/static" will be handled by it.

The directory="static" refers to the name of the directory that contains your static files.

The name="static" gives it a name that can be used internally by FastAPI.

All these parameters can be different than "static", adjust them with the needs and specific details of your own application.

For more details and options check Starlette's docs about Static Files.

**Examples**:

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

---

## Sub-dependencies - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/

**Contents**:
- Sub-dependencies¶
- First dependency "dependable"¶
- Second dependency, "dependable" and "dependant"¶
- Use the dependency¶
- Using the same dependency multiple times¶
- Recap¶

You can create dependencies that have sub-dependencies.

They can be as deep as you need them to be.

FastAPI will take care of solving them.

You could create a first dependency ("dependable") like:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

It declares an optional query parameter q as a str, and then it just returns it.

This is quite simple (not very useful), but will help us focus on how the sub-dependencies work.

Then you can create another dependency function (a "dependable") that at the same time declares a dependency of its own (so it is a "dependant" too):

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Let's focus on the parameters declared:

Then we can use the dependency with:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Notice that we are only declaring one dependency in the path operation function, the query_or_cookie_extractor.

But FastAPI will know that it has to solve query_extractor first, to pass the results of that to query_or_cookie_extractor while calling it.

If one of your dependencies is declared multiple times for the same path operation, for example, multiple dependencies have a common sub-dependency, FastAPI will know to call that sub-dependency only once per request.

And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific request, instead of calling the dependency multiple times for the same request.

In an advanced scenario where you know you need the dependency to be called at every step (possibly multiple times) in the same request instead of using the "cached" value, you can set the parameter use_cache=False when using Depends:

Prefer to use the Annotated version if possible.

Apart from all the fancy words used here, the Dependency Injection system is quite simple.

Just functions that look the same as the 

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or
...
```

```python
from typing import Annotated, Union

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_o
...
```

```python
from typing import Union

from fastapi import Cookie, Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()


def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_ext
...
```

---

## Testing - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/testing/

**Contents**:
- Testing¶
- Using TestClient¶
- Separating tests¶
  - FastAPI app file¶
  - Testing file¶
- Testing: extended example¶
  - Extended FastAPI app file¶
  - Extended testing file¶

Thanks to Starlette, testing FastAPI applications is easy and enjoyable.

It is based on HTTPX, which in turn is designed based on Requests, so it's very familiar and intuitive.

With it, you can use pytest directly with FastAPI.

To use TestClient, first install httpx.

Make sure you create a virtual environment, activate it, and then install it, for example:

Create a TestClient by passing your FastAPI application to it.

Create functions with a name that starts with test_ (this is standard pytest conventions).

Use the TestClient object the same way as you do with httpx.

Write simple assert statements with the standard Python expressions that you need to check (again, standard pytest).

Notice that the testing functions are normal def, not async def.

And the calls to the client are also normal calls, not using await.

This allows you to use pytest directly without complications.

You could also use from starlette.testclient import TestClient.

FastAPI provides the same starlette.testclient as fastapi.testclient just as a convenience for you, the developer. But it comes directly from Starlette.

If you want to call async functions in your tests apart from sending requests to your FastAPI application (e.g. asynchronous database functions), have a look at the Async Tests in the advanced tutorial.

In a real application, you probably would have your tests in a different file.

And your FastAPI application might also be composed of several files/modules, etc.

Let's say you have a file structure as described in Bigger Applications:

In the file main.py you have your FastAPI app:

Then you could have a file test_main.py with your tests. It could live on the same Python package (the same directory with a __init__.py file):

Because this file is in the same package, you can use relative imports to import the object app from the main module (main.py):

...and have the code for the tests just like before.

Now let's extend this example and add more details to see how to 

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install httpx
```

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
```

```text
.
├── app
│   ├── __init__.py
│   └── main.py
```

---

## Tutorial - User Guide - FastAPI

**URL**: https://fastapi.tiangolo.com/tutorial/

**Contents**:
- Tutorial - User Guide¶
- Run the code¶
- Install FastAPI¶
- Advanced User Guide¶

This tutorial shows you how to use FastAPI with most of its features, step by step.

Each section gradually builds on the previous ones, but it's structured to separate topics, so that you can go directly to any specific one to solve your specific API needs.

It is also built to work as a future reference so you can come back and see exactly what you need.

All the code blocks can be copied and used directly (they are actually tested Python files).

To run any of the examples, copy the code to a file main.py, and start fastapi dev with:

It is HIGHLY encouraged that you write or copy the code, edit it and run it locally.

Using it in your editor is what really shows you the benefits of FastAPI, seeing how little code you have to write, all the type checks, autocompletion, etc.

The first step is to install FastAPI.

Make sure you create a virtual environment, activate it, and then install FastAPI:

When you install with pip install "fastapi[standard]" it comes with some default optional standard dependencies, including fastapi-cloud-cli, which allows you to deploy to FastAPI Cloud.

If you don't want to have those optional dependencies, you can instead install pip install fastapi.

If you want to install the standard dependencies but without the fastapi-cloud-cli, you can install with pip install "fastapi[standard-no-fastapi-cloud-cli]".

There is also an Advanced User Guide that you can read later after this Tutorial - User guide.

The Advanced User Guide builds on this one, uses the same concepts, and teaches you some extra features.

But you should first read the Tutorial - User Guide (what you are reading right now).

It's designed so that you can build a complete application with just the Tutorial - User Guide, and then extend it in different ways, depending on your needs, using some of the additional ideas from the Advanced User Guide.

**Examples**:

```python
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166
...
```

```text
$ pip install "fastapi[standard]"

---> 100%
```

---

## 查询参数 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/tutorial/query-params/

**Contents**:
- 查询参数¶
- 默认值¶
- 可选参数¶
- 查询参数类型转换¶
- 多个路径和查询参数¶
- 必选查询参数¶

声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数。

查询字符串是键值对的集合，这些键值对位于 URL 的 ? 之后，以 & 分隔。

这些值都是 URL 的组成部分，因此，它们的类型本应是字符串。

但声明 Python 类型（上例中为 int）之后，这些值就会转换为声明的类型，并进行类型校验。

所有应用于路径参数的流程也适用于查询参数：

查询参数不是路径的固定内容，它是可选的，还支持默认值。

上例用 skip=0 和 limit=10 设定默认值。

同理，把默认值设为 None 即可声明可选的查询参数：

本例中，查询参数 q 是可选的，默认值为 None。

注意，FastAPI 可以识别出 item_id 是路径参数，q 不是路径参数，而是查询参数。

因为默认值为 = None，FastAPI 把 q 识别为可选参数。

FastAPI 不使用 Optional[str] 中的 Optional（只使用 str），但 Optional[str] 可以帮助编辑器发现代码中的错误。

参数还可以声明为 bool 类型，FastAPI 会自动转换参数类型：

或其它任意大小写形式（大写、首字母大写等），函数接收的 short 参数都是布尔值 True。值为 False 时也一样。

FastAPI 可以识别同时声明的多个路径参数和查询参数。

为不是路径参数的参数声明默认值（至此，仅有查询参数），该参数就不是必选的了。

如果只想把参数设为可选，但又不想指定参数的值，则要把默认值设为 None。

如果要把查询参数设置为必选，就不要声明默认值：

这里的查询参数 needy 是类型为 str 的必选查询参数。

……因为路径中没有必选参数 needy，返回的响应中会显示如下错误信息：

needy 是必选参数，因此要在 URL 中设置值：

当然，把一些参数定义为必选，为另一些参数设置默认值，再把其它参数定义为可选，这些操作都是可以的：

还可以像在路径参数 中那样使用 Enum。

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

```text
http://127.0.0.1:8000/items/?skip=0&limit=10
```

```text
http://127.0.0.1:8000/items/
```

---

## 查询参数和字符串校验 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/tutorial/query-params-str-validations/

**Contents**:
- 查询参数和字符串校验¶
- 额外的校验¶
  - 导入 Query¶
- 使用 Query 作为默认值¶
- 添加更多校验¶
- 添加正则表达式¶
- 默认值¶
- 声明为必需参数¶

FastAPI 允许你为参数声明额外的信息和校验。

查询参数 q 的类型为 str，默认值为 None，因此它是可选的。

我们打算添加约束条件：即使 q 是可选的，但只要提供了该参数，则该参数值不能超过50个字符的长度。

为此，首先从 fastapi 导入 Query：

Prefer to use the Annotated version if possible.

现在，将 Query 用作查询参数的默认值，并将它的 max_length 参数设置为 50：

Prefer to use the Annotated version if possible.

由于我们必须用 Query(default=None) 替换默认值 None，Query 的第一个参数同样也是用于定义默认值。

但是 Query 显式地将其声明为查询参数。

然后，我们可以将更多的参数传递给 Query。在本例中，适用于字符串的 max_length 参数：

将会校验数据，在数据无效时展示清晰的错误信息，并在 OpenAPI 模式的路径操作中记录该参​​数。

你还可以添加 min_length 参数：

Prefer to use the Annotated version if possible.

你可以定义一个参数值必须匹配的正则表达式：

Prefer to use the Annotated version if possible.

这个指定的正则表达式通过以下规则检查接收到的参数值：

如果你对所有的这些「正则表达式」概念感到迷茫，请不要担心。对于许多人来说这都是一个困难的主题。你仍然可以在无需正则表达式的情况下做很多事情。

但是，一旦你需要用到并去学习它们时，请了解你已经可以在 FastAPI 中直接使用它们。

你可以向 Query 的第一个参数传入 None 用作查询参数的默认值，以同样的方式你也可以传递其他默认值。

假设你想要声明查询参数 q，使其 min_length 为 3，并且默认值为 fixedquery：

当我们不需要声明额外的校验或元数据时，只需不声明默认值就可以使 q 参数成为必需参数，例如：

但是现在我们正在用 Query 声明它，例如：

因此，当你在使用 Query 且需要声明一个值是必需的时，只需不声明默认参数：

你可以声明一个参数可以接收None值，但它仍然是必需的。这将强制客户端发送一个值，即使该值是None。

为此，你可以声明None是一个有效的类型，并仍然使用default=...：

Prefer to use the Annotated version if possible.

Pydantic 是 FastAPI 中所有数据验证和序列化的核心，当你在没有设默认值的情况下使用 Optional 或 Union[Something, None] 时，它具有特殊行为，你可以在 Pydantic 文档中阅读有关必需可选字段的更多信息。

当你使用 Query 显式地定义查询参数时，你还可以声明它去接收一组值，或换句话来说，接收多个值。

例如，要声明一个可在 URL 中出现多次的查询参数 q，你可以这样写：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

你会在路径操作函数的函数参数 q 中以一个 Python list 的形式接收到查询参数 q 的多个值（foo 和 bar）。

要声明类型为 list 的查询参数，如上例所示，你需要显式地使用 Query，否则该参数将被解释为请求体。

交互式 API 文档将会相应地进行更新，以允许使用多个值：

你还可以定义在没有任何给定值时的默认 list 值：

Prefer to use the Annotated version if possible.

q 的默认值将为：["foo", "bar"]，你的响应会是：

你也可以直接使用 list 代替 List [str]：

请记住，在这种情况下 FastAPI 将不会检查列表的内容。

例如，List[int] 将检查（并记录到文档）列表的内容必须是整数。但是单独的 list 不会。

这些信息将包含在生成的 OpenAPI 模式中，并由文档用户界面和外部工具所使用。

请记住，不同的工具对 OpenAPI 的支持程度可能不同。

其中一些可能不会展示所有已声明的额外信息，尽管在大多数情况下，缺少的这部分功能已经计划进行开发。

Prefer to use the Annotated version if possib

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

---

## 请求体 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/tutorial/body/

**Contents**:
- 请求体¶
- 导入 Pydantic 的 BaseModel¶
- 创建数据模型¶
- 声明请求体参数¶
- 结论¶
- API 文档¶
- 编辑器支持¶
- 使用模型¶

FastAPI 使用请求体从客户端（例如浏览器）向 API 发送数据。

请求体是客户端发送给 API 的数据。响应体是 API 发送给客户端的数据。

API 基本上肯定要发送响应体，但是客户端不一定发送请求体。

使用 Pydantic 模型声明请求体，能充分利用它的功能和优点。

发送数据使用 POST（最常用）、PUT、DELETE、PATCH 等操作。

规范中没有定义使用 GET 发送请求体的操作，但不管怎样，FastAPI 也支持这种方式，只不过仅用于非常复杂或极端的用例。

我们不建议使用 GET，因此，在 Swagger UI 交互文档中不会显示有关 GET 的内容，而且代理协议也不一定支持 GET。

从 pydantic 中导入 BaseModel：

把数据模型声明为继承 BaseModel 的类。

使用 Python 标准类型声明所有属性：

与声明查询参数一样，包含默认值的模型属性是可选的，否则就是必选的。默认值为 None 的模型属性也是可选的。

例如，上述模型声明如下 JSON 对象（即 Python 字典）：

……由于 description 和 tax 是可选的（默认值为 None），下面的 JSON 对象也有效：

使用与声明路径和查询参数相同的方式声明请求体，把请求体添加至路径操作：

……此处，请求体参数的类型为 Item 模型。

仅使用 Python 类型声明，FastAPI 就可以：

Pydantic 模型的 JSON 概图是 OpenAPI 生成的概图部件，可在 API 文档中显示：

而且，还会用于 API 文档中使用了概图的路径操作：

在编辑器中，函数内部均可使用类型提示、代码补全（如果接收的不是 Pydantic 模型，而是字典，就没有这样的支持）：

这并非偶然，整个 FastAPI 框架都是围绕这种思路精心设计的。

并且，在 FastAPI 的设计阶段，我们就已经进行了全面测试，以确保 FastAPI 可以获得所有编辑器的支持。

我们还改进了 Pydantic，让它也支持这些功能。

虽然上面的截图取自 Visual Studio Code。

但 PyCharm 和大多数 Python 编辑器也支持同样的功能：

使用 PyCharm 编辑器时，推荐安装 Pydantic PyCharm 插件。

该插件用于完善 PyCharm 对 Pydantic 模型的支持，优化的功能如下：

在路径操作函数内部直接访问模型对象的属性：

FastAPI 支持同时声明路径参数和请求体。

FastAPI 能识别与路径参数匹配的函数参数，还能识别从请求体中获取的类型为 Pydantic 模型的函数参数。

FastAPI 支持同时声明请求体、路径参数和查询参数。

FastAPI 能够正确识别这三种参数，并从正确的位置获取数据。

因为默认值是 None， FastAPI 会把 q 当作可选参数。

FastAPI 不使用 Optional[str] 中的 Optional， 但 Optional 可以让编辑器提供更好的支持，并检测错误。

即便不使用 Pydantic 模型也能使用 Body 参数。详见请求体 - 多参数：请求体中的单值。

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

---

## 请求体 - 多个参数 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/tutorial/body-multiple-params/

**Contents**:
- 请求体 - 多个参数¶
- 混合使用 Path、Query 和请求体参数¶
- 多个请求体参数¶
- 请求体中的单一值¶
- 多个请求体参数和查询参数¶
- 嵌入单个请求体参数¶
- 总结¶

既然我们已经知道了如何使用 Path 和 Query，下面让我们来了解一下请求体声明的更高级用法。

首先，毫无疑问地，你可以随意地混合使用 Path、Query 和请求体参数声明，FastAPI 会知道该如何处理。

你还可以通过将默认值设置为 None 来将请求体参数声明为可选参数：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

请注意，在这种情况下，将从请求体获取的 item 是可选的。因为它的默认值为 None。

在上面的示例中，路径操作将期望一个具有 Item 的属性的 JSON 请求体，就像：

但是你也可以声明多个请求体参数，例如 item 和 user：

在这种情况下，FastAPI 将注意到该函数中有多个请求体参数（两个 Pydantic 模型参数）。

因此，它将使用参数名称作为请求体中的键（字段名称），并期望一个类似于以下内容的请求体：

请注意，即使 item 的声明方式与之前相同，但现在它被期望通过 item 键内嵌在请求体中。

FastAPI 将自动对请求中的数据进行转换，因此 item 参数将接收指定的内容，user 参数也是如此。

它将执行对复合数据的校验，并且像现在这样为 OpenAPI 模式和自动化文档对其进行记录。

与使用 Query 和 Path 为查询参数和路径参数定义额外数据的方式相同，FastAPI 提供了一个同等的 Body。

例如，为了扩展先前的模型，你可能决定除了 item 和 user 之外，还想在同一请求体中具有另一个键 importance。

如果你就按原样声明它，因为它是一个单一值，FastAPI 将假定它是一个查询参数。

但是你可以使用 Body 指示 FastAPI 将其作为请求体的另一个键进行处理。

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

在这种情况下，FastAPI 将期望像这样的请求体：

同样的，它将转换数据类型，校验，生成文档等。

当然，除了请求体参数外，你还可以在任何需要的时候声明额外的查询参数。

由于默认情况下单一值被解释为查询参数，因此你不必显式地添加 Query，你可以仅执行以下操作：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Body 同样具有与 Query、Path 以及其他后面将看到的类完全相同的额外校验和元数据参数。

假设你只有一个来自 Pydantic 模型 Item 的请求体参数 item。

默认情况下，FastAPI 将直接期望这样的请求体。

但是，如果你希望它期望一个拥有 item 键并在值中包含模型内容的 JSON，就像在声明额外的请求体参数时所做的那样，则可以使用一个特殊的 Body 参数 embed：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

在这种情况下，FastAPI 将期望像这样的请求体：

你可以添加多个请求体参数到路径操作函数中，即使一个请求只能有一个请求体。

但是 FastAPI 会处理它，在函数中为你提供正确的数据，并在路径操作中校验并记录正确的模式。

你还可以声明将作为请求体的一部分所接收的单一值。

你还可以指示 FastAPI 在仅声明了一个请求体参数的情况下，将原本的请求体嵌入到一个键中。

**Examples**:

```python
from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"
...
```

```python
from typing import Annotated, Union

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    
...
```

```python
from typing import Union

from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    result
...
```

---

## 请求体 - 字段 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/tutorial/body-fields/

**Contents**:
- 请求体 - 字段¶
- 导入 Field¶
- 声明模型属性¶
- 添加更多信息¶
- 小结¶

与在路径操作函数中使用 Query、Path 、Body 声明校验与元数据的方式一样，可以使用 Pydantic 的 Field 在 Pydantic 模型内部声明校验和元数据。

首先，从 Pydantic 中导入 Field：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

注意，与从 fastapi 导入 Query，Path、Body 不同，要直接从 pydantic 导入 Field 。

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

Field 的工作方式和 Query、Path、Body 相同，参数也相同。

实际上，Query、Path 都是 Params 的子类，而 Params 类又是 Pydantic 中 FieldInfo 的子类。

Pydantic 的 Field 返回也是 FieldInfo 的类实例。

Body 直接返回的也是 FieldInfo 的子类的对象。后文还会介绍一些 Body 的子类。

注意，从 fastapi 导入的 Query、Path 等对象实际上都是返回特殊类的函数。

注意，模型属性的类型、默认值及 Field 的代码结构与路径操作函数的参数相同，只不过是用 Field 替换了Path、Query、Body。

Field、Query、Body 等对象里可以声明更多信息，并且 JSON Schema 中也会集成这些信息。

声明示例一章中将详细介绍添加更多信息的知识。

Pydantic 的 Field 可以为模型属性声明更多校验和元数据。

传递 JSON Schema 元数据还可以使用更多关键字参数。

**Examples**:

```python
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    r
...
```

```python
from typing import Annotated, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(e
...
```

```python
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int,
...
```

---

## 路径参数和数值校验 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/tutorial/path-params-numeric-validations/

**Contents**:
- 路径参数和数值校验¶
- 导入 Path¶
- 声明元数据¶
- 按需对参数排序¶
- 按需对参数排序的技巧¶
- 数值校验：大于等于¶
- 数值校验：大于和小于等于¶
- 数值校验：浮点数、大于和小于¶

与使用 Query 为查询参数声明更多的校验和元数据的方式相同，你也可以使用 Path 为路径参数声明相同类型的校验和元数据。

首先，从 fastapi 导入 Path：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

你可以声明与 Query 相同的所有参数。

例如，要声明路径参数 item_id的 title 元数据值，你可以输入：

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

路径参数总是必需的，因为它必须是路径的一部分。

所以，你应该在声明时使用 ... 将其标记为必需参数。

然而，即使你使用 None 声明路径参数或设置一个其他默认值也不会有任何影响，它依然会是必需参数。

假设你想要声明一个必需的 str 类型查询参数 q。

而且你不需要为该参数声明任何其他内容，所以实际上你并不需要使用 Query。

但是你仍然需要使用 Path 来声明路径参数 item_id。

如果你将带有「默认值」的参数放在没有「默认值」的参数之前，Python 将会报错。

但是你可以对其重新排序，并将不带默认值的值（查询参数 q）放到最前面。

对 FastAPI 来说这无关紧要。它将通过参数的名称、类型和默认值声明（Query、Path 等）来检测参数，而不在乎参数的顺序。

如果你想不使用 Query 声明没有默认值的查询参数 q，同时使用 Path 声明路径参数 item_id，并使它们的顺序与上面不同，Python 对此有一些特殊的语法。

Python 不会对该 * 做任何事情，但是它将知道之后的所有参数都应作为关键字参数（键值对），也被称为 kwargs，来调用。即使它们没有默认值。

使用 Query 和 Path（以及你将在后面看到的其他类）可以声明字符串约束，但也可以声明数值约束。

像下面这样，添加 ge=1 后，item_id 将必须是一个大于（greater than）或等于（equal）1 的整数。

能够声明 gt 而不仅仅是 ge 在这个前提下变得重要起来。例如，你可以要求一个值必须大于 0，即使它小于 1。

因此，0.5 将是有效值。但是 0.0或 0 不是。

你能够以与 查询参数和字符串校验 相同的方式使用 Query、Path（以及其他你还没见过的类）声明元数据和字符串校验。

Query、Path 以及你后面会看到的其他类继承自一个共同的 Param 类（不需要直接使用它）。

而且它们都共享相同的所有你已看到并用于添加额外校验和元数据的参数。

当你从 fastapi 导入 Query、Path 和其他同类对象时，它们实际上是函数。

如此，你导入 Query 这个函数。当你调用它时，它将返回一个同样命名为 Query 的类的实例。

因为使用了这些函数（而不是直接使用类），所以你的编辑器不会标记有关其类型的错误。

这样，你可以使用常规的编辑器和编码工具，而不必添加自定义配置来忽略这些错误。

**Examples**:

```python
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Annotated, Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

```python
from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

---
