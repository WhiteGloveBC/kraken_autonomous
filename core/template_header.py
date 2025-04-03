import os, sys, subprocess

def env(key, default=None):
    return os.getenv(key, default)

def run(cmd):
    subprocess.run(cmd, check=True)

def reflect(message):
    print(f"[REFLECT] {message}")

def get_arg(index, default=None):
    try:
        return sys.argv[index]
    except IndexError:
        return default
