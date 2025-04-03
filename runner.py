from ask_architect import prompt_architect
from code_generator import generate_code
from workflow_builder import build_workflow

def run():
    modules = prompt_architect()
    generate_code(modules)
    workflow = build_workflow(modules)
    for fn in workflow:
        fn()

if __name__ == "__main__":
    run()
