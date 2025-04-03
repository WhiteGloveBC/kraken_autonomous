from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
import time, subprocess

@wrap_execution
def schedule():
    reflect("Scheduler active. Running every 15 minutes.")
    while True:
        subprocess.run(["python", "core/troubleshooter_jw.py"])
        subprocess.run(["python", "core/optimizer_jw.py"])
        subprocess.run(["python", "workflows/codebase_sync.py"])
        reflect("Cycle complete. Sleeping 15 minutes.")
        time.sleep(900)  # 15 minutes
    finalize()

if __name__ == "__main__":
    schedule()
