import importlib
import os

from fastapi import FastAPI
from starlette.responses import RedirectResponse


api_version = "Unknown"

routes = []

for file in sorted(os.listdir("api")):
    if file.endswith(".py"):
        name = file[:-3]
        api_version = name
        module = importlib.import_module(f"api.{name}")
        routes.append((name, module.router))


app = FastAPI(
    title="Time API",
    description="""
A simple API for getting the current time. You can use this for devices that don't have a clock.

- [GitHub](https://github.com/dodaucy/time-api)
- [Swagger Documentation](/)
- [Redoc Documentation](/redoc)
    """.strip(),
    version=api_version,
    docs_url="/",
    redoc_url="/redoc"
)


@app.get("/docs", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse("/")


for name, router in routes:
    app.include_router(router, prefix=f"/{name}", tags=[name])
