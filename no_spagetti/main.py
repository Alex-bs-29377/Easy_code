import ssl
import aiohttp
import asyncio

from vkbottle import Bot, API, AiohttpClient
from handlers import start, echo_bot, task1, task2, task3, task4

import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("VK_TOKEN")


async def main():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    connector = aiohttp.TCPConnector(ssl=ssl_context)
    http_client = AiohttpClient(connector=connector)

    api = API(token=TOKEN, http_client=http_client)
    bot = Bot(api=api)

    await task4.start_func(bot)
    await task2.start_func(bot)
    await task3.start_func(bot)
    await task1.start_func(bot)
    await start.start_func(bot)
    await echo_bot.echo_password(bot)
    
    await bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
