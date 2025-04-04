# tool_design.py
import streamlit as st
import requests
import json

def process_job_description(api_key, job_description, detailed_breakdown=False):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    if detailed_breakdown:
        prompt = f"""Analyze this job description and provide a detailed breakdown in the following structured format:
        - Tools and Tech Stack: [list specific tools/tech mentioned in the job description]
        - Desired Activities: [list specific activities the employee would perform]
        - Required Skills: [list specific skills required for the role]
        Job Description: {job_description}"""
    else:
        prompt = f"Analyze this job description and suggest a Streamlit tool design to accomplish the tasks described: {job_description}"

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response generated")
    except requests.exceptions.Timeout:
        return "Error: API request timed out"
    except requests.exceptions.RequestException as e:
        return f"Error calling API: {str(e)}"

def parse_analysis(result):
    sections = {
        "Tools and Tech Stack": [],
        "Desired Activities": [],
        "Required Skills": []
    }
    current_section = None
    for line in result.split('\n'):
        line = line.strip()
        if line in sections:
            current_section = line
        elif current_section and line.startswith('-') and line[1:].strip():
            sections[current_section].append(line[1:].strip())
    return sections

def generate_workflow_code(analysis):
    tools = analysis["Tools and Tech Stack"]
    activities = analysis["Desired Activities"]
    skills = analysis["Required Skills"]

    # Base import - only Streamlit is assumed
    imports = ["import streamlit as st"]

    workflow_steps = [activity.strip() for activity in activities if activity.strip()] or ["General Task"]
    skills_list = "\n".join(f"- {skill}" for skill in skills if skill) if skills else "No skills identified"
    skills_markdown = f"""st.markdown('''
{skills_list}
''')"""

    main_code = """# daily_workflow.py
import streamlit as st

def main():
    st.set_page_config(page_title="Daily Workflow", layout="wide")
    st.title("Daily Workflow")
    st.subheader("Custom Workflow Based on Job Description")

    # Available tools from job description
    TOOLS = """ + json.dumps(tools if tools else []) + """

    # Sidebar for navigation
    st.sidebar.title("Workflow Steps")
    step = st.sidebar.radio("Select Activity", """ + json.dumps(workflow_steps) + """)

    # Dynamic content based on selected step
"""
    for step in workflow_steps:
        main_code += f"""    if step == "{step}":
        st.header("{step}")
        tool = st.selectbox("Select Tool for {step}", TOOLS)
        task_details = st.text_area("Task Details", "Describe your work with {{tool}} here")
        if st.button("Execute {step}"):
            st.success(f"Executed '{step}' using {{tool}}")
            st.write(f"Output: [Mock result using {{tool}}]")
"""

    main_code += """
    # Collaboration section
    with st.expander("Collaboration"):
        report_content = st.text_area("Report Content", "Daily update...")
        if st.button("Generate Report"):
            st.download_button(
                label="Download Report",
                data=report_content,
                file_name="daily_report.txt",
                mime="text/plain"
            )

    # Display skills reference
    with st.expander("Required Skills"):
        st.write("Skills required for this role:")
        """ + skills_markdown + """

if __name__ == "__main__":
    main()
"""
    return main_code

def main():
    st.set_page_config(page_title="Generic Tool Design Analyzer", layout="wide")
    st.title("Generic Tool Design Analyzer")
    st.subheader("Analyze Any Job Description")

    # Input section
    with st.expander("Input", expanded=True):
        api_key = st.text_input("Google AI Studio API Key", type="password", help="Enter your API key")
        job_input_method = st.radio("How would you like to provide the job description?", 
                                   ["Paste Text", "Upload File"])
        
        job_description = ""
        if job_input_method == "Paste Text":
            job_description = st.text_area("Job Description", height=300, help="Paste the job description here")
        else:
            uploaded_file = st.file_uploader("Upload Job Description", type=["txt", "md"])
            if uploaded_file:
                job_description = uploaded_file.read().decode("utf-8")

    # Process button outside tabs
    if st.button("Process Job Description"):
        if not api_key or not job_description:
            st.error("Please provide both API key and job description")
        else:
            with st.spinner("Processing job description..."):
                # Store results in session state to share across tabs
                st.session_state.breakdown_result = process_job_description(api_key, job_description, detailed_breakdown=True)
                st.session_state.tool_design_result = process_job_description(api_key, job_description, detailed_breakdown=False)
                st.success("Job description processed successfully!")

    # Tabs for displaying results
    if "breakdown_result" in st.session_state and "tool_design_result" in st.session_state:
        tab1, tab2, tab3, tab4 = st.tabs(["Tools and Tech Stack", "Desired Activities", "Required Skills", "Proposed Tool Design"])
        
        # Breakdown tabs
        analysis = parse_analysis(st.session_state.breakdown_result)
        
        with tab1:
            st.markdown("\n".join(f"- {item}" for item in analysis["Tools and Tech Stack"]) or "No tools identified")
        with tab2:
            st.markdown("\n".join(f"- {item}" for item in analysis["Desired Activities"]) or "No activities identified")
        with tab3:
            st.markdown("\n".join(f"- {item}" for item in analysis["Required Skills"]) or "No skills identified")
        
        # Proposed Tool Design tab (from techstacks2toolsv1.py)
        with tab4:
            st.subheader("Proposed Tool Design")
            st.write(st.session_state.tool_design_result)
            
            # Download Proposed Tool Design
            st.download_button(
                label="Download Proposed Tool Design",
                data=st.session_state.tool_design_result,
                file_name="proposed_tool_design.txt",
                mime="text/plain"
            )
            
            # Generate and download daily_workflow.py
            workflow_code = generate_workflow_code(analysis)
            if st.button("Generate Daily Workflow"):
                st.code(workflow_code, language="python")
                st.download_button(
                    label="Download Daily Workflow Code",
                    data=workflow_code,
                    file_name="daily_workflow.py",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()
