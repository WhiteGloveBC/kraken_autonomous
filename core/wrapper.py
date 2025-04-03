from core.pushover_alert import send_alert
import os
import traceback

def wrap_execution(func):
    def wrapper(*args, **kwargs):
        name = os.path.basename(func.__code__.co_filename)
        try:
            result = func(*args, **kwargs)
            msg = f"✅ {name} — `{func.__name__}` executed successfully."
            print(f"[REFLECT] {msg}")
            send_alert(msg, title="ASZA Success")
            return result
        except Exception as e:
            tb = traceback.format_exc()
            msg = f"❌ {name} — Error in `{func.__name__}`:\n{str(e)}"
            print(f"[ERROR] {msg}")
            print(tb)
            send_alert(f"{msg}\n\n{tb}", title="ASZA Failure")
            return None
    return wrapper

def with_reflection(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name = os.path.basename(func.__code__.co_filename)
            reflect_msg = f"[NOTICE] {name} — {message}"
            print(f"[REFLECT] {reflect_msg}")
            send_alert(reflect_msg, title="ASZA Notice")
            return func(*args, **kwargs)
        return wrapper
    return decorator
