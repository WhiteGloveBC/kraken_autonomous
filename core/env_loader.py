import os

def load_env(path=".env"):
    if not os.path.exists(path):
        print(f"[ENV] {path} file not found.")
        return
    with open(path) as f:
        for line in f:
            if line.strip() and not line.startswith("#") and "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key.strip()] = value.strip()
    print("[ENV] Environment variables loaded.")
