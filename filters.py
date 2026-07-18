HIGH_IMPACT_KEYWORDS = [
    # Gold
    "gold",
    "xauusd",

    # US News
    "fomc",
    "fed",
    "powell",
    "cpi",
    "ppi",
    "nfp",
    "inflation",
    "interest rate",
    "rate decision",

    # War
    "iran",
    "israel",
    "ukraine",
    "russia",
    "china",
    "taiwan",

    # Oil
    "crude",
    "oil",
    "opec",

    # Economy
    "recession",
    "tariff",
    "sanctions",

    # India
    "rbi",
    "nifty",
    "sensex"
]


def is_high_impact(title):
    title = title.lower()

    for keyword in HIGH_IMPACT_KEYWORDS:
        if keyword in title:
            return True

    return False
