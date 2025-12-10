from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def main_rkm(locale: str) :
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_("Asosiy menu", locale=locale)))
    rkb.add(KeyboardButton(text=_("Statistika", locale=locale)))
    rkb.row(KeyboardButton(text=_("Sozlamalar", locale=locale)))
    return rkb.as_markup(is_persistent=True)
