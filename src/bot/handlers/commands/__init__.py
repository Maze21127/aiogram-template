from aiogram import Router

from src.bot.handlers.commands.start import router as start_router

router = Router()
router.include_router(start_router)
