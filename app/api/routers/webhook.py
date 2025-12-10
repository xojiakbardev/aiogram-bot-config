from fastapi import APIRouter, Request
from app.core.settings import settings
from app.bot import dp, bot

router = APIRouter(tags=["Webhook"])


@router.post(settings.WEBHOOK_STR)
async def webhook_handler(request: Request):
    updated_data = await request.json()
    await dp.feed_webhook_update(bot, updated_data)
