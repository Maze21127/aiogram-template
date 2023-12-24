from aiogram import Bot, Dispatcher

from src.config import get_settings

settings = get_settings()
bot = Bot(token=settings.bot.TOKEN.get_secret_value())

dp = Dispatcher()
