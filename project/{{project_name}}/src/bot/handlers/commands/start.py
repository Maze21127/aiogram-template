from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.utils.messages import get_messages

router = Router()
messages = get_messages()


@router.message(CommandStart())
async def cmd_start(message: Message) -> Message:
    return await message.answer(messages.commands.start)
