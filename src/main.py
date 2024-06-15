import asyncio
import logging
import sys
from os import getenv
import sqlite3

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    '''
    This handler receives messages with '/start' command
    '''
    user_name = message.from_user.full_name
    await message.answer(f'''
Привет, {user_name}!
Я создан, чтобы помочь вам вести учет личных расходов.
Как я могу вам помочь ?
''')

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
