from aiogram import Bot, Dispatcher

from .handlers import r as router 

from config import settings

bot = Bot(token=settings.BOT_API_TOKEN)

dp = Dispatcher()
dp.include_router(router)