# Fastapi - Other

**Pages**: 34

---

## About - FastAPI

**URL**: https://fastapi.tiangolo.com/about/

**Contents**:
- About¶

About FastAPI, its design, inspiration and more. 🤓

---

## Benchmarks - FastAPI

**URL**: https://fastapi.tiangolo.com/benchmarks/

**Contents**:
- Benchmarks¶
- Benchmarks and speed¶

Independent TechEmpower benchmarks show FastAPI applications running under Uvicorn as one of the fastest Python frameworks available, only below Starlette and Uvicorn themselves (used internally by FastAPI).

But when checking benchmarks and comparisons you should keep the following in mind.

When you check the benchmarks, it is common to see several tools of different types compared as equivalent.

Specifically, to see Uvicorn, Starlette and FastAPI compared together (among many other tools).

The simpler the problem solved by the tool, the better performance it will get. And most of the benchmarks don't test the additional features provided by the tool.

The hierarchy is like:

Uvicorn: an ASGI server

---

## Concurrency and async / await - FastAPI

**URL**: https://fastapi.tiangolo.com/async/

**Contents**:
- Concurrency and async / await¶
- In a hurry?¶
- Technical Details¶
- Asynchronous Code¶
  - Concurrency and Burgers¶
  - Concurrent Burgers¶
  - Parallel Burgers¶
  - Burger Conclusion¶

Details about the async def syntax for path operation functions and some background about asynchronous code, concurrency, and parallelism.

If you are using third party libraries that tell you to call them with await, like:

Then, declare your path operation functions with async def like:

You can only use await inside of functions created with async def.

If you are using a third party library that communicates with something (a database, an API, the file system, etc.) and doesn't have support for using await, (this is currently the case for most database libraries), then declare your path operation functions as normally, with just def, like:

If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def, even if you don't need to use await inside.

If you just don't know, use normal def.

Note: You can mix def and async def in your path operation functions as much as you need and define each one using the best option for you. FastAPI will do the right thing with them.

Anyway, in any of the cases above, FastAPI will still work asynchronously and be extremely fast.

But by following the steps above, it will be able to do some performance optimizations.

Modern versions of Python have support for "asynchronous code" using something called "coroutines", with async and await syntax.

Let's see that phrase by parts in the sections below:

Asynchronous code just means that the language 💬 has a way to tell the computer / program 🤖 that at some point in the code, it 🤖 will have to wait for something else to finish somewhere else. Let's say that something else is called "slow-file" 📝.

So, during that time, the computer can go and do some other work, while "slow-file" 📝 finishes.

Then the computer / program 🤖 will come back every time it has a chance because it's waiting again, or whenever it 🤖 finished all the work it had at that point. And it 🤖 will see if any of the tasks it was waiting for have already finished,

*[Content truncated - see full docs]*

**Examples**:

```text
results = await some_library()
```

```python
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

```python
@app.get('/')
def results():
    results = some_library()
    return results
```

---

## Conditional OpenAPI - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/conditional-openapi/

**Contents**:
- Conditional OpenAPI¶
- About security, APIs, and docs¶
- Conditional OpenAPI from settings and env vars¶

If you needed to, you could use settings and environment variables to configure OpenAPI conditionally depending on the environment, and even disable it entirely.

Hiding your documentation user interfaces in production shouldn't be the way to protect your API.

That doesn't add any extra security to your API, the path operations will still be available where they are.

If there's a security flaw in your code, it will still exist.

Hiding the documentation just makes it more difficult to understand how to interact with your API, and could make it more difficult for you to debug it in production. It could be considered simply a form of Security through obscurity.

If you want to secure your API, there are several better things you can do, for example:

Nevertheless, you might have a very specific use case where you really need to disable the API docs for some environment (e.g. for production) or depending on configurations from environment variables.

You can easily use the same Pydantic settings to configure your generated OpenAPI and the docs UIs.

Here we declare the setting openapi_url with the same default of "/openapi.json".

And then we use it when creating the FastAPI app.

Then you could disable OpenAPI (including the UI docs) by setting the environment variable OPENAPI_URL to the empty string, like:

Then if you go to the URLs at /openapi.json, /docs, or /redoc you will just get a 404 Not Found error like:

**Examples**:

```python
from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"


settings = Settings()

app = FastAPI(openapi_url=settings.openapi_url)


@app.get("/")
def root():
    return {"message": "Hello World"}
```

```text
$ OPENAPI_URL= uvicorn main:app

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

```text
{
    "detail": "Not Found"
}
```

---

## Configure Swagger UI - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/configure-swagger-ui/

**Contents**:
- Configure Swagger UI¶
- Disable Syntax Highlighting¶
- Change the Theme¶
- Change Default Swagger UI Parameters¶
- Other Swagger UI Parameters¶
- JavaScript-only settings¶

You can configure some extra Swagger UI parameters.

To configure them, pass the swagger_ui_parameters argument when creating the FastAPI() app object or to the get_swagger_ui_html() function.

swagger_ui_parameters receives a dictionary with the configurations passed to Swagger UI directly.

FastAPI converts the configurations to JSON to make them compatible with JavaScript, as that's what Swagger UI needs.

For example, you could disable syntax highlighting in Swagger UI.

Without changing the settings, syntax highlighting is enabled by default:

But you can disable it by setting syntaxHighlight to False:

...and then Swagger UI won't show the syntax highlighting anymore:

The same way you could set the syntax highlighting theme with the key "syntaxHighlight.theme" (notice that it has a dot in the middle):

That configuration would change the syntax highlighting color theme:

FastAPI includes some default configuration parameters appropriate for most of the use cases.

It includes these default configurations:

You can override any of them by setting a different value in the argument swagger_ui_parameters.

For example, to disable deepLinking you could pass these settings to swagger_ui_parameters:

To see all the other possible configurations you can use, read the official docs for Swagger UI parameters.

Swagger UI also allows other configurations to be JavaScript-only objects (for example, JavaScript functions).

FastAPI also includes these JavaScript-only presets settings:

These are JavaScript objects, not strings, so you can't pass them from Python code directly.

If you need to use JavaScript-only configurations like those, you can use one of the methods above. Override all the Swagger UI path operation and manually write any JavaScript you need.

**Examples**:

```python
from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
```

```python
from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
```

```text
# Code above omitted 👆

swagger_ui_default_parameters: Annotated[
    Dict[str, Any],
    Doc(
        """
        Default configurations for Swagger UI.

        You can use it as a template to add any other configurations needed.
        """
    ),
] = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
}

# Code below omitted 👇
```

---

## Custom Docs UI Static Assets (Self-Hosting) - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/

**Contents**:
- Custom Docs UI Static Assets (Self-Hosting)¶
- Custom CDN for JavaScript and CSS¶
  - Disable the automatic docs¶
  - Include the custom docs¶
  - Create a path operation to test it¶
  - Test it¶
- Self-hosting JavaScript and CSS for docs¶
  - Project file structure¶

The API docs use Swagger UI and ReDoc, and each of those need some JavaScript and CSS files.

By default, those files are served from a CDN.

But it's possible to customize it, you can set a specific CDN, or serve the files yourself.

