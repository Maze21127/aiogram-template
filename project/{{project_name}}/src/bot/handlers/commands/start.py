from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from src.bot.keyboards.inline.core import KeyboardCallback, get_keyboard
from src.bot.utils.messages import messages

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> Message:
    return await message.answer(messages.commands.start, reply_markup=get_keyboard())


@router.callback_query(KeyboardCallback.filter(F.id > 0))
async def keyboard_callback_handler(callback_query: CallbackQuery,
                                    callback_data: KeyboardCallback) -> Message:
    return await callback_query.message.answer(str(callback_data))
