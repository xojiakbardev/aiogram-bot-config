import asyncio
from app.bot import dp, bot
from app.core.settings import settings
from app.core.logging import setup_logging
from app.bot.handlers import register_handlers
from app.bot.middlewares import register_middleware


async def start_bot_polling():
    await register_handlers(dp)
    await register_middleware(dp)
    await bot.delete_webhook()
    await dp.start_polling(bot)


async def set_webhook():
    if not settings.SET_WEBHOOK:
        return
    await bot.set_webhook(
        url=settings.WEBHOOK_URL,
        drop_pending_updates=True
    )


if __name__ == "__main__":
    setup_logging()
    asyncio.run(start_bot_polling())
