# 📡 TelcoPilot AI

**AI-Powered Telecom Operations Copilot**

TelcoPilot AI is an intelligent Network Operations Center (NOC) assistant that helps telecom engineers analyze network incidents, identify possible root causes, retrieve relevant enterprise knowledge, recommend corrective actions, and generate professional incident reports.

Built using **LangGraph**, **LangChain**, **ChromaDB**, **Groq/Gemini LLM**, and **Streamlit**, the application combines Retrieval-Augmented Generation (RAG) with a multi-agent workflow to provide evidence-based telecom troubleshooting.

---

## 🚀 Features

- 🔍 AI-powered telecom incident analysis
- 📚 Retrieval-Augmented Generation (RAG) using enterprise telecom documents
- 🧠 Multi-agent workflow using LangGraph
- ⚡ Root cause detection
- 🛠 Intelligent troubleshooting recommendations
- 📄 Automatic PDF incident report generation
- 📊 Live Network KPI Dashboard
- 📑 Enterprise SOP & Runbook retrieval
- 📈 Structured AI responses
- 🎯 Clean Streamlit dashboard

---

## 🏗️ Architecture

```
                    User
                      │
                      ▼
              Streamlit Dashboard
                      │
                      ▼
             LangGraph Workflow
        ┌─────────────────────────┐
        │ Retriever Agent         │
        │ Analyzer Agent          │
        │ KPI Agent               │
        │ Report Generator Agent  │
        └─────────────────────────┘
                      │
                      ▼
             Chroma Vector Database
                      │
          Enterprise Knowledge Base
     (SOPs, Runbooks, Incident Logs,
         KPI Data & Telecom Manuals)
                      │
                      ▼
                 Groq / Gemini LLM
```

---

# 📂 Project Structure

```
telcopilot-ai/
│
├── agents/
│   ├── analyzer.py
│   ├── retriever.py
│   ├── report_generator.py
│   └── kpi_agent.py
│
├── graph/
│   ├── workflow.py
│   ├── run_graph.py
│   └── state.py
│
├── models/
│   └── incident_schema.py
│
├── rag/
│   ├── retrieval.py
│   └── embeddings.py
│
├── data/
│   ├── telecom_manuals/
│   ├── incident_logs/
│   ├── sop/
│   └── kpi_data/
│
├── utils/
│   ├── pdf_generator.py
│   └── kpi_dashboard.py
│
├── scripts/
│   ├── ingest_documents.py
│   └── test_graph.py
│
├── vectorstore/
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

### AI

- LangGraph
- LangChain
- Groq (Llama 3.3 70B) / Google Gemini
- ChromaDB
- HuggingFace Embeddings

### Backend

- Python

### Frontend

- Streamlit

### Data

- Enterprise SOPs
- Telecom Manuals
- Incident Logs
- KPI Dataset

---

# 🧠 Multi-Agent Workflow

The application follows a multi-agent architecture:

### 1. Retriever Agent

- Searches enterprise telecom knowledge
- Retrieves relevant SOPs, runbooks and incident logs

### 2. Analyzer Agent

- Detects incident type
- Determines severity
- Identifies technology
- Performs root cause analysis
- Estimates business impact

### 3. KPI Agent

- Updates network KPI dashboard based on the detected incident

### 4. Report Generator Agent

- Produces a structured incident report
- Supports PDF export

---

# 📄 Enterprise Knowledge Base

The RAG pipeline retrieves information from internal telecom documentation including:

- Network SOPs
- 5G Operations Manual
- Fiber Backhaul Runbook
- Router Troubleshooting Guide
- Escalation Matrix
- Historical Incident Logs

---

# 📊 Dashboard

The dashboard provides:

- Healthy Towers
- Active Alerts
- Critical Incidents
- Average Network Latency

along with:

- Incident Summary
- Business Impact
- Root Cause Analysis
- Recommended Actions
- Supporting Knowledge
- Downloadable Incident Report

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/telcopilot-ai.git

cd telcopilot-ai
```

Create virtual environment

```bash
python -m venv env
```

Activate environment

Windows

```bash
env\Scripts\activate
```

Linux / macOS

```bash
source env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

For Groq

```env
GROQ_API_KEY=YOUR_API_KEY
```

or for Gemini

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# 📥 Build Knowledge Base

Run

```bash
python -m scripts.ingest_documents
```

This creates the Chroma vector database.

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧪 Sample Incident Queries

```
Customers in Berlin are experiencing high latency on the 5G network.

Users are unable to establish internet sessions.

Packet loss is observed across multiple towers.

My router is not working.

Fiber backhaul failure affecting several sites.

Authentication failures after scheduled maintenance.
```

---

# 📄 Generated Outputs

For every incident the system generates:

- Incident Summary
- Business Impact
- Root Cause Analysis
- Recommended Actions
- Enterprise Knowledge References
- Network KPI Dashboard
- Downloadable PDF Report

---

# 🚀 Future Improvements

- Real-time telecom monitoring integration
- SNMP & Prometheus support
- Grafana integration
- Live alert ingestion
- Historical incident analytics
- Multi-user authentication
- Cloud deployment

---

# 👩‍💻 Author

**Shreya Trivedi**

Built for the **Deutsche Telekom AI Hackathon** using LangGraph, LangChain, ChromaDB, Groq/Gemini, and Streamlit.