"""API requests handlers"""

from fastapi import APIRouter

from aiogram.types import Update

from bot import bot, dp

r = APIRouter()

WEBHOOK_PATH = "/webhook"


@r.post(WEBHOOK_PATH)
async def handle_webhook(update: dict):
    """Handler for updates from Telegram"""
    await dp.feed_update(bot, Update(**update))
