def get_summary(title):

    title = title.lower()

    # CPI
    if "cpi" in title:
        return (
            "US inflation data can create strong volatility in Gold and the US Dollar.\n\n"
            "If CPI comes higher than expected, USD may strengthen while Gold can face selling pressure."
        )

    # NFP
    elif "nfp" in title:
        return (
            "Non-Farm Payrolls is one of the biggest market-moving events.\n\n"
            "Expect high volatility in Gold, USD and major Forex pairs."
        )

    # FOMC
    elif "fomc" in title or "fed" in title:
        return (
            "Federal Reserve decisions directly affect interest rates.\n\n"
            "Markets usually react sharply in Gold and the US Dollar."
        )

    # Powell
    elif "powell" in title:
        return (
            "Jerome Powell's comments can rapidly change market sentiment.\n\n"
            "Watch Gold and USD closely."
        )

    # Gold
    elif "gold" in title or "xauusd" in title:
        return (
            "Gold is attracting market attention.\n\n"
            "Watch for safe-haven demand and key support/resistance levels."
        )

    # Bitcoin
    elif "bitcoin" in title or "btc" in title:
        return (
            "Bitcoin sentiment is changing.\n\n"
            "Crypto volatility may increase."
        )

    # Oil
    elif "oil" in title or "crude" in title:
        return (
            "Oil prices are moving.\n\n"
            "Higher oil prices can increase inflation expectations and indirectly support Gold."
        )

    # War
    elif (
        "iran" in title
        or "israel" in title
        or "ukraine" in title
        or "russia" in title
    ):
        return (
            "Geopolitical tensions are increasing.\n\n"
            "Safe-haven assets like Gold often benefit during uncertain periods."
        )

    # Default
    return (
        "This news may affect market sentiment.\n\n"
        "Watch price action before taking any trade."
    )