import asyncio
import logging
from tg_bot import dp, bot

logging.basicConfig(level=logging.INFO)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())