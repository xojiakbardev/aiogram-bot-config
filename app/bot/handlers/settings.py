from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("settings"))
async def handle_settings_message(msg: Message):
    await msg.answer("S")
