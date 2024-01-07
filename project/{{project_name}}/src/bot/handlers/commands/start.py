from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.bot.keyboards.inline.core import KeyboardCallback, get_keyboard
from src.bot.utils.messages import messages

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> Message:
    await state.clear()
    return await message.answer(messages.commands.start, reply_markup=get_keyboard())


@router.callback_query(KeyboardCallback.filter(F.id > 0))
async def keyboard_callback_handler(callback_query: CallbackQuery,
                                    callback_data: KeyboardCallback) -> Message:
    return await callback_query.message.answer(str(callback_data))
