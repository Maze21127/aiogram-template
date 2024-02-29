from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.utils.models import Actions

class KeyboardCallback(CallbackData, prefix="keyboard"):
    action: Actions


def get_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )
    builder.row(InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )
    builder.row(InlineKeyboardButton(
        text="Callback Data Button",
        callback_data=KeyboardCallback(action=Actions.ACTION).pack()
    ))
    return builder.as_markup()
