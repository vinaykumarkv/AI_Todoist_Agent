# AI Todoist Agent

# Overview
This repository contains "AI Todoist Agent", a simple agent that integrates a Google Gemini-powered LLM with the Todoist API to manage tasks via natural language. The agent uses LangChain tooling and a small set of custom tools to add tasks and display the current task list. It runs locally as a CLI chat loop and can be adapted into a web or conversational UI.

# Features
- Add tasks to Todoist using natural language (Todoist API).
- Show current tasks in a readable bullet list.
- Uses Google Gemini (gemini-2.5-flash) for LLM-based understanding and planning.
- LangChain agent and tools abstraction for extensibility.
- Lightweight CLI interface; easy to adapt to Gradio/FastAPI or other front-ends.

# Prerequisites
- Python 3.10 or 3.11 (recommended)
- A Google Gemini API key with access to the gemini-2.5-flash model
- A Todoist API token
- Internet connection

# Setup
1. Clone the repository
```bash
git clone <repo-url>
cd AI_Todoist_Agent
```

2. Create and activate a virtual environment (recommended)
```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
```

3. Install dependencies
```bash   
pip install -r requirements.txt
```

4. Configure environment variables
 
    Create a .env file in the project root with the following keys:
```bash  
   TODOIST_API_KEY=your_todoist_api_token
   GEM_API_KEY=your_google_gemini_api_key
```

# Usage
Run the CLI agent:
```bash
   python main.py
```

# Interaction examples:
- "Add a task to buy groceries tomorrow"
- "Show me my tasks"
- "Add task: Prepare presentation; Description: Slides for Monday meeting"

# How it works
- *Tools*: Two LangChain tools are defined—add_task (adds a Todoist task) and show_task (retrieves and formats current tasks).
- *LLM*: ChatGoogleGenerativeAI (gemini-2.5-flash) processes user intent and decides which tool to call via the LangChain agent.
- *Prompting*: A system prompt sets the assistant’s behavior; conversation history is maintained and passed into the agent to provide context across turns.
- *Agent loop*: A simple CLI loop reads user input, invokes the agent with history, prints the agent output, and updates the history with human and AI messages.

# Project Structure
- main.py — Agent implementation and CLI loop
- requirements.txt — Python dependencies
- .env.example — Example file showing required environment variables
- README.md — This file

# Extensibility and Notes
- Front-ends: Swap the CLI for a Gradio UI or FastAPI endpoint for web use.
- Persistence: Add a database to persist conversation history or cache tool outputs.
- Security: Don’t commit your .env with API keys. Use secret management for production.
- Error handling: The current implementation prints results and assumes success; add try/except blocks and validations for robustness.
- Rate limits: Watch Gemini and Todoist API rate limits; implement retries/backoff if deploying.

# Troubleshooting
- API authentication errors: Verify keys in .env and ensure APIs are enabled/active.
- Missing packages: Run pip install -r requirements.txt and ensure Python 3.10/3.11.
- Gemini access: Confirm your Google Cloud/Gemini account has access to the requested model.

# License
MIT License — feel free to use and adapt for learning or production.

# Acknowledgments
- LangChain and langchain-google-genai for agent and LLM abstractions
- Todoist API client for task management
- Google Gemini models for conversational understanding

# Security note: 
The README includes best-practice reminders about not committing secrets and using secure key management for production deployments.
