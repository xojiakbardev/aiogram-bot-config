from aiogram.utils.i18n import I18n

from app.core.settings import settings


i18n = I18n(
    path="app/bot/localization/locales",
    default_locale=settings.DEFAULT_LOCALE
)
