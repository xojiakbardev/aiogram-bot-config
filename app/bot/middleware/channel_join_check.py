from aiogram.dispatcher.middlewares.base import BaseMiddleware


class ChannelJoinCheckMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        return await handler(event, data)
