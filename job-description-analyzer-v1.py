import streamlit as st
import requests
import json

def process_job_description(api_key, job_description):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"""Analyze this job description and provide a detailed breakdown in the following structured format:
    - Tools and Tech Stack: [list specific tools/tech mentioned in the job description]
    - Desired Activities: [list specific activities the employee would perform]
    - Required Skills: [list specific skills required for the role]
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

def main():
    st.set_page_config(page_title="Job Description Analyzer", layout="wide")
    st.title("Job Description Analyzer")
    st.subheader("Break Down Any Job Description")

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

    # Process button
    if st.button("Process Job Description"):
        if not api_key or not job_description:
            st.error("Please provide both API key and job description")
        else:
            with st.spinner("Processing job description..."):
                st.session_state.breakdown_result = process_job_description(api_key, job_description)
                st.success("Job description processed successfully!")

    # Tabs for displaying results
    if "breakdown_result" in st.session_state:
        tab1, tab2, tab3 = st.tabs(["Tools and Tech Stack", "Desired Activities", "Required Skills"])
        
        # Parse and display breakdown
        analysis = parse_analysis(st.session_state.breakdown_result)
        
        with tab1:
            st.markdown("\n".join(f"- {item}" for item in analysis["Tools and Tech Stack"]) or "No tools identified")
        with tab2:
            st.markdown("\n".join(f"- {item}" for item in analysis["Desired Activities"]) or "No activities identified")
        with tab3:
            st.markdown("\n".join(f"- {item}" for item in analysis["Required Skills"]) or "No skills identified")

if __name__ == "__main__":
    main()
