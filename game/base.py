import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

token = Bot(token="6080812185:AAGv-Oa7Jnhqji0tjYHZQI6IhNV1-lB42aQ")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.message):
    await message.answer("hello")


@dp.message()
async def echo(message: types.message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(token)


asyncio.run(main())
