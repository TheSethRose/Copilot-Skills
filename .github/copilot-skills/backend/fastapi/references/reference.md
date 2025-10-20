# Fastapi - Reference

**Pages**: 21

---

## APIRouter class - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/apirouter/

**Contents**:
- APIRouter class¶
- fastapi.APIRouter ¶
    - Example¶
  - websocket ¶
      - Example¶
  - include_router ¶
      - Example¶
  - get ¶

Here's the reference information for the APIRouter class, with all its parameters, attributes and methods.

You can import the APIRouter class directly from fastapi:

APIRouter class, used to group path operations, for example to structure an app in multiple files. It would then be included in the FastAPI app, or in another APIRouter (ultimately included in the app).

Read more about it in the FastAPI docs for Bigger Applications - Multiple Files.

An optional path prefix for the router.

TYPE: str DEFAULT: ''

A list of tags to be applied to all the path operations in this router.

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more about it in the FastAPI docs for Path Operation Configuration.

TYPE: Optional[List[Union[str, Enum]]] DEFAULT: None

A list of dependencies (using Depends()) to be applied to all the path operations in this router.

Read more about it in the FastAPI docs for Bigger Applications - Multiple Files.

TYPE: Optional[Sequence[Depends]] DEFAULT: None

The default response class to be used.

Read more in the FastAPI docs for Custom Response - HTML, Stream, File, others.

TYPE: Type[Response] DEFAULT: Default(JSONResponse)

Additional responses to be shown in OpenAPI.

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more about it in the FastAPI docs for Additional Responses in OpenAPI.

And in the FastAPI docs for Bigger Applications.

TYPE: Optional[Dict[Union[int, str], Dict[str, Any]]] DEFAULT: None

OpenAPI callbacks that should apply to all path operations in this router.

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more about it in the FastAPI docs for OpenAPI Callbacks.

TYPE: Optional[List[BaseRoute]] DEFAULT: None

Note: you probably shouldn't use this parameter, it is inherited from Starlette and supported for compatibility.

A list of routes to serve incoming HTTP and WebSocket requests.

TYPE: Optional[List[BaseRoute]] DEFAULT: None

Whether to detect an

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import APIRouter
```

```javascript
APIRouter(
    *,
    prefix="",
    tags=None,
    dependencies=None,
    default_response_class=Default(JSONResponse),
    responses=None,
    callbacks=None,
    routes=None,
    redirect_slashes=True,
    default=None,
    dependency_overrides_provider=None,
    route_class=APIRoute,
    on_startup=None,
    on_shutdown=None,
    lifespan=None,
    deprecated=None,
    include_in_schema=True,
    generate_unique_id_function=Default(generate_unique_id)
)
```

```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


app.include_router(router)
```

---

## Background Tasks - BackgroundTasks - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/background/

**Contents**:
- Background Tasks - BackgroundTasks¶
- fastapi.BackgroundTasks ¶
    - Example¶
  - func instance-attribute ¶
  - args instance-attribute ¶
  - kwargs instance-attribute ¶
  - is_async instance-attribute ¶
  - tasks instance-attribute ¶

You can declare a parameter in a path operation function or dependency function with the type BackgroundTasks, and then you can use it to schedule the execution of background tasks after the response is sent.

You can import it directly from fastapi:

Bases: BackgroundTasks

A collection of background tasks that will be called after a response has been sent to the client.

Read more about it in the FastAPI docs for Background Tasks.

Add a function to be called in the background after the response is sent.

Read more about it in the FastAPI docs for Background Tasks.

The function to call after the response is sent.

It can be a regular def function or an async def function.

TYPE: Callable[P, Any]

**Examples**:

```python
from fastapi import BackgroundTasks
```

```text
BackgroundTasks(tasks=None)
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

## Custom Response Classes - File, HTML, Redirect, Streaming, etc. - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/responses/

