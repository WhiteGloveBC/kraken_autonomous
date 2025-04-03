from core.template_header import *
from core.pushover_alert import send_alert

def reflect(tag, message):
    log = f"{tag} {message}"
    print(f"[REFLECT] {log}")
    send_alert(log, title=tag.strip("[]"))

def wrap_execution(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            reflect("[ERROR]", f"{func.__name__} — {e}")
            raise
    return wrapper

def with_reflection(message="Function executed"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            reflect("[NOTICE]", f"{func.__name__} — {message}")
            try:
                result = func(*args, **kwargs)
                reflect("[REFLECT]", f"{func.__name__} executed successfully.")
                return result
            except Exception as e:
                reflect("[ERROR]", f"{func.__name__} — Error in `{func.__name__}`:\n{e}")
                raise
        return wrapper
    return decorator
