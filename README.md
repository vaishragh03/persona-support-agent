# 🤖 Persona-Adaptive AI Support Agent

An intelligent AI-powered customer support assistant built using **Retrieval-Augmented Generation (RAG)**, **persona-aware response generation**, and **human escalation detection**.

This system dynamically adapts its responses based on different customer personas such as:

* 😡 Frustrated Users
* 👨‍💻 Technical Experts
* 💼 Business Executives

The assistant retrieves relevant information from a custom SaaS knowledge base and generates context-aware responses using modern LLM orchestration techniques.

---

# 🚀 Live Demo

> Add your deployed Streamlit URL here after deployment

```text
https://persona-support-agent-2026.streamlit.app/
```

---

# 📌 Project Overview

Traditional support bots provide generic responses regardless of customer behavior or context.

This project solves that problem by combining:

* Persona Classification
* Retrieval-Augmented Generation (RAG)
* Vector Search
* Escalation Intelligence
* Adaptive Response Generation

The result is an AI support assistant capable of delivering personalized, context-aware customer support experiences.

---

# ✨ Features

## 🧠 Persona Detection

Automatically classifies customer queries into:

* Technical Expert
* Frustrated User
* Business Executive

and adapts response tone dynamically.

---

## 📚 Retrieval-Augmented Generation (RAG)

The system retrieves relevant knowledge-base articles before generating responses.

This improves:

* factual grounding
* response relevance
* hallucination reduction

---

## 🗂️ Chroma Vector Database

Uses vector embeddings for semantic document retrieval.

Supports:

* similarity search
* semantic matching
* scalable retrieval pipelines

---

## ⚠️ Escalation Detection

Automatically recommends human escalation for:

* billing disputes
* security concerns
* payment failures
* low-confidence retrieval
* frustrated customer behavior

---

## 💬 Adaptive AI Responses

Different users receive different response styles:

| Persona            | Response Style         |
| ------------------ | ---------------------- |
| Technical Expert   | Detailed & technical   |
| Frustrated User    | Calm & empathetic      |
| Business Executive | Concise & professional |

---

## 🌐 Interactive Streamlit UI

Modern SaaS-style interface with:

* AI response generation
* retrieved knowledge sources
* escalation alerts
* sample testing prompts

---

# 🏗️ System Architecture

```text
User Query
    ↓
Persona Classification
    ↓
RAG Retrieval
    ↓
Escalation Detection
    ↓
Adaptive Prompting
    ↓
LLM Response Generation
```

---

# 🛠️ Tech Stack

| Technology              | Purpose                 |
| ----------------------- | ----------------------- |
| Python                  | Backend Logic           |
| Streamlit               | Frontend UI             |
| ChromaDB                | Vector Database         |
| Google Gemini           | Embeddings              |
| OpenRouter API          | LLM Response Generation |
| Markdown Knowledge Base | Support Documentation   |

---

# 📂 Project Structure

```text
persona-support-agent/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── password_reset.md
│   ├── billing_policy.md
│   ├── refund_policy.md
│   └── ...
│
├── src/
│   ├── rag_pipeline.py
│   ├── generator.py
│   ├── classifier.py
│   └── escalator.py
```

---

# 📖 Knowledge Base Topics

The RAG pipeline uses custom SaaS support documentation covering:

1. Password Reset
2. API Authentication
3. Billing Policy
4. Refund Policy
5. Payment Failure
6. Database Connection Issues
7. Account Lockout
8. Cookie Clearing Guide
9. Subscription Upgrade
10. Security Best Practices

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/vaishragh03/persona-support-agent.git

cd persona-support-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_key

OPENROUTER_API_KEY=your_key
```

---

# ▶️ Running the Project

## Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

# 🧪 Sample Test Queries

## 😡 Frustrated User

```text
Your login system is terrible and not working
```

---

## 👨‍💻 Technical Expert

```text
API authentication returning 401 unauthorized error
```

---

## 💼 Business Executive

```text
Need clarification regarding enterprise billing policy
```

---

## 🔐 Security Issue

```text
I think my account was hacked
```

---

# 🔮 Future Improvements

* Conversation Memory
* Chat History
* Voice Input
* PDF Upload Support
* Multi-language Support
* Advanced Sentiment Analysis
* Confidence Scoring
* Agent Analytics Dashboard

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Prompt Engineering
* Persona-Adaptive AI Systems
* Human Escalation Logic
* LLM Orchestration
* AI SaaS Product Design

---

# 🙌 Acknowledgements

Built using:

* Streamlit
* ChromaDB
* Google Gemini
* OpenRouter APIs

---

# 📧 Author

### Vaishnavi Raghavan

Frontend & AI Enthusiast passionate about building intelligent user-centric systems.

GitHub: https://github.com/vaishragh03

---
