import os, json

ROADMAP_FILE = "roadmap.json"

def load_roadmap():
    if not os.path.exists(ROADMAP_FILE):
        return []
    with open(ROADMAP_FILE, "r") as f:
        return json.load(f)

def save_roadmap(data):
    with open(ROADMAP_FILE, "w") as f:
        json.dump(data, f, indent=2)