**Contents**:
- Custom Response Classes - File, HTML, Redirect, Streaming, etc.¶
- FastAPI Responses¶
- fastapi.responses.UJSONResponse ¶
  - charset class-attribute instance-attribute ¶
  - status_code instance-attribute ¶
  - media_type class-attribute instance-attribute ¶
  - body instance-attribute ¶
  - background instance-attribute ¶

There are several custom response classes you can use to create an instance and return them directly from your path operations.

Read more about it in the FastAPI docs for Custom Response - HTML, Stream, File, others.

You can import them directly from fastapi.responses:

There are a couple of custom FastAPI response classes, you can use them to optimize JSON performance.

JSON response using the high-performance ujson library to serialize data to JSON.

Read more about it in the FastAPI docs for Custom Response - HTML, Stream, File, others.

JSON response using the high-performance orjson library to serialize data to JSON.

Read more about it in the FastAPI docs for Custom Response - HTML, Stream, File, others.

**Examples**:

```python
from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    ORJSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
    UJSONResponse,
)
```

```text
UJSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)
```

```python
def __init__(
    self,
    content: Any,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> None:
    super().__init__(content, status_code, headers, media_type, background)
```

---

## Encoders - jsonable_encoder - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/encoders/

**Contents**:
- Encoders - jsonable_encoder¶
- fastapi.encoders.jsonable_encoder ¶

Convert any object to something that can be encoded in JSON.

This is used internally by FastAPI to make sure anything you return can be encoded as JSON before it is sent to the client.

You can also use it yourself, for example to convert objects before saving them in a database that supports only JSON.

Read more about it in the FastAPI docs for JSON Compatible Encoder.

The input object to convert to JSON.

Pydantic's include parameter, passed to Pydantic models to set the fields to include.

TYPE: Optional[IncEx] DEFAULT: None

Pydantic's exclude parameter, passed to Pydantic models to set the fields to exclude.

TYPE: Optional[IncEx] DEFAULT: None

Pydantic's by_alias parameter, passed to Pydantic models to define if the output should use the alias names (when provided) or the Python attribute names. In an API, if you set an alias, it's probably because you want to use it in the result, so you probably want to leave this set to True.

TYPE: bool DEFAULT: True

Pydantic's exclude_unset parameter, passed to Pydantic models to define if it should exclude from the output the fields that were not explicitly set (and that only had their default values).

TYPE: bool DEFAULT: False

Pydantic's exclude_defaults parameter, passed to Pydantic models to define if it should exclude from the output the fields that had the same default value, even when they were explicitly set.

TYPE: bool DEFAULT: False

Pydantic's exclude_none parameter, passed to Pydantic models to define if it should exclude from the output any fields that have a None value.

TYPE: bool DEFAULT: False

Pydantic's custom_encoder parameter, passed to Pydantic models to define a custom encoder.

TYPE: Optional[Dict[Any, Callable[[Any], Any]]] DEFAULT: None

Exclude from the output any fields that start with the name _sa.

This is mainly a hack for compatibility with SQLAlchemy objects, they store internal SQLAlchemy-specific state in attributes named with _sa, and those objects can't (and shouldn't be) seria

*[Content truncated - see full docs]*

**Examples**:

```text
jsonable_encoder(
    obj,
    include=None,
    exclude=None,
    by_alias=True,
    exclude_unset=False,
    exclude_defaults=False,
    exclude_none=False,
    custom_encoder=None,
    sqlalchemy_safe=True,
)
```

```python
def jsonable_encoder(
    obj: Annotated[
        Any,
        Doc(
            """
            The input object to convert to JSON.
            """
        ),
    ],
    include: Annotated[
        Optional[IncEx],
        Doc(
            """
            Pydantic's `include` parameter, passed to Pydantic models to set the
            fields to include.
            """
        ),
    ] = None,
    exclude: Annotated[
        Optional[IncEx],
        Doc(
            """
            Pydantic's `
