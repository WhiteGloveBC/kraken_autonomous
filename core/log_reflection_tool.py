from core.reflection_logger import write_reflection

def tool_log_reflection(args):
    return write_reflection(
        module=args["module"],
        message=args["message"],
        status=args.get("status", "info"),
        tags=args.get("tags", [])
    )