Let's say that you want to use a different CDN, for example you want to use https://unpkg.com/.

This could be useful if for example you live in a country that restricts some URLs.

The first step is to disable the automatic docs, as by default, those use the default CDN.

To disable them, set their URLs to None when creating your FastAPI app:

Now you can create the path operations for the custom docs.

You can reuse FastAPI's internal functions to create the HTML pages for the docs, and pass them the needed arguments:

And similarly for ReDoc...

The path operation for swagger_ui_redirect is a helper for when you use OAuth2.

If you integrate your API with an OAuth2 provider, you will be able to authenticate and come back to the API docs with the acquired credentials. And interact with it using the real OAuth2 authentication.

Swagger UI will handle it behind the scenes for you, but it needs this "redirect" helper.

Now, to be able to test that everything works, create a path operation:

Now, you should be able to go to your docs at http://127.0.0.1:8000/docs, and reload the page, it will load those assets from the new CDN.

Self-hosting the JavaScript and CSS could be useful if, for example, you need your app to keep working even while offline, without open Internet access, or in a local network.

Here you'll see how to serve those files yourself, in the same FastAPI app, and configure the docs to use them.

Let's say your project file structure looks like this:

Now create a directory to store those static files.

Your new file structure could look like this:

Download the static files needed for the docs and put them on that static/ directory.

You can probably right-click each link and select an option similar to "Save link as...

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swag
...
```

```python
from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swag
...
```

```python
from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swag
...
```

---

## Custom Request and APIRoute class - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/custom-request-and-route/

**Contents**:
- Custom Request and APIRoute class¶
- Use cases¶
- Handling custom request body encodings¶
  - Create a custom GzipRequest class¶
  - Create a custom GzipRoute class¶
- Accessing the request body in an exception handler¶
- Custom APIRoute class in a router¶

In some cases, you may want to override the logic used by the Request and APIRoute classes.

In particular, this may be a good alternative to logic in a middleware.

For example, if you want to read or manipulate the request body before it is processed by your application.

This is an "advanced" feature.

If you are just starting with FastAPI you might want to skip this section.

Some use cases include:

Let's see how to make use of a custom Request subclass to decompress gzip requests.

And an APIRoute subclass to use that custom request class.

This is a toy example to demonstrate how it works, if you need Gzip support, you can use the provided GzipMiddleware.

First, we create a GzipRequest class, which will overwrite the Request.body() method to decompress the body in the presence of an appropriate header.

If there's no gzip in the header, it will not try to decompress the body.

That way, the same route class can handle gzip compressed or uncompressed requests.

Next, we create a custom subclass of fastapi.routing.APIRoute that will make use of the GzipRequest.

This time, it will overwrite the method APIRoute.get_route_handler().

This method returns a function. And that function is what will receive a request and return a response.

Here we use it to create a GzipRequest from the original request.

A Request has a request.scope attribute, that's just a Python dict containing the metadata related to the request.

A Request also has a request.receive, that's a function to "receive" the body of the request.

The scope dict and receive function are both part of the ASGI specification.

And those two things, scope and receive, are what is needed to create a new Request instance.

To learn more about the Request check Starlette's docs about Requests.

The only thing the function returned by GzipRequest.get_route_handler does differently is convert the Request to a GzipRequest.

Doing this, our GzipRequest will take care of decompressing the data (if necessary) bef

*[Content truncated - see full docs]*

**Examples**:

```python
import gzip
from typing import Callable, List

from fastapi import Body, FastAPI, Request, Response
from fastapi.routing import APIRoute


class GzipRequest(Request):
    async def body(self) -> bytes:
        if not hasattr(self, "_body"):
            body = await super().body()
            if "gzip" in self.headers.getlist("Content-Encoding"):
                body = gzip.decompress(body)
            self._body = body
        return self._body


class GzipRoute(APIRoute):
    def get_route_hand
...
```

```python
import gzip
from typing import Callable, List

from fastapi import Body, FastAPI, Request, Response
from fastapi.routing import APIRoute


class GzipRequest(Request):
    async def body(self) -> bytes:
        if not hasattr(self, "_body"):
            body = await super().body()
            if "gzip" in self.headers.getlist("Content-Encoding"):
                body = gzip.decompress(body)
            self._body = body
        return self._body


class GzipRoute(APIRoute):
    def get_route_hand
...
```

```python
from typing import Callable, List

from fastapi import Body, FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute


class ValidationErrorLoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
    
...
```

---

## Development - Contributing - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/contributing/

**Contents**:
- Development - Contributing¶
- Developing¶
  - Virtual environment¶
  - Install requirements¶
  - Using your local FastAPI¶
  - Format the code¶
- Tests¶
- Docs¶

The current page still doesn't have a translation for this language.

But you can help translating it: Contributing.

First, you might want to see the basic ways to help FastAPI and get help.

If you already cloned the fastapi repository and you want to deep dive in the code, here are some guidelines to set up your environment.

Follow the instructions to create and activate a virtual environment for the internal code of fastapi.

After activating the environment, install the required packages:

It will install all the dependencies and your local FastAPI in your local environment.

If you create a Python file that imports and uses FastAPI, and run it with the Python from your local environment, it will use your cloned local FastAPI source code.

And if you update that local FastAPI source code when you run that Python file again, it will use the fresh version of FastAPI you just edited.

That way, you don't have to "install" your local version to be able to test every change.

This only happens when you install using this included requirements.txt instead of running pip install fastapi directly.

That is because inside the requirements.txt file, the local version of FastAPI is marked to be installed in "editable" mode, with the -e option.

There is a script that you can run that will format and clean all your code:

It will also auto-sort all your imports.

There is a script that you can run locally to test all the code and generate coverage reports in HTML:

This command generates a directory ./htmlcov/, if you open the file ./htmlcov/index.html in your browser, you can explore interactively the regions of code that are covered by the tests, and notice if there is any region missing.

First, make sure you set up your environment as described above, that will install all the requirements.

During local development, there is a script that builds the site and checks for any changes, live-reloading:

It will serve the documentation on http://127.0.0.1:8008.

That way, 

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install -r requirements.txt

---> 100%
```

```text
$ uv pip install -r requirements.txt

---> 100%
```

```text
$ bash scripts/format.sh
```

---

## Development - Contributing - FastAPI

**URL**: https://fastapi.tiangolo.com/contributing/

**Contents**:
- Development - Contributing¶
- Developing¶
  - Virtual environment¶
  - Install requirements¶
  - Using your local FastAPI¶
  - Format the code¶
- Tests¶
- Docs¶

First, you might want to see the basic ways to help FastAPI and get help.

If you already cloned the fastapi repository and you want to deep dive in the code, here are some guidelines to set up your environment.

Follow the instructions to create and activate a virtual environment for the internal code of fastapi.

After activating the environment, install the required packages:

It will install all the dependencies and your local FastAPI in your local environment.

If you create a Python file that imports and uses FastAPI, and run it with the Python from your local environment, it will use your cloned local FastAPI source code.

And if you update that local FastAPI source code when you run that Python file again, it will use the fresh version of FastAPI you just edited.

That way, you don't have to "install" your local version to be able to test every change.

This only happens when you install using this included requirements.txt instead of running pip install fastapi directly.

