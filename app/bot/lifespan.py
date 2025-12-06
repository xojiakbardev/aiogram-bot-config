from app.core.logging import get_logger

logger = get_logger(__name__)


async def on_startup():
    logger.info("Bot is starting up ✅")


async def on_shutdown():
    logger.info("Bot is shutting down ✅")
