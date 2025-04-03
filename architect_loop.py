from core.template_header import *
from core.roadmap_agent import get_next_task
from core.architect_request import send_prompt_to_llm
from core.module_factory import create_module

@wrap_execution
def run_architect_loop():
    task = get_next_task()
    if not task:
        reflect("No pending roadmap task.")
        return
    reflect(f"Architect processing task: {task}")
    modules = send_prompt_to_llm(task)
    if not isinstance(modules, list):
        reflect("Architect returned invalid module list.")
        return
    for mod in modules:
        create_module(mod)

if __name__ == "__main__":
    run_architect_loop()
