from core.llm_api_client import call_llm
from core.wrapper import wrap_execution

@wrap_execution
def send_prompt_to_llm(prompt):
    print("[ARCHITECT] Sending prompt...")
    return call_llm(prompt)

@wrap_execution
def stream_prompt_to_llm(prompt):
    print("[ARCHITECT] Streaming prompt to LLM...")
    return call_llm(prompt, stream=True)
