import sys

def finalize():
    name = sys.argv[0] if sys.argv else "Unknown"
    print(f"[REFLECT] Module {name} complete.")
