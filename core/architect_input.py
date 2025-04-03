from core.wrapper import with_reflection
import sys

@with_reflection
def get_prompt():
    return " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("[ARCHITECT] Describe the system you want to build: ")
