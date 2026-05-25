from data_fetcher import get_intraday

def analyze_market(symbol):
    data = get_intraday(symbol)

    if "Time Series (5min)" not in data:
        return {"error": "API limit or invalid response"}

    latest = list(data["Time Series (5min)"].values())[0]
    close_price = float(latest["4. close"])

    if close_price > 0:
        return {
            "symbol": symbol,
            "signal": "BULLISH",
            "price": close_price
        }

    return {
        "symbol": symbol,
        "signal": "NEUTRAL"
    }
