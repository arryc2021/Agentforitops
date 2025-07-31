import os
import subprocess
from langchain_community.chat_models import ChatOllama
from langchain.schema.messages import HumanMessage
import logging

logging.basicConfig(level=logging.INFO)

# Basic system tasks
def restart_service(service_name: str):
    subprocess.run(["systemctl", "restart", service_name], check=True)
    logging.info(f"Service '{service_name}' restarted.")

def clean_temp():
    subprocess.run(["rm", "-rf", "/tmp/*"], check=True)
    logging.info("Temporary files cleaned.")

def check_disk():
    result = subprocess.check_output(["df", "-h"]).decode()
    logging.info("Disk Usage:\n" + result)
    return result

# Natural language interface via Ollama
class LLMITOpsAgent:
    def __init__(self, model_name="llama3"):
        self.llm = ChatOllama(model=model_name)

    def handle_request(self, user_input: str):
        prompt = f"""
You're an ITOps assistant. Given a user command, map it to one or more of the following system functions:
- restart_service(service_name)
- clean_temp()
- check_disk()

User input: {user_input}
Respond ONLY with Python function calls, no explanation.
"""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        code = response.content.strip()
        logging.info(f"Generated code: {code}")

        # Execute generated function calls
        try:
            local_vars = {
                "restart_service": restart_service,
                "clean_temp": clean_temp,
                "check_disk": check_disk,
            }
            exec(code, {}, local_vars)
        except Exception as e:
            logging.error(f"Error during execution: {e}")

if __name__ == "__main__":
    agent = LLMITOpsAgent()
    user_input = input("What would you like the agent to do? ")
    agent.handle_request(user_input)
