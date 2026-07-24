from filters import get_category
from impact import get_summary


def get_market_impact(category):

    category = category.lower()

    if category == "gold":
        return (
            "🟢 Gold : Bullish\n"
            "🟡 Bitcoin : Neutral\n"
            "🟡 USD : Neutral"
        )

    elif category == "oil":
        return (
            "🟢 Oil : Bullish\n"
            "🟢 Gold : Bullish\n"
            "🔴 USD : Bearish"
        )

    elif category == "war":
        return (
            "🟢 Gold : Bullish\n"
            "🔴 Stocks : Bearish\n"
            "🟢 Oil : Bullish"
        )

    elif category == "interest rates":
        return (
            "🔴 Gold : Bearish\n"
            "🟢 USD : Bullish\n"
            "🔴 Bitcoin : Bearish"
        )

    elif category == "economy":
        return (
            "🟡 Gold : Neutral\n"
            "🟡 USD : Neutral\n"
            "🟡 Bitcoin : Neutral"
        )

    else:
        return (
            "🟡 Gold : Neutral\n"
            "🟡 Bitcoin : Neutral\n"
            "🟡 USD : Neutral"
        )


def format_news(title, link):

    category = get_category(title)
    impact = get_market_impact(category)
    summary = get_summary(title)

    return f"""
🚨 <b>BREAKING MARKET ALERT</b>

📰 <b>{title}</b>

━━━━━━━━━━━━━━━━━━

📌 <b>Summary</b>

{summary}

━━━━━━━━━━━━━━━━━━

📂 <b>Category</b>

{category}

━━━━━━━━━━━━━━━━━━

📊 <b>Market Impact</b>

{impact}

━━━━━━━━━━━━━━━━━━

🔥 <b>Impact Level</b>

⭐⭐⭐⭐⭐ HIGH

━━━━━━━━━━━━━━━━━━

🎯 <b>Watchlist</b>

• XAUUSD
• EURUSD
• GBPUSD
• BTCUSD

━━━━━━━━━━━━━━━━━━

🔗 <a href="{link}">Read Full News</a>
"""