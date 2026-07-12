from datetime import datetime
import uuid


def report_generator_agent(state):

    analysis = state["analysis"]

    report = f"""
===========================================================
                 INCIDENT REPORT
===========================================================

Incident ID : {str(uuid.uuid4())[:8].upper()}

Generated At : {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

-----------------------------------------------------------

Incident Type : {analysis.incident_type}

Severity : {analysis.severity}

Technology : {analysis.technology}

Location : {analysis.location}

Confidence : {analysis.confidence}%

-----------------------------------------------------------

SUMMARY

{analysis.summary}

-----------------------------------------------------------

POSSIBLE ROOT CAUSES

"""

    for i, cause in enumerate(analysis.possible_root_causes, start=1):
        report += f"{i}. {cause}\n"

    report += "\n-----------------------------------------------------------\n"

    report += "RECOMMENDED ACTIONS\n\n"

    for i, rec in enumerate(analysis.recommendations, start=1):
        report += f"{i}. {rec}\n"

    report += "\n===========================================================\n"

    return {
        "report": report
    }