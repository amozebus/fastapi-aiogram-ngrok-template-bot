"""Bot messages handlers"""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

r = Router()


@r.message(CommandStart())
async def hello(msg: Message):
    """'/start' command handler"""
    await msg.answer(f"Hello, {msg.from_user.first_name}!")
