from fastapi import FastAPI

from app.api.routers import router
from app.api.lifespan import lifespan


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan
    )
    app.include_router(router)
    return app
