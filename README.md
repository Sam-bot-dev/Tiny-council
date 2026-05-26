# 🏛️ Tiny Council
> A multi-agent AI system where specialized agents debate, critique, and synthesize decisions — just like a real engineering council.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![AI](https://img.shields.io/badge/AI-Multi--Agent-purple)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Overview

**Tiny Council** is an experimental **multi-agent AI architecture** where multiple autonomous AI agents collaborate, debate, and challenge each other to arrive at high-quality, explainable decisions.

Instead of relying on a single AI response, Tiny Council forms a **council of experts**, each with a distinct role — mimicking how real-world engineering teams think.

---

## 🧠 Why Tiny Council?

Traditional AI systems:
- Provide single-point answers
- Lack internal critique
- Hide reasoning paths

**Tiny Council introduces:**
- 🗣️ Inter-agent debate
- ⚖️ Conflict-driven reasoning
- 🔍 Explicit critique and validation
- 🧩 Consensus-based decision making

This makes the system **more robust, explainable, and realistic**.

---

## 🏗️ Core Architecture

```text
           User Query
               |
               v
      +-------------------+
      |  Council Manager  |
      +-------------------+
        |       |       |
        v       v       v
+---------+ +---------+ +---------+
| Planner | | Critic  | | Expert  |
+---------+ +---------+ +---------+
      \         |         /
       \        |        /
        v       v       v
      +-------------------+
      | Consensus Engine  |
      +-------------------+
                |
                v
   Final Answer + Reasoning Trace
```

---

## 👥 Council Agents (v1)

| Agent | Role |
|-----|-----|
| 🧠 Planner | Breaks down the problem and proposes a solution |
| 🔎 Critic | Challenges assumptions, finds flaws and risks |
| 📚 Domain Expert | Ensures factual and technical correctness |
| 🧩 Synthesizer | Merges arguments into a final response |

Each agent operates independently and communicates through a structured debate loop.

---

# ⚙️ How Tiny Council Works

Tiny Council follows a **multi-agent orchestration workflow** where multiple AI agents collaboratively solve problems through structured debate, critique, and synthesis.

Instead of relying on a single AI response, the system creates a council of specialized agents that independently analyze the query and contribute their perspectives.

---

## 🔄 Workflow

```text
User Query
    ↓
Council Manager receives request
    ↓
Planner Agent proposes solution
    ↓
Critic Agent challenges assumptions
    ↓
Domain Expert validates correctness
    ↓
Synthesizer merges all viewpoints
    ↓
Final Answer + Reasoning Trace
```

---

## 🧠 Agent Responsibilities

### 🧠 Planner Agent
- Breaks down the problem
- Creates an initial strategy
- Suggests possible approaches

---

### 🔎 Critic Agent
- Identifies flaws and risks
- Challenges weak assumptions
- Detects inconsistencies

---

### 📚 Domain Expert Agent
- Validates technical accuracy
- Ensures factual correctness
- Provides domain-specific insights

---

### 🧩 Synthesizer Agent
- Combines all responses
- Resolves conflicts
- Produces final explainable answer

---

## ⚖️ Why Multi-Agent Systems?

Traditional AI systems:
- Generate single-pass responses
- Lack internal critique
- Hide reasoning paths

Tiny Council improves this by:
- Enabling collaborative reasoning
- Increasing explainability
- Supporting transparent decision-making
- Producing more robust responses
---

## 🛠️ Tech Stack

- **Language:** Python  
- **Backend:** FastAPI  
- **AI Layer:** Pluggable LLM interface (OpenAI / Local models)  
- **Data Models:** Pydantic  
- **Architecture:** Modular, agent-based design  

---

# ⚡ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/tiny-council.git
cd tiny-council
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Tiny Council currently uses Hugging Face hosted LLMs for agent reasoning and collaborative responses.

Create a `.env` file in the root directory:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

Generate your API key from:

https://huggingface.co/settings/tokens

---

## 4️⃣ Run Tiny Council

```bash
python -m api.main
```

> Replace `main.py` with your actual project entry file if different.

---

## 💻 Current Interface

Tiny Council currently operates through a terminal-based CLI workflow where agents debate and collaboratively generate responses directly in the console.

Future versions will include:
- FastAPI backend
- Web dashboard
- Live debate visualization
- Agent monitoring UI

---

## 📁 Project Structure

```text
tiny-council/
│
├── agents/
│ ├── base_agent.py
│ ├── planner.py
│ ├── critic.py
│ ├── expert.py
│ └── synthesizer.py
│
├── council/
│ ├── manager.py
│ └── consensus.py
│
├── prompts/
│ ├── planner.txt
│ ├── critic.txt
│ └── expert.txt
│
├── api/
│ └── main.py
│
├── cli/
│ └── banner.py
|
├── tests/
│ └── test_manager.py
├── requirements.txt
└── README.md
```


---

## ⚙️ Current Features

- ✔️ Modular agent system  
- ✔️ Role-specific prompting  
- ✔️ Turn-based agent debate  
- ✔️ Consensus synthesis  

---

## 🧭 Roadmap

### Phase 1
- Core agent framework
- Single-round debate

### Phase 2
- Multi-round discussions
- Agent scoring & voting

### Phase 3
- Persistent memory per agent
- Explainable reasoning logs

### Phase 4
- Web UI for live agent debates
- Exportable decision reports

---

## 🎓 Use Cases

- AI research & experimentation  
- Engineering decision support  
- Code review & system design critique  
- GSoC / research internship portfolios  
- Explainable AI demonstrations  

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🔗 Connect With Me

<p align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <div>
          <img src="https://avatars.githubusercontent.com/Sam-bot-dev?s=120" width="120px;" height="120px;" alt="Bhavesh"/>
        </div>
        <div><strong>Lead Dev</strong></div>
        <div><strong>Bhavesh</strong></div>
        <a href="https://github.com/Sam-bot-dev">🌐 GitHub</a>
      </td>
    </tr>
  </table>
</p>
