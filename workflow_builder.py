from core.wrapper import with_reflection

@with_reflection
def build_workflow(modules):
    workflow = []
    for m in modules:
        mod = __import__(f"core.{m['filename'].replace('.py','')}", fromlist=[m["function"]])
        workflow.append(getattr(mod, m["function"]))
    return workflow
