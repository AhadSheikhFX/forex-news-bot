import json
import os

DB_FILE = "sent_news.json"


def load_sent_news():
    if not os.path.exists(DB_FILE):
        return set()

    with open(DB_FILE, "r") as f:
        try:
            return set(json.load(f))
        except:
            return set()


def save_sent_news(news_set):
    with open(DB_FILE, "w") as f:
        json.dump(list(news_set), f)