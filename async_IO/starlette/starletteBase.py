"""
Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.

It is production-ready, and gives you the following:
    - Seriously impressive performance.
    - WebSocket support.
    - GraphQL support.
    - In-process background tasks.
    - Startup and shutdown events.
    - Test client built on requests.
    - CORS, GZip, Static Files, Streaming responses.
    - Session and Cookie support.
    - 100% test coverage.
    - 100% type annotated codebase.
    - Zero hard dependencies.

Installation
    $ pip3 install starlette
You'll also want to install an ASGI server, such as uvicorn, daphne, or hypercorn.
    $ pip3 install uvicorn

References:
    - https://www.starlette.io/
"""
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import time
import json


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def get_user(request):
    # start = time.time()
    user = [
        {'name': 'george'},
        {'name': 'may'},
        {'name': 'bob'},
    ]
    # end = time.time()
    # print(f'total: {start - end}')
    return JSONResponse(user)


async def get_sector(request):
    user = [
        {'sector': 'booking'},
        {'sector': 'shopping'},
        {'sector': 'shipping'},
    ]
    return JSONResponse(user)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/user', get_user),
    Route('/sector', get_sector),
])



