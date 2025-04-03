from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *

@wrap_execution
def main():
    reflect("Starting module: Will output a list of potential trades for evaluation.")
    # TODO: implement logic
    finalize()

if __name__ == "__main__":
    main()
