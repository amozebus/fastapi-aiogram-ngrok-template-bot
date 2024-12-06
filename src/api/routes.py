from fastapi import APIRouter

from aiogram.types import Update

from bot import bot, dp

r = APIRouter()

webhook_path = "/webhook"

@r.post(webhook_path)
async def handle_webhook(update: dict):
    await dp.feed_update(bot, Update(**update))