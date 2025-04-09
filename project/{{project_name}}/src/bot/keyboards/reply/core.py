from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")
    )
    return builder.as_markup(resize_keyboard=True)


get_contact_keyboard = (
    ReplyKeyboardBuilder()
    .add(
        KeyboardButton(
            text="Отправить номер телефона 📱", request_contact=True
        )
    )
    .as_markup(resize_keyboard=True)
)
