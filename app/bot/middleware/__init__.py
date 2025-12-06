from aiogram import Dispatcher

from app.bot.middleware.channel_join_check import ChannelJoinCheckMiddleware


async def register_middleware(dp: Dispatcher):
    dp.update.outer_middleware.register(ChannelJoinCheckMiddleware())
