import requests
import time
from config import BOT_TOKEN

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    return requests.get(url, params=params).json()

def main():
    offset = None

    print("Bot jalan... kirim pesan di TOPIC grup kamu")

    while True:
        data = get_updates(offset)

        if data["ok"]:
            for update in data["result"]:

                offset = update["update_id"] + 1

                message = update.get("message")
                if not message:
                    continue

                chat = message.get("chat", {})
                text = message.get("text", "")

                chat_id = chat.get("id")
                thread_id = message.get("message_thread_id", None)

                print("\n======================")
                print("CHAT ID:", chat_id)
                print("TEXT:", text)
                print("THREAD ID:", thread_id)
                print("======================\n")

        time.sleep(1)

if __name__ == "__main__":
    main()
