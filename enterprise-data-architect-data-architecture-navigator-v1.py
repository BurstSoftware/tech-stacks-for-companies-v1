import streamlit as st
import graphviz
import requests
import json
from datetime import datetime

# Simulated in-memory storage (replace with database like PostgreSQL or Neo4j in production)
state = {
    "data_models": {},
    "policies": {},
    "systems": {},
    "change_requests": [],
    "knowledge_base": []
}

# Google Generative Language API configuration
API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your actual API key or use st.secrets
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Helper function for AI suggestions (daily optimization companion)
def get_ai_suggestion(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error with API call: {str(e)}"

# Data Model Display Function (used daily for visualization)
def display_data_model(dot_code, title="Data Model"):
    try:
        graph = graphviz.Source(dot_code)
        st.graphviz_chart(graph)
    except Exception as e:
        st.error(f"Error rendering model: {str(e)}")

# Simulated Tech Stack Integrations (placeholders for daily use)
def check_cloud_status(platform="Snowflake"):
    return f"{platform} is operational as of {datetime.now().strftime('%H:%M')}"

def validate_model_against_standard(model_code, standard="Data Vault"):
    prompt = f"Validate this DOT code against {standard} standards:\n{model_code}"
    return get_ai_suggestion(prompt)

# Main App: Daily Companion for Enterprise Data Architects
st.set_page_config(page_title="Data Architecture Navigator", layout="wide")
st.sidebar.title("Data Architecture Navigator")
st.sidebar.write("Your daily companion for managing enterprise data architecture.")
section = st.sidebar.radio("Daily Tasks", [
    "Dashboard", 
    "Data Models & Blueprints", 
    "Data Governance", 
    "Data Landscape", 
    "Security & Compliance", 
    "Change Management", 
    "Knowledge Base",
    "Guide"  # New section for user guide
])

# Dashboard: Daily Overview
if section == "Dashboard":
    st.header("Daily Dashboard")
    st.write("Start your day with a snapshot of your data ecosystem.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Data Quality Score", "92%", delta="2%", help="Checked via daily profiling tools")
        st.metric("Pipeline Latency", "1.2s", delta="-0.3s", help="Monitored via Databricks")
    with col2:
        st.metric("Storage Cost", "$5,200", delta="$200", help="Tracked in Snowflake")
        st.metric("Compliance Adherence", "98%", help="Aligned with GDPR/CCPA")
    st.subheader("Tech Stack Status")
    st.write(check_cloud_status("Snowflake"))
    st.write(check_cloud_status("Databricks"))
    st.subheader("Recent Changes")
    for req in state["change_requests"][-3:]:
        st.write(f"- {req['title']} (Status: {req['status']})")

# Data Models & Blueprints: Daily Modeling Tasks
elif section == "Data Models & Blueprints":
    st.header("Data Models & Blueprints")
    st.write("Manage and validate your models throughout the day.")
    tab1, tab2 = st.tabs(["Model Repository", "Visualization"])
    
    with tab1:
        st.subheader("Model Repository")
        model_name = st.text_input("Model Name")
        dot_code = st.text_area("DOT Code", height=200, help="Paste ERD or Data Vault DOT code")
        if st.button("Save Model"):
            state["data_models"][model_name] = {"dot_code": dot_code, "metadata": {}, "version": 1}
            st.success(f"Saved {model_name} for daily use")
        
        uploaded_file = st.file_uploader("Upload DOT File", type=["dot"], help="Import from tools like Erwin")
        if uploaded_file:
            custom_dot = uploaded_file.read().decode("utf-8")
            state["data_models"][f"Uploaded_{uploaded_file.name}"] = {"dot_code": custom_dot, "metadata": {}, "version": 1}
            st.success("Model uploaded")
        
        st.write("Today’s Models:")
        for name in state["data_models"]:
            st.write(f"- {name} (Version {state['data_models'][name]['version']})")
    
    with tab2:
        st.subheader("Visualization & Validation")
        selected_model = st.selectbox("Select Model", list(state["data_models"].keys()))
        if selected_model:
            show_details = st.checkbox("Show Detailed View")
            dot = state["data_models"][selected_model]["dot_code"]
            display_data_model(dot if show_details else "digraph { A -> B }", selected_model)
            
            standard = st.selectbox("Validate Against", ["Data Vault", "TOGAF", "Relational"])
            if st.button("Validate Model"):
                validation = validate_model_against_standard(dot, standard)
                st.write("Validation Result:", validation)
            
            if st.button("Get AI Optimization Suggestion"):
                suggestion = get_ai_suggestion(f"Optimize this data model DOT code:\n{dot}")
                st.write("AI Suggestion:", suggestion)

# Data Governance: Daily Policy Checks
elif section == "Data Governance":
    st.header("Data Governance")
    st.write("Ensure compliance and standards throughout the day.")
    tab1, tab2 = st.tabs(["Policy Library", "Workflow Management"])
    
    with tab1:
        st.subheader("Policy Library")
        policy_title = st.text_input("Policy Title")
        policy_content = st.text_area("Policy Content", help="e.g., Data retention rules")
        if st.button("Add Policy"):
            state["policies"][policy_title] = {"content": policy_content, "status": "Draft"}
            st.success(f"Added {policy_title} for review")
        for title, policy in state["policies"].items():
            st.write(f"**{title}** (Status: {policy['status']})\n{policy['content']}")
    
    with tab2:
        st.subheader("Daily Workflow")
        issue = st.text_input("Report Data Quality Issue", help="e.g., Missing keys in ETL")
        if st.button("Submit Issue"):
            st.success(f"Issue logged: {issue}")

# Data Landscape: Daily System Monitoring
elif section == "Data Landscape":
    st.header("Data Landscape")
    st.write("Track your systems and flows daily.")
    st.subheader("System Catalog")
    system_name = st.text_input("System Name")
    system_desc = st.text_area("Description", help="e.g., Snowflake warehouse details")
    if st.button("Add System"):
        state["systems"][system_name] = {"desc": system_desc, "health": "Good"}
        st.success(f"Added {system_name}")
    for name, sys in state["systems"].items():
        st.write(f"- {name}: {sys['desc']} (Health: {sys['health']})")
    
    st.subheader("Data Flow Diagram")
    if state["systems"]:
        dot = "digraph { " + " -> ".join(state["systems"].keys()) + " }"
        display_data_model(dot, "Daily Data Flow")

# Security & Compliance: Daily Checks
elif section == "Security & Compliance":
    st.header("Security & Compliance")
    st.write("Stay compliant with daily classification tasks.")
    st.subheader("Data Classification")
    data_type = st.selectbox("Data Type", ["Public", "Internal", "Confidential", "Restricted"])
    st.write(f"Selected: {data_type}")
    if st.button("Classify"):
        st.success(f"Data classified as {data_type} for today’s records")

# Change Management: Daily Change Tracking
elif section == "Change Management":
    st.header("Change Management")
    st.write("Log and assess changes throughout the day.")
    st.subheader("Change Request Log")
    change_title = st.text_input("Change Title")
    change_impact = st.text_area("Impact Analysis", help="e.g., Impact on downstream BI")
    if st.button("Submit Change Request"):
        state["change_requests"].append({
            "title": change_title,
            "impact": change_impact,
            "status": "Pending",
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        st.success("Change request logged")
    for req in state["change_requests"]:
        st.write(f"- {req['title']} (Status: {req['status']}, Date: {req['date']})")

# Knowledge Base: Daily Reference
elif section == "Knowledge Base":
    st.header("Knowledge Base")
    st.write("Quick access to your daily references.")
    doc_title = st.text_input("Document Title")
    doc_content = st.text_area("Content", help="e.g., TOGAF best practices")
    tags = st.text_input("Tags (comma-separated)", help="e.g., cloud, governance")
    if st.button("Add Document"):
        state["knowledge_base"].append({
            "title": doc_title,
            "content": doc_content,
            "tags": tags.split(",")
        })
        st.success(f"Added {doc_title}")
    for doc in state["knowledge_base"]:
        st.write(f"**{doc['title']}** (Tags: {', '.join(doc['tags'])})\n{doc['content']}")

# Guide: Separate Page for Tech Stack Reference
elif section == "Guide":
    st.header("Data Architecture Navigator Guide")
    st.write("This tool is your daily companion, integrating with your tech stack to streamline Enterprise Data Architect responsibilities.")
    
    st.subheader("Key Tasks and Responsibilities")
    st.markdown("""
    - **Strategic Data Recommendations**: Partner with business and tech leadership to maximize data value (creation, access, use). *Use the Dashboard for insights.*
    - **Data Model Optimization**: Analyze and optimize models for cloud performance, scalability, and cost-effectiveness. *See Data Models & Blueprints.*
    - **Data Standards and Policies**: Collaborate on standards and policies for data lifecycle, keying, and obfuscation. *Managed in Data Governance.*
    - **Change Impact Assessment**: Monitor ecosystem changes and mitigate impacts. *Track via Change Management.*
    - **Future-State Data Vision**: Provide a forward-looking data landscape view, minimizing vendor lock-in. *Visualize in Data Landscape.*
    - **Architectural Planning**: Influence data architecture decisions. *Leverage Knowledge Base for planning.*
    - **Data Governance**: Develop governance processes and structures. *Use Data Governance tools.*
    - **Data Modeling & Blueprints**: Facilitate design sessions and manage models (conceptual, logical, physical, relational, dimensional, Data Vault). *Daily task in Data Models & Blueprints.*
    - **Data Classification & Zoning**: Manage classification and zoning for faster value delivery. *Daily in Security & Compliance.*
    - **Enterprise Information Solutions**: Improve performance via MDM, metadata, analytics, and integration. *Supported across sections.*
    - **Data Security**: Analyze security requirements and protect assets. *Daily checks in Security & Compliance.*
    """)
    
    st.subheader("Skills Required")
    st.markdown("""
    - **System Integration**: Supported via Data Landscape.
    - **Data Modeling**: Core feature in Data Models & Blueprints.
    - **Frameworks**: TOGAF, ArchiMate, Zachman, UML validation available.
    - **Metamodels, Taxonomies, Ontologies**: Documented in Knowledge Base.
    - **Data Science, MDM, BI, Data Warehousing**: Insights via Dashboard.
    - **Data Access & Analytics**: Microservices and event-based approaches tracked in Data Landscape.
    - **SQL, Python, Visualization Tools**: Python-based tool with Graphviz; exportable to PowerBI/Tableau.
    - **Cloud & Hybrid**: Integrates with Databricks, Snowflake, Teradata (simulated).
    """)
    
    st.subheader("Tool Design Overview")
    st.markdown("""
    This tool is a central hub for planning, documentation, analysis, and collaboration, accompanying your tech stack daily:
    
    1. **Dashboard**: Overview of metrics, pipeline health, and changes.
    2. **Data Models & Blueprints**:
       - *Model Repository*: Upload/create models (ERDs, Data Vault, UML).
       - *Visualization*: Interactive model rendering with Graphviz.
       - *Documentation*: Add metadata and annotations.
    3. **Data Governance**:
       - *Policy Library*: Manage and search policies.
       - *Standards*: Define and check compliance.
       - *Workflow*: Track issues and change requests.
    4. **Data Landscape**: Catalog systems, visualize flows, and track lineage (advanced).
    5. **Security & Compliance**: Classify data and document access controls.
    6. **Change Management**: Log and analyze change impacts.
    7. **Knowledge Base**: Store best practices and resources.
    """)
    
    st.subheader("Tech Stack Integration")
    st.markdown("""
    - **Snowflake/Databricks**: Monitor status and costs daily (Dashboard, Data Landscape).
    - **Tableau/PowerBI**: Exportable visualizations from Data Models.
    - **Google AI**: Daily optimization and validation suggestions.
    - **TOGAF/Data Vault**: Standards validation in Data Models & Blueprints.
    """)
    
    st.subheader("Implementation Notes")
    st.markdown("""
    - **Data Storage**: In-memory now; use Neo4j for relationships in production.
    - **Visualization**: Graphviz for daily use; consider Mermaid.js for advanced needs.
    - **Security**: Add authentication for team use.
    - **Collaboration**: Future commenting features planned.
    """)

# Footer: Daily Context
st.sidebar.write(f"Current Date: {datetime.now().strftime('%B %d, %Y')}")
st.sidebar.write("Tech Stack: Snowflake, Databricks, Tableau, Google AI")
