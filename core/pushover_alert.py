import os
import requests
from core.env_loader import load_env

# Force environment load immediately
load_env()

def send_alert(message, title="ASZA Alert"):
    user_key = os.environ.get("PUSHOVER_USER_KEY")
    token = os.environ.get("PUSHOVER_API_TOKEN")

    if not user_key or not token:
        print(f"[PUSH] Missing credentials. User: {user_key}, Token: {token}")
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
