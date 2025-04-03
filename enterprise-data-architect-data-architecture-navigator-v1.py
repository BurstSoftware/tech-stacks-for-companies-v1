import streamlit as st
import graphviz
import requests
import json
from datetime import datetime

# Simulated in-memory storage (replace with database like Neo4j in production)
state = {
    "data_models": {},
    "policies": {},
    "systems": {},
    "change_requests": [],
    "knowledge_base": [],
    "announcements": []
}

# Google Generative Language API configuration
API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your actual API key or use st.secrets
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Helper function for AI suggestions
def get_ai_suggestion(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error with API call: {str(e)}"

# Data Model Display Function
def display_data_model(dot_code, title="Data Model"):
    graph = graphviz.Source(dot_code)
    st.graphviz_chart(graph)

# Main App
st.set_page_config(page_title="Data Architecture Navigator", layout="wide")
st.sidebar.title("Data Architecture Navigator")
st.sidebar.write("A central hub for Enterprise Data Architects to manage daily tasks.")
section = st.sidebar.radio("Navigate", [
    "Dashboard", 
    "Data Models & Blueprints", 
    "Data Governance", 
    "Data Landscape", 
    "Security & Compliance", 
    "Change Management", 
    "Knowledge Base"
])

# 1. Dashboard (Strategic Data Recommendations, Future-State Vision)
if section == "Dashboard":
    st.header("Dashboard")
    st.write("Overview of the data landscape to support strategic recommendations and future-state planning.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Data Quality Score", "92%", delta="2%", help="Supports Data Governance")
        st.metric("Data Latency", "1.2s", delta="-0.3s", help="Monitors pipeline health")
    with col2:
        st.metric("Storage Cost", "$5,200", delta="$200", help="Optimizes cloud cost-effectiveness")
        st.metric("Compliance Adherence", "98%", help="Ensures regulatory alignment")
    
    st.subheader("Data Pipeline Health")
    st.write("Status: All pipelines operational (simulated).")
    
    st.subheader("Recent Changes")
    for req in state["change_requests"][-3:]:
        st.write(f"- {req['title']} (Status: {req['status']})")
    
    st.subheader("Announcements")
    announcement = st.text_input("New Announcement")
    if st.button("Post Announcement"):
        state["announcements"].append({"text": announcement, "date": datetime.now().strftime("%Y-%m-%d")})
    for ann in state["announcements"]:
        st.write(f"- {ann['text']} ({ann['date']})")

# 2. Data Models & Blueprints (Data Modeling & Blueprints, Data Model Optimization)
elif section == "Data Models & Blueprints":
    st.header("Data Models & Blueprints")
    st.write("Manage and optimize data models (conceptual, logical, physical, Data Vault, etc.).")
    tab1, tab2, tab3 = st.tabs(["Model Repository", "Visualization", "Documentation"])
    
    with tab1:  # Model Repository
        st.subheader("Model Repository")
        model_name = st.text_input("Model Name")
        model_type = st.selectbox("Model Type", ["Conceptual", "Logical", "Physical", "Data Vault"])
        dot_code = st.text_area("DOT Code", height=200)
        if st.button("Save Model"):
            state["data_models"][model_name] = {
                "dot_code": dot_code, 
                "type": model_type, 
                "metadata": {}, 
                "version": 1, 
                "tags": []
            }
            st.success(f"Saved {model_name}")
        
        uploaded_file = st.file_uploader("Upload DOT File", type=["dot"])
        if uploaded_file:
            custom_dot = uploaded_file.read().decode("utf-8")
            state["data_models"][f"Uploaded_{uploaded_file.name}"] = {
                "dot_code": custom_dot, 
                "type": "Unknown", 
                "metadata": {}, 
                "version": 1, 
                "tags": []
            }
            st.success("Model uploaded")
        
        st.write("Search Models:")
        search_term = st.text_input("Search by name or tag")
        for name, model in state["data_models"].items():
            if search_term.lower() in name.lower() or any(search_term.lower() in tag.lower() for tag in model["tags"]):
                st.write(f"- {name} (Type: {model['type']}, Version: {model['version']})")
    
    with tab2:  # Visualization
        st.subheader("Visualization")
        selected_model = st.selectbox("Select Model", list(state["data_models"].keys()))
        if selected_model:
            show_details = st.checkbox("Show Detailed View")
            dot = state["data_models"][selected_model]["dot_code"]
            display_data_model(dot if show_details else "digraph { A -> B }", selected_model)
            if st.button("Compare with Previous Version"):
                st.write("Version comparison not yet implemented (requires version history).")
            if st.button("Optimize with AI"):
                prompt = f"Optimize this {state['data_models'][selected_model]['type']} data model for cloud performance and scalability:\n{dot}"
                suggestion = get_ai_suggestion(prompt)
                st.write("AI Optimization Suggestion:", suggestion)
    
    with tab3:  # Documentation
        st.subheader("Documentation")
        if selected_model:
            metadata = st.text_area("Metadata (e.g., descriptions, constraints)", json.dumps(state["data_models"][selected_model]["metadata"]))
            tags = st.text_input("Tags (comma-separated)")
            notes = st.text_area("Notes & Annotations")
            if st.button("Save Documentation"):
                state["data_models"][selected_model]["metadata"] = json.loads(metadata)
                state["data_models"][selected_model]["tags"] = tags.split(",")
                state["data_models"][selected_model]["notes"] = notes
                st.success("Documentation saved")

# 3. Data Governance (Data Standards and Policies, Data Governance)
elif section == "Data Governance":
    st.header("Data Governance")
    st.write("Collaborate on standards, policies, and workflows.")
    tab1, tab2, tab3 = st.tabs(["Policy Library", "Data Standards", "Workflow Management"])
    
    with tab1:  # Policy Library
        st.subheader("Policy Library")
        policy_title = st.text_input("Policy Title")
        policy_content = st.text_area("Policy Content")
        policy_status = st.selectbox("Status", ["Draft", "Approved", "Retired"])
        if st.button("Add Policy"):
            state["policies"][policy_title] = {"content": policy_content, "status": policy_status}
            st.success(f"Added {policy_title}")
        search_policy = st.text_input("Search Policies")
        for title, policy in state["policies"].items():
            if search_policy.lower() in title.lower():
                st.write(f"**{title}** (Status: {policy['status']})\n{policy['content']}")
    
    with tab2:  # Data Standards
        st.subheader("Data Standards")
        standard_name = st.text_input("Standard Name (e.g., Naming Convention)")
        standard_def = st.text_area("Definition")
        if st.button("Define Standard"):
            st.success(f"Defined {standard_name}")
    
    with tab3:  # Workflow Management
        st.subheader("Workflow Management")
        issue = st.text_input("Report Data Quality Issue")
        if st.button("Submit Issue"):
            st.success(f"Issue reported: {issue}")
        change_title = st.text_input("Change Request Title")
        if st.button("Submit Change Request"):
            st.success(f"Change request submitted: {change_title}")

# 4. Data Landscape (Architectural Planning, Enterprise Information Solutions)
elif section == "Data Landscape":
    st.header("Data Landscape")
    st.write("Visualize systems, data flows, and dependencies for planning.")
    tab1, tab2 = st.tabs(["System Catalog", "Data Flow Diagram"])
    
    with tab1:  # System Catalog
        st.subheader("System Catalog")
        system_name = st.text_input("System Name")
        system_desc = st.text_area("Purpose/Description")
        system_owner = st.text_input("Owner")
        if st.button("Add System"):
            state["systems"][system_name] = {"desc": system_desc, "owner": system_owner, "health": "Good"}
            st.success(f"Added {system_name}")
        for name, sys in state["systems"].items():
            st.write(f"- {name}: {sys['desc']} (Owner: {sys['owner']}, Health: {sys['health']})")
    
    with tab2:  # Data Flow Diagram
        st.subheader("Data Flow Diagram")
        if state["systems"]:
            dot = "digraph { " + " -> ".join(state["systems"].keys()) + " }"
            display_data_model(dot, "Data Flow")
        else:
            st.write("Add systems to visualize data flows.")

# 5. Security & Compliance (Data Security, Data Classification & Zoning)
elif section == "Security & Compliance":
    st.header("Security & Compliance")
    st.write("Manage data classification and compliance.")
    tab1, tab2 = st.tabs(["Data Classification", "Access Control"])
    
    with tab1:  # Data Classification
        st.subheader("Data Classification")
        data_type = st.selectbox("Classification Level", ["Public", "Internal", "Confidential", "Restricted"])
        data_zone = st.text_input("Zone (e.g., Production, Staging)")
        if st.button("Classify"):
            st.success(f"Data classified as {data_type} in {data_zone}")
    
    with tab2:  # Access Control
        st.subheader("Access Control")
        policy = st.text_area("Access Control Policy")
        if st.button("Save Policy"):
            st.success("Access control policy saved")

# 6. Change Management (Change Impact Assessment)
elif section == "Change Management":
    st.header("Change Management")
    st.write("Assess and log changes to mitigate impacts.")
    change_title = st.text_input("Change Title")
    change_impact = st.text_area("Impact Analysis")
    affected_systems = st.multiselect("Affected Systems", list(state["systems"].keys()))
    if st.button("Submit Change Request"):
        state["change_requests"].append({
            "title": change_title,
            "impact": change_impact,
            "affected_systems": affected_systems,
            "status": "Pending",
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        st.success("Change request submitted")
    for req in state["change_requests"]:
        st.write(f"- {req['title']} (Status: {req['status']}, Date: {req['date']}, Affected: {', '.join(req['affected_systems'])})")

# 7. Knowledge Base (Collaboration, Documentation)
elif section == "Knowledge Base":
    st.header("Knowledge Base")
    st.write("Store documentation and best practices.")
    doc_title = st.text_input("Document Title")
    doc_content = st.text_area("Content")
    tags = st.text_input("Tags (comma-separated)")
    if st.button("Add Document"):
        state["knowledge_base"].append({
            "title": doc_title,
            "content": doc_content,
            "tags": tags.split(",")
        })
        st.success(f"Added {doc_title}")
    search_kb = st.text_input("Search Knowledge Base")
    for doc in state["knowledge_base"]:
        if search_kb.lower() in doc["title"].lower() or any(search_kb.lower() in tag.lower() for tag in doc["tags"]):
            st.write(f"**{doc['title']}** (Tags: {', '.join(doc['tags'])})\n{doc['content']}")

# Footer
st.sidebar.write("Current Date: April 03, 2025")
