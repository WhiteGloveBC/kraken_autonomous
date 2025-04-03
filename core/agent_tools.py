from core.create_module_tool import tool_create_module
from core.log_reflection_tool import tool_log_reflection
from core.generate_context_tool import tool_generate_context
from core.tool_registry import get_tool_list

def handle_tool_call(tool_call):
    name = tool_call.get("name")
    args = tool_call.get("arguments", {})

    if name == "create_module":
        return tool_create_module(args)
    elif name == "log_reflection":
        return tool_log_reflection(args)
    elif name == "generate_context":
        return tool_generate_context(args)
    else:
        return f"Unknown tool: {name}"
