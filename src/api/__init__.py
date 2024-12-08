"""App initialization"""
import logging

from contextlib import asynccontextmanager

from fastapi import FastAPI

from bot import bot

from config import settings

from .routes import r, WEBHOOK_PATH


@asynccontextmanager
async def lifespan(app: FastAPI):
    """On-startup and on-shutdown events"""
    logging.info(f"{app.title} startup")
    await bot.set_webhook(f"{settings.NGROK_URL}{WEBHOOK_PATH}")
    yield
    logging.info(f"{app.title} shutdown")
    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)

app.include_router(r)
