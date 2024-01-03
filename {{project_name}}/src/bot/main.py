import asyncio

from aiogram import Bot
from aiogram.types import BotCommand
from loguru import logger

from src.bot.handlers.commands import router as commands_router
from src.bot.loader import bot, dp


async def set_default_commands(bot_: Bot) -> None:
    await bot_.set_my_commands(
        [
            BotCommand(command="start", description="Запустить бота"),
            BotCommand(command="help", description="Получить помощь"),
        ]
    )
    logger.info("Set default commands")


async def on_startup(bot_: Bot) -> None:
    await set_default_commands(bot_)
    logger.info("Bot started")


async def on_shutdown(bot_: Bot) -> None:
    logger.info("Bot shutdown")


async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.include_router(commands_router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
