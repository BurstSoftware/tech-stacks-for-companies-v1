import streamlit as st
import requests
import json

def process_job_description(api_key, job_description):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"""Analyze this job description and return the response in this exact structured markdown format:
    - Key Tasks and Responsibilities: [list key tasks and responsibilities here, e.g., Analyze data]
    - Skills Required: [list skills required here, e.g., Programming]
    - Tool Design Overview: [provide a brief overview of a tool design to support the role, e.g., A dashboard tool]
    - Tech Stack Integration: [list how the tech stack integrates, e.g., Python with SQL databases]
    - Implementation Notes: [list notes on implementation, e.g., Use APIs for data retrieval]
    If no items are identified for a section, use an empty list [].
    Job Description: {job_description}"""

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
        "Key Tasks and Responsibilities": [],
        "Skills Required": [],
        "Tool Design Overview": [],
        "Tech Stack Integration": [],
        "Implementation Notes": []
    }
    current_section = None
    
    if result.startswith("Error:"):
        return sections, result
    
    for line in result.split('\n'):
        line = line.strip()
        if line in sections:
            current_section = line
        elif current_section and line.startswith('-') and line[1:].strip():
            sections[current_section].append(line[1:].strip())
    
    if not any(sections.values()):
        return sections, "Warning: Could not parse API response into structured format"
    
    return sections, None

def main():
    st.set_page_config(page_title="Job Description Analyzer", layout="wide")
    st.title("Job Description Analyzer")
    st.subheader("Break Down Any Job Description")

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

    if st.button("Process Job Description"):
        if not api_key or not job_description:
            st.error("Please provide both API key and job description")
        else:
            with st.spinner("Processing job description..."):
                st.session_state.breakdown_result = process_job_description(api_key, job_description)
                st.success("Job description processed successfully!")

    if "breakdown_result" in st.session_state:
        with st.expander("Raw API Response (Debug)", expanded=True):
            st.text(st.session_state.breakdown_result)

        analysis, error_message = parse_analysis(st.session_state.breakdown_result)
        
        if error_message:
            st.warning(error_message)
        else:
            st.subheader("Analysis Results")
            with st.expander("Key Tasks and Responsibilities", expanded=True):
                st.markdown("\n".join(f"- {item}" for item in analysis["Key Tasks and Responsibilities"]) or "No tasks identified")
            with st.expander("Skills Required", expanded=True):
                st.markdown("\n".join(f"- {item}" for item in analysis["Skills Required"]) or "No skills identified")
            with st.expander("Tool Design Overview", expanded=True):
                st.markdown("\n".join(f"- {item}" for item in analysis["Tool Design Overview"]) or "No overview provided")
            with st.expander("Tech Stack Integration", expanded=True):
                st.markdown("\n".join(f"- {item}" for item in analysis["Tech Stack Integration"]) or "No integration details provided")
            with st.expander("Implementation Notes", expanded=True):
                st.markdown("\n".join(f"- {item}" for item in analysis["Implementation Notes"]) or "No notes provided")

if __name__ == "__main__":
    main()
