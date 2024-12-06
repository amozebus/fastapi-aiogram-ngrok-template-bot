# [Telegram](https://telegram.org) Bot Template (fastapi-aiogram-ngrok-template-bot)

Template for [Telegram](https://telegram.org) bot using [aiogram](https://aiogram.dev) and [webhooks](https://en.wikipedia.org/wiki/Webhook) with [FastAPI](https://fastapi.tiangolo.com)

Deploy with [Docker](https://docker.com) (Compose) and [ngrok](https://ngrok.com)

[Русская версия README.md](./README.ru.md)

## How to launch 

- Create a [Telegram](https://telegram.org) bot using [@BotFather](https://t.me/BotFather), copy API token

- Rename the [`.env.example`](./.env.example) file to [`.env`](./.env) and fill `BOT_API_TOKEN` field with copied token

- Create an account on [ngrok](https://ngrok.com), copy your authentication token and paste it to `NGROK_AUTHTOKEN` field in [`.env`](./.env)

- Create an HTTPS Edge on [ngrok dashboard](https://dashboard.ngrok.com/edges), copy URL in Endpoints section and paste it to `NGROK_URL` field in [`.env`](./.env) file

- Copy edge label without `edge=` in beginning and paste it to `NGROK_EDGE` field in [`.env`](./.env) file

For Windows:

- Install and start [Docker Desktop](https://docker.com)

For Linux:

- Install `docker`, `docker-compose` packages with package manager of your distro (example for Arch):

```sh
pacman -S docker docker-compose
```

Run this command in root of project:

```sh
docker compose up --build
```

- Check the bot in [Telegram](https://telegram.org). Search it by the username which you gave to [@BotFather](https://t.me/BotFather)