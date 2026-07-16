import feedparser

RSS_FEEDS = [
    "https://www.forexlive.com/feed/"
]

def get_news():
    news = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            news.append({
                "title": entry.title,
                "link": entry.link
            })

    return news
