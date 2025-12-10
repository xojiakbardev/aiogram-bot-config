from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.logging import get_logger

scheduler = AsyncIOScheduler()

logger = get_logger(__name__)


def start_scheduler():
    scheduler.start()