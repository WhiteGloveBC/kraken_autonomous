def wrap_execution(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print("[REFLECT] Function executed successfully.")
            return result
        except Exception as e:
            print(f"[ERROR] {func.__name__} failed: {e}")
            return None
    return wrapper

def with_reflection(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[REFLECT] {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
