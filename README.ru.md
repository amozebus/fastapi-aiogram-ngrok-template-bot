<div align="center">

<a href="./README.md">English</a> | Русский

# Шаблон <a href="https://telegram.org">Telegram</a>-бота (fastapi-aiogram-ngrok-template-bot)

<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="code style: black" /></a>

Шаблон <a href="https://telegram.org">Telegram</a>-бота, использующего <a href="https://ru.wikipedia.org/wiki/Webhook">вебхук</a>. Написан на <a href="https://python.org">Python</a> с помощью <a href="https://aiogram.dev">aiogram</a> на <a href="https://fastapi.tiangolo.com">FastAPI</a>

<a href="https://ru.wikipedia.org/wiki/%D0%A2%D1%83%D0%BD%D0%BD%D0%B5%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_(%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B5_%D1%81%D0%B5%D1%82%D0%B8)">Туннелирование</a> вебхука через <a href="https://ngrok.com">ngrok</a>.

</div>

## Запуск (Docker Compose)

1. Создайте [Telegram](https://telegram.org) бота используя [@BotFather](https://t.me/BotFather), скопируйте API токен

2. Переименуйте файл [`.env.example`](./.env.example) в [`.env`](./.env) и вставьте скопированный токен в поле `BOT_API_TOKEN`

3. Создайте аккаунт [ngrok](https://ngrok.com), скопируйте токен авторизации и вставьте его в поле `NGROK_AUTHTOKEN` в файле [`.env`](./.env)

4. Создайте HTTPS Edge в [панели ngrok](https://dashboard.ngrok.com/edges), скопируйте URL в секции Endpoints и вставьте в поле `NGROK_URL` в файле [`.env`](./.env)

5. Скопируйте ярлык Edge без `edge=` в начале и вставьте в поле `NGROK_EDGE` в файле [`.env`](./.env)

Для Windows:

6. Установите и запустите [Docker Desktop](https://docker.com)

Для Linux:

6. Установите пакеты `docker`, `docker-compose` с помощью менеджера пакетов вашего дистрибутива (пример для Arch):

```sh
pacman -S docker docker-compose
```

7. Запустите эту команду в корне проекта:

```sh
docker compose up --build
```

8. Проверьте бота в [Telegram](https://telegram.org). Используйте поиск по имени пользователя, которое вы задали [@BotFather](https://t.me/BotFather) при создании бота.
