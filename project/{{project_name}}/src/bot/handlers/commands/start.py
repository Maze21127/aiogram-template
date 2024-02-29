from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline.core import KeyboardCallback, get_keyboard
from bot.utils.messages import messages
from bot.utils.models import Commands, Actions

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> Message:
    await state.clear()
    return await message.answer(messages.commands.start, reply_markup=get_keyboard())


@router.callback_query(KeyboardCallback.filter(F.action == Actions.ACTION))
async def keyboard_callback_handler(callback_query: CallbackQuery,
                                    callback_data: KeyboardCallback) -> Message:
    return await callback_query.message.answer(str(callback_data))


@router.message(Command(Commands.HELP))
async def cmd_help(message: Message, state: FSMContext) -> Message:
    await state.clear()
    return await message.answer(messages.commands.help_message)


@router.callback_query(KeyboardCallback.filter(F.action == Actions.CANCEL))
async def cancel_handler(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    await state.clear()
    await callback_query.message.delete()
