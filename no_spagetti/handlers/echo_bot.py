from vkbottle import Bot
from vkbottle.bot import Message

async def echo_password(bot:Bot):
    @bot.on.message()
    async def echo_handler(message:Message):
        text = message.text.lower()
        if "секрет" in text or "пароль" in text:
            await message.answer(f"Я никому не скажу! 🤫") 
        else:
            await message.answer(text)