...
```

---

## Exceptions - HTTPException and WebSocketException - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/exceptions/

**Contents**:
- Exceptions - HTTPException and WebSocketException¶
- fastapi.HTTPException ¶
    - Example¶
  - status_code instance-attribute ¶
  - detail instance-attribute ¶
  - headers instance-attribute ¶
- fastapi.WebSocketException ¶
    - Example¶

These are the exceptions that you can raise to show errors to the client.

When you raise an exception, as would happen with normal Python, the rest of the execution is aborted. This way you can raise these exceptions from anywhere in the code to abort a request and show the error to the client.

These exceptions can be imported directly from fastapi:

An HTTP exception you can raise in your own code to show errors to the client.

This is for client errors, invalid authentication, invalid data, etc. Not for server errors in your code.

Read more about it in the FastAPI docs for Handling Errors.

HTTP status code to send to the client.

Any data to be sent to the client in the detail key of the JSON response.

TYPE: Any DEFAULT: None

Any headers to send to the client in the response.

TYPE: Optional[Dict[str, str]] DEFAULT: None

Bases: WebSocketException

A WebSocket exception you can raise in your own code to show errors to the client.

This is for client errors, invalid authentication, invalid data, etc. Not for server errors in your code.

Read more about it in the FastAPI docs for WebSockets.

A closing code from the valid codes defined in the specification.

The reason to close the WebSocket connection.

It is UTF-8-encoded data. The interpretation of the reason is up to the application, it is not specified by the WebSocket specification.

It could contain text that could be human-readable or interpretable by the client code, etc.

TYPE: Union[str, None] DEFAULT: None

**Examples**:

```python
from fastapi import HTTPException, WebSocketException
```

```text
HTTPException(status_code, detail=None, headers=None)
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

---

## FastAPI class - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/fastapi/

**Contents**:
- FastAPI class¶
- fastapi.FastAPI ¶
    - Example¶
  - openapi_version instance-attribute ¶
  - webhooks instance-attribute ¶
  - state instance-attribute ¶
  - dependency_overrides instance-attribute ¶
  - openapi ¶

Here's the reference information for the FastAPI class, with all its parameters, attributes and methods.

You can import the FastAPI class directly from fastapi:

FastAPI app class, the main entrypoint to use FastAPI.

Read more in the FastAPI docs for First Steps.

Boolean indicating if debug tracebacks should be returned on server errors.

Read more in the Starlette docs for Applications.

TYPE: bool DEFAULT: False

Note: you probably shouldn't use this parameter, it is inherited from Starlette and supported for compatibility.

A list of routes to serve incoming HTTP and WebSocket requests.

TYPE: Optional[List[BaseRoute]] DEFAULT: None

The title of the API.

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more in the FastAPI docs for Metadata and Docs URLs.

TYPE: str DEFAULT: 'FastAPI'

A short summary of the API.

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more in the FastAPI docs for Metadata and Docs URLs.

TYPE: Optional[str] DEFAULT: None

A description of the API. Supports Markdown (using CommonMark syntax).

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more in the FastAPI docs for Metadata and Docs URLs.

TYPE: str DEFAULT: ''

The version of the API.

Note This is the version of your application, not the version of the OpenAPI specification nor the version of FastAPI being used.

It will be added to the generated OpenAPI (e.g. visible at /docs).

Read more in the FastAPI docs for Metadata and Docs URLs.

TYPE: str DEFAULT: '0.1.0'

The URL where the OpenAPI schema will be served from.

If you set it to None, no OpenAPI schema will be served publicly, and the default automatic endpoints /docs and /redoc will also be disabled.

Read more in the FastAPI docs for Metadata and Docs URLs.

TYPE: Optional[str] DEFAULT: '/openapi.json'

A list of tags used by OpenAPI, these are the same tags you can set in the path operations, like:

