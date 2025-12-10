import asyncio
import uvicorn

from app.bot import bot
from app.bot.main import set_webhook
from app.core.settings import settings
from app.core.logging import setup_logging


async def main():
    setup_logging()
    await set_webhook()
    uvicorn.run(
        "app.api.main:create_app",
        host="0.0.0.0",
        port=settings.API_PORT,
        reload=True if settings.DEBUG else False,
        factory=True if settings.DEBUG else False,
    )


if __name__ == "__main__":
    asyncio.run(main())
