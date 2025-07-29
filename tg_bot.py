from config import *
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from parser import get_summaries_for_channels 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

button_get_summary = KeyboardButton(text="📝 Get summarize")
keyboard = ReplyKeyboardMarkup(keyboard=[[button_get_summary]], resize_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Hello there! I am a bot for receiving summaries from Telegram channels. "
        "Use the /sum command or click on the button below to get a summary of the last 24 hours.",
        reply_markup=keyboard
    )


@dp.message(Command("sum"))
@dp.message(lambda message: message.text == "📝 Get summarize")
async def get_summary_handler(message: Message):
    tmp_msg = await message.answer("Starting sort posts...")
    
    try:
        async for channel_name, summary_text in get_summaries_for_channels():
            await user_answer(
                message.chat.id, 
                f'@{channel_name}\n\n{summary_text}'
            )
        
        await tmp_msg.delete()
    except Exception as e:
        await message.answer(f"Critical error (tg_bot): {e}")


async def user_answer(chat_id: int, summarize_text: str):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=summarize_text,
            parse_mode="html",
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Error with HTML parse mode: {e}")
        await bot.send_message(
            chat_id=chat_id,
            text=summarize_text,
            disable_web_page_preview=True
        )
