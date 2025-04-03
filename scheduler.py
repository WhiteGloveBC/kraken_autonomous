from core.template_header import *
from core.wrapper import wrap_execution
import schedule
import time
from subprocess import run

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

@wrap_execution
def run_architect():
    reflect("Running Architect.")
    run("python ask_architect.py", shell=True, cwd=PROJECT_DIR)

@wrap_execution
def run_jw():
    reflect("Running John Wick.")
    run("python core/troubleshooter_jw.py", shell=True, cwd=PROJECT_DIR)

@wrap_execution
def run_sync():
    reflect("Running Codebase Sync.")
    run("python workflows/codebase_sync.py", shell=True, cwd=PROJECT_DIR)

# ✅ Set the schedule ONCE
reflect("Scheduler active. Running every 15 minutes.")
schedule.every(15).seconds.do(run_jw)
schedule.every(30).seconds.do(run_architect)
schedule.every(45).seconds.do(run_sync)
#schedule.every(15).minutes.do(run_jw)
#schedule.every(30).minutes.do(run_architect)
#schedule.every(45).minutes.do(run_sync)

# ✅ Now run the loop
while True:
    schedule.run_pending()
    reflect("Cycle complete. Sleeping 15 seconds...")
    time.sleep(15)
