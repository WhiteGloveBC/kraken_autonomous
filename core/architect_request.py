import requests
import json
import os
from core.env_loader import load_env

load_env()

def send_prompt_to_llm(prompt, model="command-a", tools=None):
    url = os.getenv("LLM_API_URL")
    if not url:
        raise ValueError("LLM_API_URL is not set in environment.")

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    if tools:
        payload["tools"] = tools

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response")
    except requests.RequestException as e:
        print(f"[ERROR] LLM request failed: {e}")
        return None
