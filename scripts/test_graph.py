from graph.run_graph import analyze_incident

result = analyze_incident(
    "Customers in Berlin are facing high latency on the 5G network."
)

print(result["analysis"])

print()

print(result["report"])