That is because inside the requirements.txt file, the local version of FastAPI is marked to be installed in "editable" mode, with the -e option.

There is a script that you can run that will format and clean all your code:

It will also auto-sort all your imports.

There is a script that you can run locally to test all the code and generate coverage reports in HTML:

This command generates a directory ./htmlcov/, if you open the file ./htmlcov/index.html in your browser, you can explore interactively the regions of code that are covered by the tests, and notice if there is any region missing.

First, make sure you set up your environment as described above, that will install all the requirements.

During local development, there is a script that builds the site and checks for any changes, live-reloading:

It will serve the documentation on http://127.0.0.1:8008.

That way, you can edit the documentation/source files and see the changes live.

Alternatively, you can perform the same steps t

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install -r requirements.txt

---> 100%
```

```text
$ uv pip install -r requirements.txt

---> 100%
```

```text
$ bash scripts/format.sh
```

---

## Environment Variables - FastAPI

**URL**: https://fastapi.tiangolo.com/environment-variables/

**Contents**:
- Environment Variables¶
- Create and Use Env Vars¶
- Read env vars in Python¶
- Types and Validation¶
- PATH Environment Variable¶
  - Installing Python and Updating the PATH¶
- Conclusion¶

If you already know what "environment variables" are and how to use them, feel free to skip this.

An environment variable (also known as "env var") is a variable that lives outside of the Python code, in the operating system, and could be read by your Python code (or by other programs as well).

Environment variables could be useful for handling application settings, as part of the installation of Python, etc.

You can create and use environment variables in the shell (terminal), without needing Python:

You could also create environment variables outside of Python, in the terminal (or with any other method), and then read them in Python.

For example you could have a file main.py with:

The second argument to os.getenv() is the default value to return.

If not provided, it's None by default, here we provide "World" as the default value to use.

Then you could call that Python program:

As environment variables can be set outside of the code, but can be read by the code, and don't have to be stored (committed to git) with the rest of the files, it's common to use them for configurations or settings.

You can also create an environment variable only for a specific program invocation, that is only available to that program, and only for its duration.

To do that, create it right before the program itself, on the same line:

You can read more about it at The Twelve-Factor App: Config.

These environment variables can only handle text strings, as they are external to Python and have to be compatible with other programs and the rest of the system (and even with different operating systems, as Linux, Windows, macOS).

That means that any value read in Python from an environment variable will be a str, and any conversion to a different type or any validation has to be done in code.

You will learn more about using environment variables for handling application settings in the Advanced User Guide - Settings and Environment Variables.

There is a special environment variabl

*[Content truncated - see full docs]*

**Examples**:

```text
// You could create an env var MY_NAME with
$ export MY_NAME="Wade Wilson"

// Then you could use it with other programs, like
$ echo "Hello $MY_NAME"

Hello Wade Wilson
```

```text
// Create an env var MY_NAME
$ $Env:MY_NAME = "Wade Wilson"

// Use it with other programs, like
$ echo "Hello $Env:MY_NAME"

Hello Wade Wilson
```

```python
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
```

---

## Extending OpenAPI - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/extending-openapi/

**Contents**:
- Extending OpenAPI¶
- The normal process¶
- Overriding the defaults¶
  - Normal FastAPI¶
  - Generate the OpenAPI schema¶
  - Modify the OpenAPI schema¶
  - Cache the OpenAPI schema¶
  - Override the method¶

There are some cases where you might need to modify the generated OpenAPI schema.

In this section you will see how.

The normal (default) process, is as follows.

A FastAPI application (instance) has an .openapi() method that is expected to return the OpenAPI schema.

As part of the application object creation, a path operation for /openapi.json (or for whatever you set your openapi_url) is registered.

It just returns a JSON response with the result of the application's .openapi() method.

By default, what the method .openapi() does is check the property .openapi_schema to see if it has contents and return them.

If it doesn't, it generates them using the utility function at fastapi.openapi.utils.get_openapi.

And that function get_openapi() receives as parameters:

The parameter summary is available in OpenAPI 3.1.0 and above, supported by FastAPI 0.99.0 and above.

Using the information above, you can use the same utility function to generate the OpenAPI schema and override each part that you need.

For example, let's add ReDoc's OpenAPI extension to include a custom logo.

First, write all your FastAPI application as normally:

Then, use the same utility function to generate the OpenAPI schema, inside a custom_openapi() function:

Now you can add the ReDoc extension, adding a custom x-logo to the info "object" in the OpenAPI schema:

You can use the property .openapi_schema as a "cache", to store your generated schema.

That way, your application won't have to generate the schema every time a user opens your API docs.

It will be generated only once, and then the same cached schema will be used for the next requests.

Now you can replace the .openapi() method with your new function.

Once you go to http://127.0.0.1:8000/redoc you will see that you are using your custom logo (in this example, FastAPI's logo):

**Examples**:

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.r
...
```

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.r
...
```

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.r
...
```

---

## FastAPI

**URL**: https://fastapi.tiangolo.com/

**Contents**:
- FastAPI¶
- Sponsors¶
- Opinions¶
- Typer, the FastAPI of CLIs¶
- Requirements¶
- Installation¶
- Example¶
  - Create it¶

FastAPI framework, high performance, easy to learn, fast to code, ready for production

Documentation: https://fastapi.tiangolo.com

Source Code: https://github.com/fastapi/fastapi

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

* estimation based on tests on an internal development team, building production applications.

"[...] I'm using FastAPI a ton these days. [...] I'm actually planning to use it for all of my team's ML services at Microsoft. Some of them are getting integrated into the core Windows product and some Office products."

"We adopted the FastAPI library to spawn a REST server that can be queried to obtain predictions. [for Ludwig]"

"Netflix is pleased to announce the open-source release of our crisis management orchestration framework: Dispatch! [built with FastAPI]"

"I’m over the moon excited about FastAPI. It’s so fun!"

"Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted Hug to be - it's really inspiring to see someone build that."

"If you're looking to learn one modern framework for building REST APIs, check out FastAPI [...] It's fast, easy to use and easy to learn [...]"

"We've switched over to FastAPI for our APIs [...] I think you'll like it [...]"

"If anyone is looking to build a production Python API, I would highly recommend FastAPI. It is beautifully designed, simple to use and highly scalable, it has become a key component in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer."

If you are building a CLI app to be used in the terminal instead of a web API, check out Typer.

Typer is FastAPI's little sibling. And it's intended to be the FastAPI of CLIs. ⌨️ 🚀

FastAPI stands on the shoulders of giants:

Create and activate a virtual environment and then install FastAPI:

Note: Make sure you put "fastapi[standard]" in quotes to 

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install "fastapi[standard]"

