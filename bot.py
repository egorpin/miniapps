import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command

# Загрузка переменных окружения из файла .env (если он есть)
load_dotenv()

# Получение токена бота из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("Ошибка: Не найден BOT_TOKEN в файле .env или переменных окружения.")
    exit()

# Включаем логирование для отслеживания работы бота
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- Обработка запуска Mini App ---
@dp.message(Command("start"))
async def start(message: types.Message, bot: Bot):
    web_app_info = types.WebAppInfo(url="http://127.0.0.1:5000")
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Открыть магазин", web_app=web_app_info)
    await message.answer(
        "Добро пожаловать в наш интернет-магазин!",
        reply_markup=keyboard.as_markup(),
    )


# --- Обработка данных, отправленных из Mini App (пример) ---
@dp.message(types.WebAppData)
#@dp.message(F.content_type)
async def web_app_data(message: types.Message, bot: Bot):
    received_data = message.web_app_data.data
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    username = message.from_user.username
    chat_id = message.chat.id

    logging.info(f"Получены данные от пользователя {user_id} ({username}): {received_data}")

    await bot.send_message(
        chat_id,
        f"Спасибо, {first_name}! Мы получили ваши данные:\n```\n{received_data}\n```",
        parse_mode="Markdown",
    )

# --- Запуск бота ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
