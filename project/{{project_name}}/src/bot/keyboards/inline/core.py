from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.utils.models import Actions


class KeyboardCallback(CallbackData, prefix="keyboard"):
    action: Actions


cancel_cb = KeyboardCallback(action=Actions.CANCEL).pack()
cancel_button = InlineKeyboardButton(
    text="Отмена ❌",
    callback_data=cancel_cb,
)
cancel_keyboard = InlineKeyboardBuilder().row(cancel_button).as_markup()


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


def add_cancel_button(builder: InlineKeyboardBuilder) -> None:
    builder.row(cancel_button)
