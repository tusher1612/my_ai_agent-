# Build Your Own Functional AI Coding Agent

**Description:**  
This project is based on the FreeCodeCamp tutorial “Build your own functional AI coding agent from the ground up using Python and the free Gemini Flash API” by Lane Wagner. It demonstrates how to create an **agentic AI loop** capable of interacting with a codebase, reading/writing files, executing Python code, and iteratively improving its output.  

The project introduces key concepts such as **agentic loops, tool calling, and memory**, providing hands-on experience building an AI agent from scratch.  

---

## Features  
- Implements an **agentic loop** for repeated task execution  
- Supports multiple **tools**:  
  - Get file information  
  - Read file content  
  - Write to files  
  - Execute Python code  
- Tracks conversation history and task execution  
- Includes debugging tools like verbose logging  
- Demonstrates the difference between **agentic vs. one-shot responses**  

---

## Technologies & Tools  
- Python 3.12  
- Gemini Flash API  
- UV AI Framework  
- Command-line interface for agent tasks  

---

## Getting Started  

1. **Clone the repository:**  
```bash
git clone git@github.com:YOUR_USERNAME/my_ai_agent.git
cd my_ai_agent
````

2. **Set up a virtual environment:**

```bash
uv venv
source .venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the agent:**

```bash
python agent.py
```

---

## Project Structure

```
my_ai_agent/
│
├─ agent.py        # Main agent code
├─ tools/          # Tools for agent: read/write/run files
├─ memory/         # Optional memory storage
├─ config.json     # API keys & configuration
└─ README.md```

---
 



