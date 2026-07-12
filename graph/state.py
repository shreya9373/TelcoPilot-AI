from typing import TypedDict, List
from langchain_core.documents import Document

from models.incident_schema import IncidentAnalysis


class GraphState(TypedDict):

    question: str

    context: str

    documents: List[Document]

    kpi_summary: str

    analysis: IncidentAnalysis

    report: str