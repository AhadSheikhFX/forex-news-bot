from telegram import Bot
import asyncio
import os
from dotenv import load_dotenv
from news import get_news
from database import load_sent_news, save_sent_news
from formatter import format_news

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1003964640130

bot = Bot(token=BOT_TOKEN)

sent_news = load_sent_news()
BOT_FIRST_START = len(sent_news) == 0

async def send_news():
    news = get_news()

    for item in news:
        if item["link"] not in sent_news:

            message = format_news(
                item["title"],
                item["link"]
            )

            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=message,
                parse_mode="HTML",
                disable_web_page_preview=False
            )

            sent_news.add(item["link"])
            save_sent_news(sent_news)


async def main():
    me = await bot.get_me()
    print(f"Bot Connected Successfully: @{me.username}")

    while True:
        try:
            await send_news()
        except Exception as e:
            print(e)

        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())