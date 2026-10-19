import os

from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from models.incident_schema import IncidentAnalysis


llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
    temperature=0
)

structured_llm = llm.with_structured_output(
    IncidentAnalysis,
    method="json_schema",
    strict=False
)


prompt = ChatPromptTemplate.from_template("""
You are a Senior Telecom Network Operations Engineer
working in the Network Operations Center (NOC).

Use ONLY the retrieved enterprise knowledge.

Do NOT invent facts.

If a location is not mentioned,
return "Unknown".

Analyze the incident and return:

- Incident Type
- Severity
- Technology
- Location
- Confidence (0-100)
- Short Summary
- Business Impact
- Possible Root Causes
- Recommended Actions
- Applicable SOPs or enterprise manuals used
- Escalation Team
- Estimated Resolution Time

Context:

{context}

Incident:

{question}
""")


def analyzer_agent(state):

    chain = prompt | structured_llm

    try:
        analysis = chain.invoke(
            {
                "context": state["context"],
                "question": state["question"],
                "kpi_summary": state["kpi_summary"]
            }
        )

    except Exception as e:
        print(e)
        raise

    return {
        "analysis": analysis
    }