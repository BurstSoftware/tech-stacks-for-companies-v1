import streamlit as st
import graphviz
import requests
import json
from datetime import datetime

# Simulated in-memory storage (replace with database in production)
state = {
    "data_models": {},
    "policies": {},
    "systems": {},
    "change_requests": [],
    "knowledge_base": []
}

# Google Generative Language API configuration
API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your actual API key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Helper function for AI suggestions using the curl-equivalent API call
def get_ai_suggestion(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    try:
        response = requests.post(
            f"{API_URL}?key={API_KEY}",
            headers=headers,
            json=payload
        )
        response.raise_for_status()  # Raise an error for bad status codes
        result = response.json()
        # Extract the generated text from the response
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.RequestException as e:
        return f"Error with API call: {str(e)}"
    except (KeyError, IndexError) as e:
        return f"Error parsing API response: {str(e)}"

# Data Model Display Function
def display_data_model(dot_code, title="Data Model"):
    graph = graphviz.Source(dot_code)
    st.graphviz_chart(graph)

# Main App
st.set_page_config(page_title="Data Architecture Navigator", layout="wide")
st.sidebar.title("Data Architecture Navigator")
section = st.sidebar.radio("Navigate", [
    "Dashboard", 
    "Data Models & Blueprints", 
    "Data Governance", 
    "Data Landscape", 
    "Security & Compliance", 
    "Change Management", 
    "Knowledge Base"
])

# Dashboard
if section == "Dashboard":
    st.header("Dashboard")
    st.write("High-level overview of your data landscape.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Data Quality Score", "92%", delta="2%")
        st.metric("Data Latency", "1.2s", delta="-0.3s")
    with col2:
        st.metric("Storage Cost", "$5,200", delta="$200")
        st.metric("Compliance Adherence", "98%")
    st.subheader("Recent Changes")
    for req in state["change_requests"][-3:]:
        st.write(f"- {req['title']} (Status: {req['status']})")

# Data Models & Blueprints
elif section == "Data Models & Blueprints":
    st.header("Data Models & Blueprints")
    tab1, tab2 = st.tabs(["Model Repository", "Visualization"])
    
    with tab1:
        st.subheader("Model Repository")
        model_name = st.text_input("Model Name")
        dot_code = st.text_area("DOT Code", height=200)
        if st.button("Save Model"):
            state["data_models"][model_name] = {"dot_code": dot_code, "metadata": {}, "version": 1}
            st.success(f"Saved {model_name}")
        
        uploaded_file = st.file_uploader("Upload DOT File", type=["dot"])
        if uploaded_file:
            custom_dot = uploaded_file.read().decode("utf-8")
            state["data_models"][f"Uploaded_{uploaded_file.name}"] = {"dot_code": custom_dot, "metadata": {}, "version": 1}
            st.success("Model uploaded")
        
        st.write("Existing Models:")
        for name in state["data_models"]:
            st.write(f"- {name} (Version {state['data_models'][name]['version']})")
    
    with tab2:
        st.subheader("Visualization")
        selected_model = st.selectbox("Select Model", list(state["data_models"].keys()))
        if selected_model:
            show_details = st.checkbox("Show Detailed View")
            dot = state["data_models"][selected_model]["dot_code"]
            display_data_model(dot if show_details else "digraph { A -> B }", selected_model)
            
            # AI Suggestion using the API
            if st.button("Get AI Optimization Suggestion"):
                prompt = f"Analyze this data model DOT code and suggest optimizations:\n{dot}"
                suggestion = get_ai_suggestion(prompt)
                st.write("AI Suggestion:", suggestion)

# Data Governance
elif section == "Data Governance":
    st.header("Data Governance")
    tab1, tab2 = st.tabs(["Policy Library", "Workflow Management"])
    
    with tab1:
        st.subheader("Policy Library")
        policy_title = st.text_input("Policy Title")
        policy_content = st.text_area("Policy Content")
        if st.button("Add Policy"):
            state["policies"][policy_title] = {"content": policy_content, "status": "Draft"}
            st.success(f"Added {policy_title}")
        for title, policy in state["policies"].items():
            st.write(f"**{title}** (Status: {policy['status']})\n{policy['content']}")
    
    with tab2:
        st.subheader("Workflow Management")
        issue = st.text_input("Report Data Quality Issue")
        if st.button("Submit Issue"):
            st.success(f"Issue reported: {issue}")

# Data Landscape
elif section == "Data Landscape":
    st.header("Data Landscape")
    st.subheader("System Catalog")
    system_name = st.text_input("System Name")
    system_desc = st.text_area("Description")
    if st.button("Add System"):
        state["systems"][system_name] = {"desc": system_desc, "health": "Good"}
        st.success(f"Added {system_name}")
    for name, sys in state["systems"].items():
        st.write(f"- {name}: {sys['desc']} (Health: {sys['health']})")
    
    st.subheader("Data Flow Diagram")
    if state["systems"]:
        dot = "digraph { " + " -> ".join(state["systems"].keys()) + " }"
        display_data_model(dot, "Data Flow")

# Security & Compliance
elif section == "Security & Compliance":
    st.header("Security & Compliance")
    st.subheader("Data Classification")
    data_type = st.selectbox("Data Type", ["Public", "Internal", "Confidential", "Restricted"])
    st.write(f"Selected Classification: {data_type}")
    if st.button("Classify"):
        st.success(f"Data classified as {data_type}")

# Change Management
elif section == "Change Management":
    st.header("Change Management")
    st.subheader("Change Request Log")
    change_title = st.text_input("Change Title")
    change_impact = st.text_area("Impact Analysis")
    if st.button("Submit Change Request"):
        state["change_requests"].append({
            "title": change_title,
            "impact": change_impact,
            "status": "Pending",
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        st.success("Change request submitted")
    for req in state["change_requests"]:
        st.write(f"- {req['title']} (Status: {req['status']}, Date: {req['date']})")

# Knowledge Base
elif section == "Knowledge Base":
    st.header("Knowledge Base")
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
    for doc in state["knowledge_base"]:
        st.write(f"**{doc['title']}** (Tags: {', '.join(doc['tags'])})\n{doc['content']}")

# Footer
st.sidebar.write("Current Date: April 03, 2025")  # Static for demo purposes
