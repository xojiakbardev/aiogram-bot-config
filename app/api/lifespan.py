from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.bot import dp
from app.bot.handlers import register_handlers
from app.bot.middlewares import register_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await register_handlers(dp)
    await register_middleware(dp)
    yield
