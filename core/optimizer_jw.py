from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
import subprocess, os

@wrap_execution
def optimize():
    reflect("John Wick: Optimizer activated.")
    target_dir = "trading"
    confirmed = []

    for file in os.listdir(target_dir):
        if file.endswith(".py"):
            path = os.path.join(target_dir, file)
            with open(path) as f:
                content = f.read()
            if "Strategy executed successfully" in content or "finalize()" in content:
                confirmed.append(file)

    if not confirmed:
        reflect("No winning strategies found to optimize.")
        finalize()
        return

    for strategy in confirmed:
        base = strategy.replace(".py", "")
        reflect(f"Optimizing {base}...")
        subprocess.run(["python", "core/cloner_jw.py", f"trading/{base}", "1"])
        subprocess.run(["python", "ask_architect.py", f"Improve strategy: {base}, focus on compounding, logic tuning, and error resistance."])
        reflect(f"{base} enhancement requested.")

    finalize()

if __name__ == "__main__":
    optimize()
