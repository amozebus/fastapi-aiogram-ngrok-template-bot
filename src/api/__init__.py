from fastapi import FastAPI

from bot import bot

from config import settings

from .routes import r, webhook_path

async def lifespan(app: FastAPI):
    await bot.set_webhook(f"{settings.NGROK_URL}{webhook_path}")
    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)

app.include_router(r)