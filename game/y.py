import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

Bot = Bot(token='6080812185:AAGv-Oa7Jnhqji0tjYHZQI6IhNV1-lB42aQ')

dp = Dispatcher()


@dp.message(CommandStart())
async def star(messga: types.message):
    await messga.answer('Hello')


@dp.message()
async def egho(message: types.message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(Bot)


asyncio.run(main())
