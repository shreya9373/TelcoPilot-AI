import pandas as pd


def kpi_agent(state):

    df = pd.read_csv("data/kpi_data/tower_metrics.csv")

    critical = df[df["Status"] == "Critical"]

    warning = df[df["Status"] == "Warning"]

    summary = f"""
Current Network KPIs

Healthy Towers : {(df["Status"]=="Healthy").sum()}

Warning Towers : {len(warning)}

Critical Towers : {len(critical)}

Average Latency : {df["Latency"].mean():.1f} ms

Highest CPU Usage :

{critical[['Tower','CPU','Latency','PacketLoss']].to_string(index=False)}
"""

    return {
        "kpi_summary": summary
    }