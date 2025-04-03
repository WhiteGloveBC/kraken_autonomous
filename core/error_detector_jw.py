from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
import os, importlib.util

@wrap_execution
def detect_errors(root="."):
    reflect("John Wick: Scanning for broken modules...")
    broken = []
    for dirpath, _, files in os.walk(root):
        if "clones" in dirpath or "__pycache__" in dirpath:
            continue
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(dirpath, file)
                spec = importlib.util.spec_from_file_location("mod", path)
                try:
                    importlib.util.module_from_spec(spec)
                except Exception as e:
                    reflect(f"[ERROR] {file} failed to load: {e}")
                    broken.append(path)
    reflect(f"JW found {len(broken)} broken files.")
    finalize()
    return broken

if __name__ == "__main__":
    detect_errors()
