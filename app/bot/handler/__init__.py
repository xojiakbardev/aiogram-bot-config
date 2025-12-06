from aiogram import Dispatcher
from app.bot.lifespan import on_startup, on_shutdown


async def register_handlers(dp: Dispatcher):
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
