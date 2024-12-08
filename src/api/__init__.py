"""App initialization"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from bot import bot

from config import settings

from .routes import r, WEBHOOK_PATH


@asynccontextmanager
async def lifespan():
    """On-startup and on-shutdown events"""
    await bot.set_webhook(f"{settings.NGROK_URL}{WEBHOOK_PATH}")
    yield
    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)

app.include_router(r)
