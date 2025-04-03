import os

def get_credential(key):
    return os.getenv(key) or "MISSING_CREDENTIAL"
