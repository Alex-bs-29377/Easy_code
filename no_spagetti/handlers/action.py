from vkbottle.bot import Message
# from vkbottle import Bot

def start_func(bot):
    @bot.on.message(action = "chat_invite_user")
    async def invite_user(message:Message):
        user_id = message.action.member_id
        users = await message.ctx_api.users.get(user_ids = user_id)
        user = users[0]
        await message.answer(f"Добро пожаловать в чат!, {user.last_name} {user.first_name}")

    @bot.on.message(action = "chat_kick_user")
    async def kick_user(message:Message):
        user_id = message.action.member_id
        users = await message.ctx_api.users.get(user_ids = user_id)
        user = users[0]
        await message.answer(f"Пока пока,  {user.first_name}")  


    @bot.on.message(action = "chat_title_update")
    async def title_update(message:Message):
        await message.answer("Изменение название группы")

    @bot.on.message(action = "chat_pin_message")
    async def pin_message(message:Message):
        await message.answer("Сообщение закркплино")

    @bot.on.message(action = "chat_unpin_message")
    async def unpin_message(message:Message):
        await message.answer("Сообщение откреплино")




    