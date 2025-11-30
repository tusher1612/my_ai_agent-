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

If you want, I can also **create a fully ready-to-run agent template** that you can **push to GitHub and submit for the Kaggle capstone** in just one go.  

Do you want me to do that next?
```
```

---

## References

* Tutorial: [FreeCodeCamp – Build AI Coding Agent](https://www.freecodecamp.org/news/build-your-own-functional-ai-coding-agent/)
* Interactive Course: [Boot.dev](https://www.boot.dev/courses/build-ai)
* FreeCodeCamp: [Learn to code for free](https://www.freecodecamp.org)

---

## Future Improvements

* Add long-term memory for multi-session tasks
* Integrate with APIs for more advanced automation
* Deploy as a web-based productivity agent

---

## Short Repo Description (for GitHub About section)

Build a functional AI coding agent in Python with Gemini API, featuring an agentic loop, tool calling, and memory tracking for file and code operations.


