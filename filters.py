HIGH_IMPACT_KEYWORDS = {

    "gold": "Gold",
    "xauusd": "Gold",

    "crude": "Oil",
    "oil": "Oil",
    "opec": "Oil",
    "brent": "Oil",
    "wti": "Oil",

    "bitcoin": "Crypto",
    "btc": "Crypto",
    "ethereum": "Crypto",
    "eth": "Crypto",
    "bnb": "Crypto",

    "fed": "USD",
    "fomc": "USD",
    "powell": "USD",
    "cpi": "USD",
    "ppi": "USD",
    "nfp": "USD",
    "pce": "USD",
    "inflation": "USD",
    "interest rate": "USD",
    "rate decision": "USD",

    "ecb": "EUR",
    "lagarde": "EUR",
    "main refinancing rate": "EUR",

    "boe": "GBP",
    "bank of england": "GBP",

    "boj": "JPY",

    "boc": "CAD",

    "iran": "War",
    "israel": "War",
    "ukraine": "War",
    "russia": "War",
    "china": "War",
    "taiwan": "War",
    "trump": "Politics",
    "tariff": "Politics",
    "sanctions": "Politics",

    "recession": "Economy",

    "rbi": "India",
    "nifty": "India",
    "sensex": "India"
}


def is_high_impact(title):

    title = title.lower()

    for keyword in HIGH_IMPACT_KEYWORDS:

        if keyword in title:

            return True

    return False


def get_category(title):

    title = title.lower()

    for keyword, category in HIGH_IMPACT_KEYWORDS.items():

        if keyword in title:

            return category

    return "Other"