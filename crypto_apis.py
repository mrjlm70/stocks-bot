import requests


url = "https://api.wallex.ir/v1/markets"
response = requests.get(url)

symbols_wanted = ["USDTTMN", "XAUTUSDT", "BTCUSDT", "TONUSDT"]


def get_crypto():
    if response.status_code == 200:
        data = response.json()

        results = data["result"]["symbols"]

        filtered = [results[item] for item in results if item in symbols_wanted]
        msg = ""
        for symbol in filtered:
            emoji = "🟢📈" if symbol["stats"]["24h_ch"] >= 0 else "🔴📉"

            msg += f"<code>{symbol["symbol"]}: {float(symbol["stats"]["lastPrice"]):,.2f} {emoji}{symbol["stats"]["24h_ch"]}%</code>\n\n"

        return msg
    else:
        print("خطا در دریافت داده:", response.status_code)
