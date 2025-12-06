from aiogram import Bot, Dispatcher

from app.core.settings import settings
from app.bot.handler import register_handlers
from app.bot.middleware import register_middleware


dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN)


async def start_bot_polling():
    await register_handlers(dp)
    await register_middleware(dp)
    await bot.delete_webhook()
    await dp.start_polling(bot)


async def stop_bot_polling():
    await dp.stop_polling()
    await bot.session.close()
