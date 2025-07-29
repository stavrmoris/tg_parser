import datetime
import telethon as th
from gpt_summarize import summ
from config import *


async def get_summaries_for_channels():
    try:
        async with th.TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
            for channel in CHANNELS:
                try:
                    public_channel = await client.get_entity(channel)
                    posts_list = []
                    start_of_window = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=24)
                    
                    async for message in client.iter_messages(public_channel, limit=200):
                        if message.date < start_of_window:
                            break
                        if message.text:
                            posts_list.append([message.date, message.text])

                    if posts_list:
                        gpt_answer = summ(posts_list)
                        yield (channel, gpt_answer)
                    else:
                        yield (channel, "No posts past 24 hours.")

                except Exception as e:
                    yield (channel, f"Can't view channel. Error: {e}")
    except Exception as e:
        print(f"Critical error (parser): {e}")
