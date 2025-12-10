from aiogram import Dispatcher
from app.bot.utils import lifespan
from app.bot.handlers import locale
from app.bot.handlers import start
from app.bot.handlers import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


async def register_handlers(dp: Dispatcher):
    logger.info("Registering handlers")
    dp.startup.register(lifespan.on_startup)
    dp.shutdown.register(lifespan.on_shutdown)

    dp.include_router(start.router)
    dp.include_router(locale.router)
    dp.include_router(settings.router)
    logger.info("Handlers registered")
