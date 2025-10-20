# Fastapi - Advanced

**Pages**: 34

---

## Additional Responses in OpenAPI - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/additional-responses/

**Contents**:
- Additional Responses in OpenAPI¶
- Additional Response with model¶
- Additional media types for the main response¶
- Combining information¶
- Combine predefined responses and custom ones¶
- More information about OpenAPI responses¶

This is a rather advanced topic.

If you are starting with FastAPI, you might not need this.

You can declare additional responses, with additional status codes, media types, descriptions, etc.

Those additional responses will be included in the OpenAPI schema, so they will also appear in the API docs.

But for those additional responses you have to make sure you return a Response like JSONResponse directly, with your status code and content.

You can pass to your path operation decorators a parameter responses.

It receives a dict: the keys are status codes for each response (like 200), and the values are other dicts with the information for each of them.

Each of those response dicts can have a key model, containing a Pydantic model, just like response_model.

FastAPI will take that model, generate its JSON Schema and include it in the correct place in OpenAPI.

For example, to declare another response with a status code 404 and a Pydantic model Message, you can write:

Keep in mind that you have to return the JSONResponse directly.

The model key is not part of OpenAPI.

FastAPI will take the Pydantic model from there, generate the JSON Schema, and put it in the correct place.

The correct place is:

The generated responses in the OpenAPI for this path operation will be:

The schemas are referenced to another place inside the OpenAPI schema:

You can use this same responses parameter to add different media types for the same main response.

For example, you can add an additional media type of image/png, declaring that your path operation can return a JSON object (with media type application/json) or a PNG image:

Notice that you have to return the image using a FileResponse directly.

Unless you specify a different media type explicitly in your responses parameter, FastAPI will assume the response has the same media type as the main response class (default application/json).

But if you have specified a custom response class with None as its media type, FastAPI w

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


app = FastAPI()


