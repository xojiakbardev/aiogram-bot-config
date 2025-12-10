from fastapi import APIRouter

from app.core.settings import settings
from app.api.routers.webhook import router as webhook_router


router = APIRouter(prefix=settings.API_PREFIX)


router.include_router(webhook_router)
