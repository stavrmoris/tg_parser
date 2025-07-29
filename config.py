import os
from dotenv import load_dotenv

load_dotenv()

# --- Channels to parse ---
CHANNELS = [-1001237513492, 'baxxstudio', 'cgplugin', 'nsuniversity']

# --- Telegram Bot Configuration ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
# CHAT_ID больше не нужен, бот будет отвечать динамически

# --- Telethon Parser Configuration ---
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.path.join(r"D:\Victoria\0_Nigredo\tg_parser", "parser")

# --- Gemini API ---
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

# --- Prompt for GPT ---
PROMPT = r'''
You receive a list of posts as input. Your task is to provide a summary of the posts in
html format for an aiogram bot. The language of the summary must match the language of the messages. The response should only
contain the summary, formatted as shown below. Do not add anything extra!

HTML usage rules:
 <b>Bold</b>
 <i>Italic</i>
 <code>code</code>
 <s>strikethrough</s>
 <u>underline</u>
 <pre language="c++">code block</pre>
 <a href="smth.ru">Link</a>
DON'T USE OTHER TAGS (like <br> or <p> or some other)!!!

Here is the list of posts from the channel:
'''
