import datetime
import telethon as th
from gpt_summarize import summ
from tg_bot import user_answer
from config import *


async def main():
    async with th.TelegramClient('parser', API_ID, API_HASH) as client:
        for channel in CHANNELS:
            public_channel = await client.get_entity(channel)
            posts_list = []
            start_of_window = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=24)

            async for message in client.iter_messages(public_channel):
                if message.date < start_of_window:
                    break
                posts_list.append([message.date, message.text])

            if posts_list is not None:
                gpt_answer = summ(posts_list)
                await user_answer(f'@{channel}\n\n{gpt_answer}')
