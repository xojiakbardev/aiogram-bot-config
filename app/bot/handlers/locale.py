from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _
from aiogram.types import Message, CallbackQuery
from aiogram.filters.callback_data import CallbackQueryFilter

from app.bot.keyboards.reply.main import main_rkm
from app.bot.keyboards.inline.language import language_ikm, LocaleCallback

router = Router()


@router.message(Command("change_language"))
async def handle_locale_message(msg: Message):
    ikm = language_ikm([
        {"locale": "uz", "label": "🇺🇿 O'zbek"},
        {"locale": "en", "label": "🇬🇧 English"},
    ])
    await msg.answer(_("Tilni tanlang"), reply_markup=ikm)


@router.callback_query(CallbackQueryFilter(callback_data=LocaleCallback))
async def handle_locale_callback(
        query: CallbackQuery,
        callback_data: LocaleCallback,
        state: FSMContext
):
    locale = callback_data.code
    await state.update_data(locale=locale)
    await query.message.delete()
    await query.answer(_("{} tiliga o'zgartirildi".format(locale.upper()), locale=locale))
    await query.message.answer(
        _("Sozlamalar yangilandi", locale=locale),
        reply_markup=main_rkm(locale)
    )
