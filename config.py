import os
from dotenv import load_dotenv

load_dotenv()

# --- Channels to parse ---
CHANNELS = ['epichero_dev', 'moriscode', 'nsuniversity']

# --- Telegram Bot Configuration ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID") # Chat ID where the bot will send messages (User's ID)

# --- Telethon Parser Configuration ---
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHANNELS = ['baxxstudio', 'cgplugin', 'nsuniversity'] # List of channels to parse

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
DON'T USE OTHER TAGS!!!

Here is the list of posts from the channel:
'''