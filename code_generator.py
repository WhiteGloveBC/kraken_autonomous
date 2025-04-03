from module_factory import create_module
from core.wrapper import with_reflection

@with_reflection
def generate_code(modules):
    for module in modules:
        name = module["filename"]
        func = module["function"]
        desc = module["description"]
        create_module(name, func, desc)
