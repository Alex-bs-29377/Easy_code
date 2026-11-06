from vkbottle import Bot
from vkbottle.bot import Message

import os
from dotenv import load_dotenv

import random

load_dotenv()
TOKEN = os.getenv("VK_TOKEN")

# Создайте VK-бота, который знакомится с пользователем и предлагает сыграть в игру «Орёл или решка». 
# При первом сообщении бот должен получить ID пользователя, используя message.from_id, 
# обратиться к VK API, получить имя пользователя и поприветствовать его по имени. 
# После приветствия бот предлагает сыграть в монетку. 
# Если пользователь пишет «играть», бот предлагает выбрать «орёл» или «решка». 
# Затем программа случайным образом определяет результат с помощью random.choice(), сравнивает его с выбором пользователя и сообщает, угадал ли игрок. 
# После завершения игры бот должен предложить сыграть ещё раз.


async def start_func(bot:Bot):
    @bot.on.message(text = ["привет", "старт", "start"])
    async def game(message:Message):
        user_id = message.from_id
        user = await message.ctx_api.users.get(user_ids = user_id)
        first_name = user[0].first_name
        await message.answer(f"Привет {first_name}\nХочешь сыграть в игру «Орёл или решка»?\nНапиши «играть», чтобы начать")
        return

    @bot.on.message(text="играть")
    async def start_game(message: Message):
        await message.answer("Отлично! Выбери: «орёл» или «решка».")


    @bot.on.message(text=["орёл", "орел", "решка"])
    async def guess(message: Message):
        user_id = message.from_id
        users = await message.ctx_api.users.get(user_ids=user_id)
        first_name = users[0].first_name

        text = message.text.lower()

        if text in ("орёл", "орел"):
            player_choice = "орёл"
        else:
            player_choice = "решка"

        result = random.choice(["орёл", "решка"])

        if player_choice == result:
            await message.answer(f"Выпал «{result}» — ты угадал!")
        else:
            await message.answer(f"Выпал «{result}», а ты выбрал «{player_choice}». Не угадал.")

        await message.answer("Хочешь ещё? Напиши «играть»!")