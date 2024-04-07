import requests
import datetime
import threading
import time
from AlexaMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
url = "http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0"


# بدلها بالمستخدمين عندك
users = [1748768168]

prayers = {
    "Fajr" : "الفجر", 
    "Dhuhr" : "الضهر", 
    "Asr" : "العصر", 
    "Maghrib" : "المغرب", 
    "Isha" : "العشاء"
    }

@app.on_message(filters.text & ~filters.private, group=20)
async def handle_messages(c, msg):
    if msg.text == "تفعيل الأذان":
        if msg.chat.id in chat:
            await msg.reply_text("ℹ️ الأذان مفعل بالفعل.")
        else:
            chat.append(msg.chat.id)
            await msg.reply_text("✅ تم تفعيل الأذان.")
    elif msg.text == "تعطيل الأذان":
        if msg.chat.id in chat:
            chat.remove(msg.chat.id)
            await msg.reply_text("✅ تم تعطيل الأذان.")
        else:
            await msg.reply_text("ℹ️ الأذان معطل بالفعل.")

    
def main():
    for prayer in prayers:
        thread = threading.Thread(target=loop, args=(prayer, prayers[prayer], ))
        thread.start()

def loop(prayer, name):
    while True:
        if len(users) == 0:
            continue
        response = requests.get(url).json()
        timer = response["data"]["timings"][prayer].split(":")
        broadcast_time = str(datetime.time(hour=int(timer[0]), minute=int(timer[1])).strftime("%H:%M"))
        current_time = str(datetime.datetime.now().strftime("%H:%M"))
        if current_time == broadcast_time:
            for user in users:
                client.send_message(
                    user,
                    f"حان الآن موعد آذان {name} بتوقيت القاهره ❤"
                )
            time.sleep(60)
        time.sleep(2)

if __name__ == "__main__":
    main()
    client.run()
