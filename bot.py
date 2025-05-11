import os
import requests
from dotenv import load_dotenv
import jdatetime
from crypto_apis import get_crypto
from bursindex_api import get_bursindex


today = jdatetime.date.today()
res = get_crypto()
res1 = get_bursindex()
months = [
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند",
]
weekdays = [
    "شنبه",
    "یک‌شنبه",
    "دوشنبه",
    "سه‌شنبه",
    "چهارشنبه",
    "پنج‌شنبه",
    "جمعه",
]

# * SEND TO TELEGRAM BOT (TEST)
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

day_name = weekdays[today.weekday()]
month_name = months[today.month - 1]
greeting = f"{day_name} {today.day} {month_name} {today.year} :\n\n"
msg = greeting + res + res1


def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    response = requests.post(url, data=data)
    return response.json()


send_to_telegram(msg)
