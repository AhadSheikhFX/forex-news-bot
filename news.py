import feedparser
from filters import is_high_impact
from datetime import datetime, timezone

RSS_FEEDS = [

    # Fast Forex
    "https://www.forexlive.com/feed/",
    "https://www.fxstreet.com/rss/news",

    # Market News
    "https://www.investing.com/rss/news.rss",

    # Gold
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=GC=F&region=US&lang=en-US",
]

# Sirf 30 minute purani news bhejo
MAX_NEWS_AGE = 30


def get_news():

    all_news = []
    seen = set()

    now = datetime.now(timezone.utc)

    for url in RSS_FEEDS:

        try:

            feed = feedparser.parse(url)

            if not feed.entries:
                continue

            for entry in feed.entries:

                title = entry.title.strip()
                link = entry.link

                if link in seen:
                    continue

                if not is_high_impact(title):
                    continue

                # Publish Time Check
                if hasattr(entry, "published_parsed") and entry.published_parsed:

                    published = datetime(
                        *entry.published_parsed[:6],
                        tzinfo=timezone.utc
                    )

                    age = (now - published).total_seconds() / 60

                    if age > MAX_NEWS_AGE:
                        continue

                seen.add(link)

                all_news.append({
                    "title": title,
                    "link": link
                })

        except Exception as e:
            print(f"{url} -> {e}")

    return all_news