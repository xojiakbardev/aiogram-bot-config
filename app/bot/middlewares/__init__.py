from aiogram import Dispatcher
from aiogram.utils.i18n.middleware import FSMI18nMiddleware

from app.bot.localization.config import i18n

from app.core.logging import get_logger

logger = get_logger(__name__)


async def register_middleware(dp: Dispatcher):
    logger.info("Registering middlewares")
    dp.update.outer_middleware.register(FSMI18nMiddleware(i18n))
    logger.info("Middlewares registered")
