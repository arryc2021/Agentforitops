# 🧠 LLM-Driven ITOps Assistant

A lightweight Python tool that leverages a local large language model (LLM) via **Ollama** to automate basic system administration tasks from natural language input.

---

## 🚀 Features

- 🔄 Restart system services  
- 🧹 Clean `/tmp` directory  
- 💾 Check disk usage  
- 🧠 Natural language interface powered by [LangChain](https://python.langchain.com/) and [Ollama](https://ollama.com/)

---

## 📦 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed with a supported model (e.g., `llama3`)
- Required Python packages:
  ```bash
  pip install langchain langchain-community
## 🛠️ Usage

### Start your Ollama model  
Make sure your desired model is running:

```bash
ollama run llama3
python itops_agent.py
🧩 How It Works
Your natural language command is sent to the LLM.

The LLM maps it to one or more of these predefined functions:

restart_service(service_name)

clean_temp()

check_disk()

The generated Python code is executed using exec.
