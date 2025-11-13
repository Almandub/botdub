import os
import asyncio
from aiogram import Bot, Dispatcher, types
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
client = OpenAI(api_key=OPENAI_API_KEY)

@dp.message()
async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.reply("Привет я Ботдуб твой умный бот помощник")
    else:
        await echo(message)

async def echo(message: types.Message):
    text = message.text
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты Ботдуб, дружелюбный бот помощник."},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content.strip()
        await message.reply(reply)
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.reply("Ошибка при обращении к Ботдубу")

if __name__ == "__main__":
    print("Ботдуб запущен")
    asyncio.run(dp.start_polling(bot))