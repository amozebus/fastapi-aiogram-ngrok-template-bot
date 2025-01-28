<div align="center">

English | <a href="./README.ru.md">Русский</a>

# <a href="https://telegram.org">Telegram</a>-bot template (fastapi-aiogram-ngrok-template-bot)

<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="code style: black" /></a>

Template for <a href="https://telegram.org">Telegram</a>-bot that using <a href="https://en.wikipedia.org/wiki/Webhook">webhook</a>. Written in <a href="https://python.org">Python</a> with <a href="https://aiogram.dev">aiogram</a> and <a href="https://fastapi.tiangolo.com">FastAPI</a>

<a href="https://en.wikipedia.org/wiki/Tunneling_protocol">Tunneling</a> webhook to the Web with <a href="https://ngrok.com">ngrok</a>.

</div>

## How to launch (Docker Compose)

1. Create a [Telegram](https://telegram.org) bot using [@BotFather](https://t.me/BotFather), copy API token

2. Rename the [`.env.example`](./.env.example) file to [`.env`](./.env) and fill `BOT_API_TOKEN` field with copied token

3. Create an account on [ngrok](https://ngrok.com), copy your authentication token and paste it to `NGROK_AUTHTOKEN` field in [`.env`](./.env)

4. Create an HTTPS Edge on [ngrok dashboard](https://dashboard.ngrok.com/edges), copy URL in Endpoints section and paste it to `NGROK_URL` field in [`.env`](./.env) file

5. Copy edge label without `edge=` in beginning and paste it to `NGROK_EDGE` field in [`.env`](./.env) file

For Windows:

6. Install and start [Docker Desktop](https://docker.com)

For Linux:

6. Install `docker`, `docker-compose` packages with package manager of your distro (example for Arch):

```sh
pacman -S docker docker-compose
```

7. Run this command in root of project:

```sh
docker compose up --build
```

8. Check the bot in [Telegram](https://telegram.org). Search it by the username which you gave to [@BotFather](https://t.me/BotFather)
