# 💰 AI Expense Assistant

> A simple AI-powered expense tracker built to understand how LLM Function Calling works under the hood.

This project demonstrates how a Large Language Model can understand natural language, decide which backend function should be executed, call that function, and generate a final response based on the result.

Instead of relying on frameworks such as LangChain or CrewAI, every component is implemented manually to better understand the architecture behind modern AI applications.

---

# 🚀 Features

- 💬 Natural language expense tracking
- 🤖 OpenAI Responses API
- 🛠️ Function Calling
- ⚡ FastAPI backend
- 🗄️ SQLite persistence
- 🧩 Modular architecture
- 📦 Tool execution layer
- 🔄 Two-step LLM response flow

---

# 🏗️ Architecture

text                 User                   │                   ▼           FastAPI Backend                   │                   ▼             Orchestrator                   │                   ▼           OpenAI Responses API                   │                   ▼           Function Calling                   │                   ▼              Executor                   │         ┌─────────┴─────────┐         ▼                   ▼   add_expense()      get_expenses()                   │                   ▼                SQLite                   │                   ▼           Tool Output                   │                   ▼           OpenAI Responses API                   │                   ▼             Final Response 

---

# 🧠 How It Works

When the user writes:

text I spent £8 on coffee. 

The application does not immediately generate a response.

Instead, the following happens:

1. The user's message is sent to the OpenAI Responses API.
2. The model decides that add_expense() should be executed.
3. The backend executes the function.
4. The expense is stored in SQLite.
5. The function result is sent back to the model.
6. The model generates a final response for the user.

This project demonstrates the complete Function Calling lifecycle.

---

# 📂 Project Structure

text backend/ │ ├── app/ │   ├── agent/ │   │   ├── orchestrator.py │   │   ├── responder.py │   │   └── executor.py │   │ │   ├── tools/ │   │   └── expenses.py │   │ │   ├── tool_registry/ │   │   ├── expense_tools.py │   │   └── registry.py │   │ │   ├── database/ │   │   └── connection.py │   │ │   └── api/ │       └── schemas.py │ └── main.py 

---

# 🛠️ Tech Stack

- Python
- FastAPI
- OpenAI Responses API
- SQLite

---

# 📌 Example

### User

text I spent £8 on coffee. 

### AI

text I've recorded your £8 expense for coffee under the Food & Drink category. 

---

# 🎯 Purpose

The goal of this project is not to build a complete finance application.

Instead, it focuses on understanding how modern LLM applications collaborate with backend functions using OpenAI Function Calling, from the initial user request to the final AI-generated respon