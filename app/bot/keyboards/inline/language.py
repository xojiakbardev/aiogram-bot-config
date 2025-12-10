from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _
from aiogram.filters.callback_data import CallbackData


from typing import TypedDict, List


class LocaleItem(TypedDict):
    locale: str
    label: str


class LocaleCallback(CallbackData, prefix="locale"):
    code: str


def language_ikm(locale_map: List[LocaleItem]):
    ikb = InlineKeyboardBuilder()
    for item in locale_map:
        ikb.add(InlineKeyboardButton(
            text=item["label"],
            callback_data=LocaleCallback(code=item["locale"]).pack())
        )
    return ikb.as_markup()
