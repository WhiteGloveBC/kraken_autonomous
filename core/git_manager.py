import os

def commit_and_push(msg="ASZA commit"):
    os.system("git add .")
    os.system(f"git commit -m \"{msg}\"")
    os.system("git push")
    print("[GIT] Commit and push complete.")