The order of the tags can be used to specify t

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import FastAPI
```

```javascript
FastAPI(
    *,
    debug=False,
    routes=None,
    title="FastAPI",
    summary=None,
    description="",
    version="0.1.0",
    openapi_url="/openapi.json",
    openapi_tags=None,
    servers=None,
    dependencies=None,
    default_response_class=Default(JSONResponse),
    redirect_slashes=True,
    docs_url="/docs",
    redoc_url="/redoc",
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth=None,
    middleware=None,
    exception_handlers=None,
    on_s
...
```

```python
from fastapi import FastAPI

app = FastAPI()
```

---

## HTTPConnection class - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/httpconnection/

**Contents**:
- HTTPConnection class¶
- fastapi.requests.HTTPConnection ¶
  - scope instance-attribute ¶
  - app property ¶
  - url property ¶
  - base_url property ¶
  - headers property ¶
  - query_params property ¶

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an HTTPConnection instead of a Request or a WebSocket.

You can import it from fastapi.requests:

Bases: Mapping[str, Any]

A base class for incoming HTTP connections, that is used to provide any functionality that is common to both Request and WebSocket.

**Examples**:

```python
from fastapi.requests import HTTPConnection
```

```text
HTTPConnection(scope, receive=None)
```

```python
def __init__(self, scope: Scope, receive: Receive | None = None) -> None:
    assert scope["type"] in ("http", "websocket")
    self.scope = scope
```

---

## Middleware - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/middleware/

**Contents**:
- Middleware¶
- fastapi.middleware.cors.CORSMiddleware ¶
  - app instance-attribute ¶
  - allow_origins instance-attribute ¶
  - allow_methods instance-attribute ¶
  - allow_headers instance-attribute ¶
  - allow_all_origins instance-attribute ¶
  - allow_all_headers instance-attribute ¶

There are several middlewares available provided by Starlette directly.

Read more about them in the FastAPI docs for Middleware.

It can be imported from fastapi:

It can be imported from fastapi:

It can be imported from fastapi:

It can be imported from fastapi:

It can be imported from fastapi:

**Examples**:

```text
CORSMiddleware(
    app,
    allow_origins=(),
    allow_methods=("GET",),
    allow_headers=(),
    allow_credentials=False,
    allow_origin_regex=None,
    expose_headers=(),
    max_age=600,
)
```

```python
def __init__(
    self,
    app: ASGIApp,
    allow_origins: Sequence[str] = (),
    allow_methods: Sequence[str] = ("GET",),
    allow_headers: Sequence[str] = (),
    allow_credentials: bool = False,
    allow_origin_regex: str | None = None,
    expose_headers: Sequence[str] = (),
    max_age: int = 600,
) -> None:
    if "*" in allow_methods:
        allow_methods = ALL_METHODS

    compiled_allow_origin_regex = None
    if allow_origin_regex is not None:
        compiled_allow_origin_regex 
...
```

```text
allow_origins = allow_origins
```

---

## OpenAPI - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/openapi/

**Contents**:
- OpenAPI¶

There are several utilities to handle OpenAPI.

You normally don't need to use them unless you have a specific advanced use case that requires it.

---

## OpenAPI docs - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/openapi/docs/

**Contents**:
- OpenAPI docs¶
- fastapi.openapi.docs.get_swagger_ui_html ¶
- fastapi.openapi.docs.get_redoc_html ¶
- fastapi.openapi.docs.get_swagger_ui_oauth2_redirect_html ¶
- fastapi.openapi.docs.swagger_ui_default_parameters module-attribute ¶

Utilities to handle OpenAPI automatic UI documentation, including Swagger UI (by default at /docs) and ReDoc (by default at /redoc).

Generate and return the HTML that loads Swagger UI for the interactive API docs (normally served at /docs).

You would only call this function yourself if you needed to override some parts, for example the URLs to use to load Swagger UI's JavaScript and CSS.

Read more about it in the FastAPI docs for Configure Swagger UI and the FastAPI docs for Custom Docs UI Static Assets (Self-Hosting).

The OpenAPI URL that Swagger UI should load and use.

This is normally done automatically by FastAPI using the default URL /openapi.json.

The HTML <title> content, normally shown in the browser tab.

The URL to use to load the Swagger UI JavaScript.

It is normally set to a CDN URL.

TYPE: str DEFAULT: 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js'

The URL to use to load the Swagger UI CSS.

It is normally set to a CDN URL.

TYPE: str DEFAULT: 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css'

The URL of the favicon to use. It is normally shown in the browser tab.

TYPE: str DEFAULT: 'https://fastapi.tiangolo.com/img/favicon.png'

The OAuth2 redirect URL, it is normally automatically handled by FastAPI.

TYPE: Optional[str] DEFAULT: None

A dictionary with Swagger UI OAuth2 initialization configurations.

TYPE: Optional[Dict[str, Any]] DEFAULT: None

Configuration parameters for Swagger UI.

It defaults to swagger_ui_default_parameters.

TYPE: Optional[Dict[str, Any]] DEFAULT: None

Generate and return the HTML response that loads ReDoc for the alternative API docs (normally served at /redoc).

You would only call this function yourself if you needed to override some parts, for example the URLs to use to load ReDoc's JavaScript and CSS.

Read more about it in the FastAPI docs for Custom Docs UI Static Assets (Self-Hosting).

The OpenAPI URL that ReDoc should load and use.

This is normally done automatically 

*[Content truncated - see full docs]*

**Examples**:

```text
get_swagger_ui_html(
    *,
    openapi_url,
    title,
    swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
    oauth2_redirect_url=None,
    init_oauth=None,
    swagger_ui_parameters=None
)
```

```javascript
def get_swagger_ui_html(
    *,
    openapi_url: Annotated[
        str,
        Doc(
            """
            The OpenAPI URL that Swagger UI should load and use.

            This is normally done automatically by FastAPI using the default URL
            `/openapi.json`.
            """
        ),
    ],
    title: Annotated[
        str,
        Doc(
            """
            The HTML `<title>` content, normally shown in the browser tab.
            """
        ),
    ],
    swagger_js_
...
```

```text
get_redoc_html(
    *,
    openapi_url,
    title,
    redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js",
    redoc_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
    with_google_fonts=True
)
```

---

## OpenAPI models - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/openapi/models/

**Contents**:
- OpenAPI models¶
- fastapi.openapi.models ¶
  - SchemaType module-attribute ¶
  - SchemaOrBool module-attribute ¶
  - SecurityScheme module-attribute ¶
  - BaseModelWithConfig ¶
    - model_config class-attribute instance-attribute ¶
    - Config ¶

OpenAPI Pydantic models used to generate and validate the generated OpenAPI.

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

Bases: BaseModelWithConfig

**Examples**:

```text
SchemaType = Literal[
    "array",
    "boolean",
    "integer",
    "null",
    "number",
    "object",
    "string",
]
```

```text
SchemaOrBool = Union[Schema, bool]
```

```text
SecurityScheme = Union[
    APIKey, HTTPBase, OAuth2, OpenIdConnect, HTTPBearer
]
```

---

## Reference - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/

**Contents**:
- Reference¶

Here's the reference or code API, the classes, functions, parameters, attributes, and all the FastAPI parts you can use in your applications.

If you want to learn FastAPI you are much better off reading the FastAPI Tutorial.

---

## Request Parameters - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/parameters/

**Contents**:
- Request Parameters¶
- fastapi.Query ¶
- fastapi.Path ¶
- fastapi.Body ¶
- fastapi.Cookie ¶
- fastapi.Header ¶
- fastapi.Form ¶
- fastapi.File ¶

Here's the reference information for the request parameters.

These are the special functions that you can put in path operation function parameters or dependency functions with Annotated to get data from the request.

You can import them all directly from fastapi:

Default value if the parameter field is not set.

TYPE: Any DEFAULT: Undefined

A callable to generate the default value.

This doesn't affect Path parameters as the value is always required. The parameter is available only for compatibility.

TYPE: Union[Callable[[], Any], None] DEFAULT: _Unset

An alternative name for the parameter field.

This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar.

TYPE: Optional[str] DEFAULT: None

Priority of the alias. This affects whether an alias generator is used.

TYPE: Union[int, None] DEFAULT: _Unset

'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined.

TYPE: Union[str, None] DEFAULT: None

'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time.

TYPE: Union[str, None] DEFAULT: None

Human-readable title.

TYPE: Optional[str] DEFAULT: None

Human-readable description.

TYPE: Optional[str] DEFAULT: None

Greater than. If set, value must be greater than this. Only applicable to numbers.

TYPE: Optional[float] DEFAULT: None

Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.

TYPE: Optional[float] DEFAULT: None

Less than. If set, value must be less than this. Only applicable to numbers.

TYPE: Optional[float] DEFAULT: None

Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.

TYPE: Optional[float] DEFAULT: None

Minimum length for strings.

TYPE: Opt

*[Content truncated - see full docs]*

**Examples**:

```python
from fastapi import Body, Cookie, File, Form, Header, Path, Query
```

```text
Query(
    default=Undefined,
    *,
    default_factory=_Unset,
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    exa
...
```

```python
def Query(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Union[Callable[[], Any], None],
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatib
...
```

---

## Request class - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/request/

**Contents**:
- Request class¶
- fastapi.Request ¶
  - scope instance-attribute ¶
  - app property ¶
  - url property ¶
  - base_url property ¶
  - headers property ¶
  - query_params property ¶

You can declare a parameter in a path operation function or dependency to be of type Request and then you can access the raw request object directly, without any validation, etc.

You can import it directly from fastapi:

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an HTTPConnection instead of a Request or a WebSocket.

Bases: HTTPConnection

**Examples**:

```python
from fastapi import Request
```

```text
Request(scope, receive=empty_receive, send=empty_send)
```

```python
def __init__(self, scope: Scope, receive: Receive = empty_receive, send: Send = empty_send):
    super().__init__(scope)
    assert scope["type"] == "http"
    self._receive = receive
    self._send = send
    self._stream_consumed = False
    self._is_disconnected = False
    self._form = None
```

---

## Response class - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/response/

**Contents**:
- Response class¶
- fastapi.Response ¶
  - media_type class-attribute instance-attribute ¶
  - charset class-attribute instance-attribute ¶
  - status_code instance-attribute ¶
  - background instance-attribute ¶
  - body instance-attribute ¶
  - headers property ¶

You can declare a parameter in a path operation function or dependency to be of type Response and then you can set data for the response like headers or cookies.

You can also use it directly to create an instance of it and return it from your path operations.

You can import it directly from fastapi:

**Examples**:

```python
from fastapi import Response
```

```text
Response(
    content=None,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)
```

```python
def __init__(
    self,
    content: Any = None,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> None:
    self.status_code = status_code
    if media_type is not None:
        self.media_type = media_type
    self.background = background
    self.body = self.render(content)
    self.init_headers(headers)
```

---

## Static Files - StaticFiles - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/staticfiles/

**Contents**:
- Static Files - StaticFiles¶
- fastapi.staticfiles.StaticFiles ¶
  - directory instance-attribute ¶
  - packages instance-attribute ¶
  - all_directories instance-attribute ¶
  - html instance-attribute ¶
  - config_checked instance-attribute ¶
  - follow_symlink instance-attribute ¶

You can use the StaticFiles class to serve static files, like JavaScript, CSS, images, etc.

Read more about it in the FastAPI docs for Static Files.

You can import it directly from fastapi.staticfiles:

Given directory and packages arguments, return a list of all the directories that should be used for serving static files from.

Given the ASGI scope, return the path string to serve up, with OS specific path separators, and any '..', '.' components removed.

Returns an HTTP response, given the incoming path, method and request headers.

Perform a one-off configuration check that StaticFiles is actually pointed at a directory, so that we can raise loud errors rather than just returning 404 responses.

Given the request and response headers, return True if an HTTP "Not Modified" response could be returned instead.

**Examples**:

```python
from fastapi.staticfiles import StaticFiles
```

```text
StaticFiles(
    *,
    directory=None,
    packages=None,
    html=False,
    check_dir=True,
    follow_symlink=False
)
```

```python
def __init__(
    self,
    *,
    directory: PathLike | None = None,
    packages: list[str | tuple[str, str]] | None = None,
    html: bool = False,
    check_dir: bool = True,
    follow_symlink: bool = False,
) -> None:
    self.directory = directory
    self.packages = packages
    self.all_directories = self.get_directories(directory, packages)
    self.html = html
    self.config_checked = False
    self.follow_symlink = follow_symlink
    if check_dir and directory is not None and not os
...
```

---

## Status Codes - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/status/

**Contents**:
- Status Codes¶
- Example¶
- fastapi.status ¶
  - HTTP_100_CONTINUE module-attribute ¶
  - HTTP_101_SWITCHING_PROTOCOLS module-attribute ¶
  - HTTP_102_PROCESSING module-attribute ¶
  - HTTP_103_EARLY_HINTS module-attribute ¶
  - HTTP_200_OK module-attribute ¶

You can import the status module from fastapi:

status is provided directly by Starlette.

It contains a group of named constants (variables) with integer status codes.

It can be convenient to quickly access HTTP (and WebSocket) status codes in your app, using autocompletion for the name without having to remember the integer status codes by memory.

Read more about it in the FastAPI docs about Response Status Code.

HTTP codes See HTTP Status Code Registry: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

And RFC 9110 - https://www.rfc-editor.org/rfc/rfc9110

WebSocket codes https://www.iana.org/assignments/websocket/websocket.xml#close-code-number https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent

**Examples**:

```python
from fastapi import status
```

```python
from fastapi import FastAPI, status

app = FastAPI()


@app.get("/items/", status_code=status.HTTP_418_IM_A_TEAPOT)
def read_items():
    return [{"name": "Plumbus"}, {"name": "Portal Gun"}]
```

```text
HTTP_100_CONTINUE = 100
```

---

## Templating - Jinja2Templates - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/templating/

**Contents**:
- Templating - Jinja2Templates¶
- fastapi.templating.Jinja2Templates ¶
  - context_processors instance-attribute ¶
  - env instance-attribute ¶
  - get_template ¶
  - TemplateResponse ¶

You can use the Jinja2Templates class to render Jinja templates.

Read more about it in the FastAPI docs for Templates.

You can import it directly from fastapi.templating:

templates = Jinja2Templates("templates")

return templates.TemplateResponse("index.html", {"request": request})

**Examples**:

```python
from fastapi.templating import Jinja2Templates
```

```text
Jinja2Templates(
    directory: (
        str | PathLike[str] | Sequence[str | PathLike[str]]
    ),
    *,
    context_processors: (
        list[Callable[[Request], dict[str, Any]]] | None
    ) = None,
    **env_options: Any
)
```

```text
Jinja2Templates(
    *,
    env: Environment,
    context_processors: (
        list[Callable[[Request], dict[str, Any]]] | None
    ) = None
)
```

---

## Test Client - TestClient - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/testclient/

**Contents**:
- Test Client - TestClient¶
- fastapi.testclient.TestClient ¶
  - headers property writable ¶
  - follow_redirects instance-attribute ¶
  - max_redirects instance-attribute ¶
  - is_closed property ¶
  - trust_env property ¶
  - timeout property writable ¶

You can use the TestClient class to test FastAPI applications without creating an actual HTTP and socket connection, just communicating directly with the FastAPI code.

Read more about it in the FastAPI docs for Testing.

You can import it directly from fastapi.testclient:

HTTP headers to include when sending requests.

Check if the client being closed

Authentication class used when none is passed at the request-level.

See also Authentication.

Base URL to use when sending requests with relative URLs.

Cookie values to include when sending requests.

Query parameters to include in the URL when sending requests.

Build and return a request instance.

See also: Request instances

Alternative to httpx.request() that streams the response body instead of loading it into memory at once.

Parameters: See httpx.request.

See also: Streaming Responses

The request is sent as-is, unmodified.

Typically you'll want to build one with Client.build_request() so that any client-level configuration is merged into the request, but passing an explicit httpx.Request() is supported as well.

See also: Request instances

Close transport and proxies.

**Examples**:

```python
from fastapi.testclient import TestClient
```

```text
TestClient(
    app,
    base_url="http://testserver",
    raise_server_exceptions=True,
    root_path="",
    backend="asyncio",
    backend_options=None,
    cookies=None,
    headers=None,
    follow_redirects=True,
    client=("testclient", 50000),
)
```

```python
def __init__(
    self,
    app: ASGIApp,
    base_url: str = "http://testserver",
    raise_server_exceptions: bool = True,
    root_path: str = "",
    backend: Literal["asyncio", "trio"] = "asyncio",
    backend_options: dict[str, Any] | None = None,
    cookies: httpx._types.CookieTypes | None = None,
    headers: dict[str, str] | None = None,
    follow_redirects: bool = True,
    client: tuple[str, int] = ("testclient", 50000),
) -> None:
    self.async_backend = _AsyncBackend(backend=back
...
```

---

## UploadFile class - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/uploadfile/

**Contents**:
- UploadFile class¶
- fastapi.UploadFile ¶
    - Example¶
  - file instance-attribute ¶
  - filename instance-attribute ¶
  - size instance-attribute ¶
  - headers instance-attribute ¶
  - content_type instance-attribute ¶

You can define path operation function parameters to be of the type UploadFile to receive files from the request.

You can import it directly from fastapi:

A file uploaded in a request.

Define it as a path operation function (or dependency) parameter.

If you are using a regular def function, you can use the upload_file.file attribute to access the raw standard Python file (blocking, not async), useful and needed for non-async code.

Read more about it in the FastAPI docs for Request Files.

The standard Python file object (non-async).

The original file name.

The size of the file in bytes.

The headers of the request.

The content type of the request, from the headers.

Read some bytes from the file.

To be awaitable, compatible with async, this is run in threadpool.

The number of bytes to read from the file.

TYPE: int DEFAULT: -1

Write some bytes to the file.

You normally wouldn't use this from a file you read in a request.

To be awaitable, compatible with async, this is run in threadpool.

The bytes to write to the file.

Move to a position in the file.

Any next read or write will be done from that position.

To be awaitable, compatible with async, this is run in threadpool.

The position in bytes to seek to in the file.

To be awaitable, compatible with async, this is run in threadpool.

**Examples**:

```python
from fastapi import UploadFile
```

```text
UploadFile(file, *, size=None, filename=None, headers=None)
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

---

## WebSockets - FastAPI

**URL**: https://fastapi.tiangolo.com/reference/websockets/

**Contents**:
- WebSockets¶
- fastapi.WebSocket ¶
  - scope instance-attribute ¶
  - app property ¶
  - url property ¶
  - base_url property ¶
  - headers property ¶
  - query_params property ¶

When defining WebSockets, you normally declare a parameter of type WebSocket and with it you can read data from the client and send data to it.

It is provided directly by Starlette, but you can import it from fastapi:

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an HTTPConnection instead of a Request or a WebSocket.

Bases: HTTPConnection

Receive ASGI websocket messages, ensuring valid state transitions.

Send ASGI websocket messages, ensuring valid state transitions.

When a client disconnects, a WebSocketDisconnect exception is raised, you can catch it.

You can import it directly form fastapi:

Additional classes for handling WebSockets.

Provided directly by Starlette, but you can import it from fastapi:

**Examples**:

```python
from fastapi import WebSocket
```

```text
WebSocket(scope, receive, send)
```

```python
def __init__(self, scope: Scope, receive: Receive, send: Send) -> None:
    super().__init__(scope)
    assert scope["type"] == "websocket"
    self._receive = receive
    self._send = send
    self.client_state = WebSocketState.CONNECTING
    self.application_state = WebSocketState.CONNECTING
```

---
