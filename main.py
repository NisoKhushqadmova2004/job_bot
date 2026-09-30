from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from connection import create_table
import os
import asyncio
from states import router as state_router
from callbacks import router as callback_router
from service import *
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboards import *



load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = Bot(token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    users = message.from_user
    user = await get_user(users.id)
    
    if user:
        await message.answer(f"Hello @{message.from_user.username}", reply_markup= category_batton())
    else:
       await  save_user(users.id, users.username, users.full_name)
       await message.answer(f"Hello @{message.from_user.username}", reply_markup= category_batton())



async def main():
    print("Start Bot")
    dp.include_router(state_router)
    dp.include_router(callback_router)
    await create_table()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
