from redis.asyncio import Redis
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.bot import DefaultBotProperties

from app.core.settings import settings


dp = Dispatcher(
    storage=RedisStorage(
        Redis.from_url(settings.BOT_REDIS_DSN)
    )
)

bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode="HTML"
    )
)
