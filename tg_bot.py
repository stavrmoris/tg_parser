from aiogram import Bot
from config import *

bot = Bot(token=BOT_TOKEN)


async def user_answer(summarize_text):
    try:
        await bot.send_message(
            chat_id='1075465296',
            text=summarize_text,
            parse_mode="html"
        )
    except Exception as e:
        print(f"Error with MarkdownV2: {e}")
        await bot.send_message(
            chat_id='1075465296',
            text=summarize_text
        )