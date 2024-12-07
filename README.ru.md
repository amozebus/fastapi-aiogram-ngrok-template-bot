# Образец [Telegram](https://telegram.org/) бота (fastapi-aiogram-ngrok-template-bot)

[![Docker Image CI](https://github.com/amozebus/fastapi-aiogram-ngrok-template-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/amozebus/fastapi-aiogram-ngrok-template-bot/actions/workflows/docker-image.yml)

Образец [Telegram](https://telegram.org) бота на [aiogram](https://aiogram.dev) и [вебхуках](https://ru.wikipedia.org/wiki/Webhook) на [FastAPI](https://fastapi.tiangolo.com)

Деплой с [Docker](https://docker.com) (Compose) и [ngrok](https://ngrok.com)

## Запуск

- Создайте [Telegram](https://telegram.org) бота используя [@BotFather](https://t.me/BotFather), скопируйте API токен

- Переименуйте файл [`.env.example`](./.env.example) в [`.env`](./.env) и вставьте скопированный токен в поле `BOT_API_TOKEN`

- Создайте аккаунт [ngrok](https://ngrok.com), скопируйте токен авторизации и вставьте его в поле `NGROK_AUTHTOKEN` в файле [`.env`](./.env)

- Создайте HTTPS Edge в [панели ngrok](https://dashboard.ngrok.com/edges), скопируйте URL в секции Endpoints и вставьте в поле `NGROK_URL` в файле [`.env`](./.env)

- Скопируйте ярлык Edge без `edge=` в начале и вставьте в поле `NGROK_EDGE` в файле [`.env`](./.env)

Для Windows:

- Установите и запустите [Docker Desktop](https://docker.com)

Для Linux:

- Установите пакеты `docker`, `docker-compose` с помощью менеджера пакетов вашего дистрибутива (пример для Arch):

```sh
pacman -S docker docker-compose
```

Запустите эту команду в корне проекта:

```sh
docker compose up --build
```

- Проверьте бота в [Telegram](https://telegram.org). Используйте поиск по имени пользователя, которое вы задали [@BotFather](https://t.me/BotFather) при создании бота.