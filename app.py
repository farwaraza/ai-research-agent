from agent import planner, research_tool, summarize, generate_report, generate_pdf

def run_agent(query, status_box):

    status_box.info(" Planning research tasks...")

    subtopics = planner(query)

    status_box.success(f" Generated {len(subtopics)} research topics")

    sections = []

    for topic in subtopics:

        status_box.info(f" Researching: {topic}")

        notes = research_tool(query, topic)

        status_box.success(f" Completed research: {topic}")

        status_box.info(f" Summarizing: {topic}")

        summary = summarize(topic, notes)

        status_box.success(f" Summary completed: {topic}")

        sections.append({
            "topic": topic,
            "content": summary
        })

    status_box.info(" Generating final report...")

    report = generate_report(sections)

    status_box.success(" Report generated successfully!")

    return report



# ---------------- STREAMLIT UI ---------------- #

import streamlit as st

st.set_page_config(
    page_title="AI Research Agent",
    layout="wide"
)

# ---------- Custom CSS ----------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.block-container {
    max-width: 900px;
}

h1 {
    text-align:center;
}

.stButton>button {
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

.stDownloadButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
}

.report-box{
    background:#ffffff;
    color:#000000;
    padding:25px;
    border-radius:15px;
    border:1px solid #ddd;
}
            
.small{
    color:gray;
    text-align:center;
    margin-top:-15px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------

st.title("AI Research Agent")

st.markdown(
"""
<p class="small">
Plan • Research • Summarize • Generate Report
</p>
""",
unsafe_allow_html=True
)

st.divider()

# ---------- Input ----------

query = st.text_input(
    "",
    placeholder="Research the benefits of electric vehicles..."
)

# ---------- Generate ----------

if st.button("Generate Report"):

    if query.strip() == "":

        st.warning("Please enter a research topic.")

    else:

        progress = st.progress(0)

        status = st.empty()

        progress.progress(10)

        result = run_agent(query, status)

        # Save to history

        st.session_state.history.insert(
            0,
            {
                "query": query,
                "report": result
            }
        )


        progress.progress(100)

        st.success("Research Completed Successfully!")

        st.divider()

        st.markdown("## 📄 Generated Report")

        st.markdown(
            f"""
            <div class="report-box">
            {result}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        pdf = generate_pdf(result)

        st.download_button(
            label="Download PDF Report",
            data=pdf,
            file_name="AI_Research_Report.pdf",
            mime="application/pdf"
        )

# ---------- Session History ----------

if "history" not in st.session_state:
    st.session_state.history = []


# ---------- Sidebar ----------

with st.sidebar:

    st.title(" Research History")

    if len(st.session_state.history) == 0:
        st.info("No research history yet.")

    else:

        for item in st.session_state.history:

            with st.expander(f" {item['query']}"):

                st.markdown(item["report"][:300] + "...")

    st.divider()

    if st.button(" Clear History"):

        st.session_state.history = []

        st.rerun()

    st.divider()

    st.caption(" AI Research Agent")

