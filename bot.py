"""
Бот, который открывает мини-приложение «Ленивые квесты».
Настройки читаются из /app/config.yaml (монтируется из ConfigMap).
Для локального запуска можно указать другой путь: CONFIG_PATH=./config.yaml python bot.py
"""
import asyncio
import logging
import os

import yaml
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

CONFIG_PATH = os.environ.get("CONFIG_PATH", "/app/config.yaml")
with open(CONFIG_PATH, encoding="utf-8") as f:
    config = yaml.safe_load(f)

TOKEN = config["bot"]["token"]
WEBAPP_URL = config["webapp"]["url"]

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🦥 Открыть квесты", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])
    await message.answer(
        "Привет! Здесь твои ежедневные дела превращаются в квесты.\n"
        "Выполняй, получай XP и качай ленивца 🦥",
        reply_markup=kb,
    )


async def main():
    bot = Bot(TOKEN)
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Квесты", web_app=WebAppInfo(url=WEBAPP_URL))
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, handle_signals=True)


if __name__ == "__main__":
    asyncio.run(main())
