from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
from core.error_detector_jw import detect_errors
import subprocess

@wrap_execution
def troubleshoot():
    reflect("John Wick: Troubleshooter engaged.")
    broken = detect_errors()
    if not broken:
        reflect("JW found no errors. Standing down.")
        finalize()
        return

    for i, filepath in enumerate(broken):
        base = os.path.splitext(os.path.basename(filepath))[0]
        subprocess.run(["python", "core/cloner_jw.py", base, "3"])
        reflect(f"Cloned repair squad for {base}")

    finalize()

if __name__ == "__main__":
    troubleshoot()
