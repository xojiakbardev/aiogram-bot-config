from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from app.bot.keyboards.reply.main import main_rkm

router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    locale = await state.get_value("locale")
    ikm = main_rkm(locale)
    await msg.answer(_("Xush kelibsiz"), reply_markup=ikm)
