from fastapi import APIRouter

from app.core.settings import settings
from ..webhook import router as webhook_router


router = APIRouter(prefix=settings.API_V1_STR)