---> 100%
```

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

---

## FastAPI CLI - FastAPI

**URL**: https://fastapi.tiangolo.com/fastapi-cli/

**Contents**:
- FastAPI CLI¶
- fastapi dev¶
- fastapi run¶

FastAPI CLI is a command line program that you can use to serve your FastAPI app, manage your FastAPI project, and more.

When you install FastAPI (e.g. with pip install "fastapi[standard]"), it includes a package called fastapi-cli, this package provides the fastapi command in the terminal.

To run your FastAPI app for development, you can use the fastapi dev command:

The command line program called fastapi is FastAPI CLI.

FastAPI CLI takes the path to your Python program (e.g. main.py) and automatically detects the FastAPI instance (commonly named app), determines the correct import process, and then serves it.

For production you would use fastapi run instead. 🚀

Internally, FastAPI CLI uses Uvicorn, a high-performance, production-ready, ASGI server. 😎

Running fastapi dev initiates development mode.

By default, auto-reload is enabled, automatically reloading the server when you make changes to your code. This is resource-intensive and could be less stable than when it's disabled. You should only use it for development. It also listens on the IP address 127.0.0.1, which is the IP for your machine to communicate with itself alone (localhost).

Executing fastapi run starts FastAPI in production mode by default.

By default, auto-reload is disabled. It also listens on the IP address 0.0.0.0, which means all the available IP addresses, this way it will be publicly accessible to anyone that can communicate with the machine. This is how you would normally run it in production, for example, in a container.

In most cases you would (and should) have a "termination proxy" handling HTTPS for you on top, this will depend on how you deploy your application, your provider might do this for you, or you might need to set it up yourself.

You can learn more about it in the deployment documentation.

**Examples**:

```python
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166
...
```

---

## FastAPI People - FastAPI

**URL**: https://fastapi.tiangolo.com/fastapi-people/

**Contents**:
- FastAPI People¶
- Creator¶
- Team¶
- FastAPI Experts¶
  - FastAPI Experts - Last Month¶
  - FastAPI Experts - 3 Months¶
  - FastAPI Experts - 6 Months¶
  - FastAPI Experts - 1 Year¶

FastAPI has an amazing community that welcomes people from all backgrounds.

I'm the creator of FastAPI. You can read more about that in Help FastAPI - Get Help - Connect with the author.

...But here I want to show you the community.

FastAPI receives a lot of support from the community. And I want to highlight their contributions.

These are the people that:

All these tasks help maintain the repository.

A round of applause to them. 👏 🙇

This is the current list of team members. 😎

They have different levels of involvement and permissions, they can perform repository management tasks and together we manage the FastAPI repository.

Although the team members have the permissions to perform privileged tasks, all the help from others maintaining FastAPI is very much appreciated! 🙇‍♂️

These are the users that have been helping others the most with questions in GitHub. 🙇

They have proven to be FastAPI Experts by helping many others. ✨

You could become an official FastAPI Expert too!

Just help others with questions in GitHub. 🤓

You can see the FastAPI Experts for:

These are the users that have been helping others the most with questions in GitHub during the last month. 🤓

These are the users that have been helping others the most with questions in GitHub during the last 3 months. 😎

These are the users that have been helping others the most with questions in GitHub during the last 6 months. 🧐

These are the users that have been helping others the most with questions in GitHub during the last year. 🧑‍🔬

Here are the all time FastAPI Experts. 🤓🤯

These are the users that have helped others the most with questions in GitHub through all time. 🧙

Here are the Top Contributors. 👷

These users have created the most Pull Requests that have been merged.

They have contributed source code, documentation, etc. 📦

There are hundreds of other contributors, you can see them all in the FastAPI GitHub Contributors page. 👷

These are the Top Translators. 🌐

These users have create

*[Content truncated - see full docs]*

---

## FastAPI and friends newsletter - FastAPI

**URL**: https://fastapi.tiangolo.com/newsletter/

**Contents**:
- FastAPI and friends newsletter¶

---

## FastAPI

**URL**: https://fastapi.tiangolo.com/ja/

**Contents**:
- FastAPI¶
- Sponsors¶
- 評価¶
- Typer, the FastAPI of CLIs¶
- 必要条件¶
- インストール¶
- アプリケーション例¶
  - アプリケーションの作成¶

FastAPI framework, high performance, easy to learn, fast to code, ready for production

ドキュメント: https://fastapi.tiangolo.com

ソースコード: https://github.com/fastapi/fastapi

FastAPI は、Pythonの標準である型ヒントに基づいてPython 以降でAPI を構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワークです。

高速: NodeJS や Go 並みのとても高いパフォーマンス (Starlette と Pydantic のおかげです)。 最も高速な Python フレームワークの一つです.

高速なコーディング: 開発速度を約 200%~300%向上させます。 *

* 本番アプリケーションを構築している開発チームのテストによる見積もり。

"[...] 最近 FastAPI を使っています。 [...] 実際に私のチームの全ての Microsoft の機械学習サービス で使用する予定です。 そのうちのいくつかのコアなWindows製品とOffice製品に統合されつつあります。"

"FastAPIライブラリを採用し、クエリで予測値を取得できるRESTサーバを構築しました。 [for Ludwig]"

"Netflix は、危機管理オーケストレーションフレームワーク、Dispatchのオープンソースリリースを発表できることをうれしく思います。 [built with FastAPI]"

"私はFastAPIにワクワクしています。 めちゃくちゃ楽しいです！"

"正直、超堅実で洗練されているように見えます。いろんな意味で、それは私がハグしたかったものです。"

"REST API を構築するためのモダンなフレームワークを学びたい方は、FastAPI [...] をチェックしてみてください。 [...] 高速で, 使用、習得が簡単です。[...]"

"私たちのAPIはFastAPIに切り替えました。[...] きっと気に入ると思います。 [...]"

もし Web API の代わりにターミナルで使用するCLIアプリを構築する場合は、Typerを確認してください。

Typerは FastAPI の弟分です。そして、CLI 版 の FastAPIを意味しています。

FastAPI は巨人の肩の上に立っています。

本番環境では、Uvicorn または、 Hypercornのような、 ASGI サーバーが必要になります。

async / awaitを使用するときは、 async defを使います:

わからない場合は、ドキュメントのasync と awaitにある"In a hurry?"セクションをチェックしてください。

uvicorn main:appコマンドは以下の項目を参照します:

ブラウザからhttp://127.0.0.1:8000/items/5?q=somequeryを開きます。

以下の JSON のレスポンスが確認できます:

もうすでに以下の API が作成されています:

http://127.0.0.1:8000/docsにアクセスしてみてください。

自動対話型の API ドキュメントが表示されます。 (Swagger UIが提供しています。):

http://127.0.0.1:8000/redocにアクセスしてみてください。

代替の自動ドキュメントが表示されます。(ReDocが提供しています。):

PUTリクエストからボディを受け取るためにmain.pyを修正しましょう。

Pydantic によって、Python の標準的な型を使ってボディを宣言します。

サーバーは自動でリロードされます。(上述のuvicornコマンドで--reloadオプションを追加しているからです。)

http://127.0.0.1:8000/docsにアクセスしましょう。

http://127.0.0.1:8000/redocにアクセスしましょう。

要約すると、関数のパラメータとして、パラメータやボディ などの型を一度だけ宣言します。

標準的な最新の Python の型を使っています。

新しい構文や特定のライブラリのメソッドやクラスなどを覚える必要はありません。

単なる標準的な3.8 以降の Pythonです。

...そして、この一度の宣言で、以下のようになります:

コード例に戻りましょう、FastAPI は次のようになります:

まだ表面的な部分に触れただけですが、もう全ての仕組みは分か

*[Content truncated - see full docs]*

**Examples**:

```text
$ pip install fastapi

