import requests


url = (
    "https://brsapi.ir/Api/Tsetmc/Index.php?key=Free1eKMnKy3i5ECB69ZnbQ1JbJVf4mt&type=1"
)
response = requests.get(url)


def get_bursindex():
    if response.status_code == 200:
        data = response.json()
        emoji = '🟢📈' if data["index_change"] >= 0 else '🔴📉'
        return f"<code>Tehran Stock Index: {float(data['index']):,.2f} {emoji} {float(data['index_change']):,.2f}</code>"
    else:
        print("خطا در دریافت داده:", response.status_code)
