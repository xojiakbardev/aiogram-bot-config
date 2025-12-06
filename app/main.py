import asyncio

from app.core.logging import setup_logging
from app.bot import start_bot_polling, stop_bot_polling


async def main():
    try:
        setup_logging()
        await start_bot_polling()
    except (KeyboardInterrupt, SystemExit):
        await stop_bot_polling()


if __name__ == "__main__":
    asyncio.run(main())
