import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()

TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TELEGRAM_TOKEN)  # объект экземпляра класса bot ботов может быть несколько
dp = Dispatcher()  # объект экземпляра класса dispatcher основной роутер

@dp.message(CommandStart())  # Обработчик команда start
async def cmd_start(message: Message):
    await message.answer('Hello!')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')