from langgraph.graph import StateGraph, END

from graph.state import GraphState

from agents.retriever import retriever_agent
from agents.analyzer import analyzer_agent
from agents.report_generator import report_generator_agent
from agents.kpi_agent import kpi_agent

workflow = StateGraph(GraphState)

# Nodes
workflow.add_node("Retriever", retriever_agent)
workflow.add_node("Analyzer", analyzer_agent)
workflow.add_node("ReportGenerator", report_generator_agent)
workflow.add_node("KPIAgent", kpi_agent)
# Flow
workflow.set_entry_point("Retriever")

workflow.add_edge("Retriever", "Analyzer")
workflow.add_edge("Analyzer", "ReportGenerator")
workflow.add_edge("ReportGenerator", "KPIAgent")
workflow.add_edge("KPIAgent", END)

# Compile graph
app = workflow.compile()