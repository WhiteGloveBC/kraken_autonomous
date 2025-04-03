def get_tool_list():
    return [
        {
            "name": "create_module",
            "description": "Create a new Python module with a given name and description.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"}
                },
                "required": ["name", "description"]
            }
        },
        {
            "name": "log_reflection",
            "description": "Log a reflection message about a module or action.",
            "parameters": {
                "type": "object",
                "properties": {
                    "module": {"type": "string"},
                    "message": {"type": "string"},
                    "status": {"type": "string"},
                    "tags": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["module", "message"]
            }
        },
        {
            "name": "generate_context",
            "description": "Regenerate the context summary from file index.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    ]
