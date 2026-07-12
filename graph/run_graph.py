from graph.workflow import app


def analyze_incident(question):

    state = {
        "question": question,
        "context": "",
        "documents": [],
        "kpi_summary": "",
        "analysis": None,
        "report": ""
    }

    result = app.invoke(state)

    return result