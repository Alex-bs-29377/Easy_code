from vkbottle.bot import Message, Bot
from vkbottle import BaseStateGroup

class Anketa(BaseStateGroup):
    NAME = "name"
    AGE = "age"
    EMAIL = "email"
    CITY = "city"
    HOBBI = "hobbi"

def start_funk(bot: Bot):

    @bot.on.message(text=["Анкета", "анкета"])
    async def start(message: Message):
        await bot.state_dispenser.set(message.peer_id, Anketa.NAME)
        await message.answer("Как тебя зовут?")

    @bot.on.message(state=Anketa.NAME)
    async def name(message: Message):
        name = message.text
        await bot.state_dispenser.set(message.peer_id, Anketa.AGE, name=name)
        await message.answer("Введите возраст")

    @bot.on.message(state=Anketa.AGE)
    async def age(message: Message):
        age = message.text
        data = message.state_peer.payload
        await bot.state_dispenser.set(message.peer_id, Anketa.EMAIL, name=data["name"], age=age)
        await message.answer("Введите почту")

    @bot.on.message(state=Anketa.EMAIL)
    async def email(message: Message):
        email = message.text
        data = message.state_peer.payload
        await bot.state_dispenser.set(message.peer_id, Anketa.CITY, name=data["name"], age=data["age"], email=email)
        await message.answer("Введите город")

    @bot.on.message(state=Anketa.CITY)
    async def city(message: Message):
        city = message.text
        data = message.state_peer.payload
        await bot.state_dispenser.set(message.peer_id, Anketa.HOBBI, name=data["name"], age=data["age"], email=data["email"], city=city)
        await message.answer("Введите своё хобби") 

    @bot.on.message(state=Anketa.HOBBI)
    async def hobbi(message: Message):
        hobbi = message.text
        data = message.state_peer.payload
        await message.answer(f"Анкета заполнена!\n Имя: {data['name']}\nВозраст: {data['age']}\nПочта: {data['email']}\nГород: {data['city']}\nХобби: {hobbi}")
        await bot.state_dispenser.delete(message.peer_id)