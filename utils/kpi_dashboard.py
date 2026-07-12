import random
import pandas as pd


def load_kpis(analysis=None):

    # Default dashboard
    healthy = 142
    alerts = 3
    critical = 1
    latency = 42.5

    rows = [
        {
            "Tower": "Berlin-01",
            "Status": "🟢 Healthy",
            "Latency (ms)": 34,
            "Packet Loss (%)": 0.4
        },
        {
            "Tower": "Berlin-02",
            "Status": "🟢 Healthy",
            "Latency (ms)": 37,
            "Packet Loss (%)": 0.5
        },
        {
            "Tower": "Munich-01",
            "Status": "🟢 Healthy",
            "Latency (ms)": 32,
            "Packet Loss (%)": 0.3
        },
        {
            "Tower": "Frankfurt-03",
            "Status": "🟢 Healthy",
            "Latency (ms)": 35,
            "Packet Loss (%)": 0.2
        },
        {
            "Tower": "Hamburg-02",
            "Status": "🟢 Healthy",
            "Latency (ms)": 31,
            "Packet Loss (%)": 0.2
        }
    ]

    if analysis:

        incident = analysis.incident_type.lower()
        location = analysis.location.lower()

        if "latency" in incident:

            healthy = 139
            alerts = 7
            critical = 3
            latency = 108.4

            for row in rows:
                if location in row["Tower"].lower():
                    row["Status"] = "🔴 Critical"
                    row["Latency (ms)"] = random.randint(95, 120)
                    row["Packet Loss (%)"] = round(random.uniform(3, 6), 2)

        elif "packet" in incident:

            healthy = 140
            alerts = 6
            critical = 2
            latency = 61.5

            for row in rows:
                if location in row["Tower"].lower():
                    row["Status"] = "🟠 Warning"
                    row["Packet Loss (%)"] = round(random.uniform(5, 10), 2)

        elif "fiber" in incident:

            healthy = 138
            alerts = 8
            critical = 4
            latency = 89.2

            for row in rows:
                if location in row["Tower"].lower():
                    row["Status"] = "🔴 Critical"
                    row["Latency (ms)"] = random.randint(70, 100)

    return {
        "healthy": healthy,
        "alerts": alerts,
        "critical": critical,
        "latency": latency,
        "data": pd.DataFrame(rows)
    }