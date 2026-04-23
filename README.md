# 🔭 Research Agent

An AI-powered research assistant built with LangChain and LangGraph that automatically researches any topic, generates a structured research report, and saves it to a file with a timestamp.

---

## 🚀 Features

- 🤖 AI agent powered by LLM via OpenRouter
- 🔍 Wikipedia search tool for fetching information
- 📄 Automatically saves research output to a timestamped `.txt` file
- 📦 Structured output using Pydantic models
- 💬 Interactive CLI — just type your query and get results

---

## 🛠️ Tech Stack

- [Python 3.11](https://www.python.org/)
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [LangChain OpenRouter](https://openrouter.ai/)
- [Pydantic](https://docs.pydantic.dev/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)

---

## 📁 Project Structure

```
Research Agent/
├── main.py          # Entry point — runs the agent
├── tools.py         # Tool definitions (Wikipedia, save to file)
├── .env             # API keys (not committed)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/research-agent.git
cd research-agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install langchain langchain-core langchain-community langchain-openrouter pydantic python-dotenv wikipedia
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
Get your free API key at [https://openrouter.ai](https://openrouter.ai)

---

## ▶️ Usage

```bash
python main.py
```

You will be prompted to enter a research topic:
```
What do you want to research about? Black Holes
```

The agent will:
1. Search Wikipedia for information
2. Generate a structured research report
3. Save the output to a timestamped file like `research_2026-04-23_14-30-25.txt`

---

## 📄 Output Format

```
Research Report
Generated on: 2026-04-23 14:30:25
==================================================

Topic: Black Holes

Summary:
A black hole is a region of spacetime where gravity is so strong that
nothing, not even light or other electromagnetic waves, has enough speed
to escape the event horizon...

Sources:
  - Wikipedia

Tools Used:
  - wikipedia
  - save_to_file
```

---

## 🔑 Supported Models (via OpenRouter)

| Model | Notes |
|---|---|
| `meta-llama/llama-3.3-70b-instruct` | Recommended — free & capable |
| `deepseek/deepseek-r1:free` | Strong reasoning |
| `google/gemini-2.0-flash-exp:free` | Fast & capable |
| `openai/gpt-4o-mini` | Reliable, low cost |

---

## 📌 Notes

- Python **3.11** is recommended. Python 3.13 has known compatibility issues with some LangChain packages.
- Make sure your `.env` file is listed in `.gitignore` to keep your API key safe.

---

## Resources

- [LangChain](https://www.langchain.com/) for the agent framework
- [OpenRouter](https://openrouter.ai/) for free LLM access
- [Wikipedia](https://www.wikipedia.org/) for open knowledge

---
