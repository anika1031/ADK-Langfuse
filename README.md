# ADK-Langfuse
## Purpose

The goal is to learn how to build, run and monitor AI agents using Google's open-source Agent Development Kit(ADK), and to add
observability using --> Langfuse so every agent run can be inspected step by step.

## Objectives

- Understand ADK's core concepts: agents, tools, sessions, callbacks, artifacts and the runner.
- Set up a local ADK development environment on a personal PC.

## Tech Stack

- Google Agent Development Kit (ADK)
- LiteLLM (model wrapper)
- Groq API (`openai/gpt-oss-20b`)
- Langfuse (EU cloud) for tracing
- OpenInference Google ADK instrumentor
- Python 3, virtual environment (`.venv`)

## Setup
### Part 1: Install ADK on your PC

1. **Check Python** (3.10 or newer is required):
```bash
   python --version
```

2. **Create the project folder and a virtual environment:**
```bash
   mkdir adk_project
   cd adk_project
   python -m venv .venv
```

3. **Activate the virtual environment:**
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (Git Bash): `source .venv/Scripts/activate`
   - Mac/Linux: `source .venv/bin/activate`

4. **Install the dependencies:**
```bash
   pip install -r requirements.txt
```

5. **Get an API key.** This project uses Groq through LiteLLM. Create a key at
   [console.groq.com/keys](https://console.groq.com/keys).
  
6. **Create the agent folder.** `my_agent` must sit directly inside `adk_project`
   (not inside `.venv`):
```
   adk_project/
   └── my_agent/
       ├── __init__.py     (contains: from . import agent)
       ├── agent.py
       └── .env
```

7. **Add your key to `my_agent/.env`** (see `.env.example`):
```
   GROQ_API_KEY=gsk_your_key_here
```

8. **Run it** from inside `adk_project`:
```bash
   adk web
```
   Open http://localhost:8000 

### Part 2: Connect Langfuse

1. **Create an account** at [cloud.langfuse.com](https://cloud.langfuse.com) (EU) or
   [us.cloud.langfuse.com](https://us.cloud.langfuse.com) (US). Create a project, then go to
   **Settings → API Keys** and copy the public and secret keys.

2. **Install the packages:**
```bash
   pip install langfuse openinference-instrumentation-google-adk
```

3. **Add the keys to `my_agent/.env`:**
```
   LANGFUSE_PUBLIC_KEY=pk-lf-...
   LANGFUSE_SECRET_KEY=sk-lf-...
   LANGFUSE_HOST=https://cloud.langfuse.com
```
   Use `https://us.cloud.langfuse.com` if you chose the US region.

4. **Run the agent and ask a question.** The terminal should print `Langfuse connected`
   on startup. Then open Langfuse → **Tracing**, where your run appears with the
   LLM calls and tool calls.

### Troubleshooting

- **"No agents found":** run `adk web` from `adk_project`, and make sure `my_agent`
  is not inside `.venv`.
- **429 RESOURCE_EXHAUSTED:** the Gemini free quota ran out. Use Groq instead.
- **No traces in Langfuse:** check the keys and host region, then restart `adk web`.

## How it works

Interactive walkthrough of one real run, showing how the agent uses the LLM to pick a tool and why it must re-send the message history and tool result on every call: [Agent Tool Calling (Claude artifact)](https://claude.ai/artifact/NZ6L1gCoRp9zWCvpqj7JqT)