---> 100%
```

```text
$ pip install "uvicorn[standard]"

---> 100%
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

---

## Features - FastAPI

**URL**: https://fastapi.tiangolo.com/features/

**Contents**:
- Features¶
- FastAPI features¶
  - Based on open standards¶
  - Automatic docs¶
  - Just Modern Python¶
  - Editor support¶
  - Short¶
  - Validation¶

FastAPI gives you the following:

Interactive API documentation and exploration web user interfaces. As the framework is based on OpenAPI, there are multiple options, 2 included by default.

It's all based on standard Python type declarations (thanks to Pydantic). No new syntax to learn. Just standard modern Python.

If you need a 2 minute refresher of how to use Python types (even if you don't use FastAPI), check the short tutorial: Python Types.

You write standard Python with types:

That can then be used like:

**second_user_data means:

Pass the keys and values of the second_user_data dict directly as key-value arguments, equivalent to: User(id=4, name="Mary", joined="2018-11-30")

All the framework was designed to be easy and intuitive to use, all the decisions were tested on multiple editors even before starting development, to ensure the best development experience.

In the Python developer surveys, it's clear that one of the most used features is "autocompletion".

The whole FastAPI framework is based to satisfy that. Autocompletion works everywhere.

You will rarely need to come back to the docs.

Here's how your editor might help you:

You will get completion in code you might even consider impossible before. As for example, the price key inside a JSON body (that could have been nested) that comes from a request.

No more typing the wrong key names, coming back and forth between docs, or scrolling up and down to find if you finally used username or user_name.

It has sensible defaults for everything, with optional configurations everywhere. All the parameters can be fine-tuned to do what you need and to define the API you need.

But by default, it all "just works".

Validation for most (or all?) Python data types, including:

Validation for more exotic types, like:

All the validation is handled by the well-established and robust Pydantic.

Security and authentication integrated. Without any compromise with databases or data models.

All the security sche

*[Content truncated - see full docs]*

**Examples**:

```python
from datetime import date

from pydantic import BaseModel

# Declare a variable as a str
# and get editor support inside the function
def main(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date
```

```text
my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)
```

---

## Full Stack FastAPI Template - FastAPI

**URL**: https://fastapi.tiangolo.com/project-generation/

**Contents**:
- Full Stack FastAPI Template¶
- Full Stack FastAPI Template - Technology Stack and Features¶

Templates, while typically come with a specific setup, are designed to be flexible and customizable. This allows you to modify and adapt them to your project's requirements, making them an excellent starting point. 🏁

You can use this template to get started, as it includes a lot of the initial set up, security, database and some API endpoints already done for you.

GitHub Repository: Full Stack FastAPI Template

---

## General - How To - Recipes - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/general/

**Contents**:
- General - How To - Recipes¶
- Filter Data - Security¶
- Documentation Tags - OpenAPI¶
- Documentation Summary and Description - OpenAPI¶
- Documentation Response description - OpenAPI¶
- Documentation Deprecate a Path Operation - OpenAPI¶
- Convert any Data to JSON-compatible¶
- OpenAPI Metadata - Docs¶

Here are several pointers to other places in the docs, for general or frequent questions.

To ensure that you don't return more data than you should, read the docs for Tutorial - Response Model - Return Type.

To add tags to your path operations, and group them in the docs UI, read the docs for Tutorial - Path Operation Configurations - Tags.

To add a summary and description to your path operations, and show them in the docs UI, read the docs for Tutorial - Path Operation Configurations - Summary and Description.

To define the description of the response, shown in the docs UI, read the docs for Tutorial - Path Operation Configurations - Response description.

To deprecate a path operation, and show it in the docs UI, read the docs for Tutorial - Path Operation Configurations - Deprecation.

To convert any data to JSON-compatible, read the docs for Tutorial - JSON Compatible Encoder.

To add metadata to your OpenAPI schema, including a license, version, contact, etc, read the docs for Tutorial - Metadata and Docs URLs.

To customize the OpenAPI URL (or remove it), read the docs for Tutorial - Metadata and Docs URLs.

To update the URLs used for the automatically generated docs user interfaces, read the docs for Tutorial - Metadata and Docs URLs.

---

## GraphQL - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/graphql/

**Contents**:
- GraphQL¶
- GraphQL Libraries¶
- GraphQL with Strawberry¶
- Older GraphQLApp from Starlette¶
- Learn More¶

As FastAPI is based on the ASGI standard, it's very easy to integrate any GraphQL library also compatible with ASGI.

You can combine normal FastAPI path operations with GraphQL on the same application.

GraphQL solves some very specific use cases.

It has advantages and disadvantages when compared to common web APIs.

Make sure you evaluate if the benefits for your use case compensate the drawbacks. 🤓

Here are some of the GraphQL libraries that have ASGI support. You could use them with FastAPI:

If you need or want to work with GraphQL, Strawberry is the recommended library as it has the design closest to FastAPI's design, it's all based on type annotations.

Depending on your use case, you might prefer to use a different library, but if you asked me, I would probably suggest you try Strawberry.

Here's a small preview of how you could integrate Strawberry with FastAPI:

You can learn more about Strawberry in the Strawberry documentation.

And also the docs about Strawberry with FastAPI.

Previous versions of Starlette included a GraphQLApp class to integrate with Graphene.

It was deprecated from Starlette, but if you have code that used it, you can easily migrate to starlette-graphene3, that covers the same use case and has an almost identical interface.

If you need GraphQL, I still would recommend you check out Strawberry, as it's based on type annotations instead of custom classes and types.

You can learn more about GraphQL in the official GraphQL documentation.

You can also read more about each those libraries described above in their links.

**Examples**:

```python
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
```

---

## Help FastAPI - Get Help - FastAPI

**URL**: https://fastapi.tiangolo.com/help-fastapi/

**Contents**:
- Help FastAPI - Get Help¶
- Subscribe to the newsletter¶
- Follow FastAPI on X (Twitter)¶
- Star FastAPI in GitHub¶
- Watch the GitHub repository for releases¶
- Connect with the author¶
- Tweet about FastAPI¶
- Vote for FastAPI¶

Would you like to help FastAPI, other users, and the author?

Or would you like to get help with FastAPI?

There are very simple ways to help (several involve just one or two clicks).

And there are several ways to get help too.

You can subscribe to the (infrequent) FastAPI and friends newsletter to stay updated about:

Follow @fastapi on X (Twitter) to get the latest news about FastAPI. 🐦

You can "star" FastAPI in GitHub (clicking the star button at the top right): https://github.com/fastapi/fastapi. ⭐️

By adding a star, other users will be able to find it more easily and see that it has been already useful for others.

You can "watch" FastAPI in GitHub (clicking the "watch" button at the top right): https://github.com/fastapi/fastapi. 👀

There you can select "Releases only".

By doing it, you will receive notifications (in your email) whenever there's a new release (a new version) of FastAPI with bug fixes and new features.

You can connect with me (Sebastián Ramírez / tiangolo), the author.

Tweet about FastAPI and let me and others know why you like it. 🎉

I love to hear about how FastAPI is being used, what you have liked in it, in which project/company are you using it, etc.

You can try and help others with their questions in:

In many cases you might already know the answer for those questions. 🤓

If you are helping a lot of people with their questions, you will become an official FastAPI Expert. 🎉

Just remember, the most important point is: try to be kind. People come with their frustrations and in many cases don't ask in the best way, but try as best as you can to be kind. 🤗

The idea is for the FastAPI community to be kind and welcoming. At the same time, don't accept bullying or disrespectful behavior towards others. We have to take care of each other.

Here's how to help others with questions (in discussions or issues):

Check if you can understand what is the purpose and use case of the person asking.

Then check if the question (the vast majority 

*[Content truncated - see full docs]*

---

## History, Design and Future - FastAPI

**URL**: https://fastapi.tiangolo.com/history-design-future/

**Contents**:
- History, Design and Future¶
- Alternatives¶
- Investigation¶
- Design¶
- Requirements¶
- Development¶
- Future¶

Some time ago, a FastAPI user asked:

What’s the history of this project? It seems to have come from nowhere to awesome in a few weeks [...]

Here's a little bit of that history.

I have been creating APIs with complex requirements for several years (Machine Learning, distributed systems, asynchronous jobs, NoSQL databases, etc), leading several teams of developers.

As part of that, I needed to investigate, test and use many alternatives.

The history of FastAPI is in great part the history of its predecessors.

As said in the section Alternatives:

FastAPI wouldn't exist if not for the previous work of others.

There have been many tools created before that have helped inspire its creation.

I have been avoiding the creation of a new framework for several years. First I tried to solve all the features covered by FastAPI using many different frameworks, plug-ins, and tools.

But at some point, there was no other option than creating something that provided all these features, taking the best ideas from previous tools, and combining them in the best way possible, using language features that weren't even available before (Python 3.6+ type hints).

By using all the previous alternatives I had the chance to learn from all of them, take ideas, and combine them in the best way I could find for myself and the teams of developers I have worked with.

For example, it was clear that ideally it should be based on standard Python type hints.

Also, the best approach was to use already existing standards.

So, before even starting to code FastAPI, I spent several months studying the specs for OpenAPI, JSON Schema, OAuth2, etc. Understanding their relationship, overlap, and differences.

Then I spent some time designing the developer "API" I wanted to have as a user (as a developer using FastAPI).

I tested several ideas in the most popular Python editors: PyCharm, VS Code, Jedi based editors.

By the last Python Developer Survey, that covers about 80% of the users.

It means t

*[Content truncated - see full docs]*

---

## How To - Recipes - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/

**Contents**:
- How To - Recipes¶

Here you will see different recipes or "how to" guides for several topics.

Most of these ideas would be more or less independent, and in most cases you should only need to study them if they apply directly to your project.

If something seems interesting and useful to your project, go ahead and check it, but otherwise, you might probably just skip them.

If you want to learn FastAPI in a structured way (recommended), go and read the Tutorial - User Guide chapter by chapter instead.

---

## Learn - FastAPI

**URL**: https://fastapi.tiangolo.com/learn/

**Contents**:
- Learn¶

Here are the introductory sections and the tutorials to learn FastAPI.

You could consider this a book, a course, the official and recommended way to learn FastAPI. 😎

---

## Migrate from Pydantic v1 to Pydantic v2 - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/

**Contents**:
- Migrate from Pydantic v1 to Pydantic v2¶
- Official Guide¶
- Tests¶
- bump-pydantic¶
- Pydantic v1 in v2¶
  - FastAPI support for Pydantic v1 in v2¶
  - Pydantic v1 and v2 on the same app¶
  - Pydantic v1 parameters¶

If you have an old FastAPI app, you might be using Pydantic version 1.

FastAPI has had support for either Pydantic v1 or v2 since version 0.100.0.

If you had installed Pydantic v2, it would use it. If instead you had Pydantic v1, it would use that.

Pydantic v1 is now deprecated and support for it will be removed in the next versions of FastAPI, you should migrate to Pydantic v2. This way you will get the latest features, improvements, and fixes.

Also, the Pydantic team stopped support for Pydantic v1 for the latest versions of Python, starting with Python 3.14.

If you want to use the latest features of Python, you will need to make sure you use Pydantic v2.

If you have an old FastAPI app with Pydantic v1, here I'll show you how to migrate it to Pydantic v2, and the new features in FastAPI 0.119.0 to help you with a gradual migration.

Pydantic has an official Migration Guide from v1 to v2.

It also includes what has changed, how validations are now more correct and strict, possible caveats, etc.

You can read it to understand better what has changed.

Make sure you have tests for your app and you run them on continuous integration (CI).

This way, you can do the upgrade and make sure everything is still working as expected.

In many cases, when you use regular Pydantic models without customizations, you will be able to automate most of the process of migrating from Pydantic v1 to Pydantic v2.

You can use bump-pydantic from the same Pydantic team.

This tool will help you to automatically change most of the code that needs to be changed.

After this, you can run the tests and check if everything works. If it does, you are done. 😎

Pydantic v2 includes everything from Pydantic v1 as a submodule pydantic.v1.

This means that you can install the latest version of Pydantic v2 and import and use the old Pydantic v1 components from this submodule, as if you had the old Pydantic v1 installed.

Since FastAPI 0.119.0, there's also partial support for Pydantic v1 from i

*[Content truncated - see full docs]*

**Examples**:

```python
from pydantic.v1 import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    size: float
```

```python
from typing import Union

from pydantic.v1 import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    size: float
```

```python
from fastapi import FastAPI
from pydantic.v1 import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    size: float


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item
```

---

## Python Types Intro - FastAPI

**URL**: https://fastapi.tiangolo.com/python-types/

**Contents**:
- Python Types Intro¶
- Motivation¶
  - Edit it¶
  - Add types¶
- More motivation¶
- Declaring types¶
  - Simple types¶
  - Generic types with type parameters¶

Python has support for optional "type hints" (also called "type annotations").

These "type hints" or annotations are a special syntax that allow declaring the type of a variable.

By declaring types for your variables, editors and tools can give you better support.

This is just a quick tutorial / refresher about Python type hints. It covers only the minimum necessary to use them with FastAPI... which is actually very little.

FastAPI is all based on these type hints, they give it many advantages and benefits.

But even if you never use FastAPI, you would benefit from learning a bit about them.

If you are a Python expert, and you already know everything about type hints, skip to the next chapter.

Let's start with a simple example:

Calling this program outputs:

The function does the following:

It's a very simple program.

But now imagine that you were writing it from scratch.

At some point you would have started the definition of the function, you had the parameters ready...

But then you have to call "that method that converts the first letter to upper case".

Was it upper? Was it uppercase? first_uppercase? capitalize?

Then, you try with the old programmer's friend, editor autocompletion.

You type the first parameter of the function, first_name, then a dot (.) and then hit Ctrl+Space to trigger the completion.

But, sadly, you get nothing useful:

Let's modify a single line from the previous version.

We will change exactly this fragment, the parameters of the function, from:

Those are the "type hints":

That is not the same as declaring default values like would be with:

It's a different thing.

We are using colons (:), not equals (=).

And adding type hints normally doesn't change what happens from what would happen without them.

But now, imagine you are again in the middle of creating that function, but with type hints.

At the same point, you try to trigger the autocomplete with Ctrl+Space and you see:

With that, you can scroll, seeing the options,

*[Content truncated - see full docs]*

**Examples**:

```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

```text
first_name, last_name
```

---

## Release Notes - FastAPI

**URL**: https://fastapi.tiangolo.com/release-notes/

**Contents**:
- Release Notes¶
- Latest Changes¶
  - Docs¶
  - Internal¶
- 0.119.0¶
  - Features¶
- 0.118.3¶
  - Upgrades¶

FastAPI now (temporarily) supports both Pydantic v2 models and pydantic.v1 models at the same time in the same app, to make it easier for any FastAPI apps still using Pydantic v1 to gradually but quickly migrate to Pydantic v2.

Adding this feature was a big effort with the main objective of making it easier for the few applications still stuck in Pydantic v1 to migrate to Pydantic v2.

And with this, support for Pydantic v1 is now deprecated and will be removed from FastAPI in a future version soon.

Note: have in mind that the Pydantic team already stopped supporting Pydantic v1 for recent versions of Python, starting with Python 3.14.

You can read in the docs more about how to Migrate from Pydantic v1 to Pydantic v2.

Before FastAPI 0.118.0, if you used a dependency with yield, it would run the exit code after the path operation function returned but right before sending the response.

This change also meant that if you returned a StreamingResponse, the exit code of the dependency with yield would have been already run.

For example, if you had a database session in a dependency with yield, the StreamingResponse would not be able to use that session while streaming data because the session would have already been closed in the exit code after yield.

This behavior was reverted in 0.118.0, to make the exit code after yield be executed after the response is sent.

You can read more about it in the docs for Advanced Dependencies - Dependencies with yield, HTTPException, except and Background Tasks. Including what you could do if you wanted to close a database session earlier, before returning the response to the client.

Installing fastapi[standard] now includes fastapi-cloud-cli.

This will allow you to deploy to FastAPI Cloud with the fastapi deploy command.

If you want to install fastapi with the standard dependencies but without fastapi-cloud-cli, you can install instead fastapi[standard-no-fastapi-cloud-cli].

Now you can declare Query, Header, and Cookie par

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel as BaseModelV2
from pydantic.v1 import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None


class ItemV2(BaseModelV2):
    title: str
    summary: str | None = None


app = FastAPI()


@app.post("/items/", response_model=ItemV2)
def create_item(item: Item):
    return {"title": item.name, "summary": item.description}
```

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

---

## Repository Management - FastAPI

**URL**: https://fastapi.tiangolo.com/management/

**Contents**:
- Repository Management¶
- Owner¶
- Team¶
- FastAPI Experts¶
- External Contributions¶

Here's a short description of how the FastAPI repository is managed and maintained.

I, @tiangolo, am the creator and owner of the FastAPI repository. 🤓

I normally give the final review to each PR before merging them. I make the final decisions on the project, I'm the BDFL. 😅

There's a team of people that help manage and maintain the project. 😎

They have different levels of permissions and specific instructions.

Some of the tasks they can perform include:

You can see the current team members in FastAPI People - Team.

Joining the team is by invitation only, and I could update or remove permissions, instructions, or membership.

The people that help others the most in GitHub Discussions can become FastAPI Experts.

This is normally the best way to contribute to the project.

External contributions are very welcome and appreciated, including answering questions, submitting PRs, etc. 🙇‍♂️

There are many ways to help maintain FastAPI.

---

## Repository Management Tasks - FastAPI

**URL**: https://fastapi.tiangolo.com/management-tasks/

**Contents**:
- Repository Management Tasks¶
- Be Nice¶
  - When Things are Difficult¶
- Edit PR Titles¶
- Add Labels to PRs¶
- Add Labels to Translation PRs¶
- Merge Translation PRs¶
- First Translation PR¶

These are the tasks that can be performed to manage the FastAPI repository by team members.

This section is useful only to a handful of people, team members with permissions to manage the repository. You can probably skip it. 😉

...so, you are a team member of FastAPI? Wow, you are so cool! 😎

You can help with everything on Help FastAPI - Get Help the same ways as external contributors. But additionally, there are some tasks that only you (as part of the team) can perform.

Here are the general instructions for the tasks you can perform.

Thanks a lot for your help. 🙇

First of all, be nice. 😊

You probably are super nice if you were added to the team, but it's worth mentioning it. 🤓

When things are great, everything is easier, so that doesn't need much instructions. But when things are difficult, here are some guidelines.

Try to find the good side. In general, if people are not being unfriendly, try to thank their effort and interest, even if you disagree with the main subject (discussion, PR), just thank them for being interested in the project, or for having dedicated some time to try to do something.

It's difficult to convey emotion in text, use emojis to help. 😅

In discussions and PRs, in many cases, people bring their frustration and show it without filter, in many cases exaggerating, complaining, being entitled, etc. That's really not nice, and when it happens, it lowers our priority to solve their problems. But still, try to breath, and be gentle with your answers.

Try to avoid using bitter sarcasm or potentially passive-aggressive comments. If something is wrong, it's better to be direct (try to be gentle) than sarcastic.

Try to be as specific and objective as possible, avoid generalizations.

For conversations that are more difficult, for example to reject a PR, you can ask me (@tiangolo) to handle it directly.

Once the PR is merged, a GitHub Action (latest-changes) will use the PR title to update the latest changes automatically.

So, having a ni

*[Content truncated - see full docs]*

**Examples**:

```text
🌐 Add Spanish translation for `docs/es/docs/teleporting.md`
```

```text
/// tip

This is a tip.

///
```

```text
/// tip

Esto es un consejo.

///
```

---

## Resources - FastAPI

**URL**: https://fastapi.tiangolo.com/resources/

**Contents**:
- Resources¶

Additional resources, external links, articles and more. ✈️

---

## Separate OpenAPI Schemas for Input and Output or Not - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/separate-openapi-schemas/

**Contents**:
- Separate OpenAPI Schemas for Input and Output or Not¶
- Pydantic Models for Input and Output¶
  - Model for Input¶
  - Input Model in Docs¶
  - Model for Output¶
  - Model for Output Response Data¶
  - Model for Output in Docs¶
  - Model for Input and Output in Docs¶

When using Pydantic v2, the generated OpenAPI is a bit more exact and correct than before. 😎

In fact, in some cases, it will even have two JSON Schemas in OpenAPI for the same Pydantic model, for input and output, depending on if they have default values.

Let's see how that works and how to change it if you need to do that.

Let's say you have a Pydantic model with default values, like this one:

If you use this model as an input like here:

...then the description field will not be required. Because it has a default value of None.

You can confirm that in the docs, the description field doesn't have a red asterisk, it's not marked as required:

But if you use the same model as an output, like here:

...then because description has a default value, if you don't return anything for that field, it will still have that default value.

If you interact with the docs and check the response, even though the code didn't add anything in one of the description fields, the JSON response contains the default value (null):

This means that it will always have a value, it's just that sometimes the value could be None (or null in JSON).

That means that, clients using your API don't have to check if the value exists or not, they can assume the field will always be there, but just that in some cases it will have the default value of None.

The way to describe this in OpenAPI, is to mark that field as required, because it will always be there.

Because of that, the JSON Schema for a model can be different depending on if it's used for input or output:

You can check the output model in the docs too, both name and description are marked as required with a red asterisk:

And if you check all the available Schemas (JSON Schemas) in OpenAPI, you will see that there are two, one Item-Input and one Item-Output.

For Item-Input, description is not required, it doesn't have a red asterisk.

But for Item-Output, description is required, it has a red asterisk.

With this feature from Pydant

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None

# Code below omitted 👇
```

```python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None


app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/items/")
def read_items() -> list[Item]:
    return [
        Item(
            name="Portal Gun",
            description="Device to travel through the multi-rick-verse",
        ),
        Item(name="Plumbus"),
    ]
```

```python
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None


app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/items/")
def read_items() -> list[Item]:
    return [
        Item(
            name="Portal Gun",
            description="Device to travel through the multi-rick-verse",
        ),
        Item(name="Plumbus"),
    ]
```

---

## Testing a Database - FastAPI

**URL**: https://fastapi.tiangolo.com/how-to/testing-database/

**Contents**:
- Testing a Database¶

You can study about databases, SQL, and SQLModel in the SQLModel docs. 🤓

There's a mini tutorial on using SQLModel with FastAPI. ✨

That tutorial includes a section about testing SQL databases. 😎

---

## Virtual Environments - FastAPI

**URL**: https://fastapi.tiangolo.com/virtual-environments/

**Contents**:
- Virtual Environments¶
- Create a Project¶
- Create a Virtual Environment¶
- Activate the Virtual Environment¶
- Check the Virtual Environment is Active¶
- Upgrade pip¶
- Add .gitignore¶
- Install Packages¶

When you work in Python projects you probably should use a virtual environment (or a similar mechanism) to isolate the packages you install for each project.

If you already know about virtual environments, how to create them and use them, you might want to skip this section. 🤓

A virtual environment is different than an environment variable.

An environment variable is a variable in the system that can be used by programs.

A virtual environment is a directory with some files in it.

This page will teach you how to use virtual environments and how they work.

If you are ready to adopt a tool that manages everything for you (including installing Python), try uv.

First, create a directory for your project.

What I normally do is that I create a directory named code inside my home/user directory.

And inside of that I create one directory per project.

When you start working on a Python project for the first time, create a virtual environment inside your project.

You only need to do this once per project, not every time you work.

To create a virtual environment, you can use the venv module that comes with Python.

If you have uv installed, you can use it to create a virtual environment.

By default, uv will create a virtual environment in a directory called .venv.

But you could customize it passing an additional argument with the directory name.

That command creates a new virtual environment in a directory called .venv.

You could create the virtual environment in a different directory, but there's a convention of calling it .venv.

Activate the new virtual environment so that any Python command you run or package you install uses it.

Do this every time you start a new terminal session to work on the project.

Or if you use Bash for Windows (e.g. Git Bash):

Every time you install a new package in that environment, activate the environment again.

This makes sure that if you use a terminal (CLI) program installed by that package, you use the one from your virtua

*[Content truncated - see full docs]*

**Examples**:

```text
// Go to the home directory
$ cd
// Create a directory for all your code projects
$ mkdir code
// Enter into that code directory
$ cd code
// Create a directory for this project
$ mkdir awesome-project
// Enter into that project directory
$ cd awesome-project
```

```text
$ python -m venv .venv
```

```text
$ source .venv/bin/activate
```

---

## 帮助 FastAPI 与求助 - FastAPI

**URL**: https://fastapi.tiangolo.com/zh/help-fastapi/

**Contents**:
- 帮助 FastAPI 与求助¶
- 订阅新闻邮件¶
- 在推特上关注 FastAPI¶
- 在 GitHub 上为 FastAPI 加星¶
- 关注 GitHub 资源库的版本发布¶
- 联系作者¶
- Tweet about FastAPI¶
- 为 FastAPI 投票¶

想帮助 FastAPI？其它用户？还有项目作者？

以下几种帮助的方式都非常简单（有些只需要点击一两下鼠标）。

您可以订阅 FastAPI 和它的小伙伴 新闻邮件（不会经常收到）

在 X (Twitter) 上关注 @fastapi 获取 FastAPI 的最新消息。🐦

您可以在 GitHub 上 Star FastAPI（只要点击右上角的星星就可以了）： https://github.com/fastapi/fastapi。⭐️

Star 以后，其它用户就能更容易找到 FastAPI，并了解到已经有其他用户在使用它了。

您还可以在 GitHub 上 Watch FastAPI，（点击右上角的 Watch 按钮）https://github.com/fastapi/fastapi。👀

您可以选择只关注发布（Releases only）。

这样，您就可以（在电子邮件里）接收到 FastAPI 新版发布的通知，及时了解 bug 修复与新功能。

您可以联系项目作者，就是我（Sebastián Ramírez / tiangolo）。

Tweet about FastAPI 让我和大家知道您为什么喜欢 FastAPI。🎉

知道有人使用 FastAPI，我会很开心，我也想知道您为什么喜欢 FastAPI，以及您在什么项目/哪些公司使用 FastAPI，等等。

您可以查看现有 issues，并尝试帮助其他人解决问题，说不定您能解决这些问题呢。🤓

如果帮助很多人解决了问题，您就有可能成为 FastAPI 的官方专家。🎉

您可以在 GitHub 上「监听」FastAPI（点击右上角的 "watch" 按钮）： https://github.com/fastapi/fastapi. 👀

如果您选择 "Watching" 而不是 "Releases only"，有人创建新 Issue 时，您会接收到通知。

您可以在 GitHub 资源库中创建 Issue，例如：

注意：如果您创建 Issue，我会要求您也要帮助别的用户。😉

快加入 👥 Discord 聊天服务器 👥 和 FastAPI 社区里的小伙伴一起哈皮吧。

如有问题，请在 GitHub Issues 里提问，在这里更容易得到 FastAPI 专家的帮助。

注意，聊天室更倾向于“闲聊”，经常有人会提出一些笼统得让人难以回答的问题，所以在这里提问一般没人回答。

GitHub Issues 里提供了模板，指引您提出正确的问题，有利于获得优质的回答，甚至可能解决您还没有想到的问题。而且就算答疑解惑要耗费不少时间，我还是会尽量在 GitHub 里回答问题。但在聊天室里，我就没功夫这么做了。😅

聊天室里的聊天内容也不如 GitHub 里好搜索，聊天里的问答很容易就找不到了。只有在 GitHub Issues 里的问答才能帮助您成为 FastAPI 专家，在 GitHub Issues 中为您带来更多关注。

另一方面，聊天室里有成千上万的用户，在这里，您有很大可能遇到聊得来的人。😄

您还可以通过 GitHub 赞助商资助本项目的作者（就是我）。

当然您也可以成为 FastAPI 的金牌或银牌赞助商。🏅🎉

如您在本文档中所见，FastAPI 站在巨人的肩膀上，它们分别是 Starlette 和 Pydantic。

---
