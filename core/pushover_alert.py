from core.template_header import *
import requests

def send_alert(message, title="ASZA Alert"):
    user_key = env("PUSHOVER_USER_KEY")
    token = env("PUSHOVER_API_TOKEN")
    if not user_key or not token:
        print("[PUSH] Missing credentials.")
        return

    data = {
        "token": token,
        "user": user_key,
        "title": title,
        "message": message
    }

    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data=data)
        if response.status_code == 200:
            print(f"[PUSH] Sent: {message}")
        else:
            print(f"[PUSH] Failed: {response.text}")
    except Exception as e:
        print(f"[PUSH] Error: {e}")
