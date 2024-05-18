import requests
import telebot
import json
import re

token = telebot.TeleBot("6080812185:AAGv-Oa7Jnhqji0tjYHZQI6IhNV1-lB42aQ")
API = "564324da671a38b3b26360c28e3da029"


@token.message_handler(commands=['start'])
def start(message):
    token.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")


@token.message_handler(commands=['weather'])
def weather(message):
    try:
        command, city = message.text.split(maxsplit=1)
        city = city.strip().lower()

        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        dat = json.loads(res.text)
        Temps = dat["main"]["temp"]
        token.reply_to(message, f'The weather in {city.capitalize()} now: {Temps}°C')
    except Exception as e:
        token.reply_to(message, f'Error: {e}')


@token.message_handler(content_types=['text'])
def calculate(message):
    try:
        expr = re.sub(r'[^\d+\-*/().]', '', message.text)
        result = eval(expr)
        token.send_message(message.chat.id, f"Result:  {result}")
    except:
        token.send_message(message.chat.id, "Something went wrong" ".")


token.polling(none_stop=True)