@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    return JSONResponse(status_code=404, content={"message": "Item not fou
...
```

```text
{
    "responses": {
        "404": {
            "description": "Additional Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/Message"
                    }
                }
            }
        },
        "200": {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$r
...
```

```text
{
    "components": {
        "schemas": {
            "Message": {
                "title": "Message",
                "required": [
                    "message"
                ],
                "type": "object",
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string"
                    }
                }
            },
            "Item": {
                "title": "Item",
                "requir
...
```

---

## Additional Status Codes - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/additional-status-codes/

**Contents**:
- Additional Status Codes¶
- Additional status codes¶
- OpenAPI and API docs¶

By default, FastAPI will return the responses using a JSONResponse, putting the content you return from your path operation inside of that JSONResponse.

It will use the default status code or the one you set in your path operation.

If you want to return additional status codes apart from the main one, you can do that by returning a Response directly, like a JSONResponse, and set the additional status code directly.

For example, let's say that you want to have a path operation that allows to update items, and returns HTTP status codes of 200 "OK" when successful.

But you also want it to accept new items. And when the items didn't exist before, it creates them, and returns an HTTP status code of 201 "Created".

To achieve that, import JSONResponse, and return your content there directly, setting the status_code that you want:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

When you return a Response directly, like in the example above, it will be returned directly.

It won't be serialized with a model, etc.

Make sure it has the data you want it to have, and that the values are valid JSON (if you are using JSONResponse).

You could also use from starlette.responses import JSONResponse.

FastAPI provides the same starlette.responses as fastapi.responses just as a convenience for you, the developer. But most of the available responses come directly from Starlette. The same with status.

If you return additional status codes and responses directly, they won't be included in the OpenAPI schema (the API docs), because FastAPI doesn't have a way to know beforehand what you are going to return.

But you can document that in your code, using: Additional Responses.

**Examples**:

```python
from typing import Annotated

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
async def upsert_item(
    item_id: str,
    name: Annotated[str | None, Body()] = None,
    size: Annotated[int | None, Body()] = None,
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = si
...
```

```python
from typing import Annotated, Union

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
async def upsert_item(
    item_id: str,
    name: Annotated[Union[str, None], Body()] = None,
    size: Annotated[Union[int, None], Body()] = None,
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
      
...
```

```python
from typing import Union

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse
from typing_extensions import Annotated

app = FastAPI()

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
async def upsert_item(
    item_id: str,
    name: Annotated[Union[str, None], Body()] = None,
    size: Annotated[Union[int, None], Body()] = None,
):
    if item_id in items:
        item = items[item_id]
     
...
```

---

## Advanced Dependencies - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/advanced-dependencies/

**Contents**:
- Advanced Dependencies¶
- Parameterized dependencies¶
- A "callable" instance¶
- Parameterize the instance¶
- Create an instance¶
- Use the instance as a dependency¶
- Dependencies with yield, HTTPException, except and Background Tasks¶
  - Dependencies with yield and StreamingResponse, Technical Details¶

All the dependencies we have seen are a fixed function or class.

But there could be cases where you want to be able to set parameters on the dependency, without having to declare many different functions or classes.

Let's imagine that we want to have a dependency that checks if the query parameter q contains some fixed content.

But we want to be able to parameterize that fixed content.

In Python there's a way to make an instance of a class a "callable".

Not the class itself (which is already a callable), but an instance of that class.

To do that, we declare a method __call__:

Prefer to use the Annotated version if possible.

In this case, this __call__ is what FastAPI will use to check for additional parameters and sub-dependencies, and this is what will be called to pass a value to the parameter in your path operation function later.

And now, we can use __init__ to declare the parameters of the instance that we can use to "parameterize" the dependency:

Prefer to use the Annotated version if possible.

In this case, FastAPI won't ever touch or care about __init__, we will use it directly in our code.

We could create an instance of this class with:

Prefer to use the Annotated version if possible.

And that way we are able to "parameterize" our dependency, that now has "bar" inside of it, as the attribute checker.fixed_content.

Then, we could use this checker in a Depends(checker), instead of Depends(FixedContentQueryChecker), because the dependency is the instance, checker, not the class itself.

And when solving the dependency, FastAPI will call this checker like:

...and pass whatever that returns as the value of the dependency in our path operation function as the parameter fixed_content_included:

Prefer to use the Annotated version if possible.

All this might seem contrived. And it might not be very clear how is it useful yet.

These examples are intentionally simple, but show how it all works.

In the chapters about security, there are utility func

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("bar")


@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed
...
```

```python
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("bar")


@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    retu
...
```

```python
from fastapi import Depends, FastAPI

app = FastAPI()


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("bar")


@app.get("/query-checker/")
async def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_includ
...
```

---

## Advanced Middleware - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/middleware/

**Contents**:
- Advanced Middleware¶
- Adding ASGI middlewares¶
- Integrated middlewares¶
- HTTPSRedirectMiddleware¶
- TrustedHostMiddleware¶
- GZipMiddleware¶
- Other middlewares¶

In the main tutorial you read how to add Custom Middleware to your application.

And then you also read how to handle CORS with the CORSMiddleware.

In this section we'll see how to use other middlewares.

As FastAPI is based on Starlette and implements the ASGI specification, you can use any ASGI middleware.

A middleware doesn't have to be made for FastAPI or Starlette to work, as long as it follows the ASGI spec.

In general, ASGI middlewares are classes that expect to receive an ASGI app as the first argument.

So, in the documentation for third-party ASGI middlewares they will probably tell you to do something like:

But FastAPI (actually Starlette) provides a simpler way to do it that makes sure that the internal middlewares handle server errors and custom exception handlers work properly.

For that, you use app.add_middleware() (as in the example for CORS).

app.add_middleware() receives a middleware class as the first argument and any additional arguments to be passed to the middleware.

FastAPI includes several middlewares for common use cases, we'll see next how to use them.

For the next examples, you could also use from starlette.middleware.something import SomethingMiddleware.

FastAPI provides several middlewares in fastapi.middleware just as a convenience for you, the developer. But most of the available middlewares come directly from Starlette.

Enforces that all incoming requests must either be https or wss.

Any incoming request to http or ws will be redirected to the secure scheme instead.

Enforces that all incoming requests have a correctly set Host header, in order to guard against HTTP Host Header attacks.

The following arguments are supported:

If an incoming request does not validate correctly then a 400 response will be sent.

Handles GZip responses for any request that includes "gzip" in the Accept-Encoding header.

The middleware will handle both standard and streaming responses.

The following arguments are supported:

There are many ot

*[Content truncated - see full docs]*

**Examples**:

```python
from unicorn import UnicornMiddleware

app = SomeASGIApp()

new_app = UnicornMiddleware(app, some_config="rainbow")
```

```python
from fastapi import FastAPI
from unicorn import UnicornMiddleware

app = FastAPI()

app.add_middleware(UnicornMiddleware, some_config="rainbow")
```

```python
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def main():
    return {"message": "Hello World"}
```

---

## Advanced Security - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/security/

**Contents**:
- Advanced Security¶
- Additional Features¶
- Read the Tutorial first¶

There are some extra features to handle security apart from the ones covered in the Tutorial - User Guide: Security.

The next sections are not necessarily "advanced".

And it's possible that for your use case, the solution is in one of them.

The next sections assume you already read the main Tutorial - User Guide: Security.

They are all based on the same concepts, but allow some extra functionalities.

---

## Advanced User Guide - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/

**Contents**:
- Advanced User Guide¶
- Additional Features¶
- Read the Tutorial first¶

The main Tutorial - User Guide should be enough to give you a tour through all the main features of FastAPI.

In the next sections you will see other options, configurations, and additional features.

The next sections are not necessarily "advanced".

And it's possible that for your use case, the solution is in one of them.

You could still use most of the features in FastAPI with the knowledge from the main Tutorial - User Guide.

And the next sections assume you already read it, and assume that you know those main ideas.

---

## Async Tests - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/async-tests/

**Contents**:
- Async Tests¶
- pytest.mark.anyio¶
- HTTPX¶
- Example¶
- Run it¶
- In Detail¶
- Other Asynchronous Function Calls¶

You have already seen how to test your FastAPI applications using the provided TestClient. Up to now, you have only seen how to write synchronous tests, without using async functions.

Being able to use asynchronous functions in your tests could be useful, for example, when you're querying your database asynchronously. Imagine you want to test sending requests to your FastAPI application and then verify that your backend successfully wrote the correct data in the database, while using an async database library.

Let's look at how we can make that work.

If we want to call asynchronous functions in our tests, our test functions have to be asynchronous. AnyIO provides a neat plugin for this, that allows us to specify that some test functions are to be called asynchronously.

Even if your FastAPI application uses normal def functions instead of async def, it is still an async application underneath.

The TestClient does some magic inside to call the asynchronous FastAPI application in your normal def test functions, using standard pytest. But that magic doesn't work anymore when we're using it inside asynchronous functions. By running our tests asynchronously, we can no longer use the TestClient inside our test functions.

The TestClient is based on HTTPX, and luckily, we can use it directly to test the API.

For a simple example, let's consider a file structure similar to the one described in Bigger Applications and Testing:

The file main.py would have:

The file test_main.py would have the tests for main.py, it could look like this now:

You can run your tests as usual via:

The marker @pytest.mark.anyio tells pytest that this test function should be called asynchronously:

Note that the test function is now async def instead of just def as before when using the TestClient.

Then we can create an AsyncClient with the app, and send async requests to it, using await.

This is the equivalent to:

...that we used to make our requests with the TestClient.

Note that we'r

*[Content truncated - see full docs]*

**Examples**:

```text
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Tomato"}
```

```python
import pytest
from httpx import ASGITransport, AsyncClient

from .main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}
```

---

## Behind a Proxy - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/behind-a-proxy/

**Contents**:
- Behind a Proxy¶
- Proxy Forwarded Headers¶
  - Enable Proxy Forwarded Headers¶
  - Redirects with HTTPS¶
  - How Proxy Forwarded Headers Work¶
- Proxy with a stripped path prefix¶
  - Providing the root_path¶
  - Checking the current root_path¶

In many situations, you would use a proxy like Traefik or Nginx in front of your FastAPI app.

These proxies could handle HTTPS certificates and other things.

A proxy in front of your application would normally set some headers on the fly before sending the requests to your server to let the server know that the request was forwarded by the proxy, letting it know the original (public) URL, including the domain, that it is using HTTPS, etc.

The server program (for example Uvicorn via FastAPI CLI) is capable of interpreting these headers, and then passing that information to your application.

But for security, as the server doesn't know it is behind a trusted proxy, it won't interpret those headers.

The proxy headers are:

You can start FastAPI CLI with the CLI Option --forwarded-allow-ips and pass the IP addresses that should be trusted to read those forwarded headers.

If you set it to --forwarded-allow-ips="*" it would trust all the incoming IPs.

If your server is behind a trusted proxy and only the proxy talks to it, this would make it accept whatever is the IP of that proxy.

For example, let's say you define a path operation /items/:

If the client tries to go to /items, by default, it would be redirected to /items/.

But before setting the CLI Option --forwarded-allow-ips it could redirect to http://localhost:8000/items/.

But maybe your application is hosted at https://mysuperapp.com, and the redirection should be to https://mysuperapp.com/items/.

By setting --proxy-headers now FastAPI would be able to redirect to the right location. 😎

If you want to learn more about HTTPS, check the guide About HTTPS.

Here's a visual representation of how the proxy adds forwarded headers between the client and the application server:

The proxy intercepts the original client request and adds the special forwarded headers (X-Forwarded-*) before passing the request to the application server.

These headers preserve information about the original request that would other

*[Content truncated - see full docs]*

**Examples**:

```text
$ fastapi run --forwarded-allow-ips="*"

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
def read_items():
    return ["plumbus", "portal gun"]
```

```text
https://mysuperapp.com/items/
```

---

## Custom Response - HTML, Stream, File, others - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/custom-response/

**Contents**:
- Custom Response - HTML, Stream, File, others¶
- Use ORJSONResponse¶
- HTML Response¶
  - Return a Response¶
  - Document in OpenAPI and override Response¶
    - Return an HTMLResponse directly¶
- Available responses¶
  - Response¶

By default, FastAPI will return the responses using JSONResponse.

You can override it by returning a Response directly as seen in Return a Response directly.

But if you return a Response directly (or any subclass, like JSONResponse), the data won't be automatically converted (even if you declare a response_model), and the documentation won't be automatically generated (for example, including the specific "media type", in the HTTP header Content-Type as part of the generated OpenAPI).

But you can also declare the Response that you want to be used (e.g. any Response subclass), in the path operation decorator using the response_class parameter.

The contents that you return from your path operation function will be put inside of that Response.

And if that Response has a JSON media type (application/json), like is the case with the JSONResponse and UJSONResponse, the data you return will be automatically converted (and filtered) with any Pydantic response_model that you declared in the path operation decorator.

If you use a response class with no media type, FastAPI will expect your response to have no content, so it will not document the response format in its generated OpenAPI docs.

For example, if you are squeezing performance, you can install and use orjson and set the response to be ORJSONResponse.

Import the Response class (sub-class) you want to use and declare it in the path operation decorator.

For large responses, returning a Response directly is much faster than returning a dictionary.

This is because by default, FastAPI will inspect every item inside and make sure it is serializable as JSON, using the same JSON Compatible Encoder explained in the tutorial. This is what allows you to return arbitrary objects, for example database models.

But if you are certain that the content that you are returning is serializable with JSON, you can pass it directly to the response class and avoid the extra overhead that FastAPI would have by passing your return co

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])
```

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
```

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/items/")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
```

---

## Dependencies - Depends() and Security() - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/dependencies/

**Contents**:
- Dependencies - Depends() and Security()¶
- Depends()¶
- fastapi.Depends ¶
- Security()¶
- fastapi.Security ¶

Dependencies are handled mainly with the special function Depends() that takes a callable.

Here is the reference for it and its parameters.

You can import it directly from fastapi:

Declare a FastAPI dependency.

It takes a single "dependable" callable (like a function).

Don't call it directly, FastAPI will call it for you.

Read more about it in the FastAPI docs for Dependencies.

A "dependable" callable (like a function).

Don't call it directly, FastAPI will call it for you, just pass the object directly.

TYPE: Optional[Callable[..., Any]] DEFAULT: None

By default, after a dependency is called the first time in a request, if the dependency is declared again for the rest of the request (for example if the dependency is needed by several dependencies), the value will be re-used for the rest of the request.

Set use_cache to False to disable this behavior and ensure the dependency is called again (if declared more than once) in the same request.

TYPE: bool DEFAULT: True

For many scenarios, you can handle security (authorization, authentication, etc.) with dependencies, using Depends().

But when you want to also declare OAuth2 scopes, you can use Security() instead of Depends().

You can import Security() directly from fastapi:

Declare a FastAPI Security dependency.

The only difference with a regular dependency is that it can declare OAuth2 scopes that will be integrated with OpenAPI and the automatic UI docs (by default at /docs).

It takes a single "dependable" callable (like a function).

Don't call it directly, FastAPI will call it for you.

Read more about it in the FastAPI docs for Security and in the FastAPI docs for OAuth2 scopes.

A "dependable" callable (like a function).

Don't call it directly, FastAPI will call it for you, just pass the object directly.

TYPE: Optional[Callable[..., Any]] DEFAULT: None

OAuth2 scopes required for the path operation that uses this Security dependency.

The term "scope" comes from the OAuth2 specification, it see

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import Depends
```

```text
Depends(dependency=None, *, use_cache=True)
```

```python
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

---

## FastAPI in Containers - Docker - FastAPI

**URL**: https://fastapi.tiangolo.com/deployment/docker/

**Contents**:
- FastAPI in Containers - Docker¶
- What is a Container¶
- What is a Container Image¶
- Container Images¶
- Containers and Processes¶
- Build a Docker Image for FastAPI¶
  - Package Requirements¶
  - Create the FastAPI Code¶

When deploying FastAPI applications a common approach is to build a Linux container image. It's normally done using Docker. You can then deploy that container image in one of a few possible ways.

Using Linux containers has several advantages including security, replicability, simplicity, and others.

In a hurry and already know this stuff? Jump to the Dockerfile below 👇.

Containers (mainly Linux containers) are a very lightweight way to package applications including all their dependencies and necessary files while keeping them isolated from other containers (other applications or components) in the same system.

Linux containers run using the same Linux kernel of the host (machine, virtual machine, cloud server, etc). This just means that they are very lightweight (compared to full virtual machines emulating an entire operating system).

This way, containers consume little resources, an amount comparable to running the processes directly (a virtual machine would consume much more).

Containers also have their own isolated running processes (commonly just one process), file system, and network, simplifying deployment, security, development, etc.

A container is run from a container image.

A container image is a static version of all the files, environment variables, and the default command/program that should be present in a container. Static here means that the container image is not running, it's not being executed, it's only the packaged files and metadata.

In contrast to a "container image" that is the stored static contents, a "container" normally refers to the running instance, the thing that is being executed.

When the container is started and running (started from a container image) it could create or change files, environment variables, etc. Those changes will exist only in that container, but would not persist in the underlying container image (would not be saved to disk).

A container image is comparable to the program file and contents, e.g. python 

*[Content truncated - see full docs]*

**Examples**:

```text
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]
```

```text
fastapi[standard]>=0.113.0,<0.114.0
pydantic>=2.7.0,<3.0.0
```

```text
$ pip install -r requirements.txt
---> 100%
Successfully installed fastapi pydantic
```

---

## Generating SDKs - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/generate-clients/

**Contents**:
- Generating SDKs¶
- Open Source SDK Generators¶
- SDK Generators from FastAPI Sponsors¶
- Create a TypeScript SDK¶
  - API Docs¶
  - Hey API¶
  - Using the SDK¶
- FastAPI App with Tags¶

Because FastAPI is based on the OpenAPI specification, its APIs can be described in a standard format that many tools understand.

This makes it easy to generate up-to-date documentation, client libraries (SDKs) in multiple languages, and testing or automation workflows that stay in sync with your code.

In this guide, you'll learn how to generate a TypeScript SDK for your FastAPI backend.

A versatile option is the OpenAPI Generator, which supports many programming languages and can generate SDKs from your OpenAPI specification.

For TypeScript clients, Hey API is a purpose-built solution, providing an optimized experience for the TypeScript ecosystem.

You can discover more SDK generators on OpenAPI.Tools.

FastAPI automatically generates OpenAPI 3.1 specifications, so any tool you use must support this version.

This section highlights venture-backed and company-supported solutions from companies that sponsor FastAPI. These products provide additional features and integrations on top of high-quality generated SDKs.

By ✨ sponsoring FastAPI ✨, these companies help ensure the framework and its ecosystem remain healthy and sustainable.

Their sponsorship also demonstrates a strong commitment to the FastAPI community (you), showing that they care not only about offering a great service but also about supporting a robust and thriving framework, FastAPI. 🙇

For example, you might want to try:

Some of these solutions may also be open source or offer free tiers, so you can try them without a financial commitment. Other commercial SDK generators are available and can be found online. 🤓

Let's start with a simple FastAPI application:

Notice that the path operations define the models they use for request payload and response payload, using the models Item and ResponseMessage.

If you go to /docs, you will see that it has the schemas for the data to be sent in requests and received in responses:

You can see those schemas because they were declared with the models in the a

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class ResponseMessage(BaseModel):
    message: str


@app.post("/items/", response_model=ResponseMessage)
async def create_item(item: Item):
    return {"message": "item received"}


@app.get("/items/", response_model=list[Item])
async def get_items():
    return [
        {"name": "Plumbus", "price": 3},
        {"name": "Portal Gun", "price": 9001},
    ]
```

```python
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class ResponseMessage(BaseModel):
    message: str


@app.post("/items/", response_model=ResponseMessage)
async def create_item(item: Item):
    return {"message": "item received"}


@app.get("/items/", response_model=List[Item])
async def get_items():
    return [
        {"name": "Plumbus", "price": 3},
        {"name": "Portal Gun", "pr
...
```

```text
npx @hey-api/openapi-ts -i http://localhost:8000/openapi.json -o src/client
```

---

## HTTP Basic Auth - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/security/http-basic-auth/

**Contents**:
- HTTP Basic Auth¶
- Simple HTTP Basic Auth¶
- Check the username¶
  - Timing Attacks¶
    - The time to answer helps the attackers¶
    - A "professional" attack¶
    - Fix it with secrets.compare_digest()¶
  - Return the error¶

For the simplest cases, you can use HTTP Basic Auth.

In HTTP Basic Auth, the application expects a header that contains a username and a password.

If it doesn't receive it, it returns an HTTP 401 "Unauthorized" error.

And returns a header WWW-Authenticate with a value of Basic, and an optional realm parameter.

That tells the browser to show the integrated prompt for a username and password.

Then, when you type that username and password, the browser sends them in the header automatically.

Prefer to use the Annotated version if possible.

When you try to open the URL for the first time (or click the "Execute" button in the docs) the browser will ask you for your username and password:

Here's a more complete example.

Use a dependency to check if the username and password are correct.

For this, use the Python standard module secrets to check the username and password.

secrets.compare_digest() needs to take bytes or a str that only contains ASCII characters (the ones in English), this means it wouldn't work with characters like á, as in Sebastián.

To handle that, we first convert the username and password to bytes encoding them with UTF-8.

Then we can use secrets.compare_digest() to ensure that credentials.username is "stanleyjobson", and that credentials.password is "swordfish".

Prefer to use the Annotated version if possible.

This would be similar to:

But by using the secrets.compare_digest() it will be secure against a type of attacks called "timing attacks".

But what's a "timing attack"?

Let's imagine some attackers are trying to guess the username and password.

And they send a request with a username johndoe and a password love123.

Then the Python code in your application would be equivalent to something like:

But right at the moment Python compares the first j in johndoe to the first s in stanleyjobson, it will return False, because it already knows that those two strings are not the same, thinking that "there's no need to waste more computatio

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing_extensions import Annotated

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
```

---

## Including WSGI - Flask, Django, others - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/wsgi/

**Contents**:
- Including WSGI - Flask, Django, others¶
- Using WSGIMiddleware¶
- Check it¶

You can mount WSGI applications as you saw with Sub Applications - Mounts, Behind a Proxy.

For that, you can use the WSGIMiddleware and use it to wrap your WSGI application, for example, Flask, Django, etc.

You need to import WSGIMiddleware.

Then wrap the WSGI (e.g. Flask) app with the middleware.

And then mount that under a path.

Now, every request under the path /v1/ will be handled by the Flask application.

And the rest will be handled by FastAPI.

If you run it and go to http://localhost:8000/v1/ you will see the response from Flask:

And if you go to http://localhost:8000/v2 you will see the response from FastAPI:

**Examples**:

```python
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, request
from markupsafe import escape

flask_app = Flask(__name__)


@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


app = FastAPI()


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


app.mount("/v1", WSGIMiddleware(flask_app))
```

```text
Hello, World from Flask!
```

```text
{
    "message": "Hello World"
}
```

---

## Lifespan Events - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/events/

**Contents**:
- Lifespan Events¶
- Use Case¶
- Lifespan¶
  - Lifespan function¶
  - Async Context Manager¶
- Alternative Events (deprecated)¶
  - startup event¶
  - shutdown event¶

You can define logic (code) that should be executed before the application starts up. This means that this code will be executed once, before the application starts receiving requests.

The same way, you can define logic (code) that should be executed when the application is shutting down. In this case, this code will be executed once, after having handled possibly many requests.

Because this code is executed before the application starts taking requests, and right after it finishes handling requests, it covers the whole application lifespan (the word "lifespan" will be important in a second 😉).

This can be very useful for setting up resources that you need to use for the whole app, and that are shared among requests, and/or that you need to clean up afterwards. For example, a database connection pool, or loading a shared machine learning model.

Let's start with an example use case and then see how to solve it with this.

Let's imagine that you have some machine learning models that you want to use to handle requests. 🤖

The same models are shared among requests, so, it's not one model per request, or one per user or something similar.

Let's imagine that loading the model can take quite some time, because it has to read a lot of data from disk. So you don't want to do it for every request.

You could load it at the top level of the module/file, but that would also mean that it would load the model even if you are just running a simple automated test, then that test would be slow because it would have to wait for the model to load before being able to run an independent part of the code.

That's what we'll solve, let's load the model before the requests are handled, but only right before the application starts receiving requests, not while the code is being loaded.

You can define this startup and shutdown logic using the lifespan parameter of the FastAPI app, and a "context manager" (I'll show you what that is in a second).

Let's start with an example and then 

*[Content truncated - see full docs]*

**Examples**:

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result 
...
```

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result 
...
```

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result 
...
```

---

## OAuth2 scopes - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/

**Contents**:
- OAuth2 scopes¶
- OAuth2 scopes and OpenAPI¶
- Global view¶
- OAuth2 Security scheme¶
- JWT token with scopes¶
- Declare scopes in path operations and dependencies¶
- Use SecurityScopes¶
- Use the scopes¶

You can use OAuth2 scopes directly with FastAPI, they are integrated to work seamlessly.

This would allow you to have a more fine-grained permission system, following the OAuth2 standard, integrated into your OpenAPI application (and the API docs).

OAuth2 with scopes is the mechanism used by many big authentication providers, like Facebook, Google, GitHub, Microsoft, X (Twitter), etc. They use it to provide specific permissions to users and applications.

Every time you "log in with" Facebook, Google, GitHub, Microsoft, X (Twitter), that application is using OAuth2 with scopes.

In this section you will see how to manage authentication and authorization with the same OAuth2 with scopes in your FastAPI application.

This is a more or less advanced section. If you are just starting, you can skip it.

You don't necessarily need OAuth2 scopes, and you can handle authentication and authorization however you want.

But OAuth2 with scopes can be nicely integrated into your API (with OpenAPI) and your API docs.

Nevertheless, you still enforce those scopes, or any other security/authorization requirement, however you need, in your code.

In many cases, OAuth2 with scopes can be an overkill.

But if you know you need it, or you are curious, keep reading.

The OAuth2 specification defines "scopes" as a list of strings separated by spaces.

The content of each of these strings can have any format, but should not contain spaces.

These scopes represent "permissions".

In OpenAPI (e.g. the API docs), you can define "security schemes".

When one of these security schemes uses OAuth2, you can also declare and use scopes.

Each "scope" is just a string (without spaces).

They are normally used to declare specific security permissions, for example:

In OAuth2 a "scope" is just a string that declares a specific permission required.

It doesn't matter if it has other characters like : or if it is a URL.

Those details are implementation specific.

For OAuth2 they are just strings.



*[Content truncated - see full docs]*

**Examples**:

```python
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel, ValidationError

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a956
...
```

```python
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union

import jwt
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel, ValidationError

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c81816
...
```

```python
from datetime import datetime, timedelta, timezone
from typing import List, Union

import jwt
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel, ValidationError
from typing_extensions import Annotated

# to get a string like this run:
# openssl rand -hex 32
SECR
...
```

---

## OpenAPI Callbacks - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/openapi-callbacks/

**Contents**:
- OpenAPI Callbacks¶
- An app with callbacks¶
- The normal FastAPI app¶
- Documenting the callback¶
- Write the callback documentation code¶
  - Create a callback APIRouter¶
  - Create the callback path operation¶
  - The callback path expression¶

You could create an API with a path operation that could trigger a request to an external API created by someone else (probably the same developer that would be using your API).

The process that happens when your API app calls the external API is named a "callback". Because the software that the external developer wrote sends a request to your API and then your API calls back, sending a request to an external API (that was probably created by the same developer).

In this case, you could want to document how that external API should look like. What path operation it should have, what body it should expect, what response it should return, etc.

Let's see all this with an example.

Imagine you develop an app that allows creating invoices.

These invoices will have an id, title (optional), customer, and total.

The user of your API (an external developer) will create an invoice in your API with a POST request.

Then your API will (let's imagine):

Let's first see how the normal API app would look like before adding the callback.

It will have a path operation that will receive an Invoice body, and a query parameter callback_url that will contain the URL for the callback.

This part is pretty normal, most of the code is probably already familiar to you:

The callback_url query parameter uses a Pydantic Url type.

The only new thing is the callbacks=invoices_callback_router.routes as an argument to the path operation decorator. We'll see what that is next.

The actual callback code will depend heavily on your own API app.

And it will probably vary a lot from one app to the next.

It could be just one or two lines of code, like:

But possibly the most important part of the callback is making sure that your API user (the external developer) implements the external API correctly, according to the data that your API is going to send in the request body of the callback, etc.

So, what we will do next is add the code to document how that external API should look like to rece

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Union

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Invoice(BaseModel):
    id: str
    title: Union[str, None] = None
    customer: str
    total: float


class InvoiceEvent(BaseModel):
    description: str
    paid: bool


class InvoiceEventReceived(BaseModel):
    ok: bool


invoices_callback_router = APIRouter()


@invoices_callback_router.post(
    "{$callback_url}/invoices/{$request.body.id}", response_model=Invo
...
```

```text
callback_url = "https://example.com/api/v1/invoices/events/"
httpx.post(callback_url, json={"description": "Invoice paid", "paid": True})
```

```python
from typing import Union

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Invoice(BaseModel):
    id: str
    title: Union[str, None] = None
    customer: str
    total: float


class InvoiceEvent(BaseModel):
    description: str
    paid: bool


class InvoiceEventReceived(BaseModel):
    ok: bool


invoices_callback_router = APIRouter()


@invoices_callback_router.post(
    "{$callback_url}/invoices/{$request.body.id}", response_model=Invo
...
```

---

## OpenAPI Webhooks - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/openapi-webhooks/

**Contents**:
- OpenAPI Webhooks¶
- Webhooks steps¶
- Documenting webhooks with FastAPI and OpenAPI¶
- An app with webhooks¶
  - Check the docs¶

There are cases where you want to tell your API users that your app could call their app (sending a request) with some data, normally to notify of some type of event.

This means that instead of the normal process of your users sending requests to your API, it's your API (or your app) that could send requests to their system (to their API, their app).

This is normally called a webhook.

The process normally is that you define in your code what is the message that you will send, the body of the request.

You also define in some way at which moments your app will send those requests or events.

And your users define in some way (for example in a web dashboard somewhere) the URL where your app should send those requests.

All the logic about how to register the URLs for webhooks and the code to actually send those requests is up to you. You write it however you want to in your own code.

With FastAPI, using OpenAPI, you can define the names of these webhooks, the types of HTTP operations that your app can send (e.g. POST, PUT, etc.) and the request bodies that your app would send.

This can make it a lot easier for your users to implement their APIs to receive your webhook requests, they might even be able to autogenerate some of their own API code.

Webhooks are available in OpenAPI 3.1.0 and above, supported by FastAPI 0.99.0 and above.

When you create a FastAPI application, there is a webhooks attribute that you can use to define webhooks, the same way you would define path operations, for example with @app.webhooks.post().

The webhooks that you define will end up in the OpenAPI schema and the automatic docs UI.

The app.webhooks object is actually just an APIRouter, the same type you would use when structuring your app with multiple files.

Notice that with webhooks you are actually not declaring a path (like /items/), the text you pass there is just an identifier of the webhook (the name of the event), for example in @app.webhooks.post("new-subscription"), the 

*[Content truncated - see full docs]*

**Examples**:

```python
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Subscription(BaseModel):
    username: str
    monthly_fee: float
    start_date: datetime


@app.webhooks.post("new-subscription")
def new_subscription(body: Subscription):
    """
    When a new user subscribes to your service we'll send you a POST request with this
    data to the URL that you register for the event `new-subscription` in the dashboard.
    """


@app.get("/users/
...
```

---

## Path Operation Advanced Configuration - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/

**Contents**:
- Path Operation Advanced Configuration¶
- OpenAPI operationId¶
  - Using the path operation function name as the operationId¶
- Exclude from OpenAPI¶
- Advanced description from docstring¶
- Additional Responses¶
- OpenAPI Extra¶
  - OpenAPI Extensions¶

If you are not an "expert" in OpenAPI, you probably don't need this.

You can set the OpenAPI operationId to be used in your path operation with the parameter operation_id.

You would have to make sure that it is unique for each operation.

If you want to use your APIs' function names as operationIds, you can iterate over all of them and override each path operation's operation_id using their APIRoute.name.

You should do it after adding all your path operations.

If you manually call app.openapi(), you should update the operationIds before that.

If you do this, you have to make sure each one of your path operation functions has a unique name.

Even if they are in different modules (Python files).

To exclude a path operation from the generated OpenAPI schema (and thus, from the automatic documentation systems), use the parameter include_in_schema and set it to False:

You can limit the lines used from the docstring of a path operation function for OpenAPI.

Adding an \f (an escaped "form feed" character) causes FastAPI to truncate the output used for OpenAPI at this point.

It won't show up in the documentation, but other tools (such as Sphinx) will be able to use the rest.

You probably have seen how to declare the response_model and status_code for a path operation.

That defines the metadata about the main response of a path operation.

You can also declare additional responses with their models, status codes, etc.

There's a whole chapter here in the documentation about it, you can read it at Additional Responses in OpenAPI.

When you declare a path operation in your application, FastAPI automatically generates the relevant metadata about that path operation to be included in the OpenAPI schema.

In the OpenAPI specification it is called the Operation Object.

It has all the information about the path operation and is used to generate the automatic documentation.

It includes the tags, parameters, requestBody, responses, etc.

This path operation-specific Open

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", operation_id="some_specific_id_you_define")
async def read_items():
    return [{"item_id": "Foo"}]
```

```python
from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.nam
...
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "Foo"}]
```

---

## Redirecting...

**URL**: https://fastapi.tiangolo.com/advanced/graphql/

---

## Response - Change Status Code - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/response-change-status-code/

**Contents**:
- Response - Change Status Code¶
- Use case¶
- Use a Response parameter¶

You probably read before that you can set a default Response Status Code.

But in some cases you need to return a different status code than the default.

For example, imagine that you want to return an HTTP status code of "OK" 200 by default.

But if the data didn't exist, you want to create it, and return an HTTP status code of "CREATED" 201.

But you still want to be able to filter and convert the data you return with a response_model.

For those cases, you can use a Response parameter.

You can declare a parameter of type Response in your path operation function (as you can do for cookies and headers).

And then you can set the status_code in that temporal response object.

And then you can return any object you need, as you normally would (a dict, a database model, etc).

And if you declared a response_model, it will still be used to filter and convert the object you returned.

FastAPI will use that temporal response to extract the status code (also cookies and headers), and will put them in the final response that contains the value you returned, filtered by any response_model.

You can also declare the Response parameter in dependencies, and set the status code in them. But keep in mind that the last one to be set will win.

**Examples**:

```python
from fastapi import FastAPI, Response, status

app = FastAPI()

tasks = {"foo": "Listen to the Bar Fighters"}


@app.put("/get-or-create-task/{task_id}", status_code=200)
def get_or_create_task(task_id: str, response: Response):
    if task_id not in tasks:
        tasks[task_id] = "This didn't exist before"
        response.status_code = status.HTTP_201_CREATED
    return tasks[task_id]
```

---

## Response Cookies - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/response-cookies/

**Contents**:
- Response Cookies¶
- Use a Response parameter¶
- Return a Response directly¶
  - More info¶

You can declare a parameter of type Response in your path operation function.

And then you can set cookies in that temporal response object.

And then you can return any object you need, as you normally would (a dict, a database model, etc).

And if you declared a response_model, it will still be used to filter and convert the object you returned.

FastAPI will use that temporal response to extract the cookies (also headers and status code), and will put them in the final response that contains the value you returned, filtered by any response_model.

You can also declare the Response parameter in dependencies, and set cookies (and headers) in them.

You can also create cookies when returning a Response directly in your code.

To do that, you can create a response as described in Return a Response Directly.

Then set Cookies in it, and then return it:

Keep in mind that if you return a response directly instead of using the Response parameter, FastAPI will return it directly.

So, you will have to make sure your data is of the correct type. E.g. it is compatible with JSON, if you are returning a JSONResponse.

And also that you are not sending any data that should have been filtered by a response_model.

You could also use from starlette.responses import Response or from starlette.responses import JSONResponse.

FastAPI provides the same starlette.responses as fastapi.responses just as a convenience for you, the developer. But most of the available responses come directly from Starlette.

And as the Response can be used frequently to set headers and cookies, FastAPI also provides it at fastapi.Response.

To see all the available parameters and options, check the documentation in Starlette.

**Examples**:

```python
from fastapi import FastAPI, Response

app = FastAPI()


@app.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}
```

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/cookie/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response
```

---

## Response Headers - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/response-headers/

**Contents**:
- Response Headers¶
- Use a Response parameter¶
- Return a Response directly¶
- Custom Headers¶

You can declare a parameter of type Response in your path operation function (as you can do for cookies).

And then you can set headers in that temporal response object.

And then you can return any object you need, as you normally would (a dict, a database model, etc).

And if you declared a response_model, it will still be used to filter and convert the object you returned.

FastAPI will use that temporal response to extract the headers (also cookies and status code), and will put them in the final response that contains the value you returned, filtered by any response_model.

You can also declare the Response parameter in dependencies, and set headers (and cookies) in them.

You can also add headers when you return a Response directly.

Create a response as described in Return a Response Directly and pass the headers as an additional parameter:

You could also use from starlette.responses import Response or from starlette.responses import JSONResponse.

FastAPI provides the same starlette.responses as fastapi.responses just as a convenience for you, the developer. But most of the available responses come directly from Starlette.

And as the Response can be used frequently to set headers and cookies, FastAPI also provides it at fastapi.Response.

Keep in mind that custom proprietary headers can be added using the X- prefix.

But if you have custom headers that you want a client in a browser to be able to see, you need to add them to your CORS configurations (read more in CORS (Cross-Origin Resource Sharing)), using the parameter expose_headers documented in Starlette's CORS docs.

**Examples**:

```python
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}
```

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/headers/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)
```

---

## Return a Response Directly - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/response-directly/

**Contents**:
- Return a Response Directly¶
- Return a Response¶
- Using the jsonable_encoder in a Response¶
- Returning a custom Response¶
- Notes¶

When you create a FastAPI path operation you can normally return any data from it: a dict, a list, a Pydantic model, a database model, etc.

By default, FastAPI would automatically convert that return value to JSON using the jsonable_encoder explained in JSON Compatible Encoder.

Then, behind the scenes, it would put that JSON-compatible data (e.g. a dict) inside of a JSONResponse that would be used to send the response to the client.

But you can return a JSONResponse directly from your path operations.

It might be useful, for example, to return custom headers or cookies.

In fact, you can return any Response or any sub-class of it.

JSONResponse itself is a sub-class of Response.

And when you return a Response, FastAPI will pass it directly.

It won't do any data conversion with Pydantic models, it won't convert the contents to any type, etc.

This gives you a lot of flexibility. You can return any data type, override any data declaration or validation, etc.

Because FastAPI doesn't make any changes to a Response you return, you have to make sure its contents are ready for it.

For example, you cannot put a Pydantic model in a JSONResponse without first converting it to a dict with all the data types (like datetime, UUID, etc) converted to JSON-compatible types.

For those cases, you can use the jsonable_encoder to convert your data before passing it to a response:

You could also use from starlette.responses import JSONResponse.

FastAPI provides the same starlette.responses as fastapi.responses just as a convenience for you, the developer. But most of the available responses come directly from Starlette.

The example above shows all the parts you need, but it's not very useful yet, as you could have just returned the item directly, and FastAPI would put it in a JSONResponse for you, converting it to a dict, etc. All that by default.

Now, let's see how you could use that to return a custom response.

Let's say that you want to return an XML response.

You coul

*[Content truncated - see full docs]*

**Examples**:

```python
from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_d
...
```

```python
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")
```

---

## Security Tools - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/security/

**Contents**:
- Security Tools¶
- API Key Security Schemes¶
- fastapi.security.APIKeyCookie ¶
    - Usage¶
    - Example¶
  - model instance-attribute ¶
  - scheme_name instance-attribute ¶
  - auto_error instance-attribute ¶

When you need to declare dependencies with OAuth2 scopes you use Security().

But you still need to define what is the dependable, the callable that you pass as a parameter to Depends() or Security().

There are multiple tools that you can use to create those dependables, and they get integrated into OpenAPI so they are shown in the automatic docs UI, they can be used by automatically generated clients and SDKs, etc.

You can import them from fastapi.security:

API key authentication using a cookie.

This defines the name of the cookie that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the cookie automatically and provides it as the dependency result. But it doesn't define how to set that cookie.

Create an instance object and use that object as the dependency in Depends().

The dependency result will be a string containing the key value.

Security scheme name.

It will be included in the generated OpenAPI (e.g. visible at /docs).

TYPE: Optional[str] DEFAULT: None

Security scheme description.

It will be included in the generated OpenAPI (e.g. visible at /docs).

TYPE: Optional[str] DEFAULT: None

By default, if the cookie is not provided, APIKeyCookie will automatically cancel the request and send the client an error.

If auto_error is set to False, when the cookie is not available, instead of erroring out, the dependency result will be None.

This is useful when you want to have optional authentication.

It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a cookie or in an HTTP Bearer token).

TYPE: bool DEFAULT: True

API key authentication using a header.

This defines the name of the header that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the header automatically and provides it as the dependency result. B

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi.security import (
    APIKeyCookie,
    APIKeyHeader,
    APIKeyQuery,
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPDigest,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    OAuth2PasswordRequestFormStrict,
    OpenIdConnect,
    SecurityScopes,
)
```

```text
APIKeyCookie(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)
```

```python
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyCookie

app = FastAPI()

cookie_scheme = APIKeyCookie(name="session")


@app.get("/items/")
async def read_items(session: str = Depends(cookie_scheme)):
    return {"session": session}
```

---

## Settings and Environment Variables - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/settings/

**Contents**:
- Settings and Environment Variables¶
- Types and validation¶
- Pydantic Settings¶
  - Install pydantic-settings¶
  - Create the Settings object¶
  - Use the settings¶
  - Run the server¶
- Settings in another module¶

In many cases your application could need some external settings or configurations, for example secret keys, database credentials, credentials for email services, etc.

Most of these settings are variable (can change), like database URLs. And many could be sensitive, like secrets.

For this reason it's common to provide them in environment variables that are read by the application.

To understand environment variables you can read Environment Variables.

These environment variables can only handle text strings, as they are external to Python and have to be compatible with other programs and the rest of the system (and even with different operating systems, as Linux, Windows, macOS).

That means that any value read in Python from an environment variable will be a str, and any conversion to a different type or any validation has to be done in code.

Fortunately, Pydantic provides a great utility to handle these settings coming from environment variables with Pydantic: Settings management.

First, make sure you create your virtual environment, activate it, and then install the pydantic-settings package:

It also comes included when you install the all extras with:

In Pydantic v1 it came included with the main package. Now it is distributed as this independent package so that you can choose to install it or not if you don't need that functionality.

Import BaseSettings from Pydantic and create a sub-class, very much like with a Pydantic model.

The same way as with Pydantic models, you declare class attributes with type annotations, and possibly default values.

You can use all the same validation features and tools you use for Pydantic models, like different data types and additional validations with Field().

In Pydantic v1 you would import BaseSettings directly from pydantic instead of from pydantic_settings.

If you want something quick to copy and paste, don't use this example, use the last one below.

Then, when you create an instance of that Settings class (in 

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install pydantic-settings
---> 100%
```

```text
$ pip install "fastapi[all]"
---> 100%
```

```python
from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50


settings = Settings()
app = FastAPI()


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
```

---

## Sub Applications - Mounts - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/sub-applications/

**Contents**:
- Sub Applications - Mounts¶
- Mounting a FastAPI application¶
  - Top-level application¶
  - Sub-application¶
  - Mount the sub-application¶
  - Check the automatic API docs¶
  - Technical Details: root_path¶

If you need to have two independent FastAPI applications, with their own independent OpenAPI and their own docs UIs, you can have a main app and "mount" one (or more) sub-application(s).

"Mounting" means adding a completely "independent" application in a specific path, that then takes care of handling everything under that path, with the path operations declared in that sub-application.

First, create the main, top-level, FastAPI application, and its path operations:

Then, create your sub-application, and its path operations.

This sub-application is just another standard FastAPI application, but this is the one that will be "mounted":

In your top-level application, app, mount the sub-application, subapi.

In this case, it will be mounted at the path /subapi:

Now, run the fastapi command with your file:

And open the docs at http://127.0.0.1:8000/docs.

You will see the automatic API docs for the main app, including only its own path operations:

And then, open the docs for the sub-application, at http://127.0.0.1:8000/subapi/docs.

You will see the automatic API docs for the sub-application, including only its own path operations, all under the correct sub-path prefix /subapi:

If you try interacting with any of the two user interfaces, they will work correctly, because the browser will be able to talk to each specific app or sub-app.

When you mount a sub-application as described above, FastAPI will take care of communicating the mount path for the sub-application using a mechanism from the ASGI specification called a root_path.

That way, the sub-application will know to use that path prefix for the docs UI.

And the sub-application could also have its own mounted sub-applications and everything would work correctly, because FastAPI handles all these root_paths automatically.

You will learn more about the root_path and how to use it explicitly in the section about Behind a Proxy.

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
```

---

## Templates - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/templates/

**Contents**:
- Templates¶
- Install dependencies¶
- Using Jinja2Templates¶
- Writing templates¶
  - Template Context Values¶
  - Template url_for Arguments¶
- Templates and static files¶
- More details¶

You can use any template engine you want with FastAPI.

A common choice is Jinja2, the same one used by Flask and other tools.

There are utilities to configure it easily that you can use directly in your FastAPI application (provided by Starlette).

Make sure you create a virtual environment, activate it, and install jinja2:

Before FastAPI 0.108.0, Starlette 0.29.0, the name was the first parameter.

Also, before that, in previous versions, the request object was passed as part of the key-value pairs in the context for Jinja2.

By declaring response_class=HTMLResponse the docs UI will be able to know that the response will be HTML.

You could also use from starlette.templating import Jinja2Templates.

FastAPI provides the same starlette.templating as fastapi.templating just as a convenience for you, the developer. But most of the available responses come directly from Starlette. The same with Request and StaticFiles.

Then you can write a template at templates/item.html with, for example:

In the HTML that contains:

...it will show the id taken from the "context" dict you passed:

For example, with an ID of 42, this would render:

You can also use url_for() inside of the template, it takes as arguments the same arguments that would be used by your path operation function.

So, the section with:

...will generate a link to the same URL that would be handled by the path operation function read_item(id=id).

For example, with an ID of 42, this would render:

You can also use url_for() inside of the template, and use it, for example, with the StaticFiles you mounted with the name="static".

In this example, it would link to a CSS file at static/styles.css with:

And because you are using StaticFiles, that CSS file would be served automatically by your FastAPI application at the URL /static/styles.css.

For more details, including how to test templates, check Starlette's docs on templates.

**Examples**:

```text
$ pip install jinja2

---> 100%
```

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", cont
...
```

```text
<html>
<head>
    <title>Item Details</title>
    <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">
</head>
<body>
    <h1><a href="{{ url_for('read_item', id=id) }}">Item ID: {{ id }}</a></h1>
</body>
</html>
```

---

## Testing Dependencies with Overrides - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/testing-dependencies/

**Contents**:
- Testing Dependencies with Overrides¶
- Overriding dependencies during testing¶
  - Use cases: external service¶
  - Use the app.dependency_overrides attribute¶

There are some scenarios where you might want to override a dependency during testing.

You don't want the original dependency to run (nor any of the sub-dependencies it might have).

Instead, you want to provide a different dependency that will be used only during tests (possibly only some specific tests), and will provide a value that can be used where the value of the original dependency was used.

An example could be that you have an external authentication provider that you need to call.

You send it a token and it returns an authenticated user.

This provider might be charging you per request, and calling it might take some extra time than if you had a fixed mock user for tests.

You probably want to test the external provider once, but not necessarily call it for every test that runs.

In this case, you can override the dependency that calls that provider, and use a custom dependency that returns a mock user, only for your tests.

For these cases, your FastAPI application has an attribute app.dependency_overrides, it is a simple dict.

To override a dependency for testing, you put as a key the original dependency (a function), and as the value, your dependency override (another function).

And then FastAPI will call that override instead of the original dependency.

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

You can set a dependency override for a dependency used anywhere in your FastAPI application.

The original dependency could be used in a path operation function, a path operation decorator (when you don't use the return value), a .include_router() call, etc.

FastAPI will still be able to override it.

Then you can reset your overrides (remove them) by setting app.dependency_overrides to be an empty dict:

If you want to override a dependency only during some tests, you can set the override at the beginning of the test (inside the test function) and reset it at the end (at the end of the test funct

*[Content truncated - see full docs]*

**Examples**:

```python
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Hello Items!", "params": commons}


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common
...
```

```python
from typing import Annotated, Union

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Hello Items!", "params": commons}


@app.get("/users/")
async def read_users(commons: Annotated[d
...
```

```python
from typing import Union

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
from typing_extensions import Annotated

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Hello Items!", "params": commons}


@app.get("/users/")
async def re
...
```

---

## Testing Events: lifespan and startup - shutdown - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/testing-events/

**Contents**:
- Testing Events: lifespan and startup - shutdown¶

When you need lifespan to run in your tests, you can use the TestClient with a with statement:

You can read more details about the "Running lifespan in tests in the official Starlette documentation site."

For the deprecated startup and shutdown events, you can use the TestClient as follows:

**Examples**:

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.testclient import TestClient

items = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}
    yield
    # clean up items
    items.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]


def test_read_items():
    # Before the lifespan starts, "i
...
```

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

items = {}


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]


def test_read_items():
    with TestClient(app) as client:
        response = client.get("/items/foo")
        assert response.status_code == 200
        assert response.jso
...
```

---

## Testing WebSockets - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/testing-websockets/

**Contents**:
- Testing WebSockets¶

You can use the same TestClient to test WebSockets.

For this, you use the TestClient in a with statement, connecting to the WebSocket:

For more details, check Starlette's documentation for testing WebSockets.

**Examples**:

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code =
...
```

---

## Using Dataclasses - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/dataclasses/

**Contents**:
- Using Dataclasses¶
- Dataclasses in response_model¶
- Dataclasses in Nested Data Structures¶
- Learn More¶
- Version¶

FastAPI is built on top of Pydantic, and I have been showing you how to use Pydantic models to declare requests and responses.

But FastAPI also supports using dataclasses the same way:

This is still supported thanks to Pydantic, as it has internal support for dataclasses.

So, even with the code above that doesn't use Pydantic explicitly, FastAPI is using Pydantic to convert those standard dataclasses to Pydantic's own flavor of dataclasses.

And of course, it supports the same:

This works the same way as with Pydantic models. And it is actually achieved in the same way underneath, using Pydantic.

Keep in mind that dataclasses can't do everything Pydantic models can do.

So, you might still need to use Pydantic models.

But if you have a bunch of dataclasses laying around, this is a nice trick to use them to power a web API using FastAPI. 🤓

You can also use dataclasses in the response_model parameter:

The dataclass will be automatically converted to a Pydantic dataclass.

This way, its schema will show up in the API docs user interface:

You can also combine dataclasses with other type annotations to make nested data structures.

In some cases, you might still have to use Pydantic's version of dataclasses. For example, if you have errors with the automatically generated API documentation.

In that case, you can simply swap the standard dataclasses with pydantic.dataclasses, which is a drop-in replacement:

We still import field from standard dataclasses.

pydantic.dataclasses is a drop-in replacement for dataclasses.

The Author dataclass includes a list of Item dataclasses.

The Author dataclass is used as the response_model parameter.

You can use other standard type annotations with dataclasses as the request body.

In this case, it's a list of Item dataclasses.

Here we are returning a dictionary that contains items which is a list of dataclasses.

FastAPI is still capable of serializing the data to JSON.

Here the response_model is using a type annotation

*[Content truncated - see full docs]*

**Examples**:

```python
from dataclasses import dataclass
from typing import Union

from fastapi import FastAPI


@dataclass
class Item:
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```

```python
from dataclasses import dataclass, field
from typing import List, Union

from fastapi import FastAPI


@dataclass
class Item:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    description: Union[str, None] = None
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/items/next", response_model=Item)
async def read_next_item():
    return {
        "name": "Island In The Moon",
        "price": 12.99,
        "description": "A place to be playin' and
...
```

```python
from dataclasses import field  # (1)
from typing import List, Union

from fastapi import FastAPI
from pydantic.dataclasses import dataclass  # (2)


@dataclass
class Item:
    name: str
    description: Union[str, None] = None


@dataclass
class Author:
    name: str
    items: List[Item] = field(default_factory=list)  # (3)


app = FastAPI()


@app.post("/authors/{author_id}/items/", response_model=Author)  # (4)
async def create_author_items(author_id: str, items: List[Item]):  # (5)
    retur
...
```

---

## Using the Request Directly - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/using-request-directly/

**Contents**:
- Using the Request Directly¶
- Details about the Request object¶
- Use the Request object directly¶
- Request documentation¶

Up to now, you have been declaring the parts of the request that you need with their types.

And by doing so, FastAPI is validating that data, converting it and generating documentation for your API automatically.

But there are situations where you might need to access the Request object directly.

As FastAPI is actually Starlette underneath, with a layer of several tools on top, you can use Starlette's Request object directly when you need to.

It would also mean that if you get data from the Request object directly (for example, read the body) it won't be validated, converted or documented (with OpenAPI, for the automatic API user interface) by FastAPI.

Although any other parameter declared normally (for example, the body with a Pydantic model) would still be validated, converted, annotated, etc.

But there are specific cases where it's useful to get the Request object.

Let's imagine you want to get the client's IP address/host inside of your path operation function.

For that you need to access the request directly.

By declaring a path operation function parameter with the type being the Request FastAPI will know to pass the Request in that parameter.

Note that in this case, we are declaring a path parameter beside the request parameter.

So, the path parameter will be extracted, validated, converted to the specified type and annotated with OpenAPI.

The same way, you can declare any other parameter as normally, and additionally, get the Request too.

You can read more details about the Request object in the official Starlette documentation site.

You could also use from starlette.requests import Request.

FastAPI provides it directly just as a convenience for you, the developer. But it comes directly from Starlette.

**Examples**:

```python
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}
```

---

## WebSockets - FastAPI

**URL**: https://fastapi.tiangolo.com/advanced/websockets/

**Contents**:
- WebSockets¶
- Install websockets¶
- WebSockets client¶
  - In production¶
- Create a websocket¶
- Await for messages and send messages¶
- Try it¶
- Using Depends and others¶

You can use WebSockets with FastAPI.

Make sure you create a virtual environment, activate it, and install websockets (a Python library that makes it easy to use the "WebSocket" protocol):

In your production system, you probably have a frontend created with a modern framework like React, Vue.js or Angular.

And to communicate using WebSockets with your backend you would probably use your frontend's utilities.

Or you might have a native mobile application that communicates with your WebSocket backend directly, in native code.

Or you might have any other way to communicate with the WebSocket endpoint.

But for this example, we'll use a very simple HTML document with some JavaScript, all inside a long string.

This, of course, is not optimal and you wouldn't use it for production.

In production you would have one of the options above.

But it's the simplest way to focus on the server-side of WebSockets and have a working example:

In your FastAPI application, create a websocket:

You could also use from starlette.websockets import WebSocket.

FastAPI provides the same WebSocket directly just as a convenience for you, the developer. But it comes directly from Starlette.

In your WebSocket route you can await for messages and send messages.

You can receive and send binary, text, and JSON data.

If your file is named main.py, run your application with:

Open your browser at http://127.0.0.1:8000.

You will see a simple page like:

You can type messages in the input box, and send them:

And your FastAPI application with WebSockets will respond back:

You can send (and receive) many messages:

And all of them will use the same WebSocket connection.

In WebSocket endpoints you can import from fastapi and use:

They work the same way as for other FastAPI endpoints/path operations:

Prefer to use the Annotated version if possible.

Prefer to use the Annotated version if possible.

As this is a WebSocket it doesn't really make sense to raise an HTTPException, instead we ra

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install websockets

---> 100%
```

```python
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws:/
...
```

```python
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws:/
...
```

---
