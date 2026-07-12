# TelcoPilot AI Architecture

```text
                    User Incident
                           │
                           ▼
                 Streamlit Dashboard
                           │
                           ▼
                 LangGraph Workflow
                           │
     ┌─────────────────────┼─────────────────────┐
     ▼                     ▼                     ▼
Retriever Agent      KPI Agent          Analyzer Agent
     │                     │                     │
     └──────────────┬──────┴─────────────────────┘
                    ▼
          Report Generator Agent
                    │
                    ▼
             Incident Report (PDF)

```

### Technologies Used

- Python
- Streamlit
- LangChain
- LangGraph
- Gemini 2.5 Flash
- ChromaDB
- HuggingFace Embeddings
- RAG
- Structured Output (Pydantic)
- ReportLab