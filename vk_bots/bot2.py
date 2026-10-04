import os
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
import random

load_dotenv()

TOKEN = os.getenv("VK_TOKEN")
bot = Bot(token = TOKEN)

@bot.on.message(text="Привет")
async def greetings(message:Message):
    await message.answer("Привет! Все работает правильно")

@bot.on.message(text="Пока")
async def goodbye(message:Message):
    await message.answer("Пока, хорошего дня. Приходи ещё.")

@bot.on.message(text="кубик")
async def dice(message:Message):
    kub_number = random.randint(1,6)
    await message.answer(f"Выполо число: {kub_number}")

@bot.on.message(text="Бросок 2")
async def dice(message:Message):
    kub_number1 = random.randint(1,6)
    kub_number2 = random.randint(1,6)
    kub_sum= kub_number1 + kub_number2
    await message.answer(f"Выпaло: {kub_number1} и {kub_number2} \nСумма двух бросков: {kub_sum}")

@bot.on.message()
async def all_message(message:Message):
    responce = ["да" , "нет" , "скорее всего"]
    word = random.choice(responce)
    await message.answer(word)

bot.run()