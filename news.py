import feedparser
from filters import is_high_impact

RSS_FEEDS = [
    "https://www.forexlive.com/feed/",
    "https://www.fxstreet.com/rss/news",
    "https://www.investing.com/rss/news.rss",
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=GC=F&region=US&lang=en-US"
]

def get_news():
    news = []

    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)

            for entry in feed.entries[:5]:
                if is_high_impact(entry.title):
                    news.append({
                        "title": entry.title,
                        "link": entry.link
                    })

        except Exception as e:
            print(f"Error loading {url}: {e}")

    return news