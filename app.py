import streamlit as st
import os
from graph.run_graph import analyze_incident
from utils.pdf_generator import generate_pdf
from utils.kpi_dashboard import load_kpis
# from streamlit_autorefresh import st_autorefresh

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="TelcoPilot AI",
    page_icon="📡",
    layout="wide"
)

# st_autorefresh(
#     interval=10000,
#     key="dashboard_refresh"
# )

# ---------------- Session State ---------------- #

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "documents" not in st.session_state:
    st.session_state.documents = []

if "report" not in st.session_state:
    st.session_state.report = ""


# ---------------- KPI ---------------- #

kpis = load_kpis(st.session_state.analysis)

# ---------------- Header ---------------- #

st.title("📡 TelcoPilot AI")

st.caption(
    "AI-powered Network Operations Center (NOC) Copilot for telecom incident analysis, "
    "root cause detection, and intelligent troubleshooting."
)

col1, col2 = st.columns([5, 1])

with col2:
    st.success("🟢 System Healthy")

st.divider()

# ---------------- Dashboard ---------------- #

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🟢 Healthy Towers", kpis["healthy"])

with col2:
    st.metric("🟠 Active Alerts", kpis["alerts"])

with col3:
    st.metric("🔴 Critical Incidents", kpis["critical"])

with col4:
    st.metric("📶 Avg Latency", f"{kpis['latency']} ms")

st.divider()

# ---------------- Incident Input ---------------- #

with st.container(border=True):

    st.subheader("🚨 Report Network Incident")

    st.caption(
        "Describe the telecom issue. AI will retrieve SOPs, analyze network KPIs and generate an incident report."
    )

    question = st.text_area(
    "Incident Description",
    placeholder="Example: Customers in Berlin are experiencing high latency on the 5G network.",
    height=90,
    label_visibility="collapsed"
)

    analyze = st.button(
        "🔍 Analyze Incident",
        use_container_width=True
    )

if analyze:

    if not question.strip():
        st.warning("Please describe the incident.")
        st.stop()

    with st.spinner("Analyzing Network Incident..."):
        try:
            result = analyze_incident(question)
        except Exception as e:
            st.exception(e)
            st.stop()

    st.session_state.analysis = result["analysis"]
    st.session_state.documents = result["documents"]
    st.session_state.report = result["report"]


# ---------------- Display Result ---------------- #

if st.session_state.analysis:

    answer = st.session_state.analysis
    docs = st.session_state.documents
    report = st.session_state.report

    st.success("✅ Incident analyzed successfully.")

    st.divider()

    left, right = st.columns([2, 1])

    # LEFT COLUMN

    with left:

        st.subheader("📍 Incident Summary")

        st.info(answer.summary)

        st.subheader("🚨 Business Impact")

        st.error(answer.business_impact)

        st.subheader("🔍 Possible Root Causes")

        for cause in answer.possible_root_causes:
            st.warning(cause)

        st.subheader("🛠 Recommended Actions")

        for rec in answer.recommendations:
            st.checkbox(rec, value=True, disabled=True)

    # RIGHT COLUMN

    with right:

        d1, d2 = st.columns(2)

        with d1:
            st.metric("Severity", answer.severity)
            st.metric("Technology", answer.technology)

        with d2:
            st.metric("Incident Type", answer.incident_type)
            st.metric("Location", answer.location)

        confidence = str(answer.confidence).replace("%", "")

        st.metric("Confidence", f"{confidence}%")

    st.divider()

    # ---------------- Supporting Knowledge ---------------- #

    st.subheader("📄 Supporting Knowledge")

    for doc in docs:

        source = doc.metadata.get("source", "Unknown")

        filename = os.path.splitext(os.path.basename(source))[0]
        filename = filename.replace("_", " ").title()

        with st.expander(f"📄 {filename}"):
            st.write(doc.page_content)

    st.divider()

    # ---------------- Report ---------------- #

    st.subheader("📑 Incident Report")

    with st.expander("View Generated Report"):

        st.text(report)

    pdf_filename = generate_pdf(report)

    with open(pdf_filename, "rb") as pdf:

        st.download_button(
            "📥 Download Incident Report (PDF)",
            pdf,
            file_name="Incident_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.divider()

    # ---------------- KPI Table ---------------- #

    st.subheader("📊 Live Network KPI Dashboard")

    st.dataframe(
        kpis["data"],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.caption(
        "© 2026 TelcoPilot AI • Powered by LangGraph • Gemini 2.5 Flash • ChromaDB • Streamlit"
    )