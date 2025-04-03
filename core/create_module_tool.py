from file_creator import write_module_file

def tool_create_module(args):
    return write_module_file(args["name"], args["description"])
