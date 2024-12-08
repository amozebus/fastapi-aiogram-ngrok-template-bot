"""Bot initialization"""

from aiogram import Bot, Dispatcher

from config import settings

from .handlers import r as router

bot = Bot(token=settings.BOT_API_TOKEN)

dp = Dispatcher()
dp.include_router(router)
