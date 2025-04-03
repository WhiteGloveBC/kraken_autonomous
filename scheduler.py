import schedule
import time
import subprocess

def sync():
    subprocess.call(["python", "codebase_sync.py"])

schedule.every(10).minutes.do(sync)

while True:
    schedule.run_pending()
    time.sleep(1)
