import streamlit as st
import requests
import json

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 20px;
        border-radius: 10px;
    }
    .stExpander {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stExpander > div > div > div > p {
        font-size: 16px;
        color: #333333;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #357abd;
    }
    .stTextInput>label, .stRadio>label, .stFileUploader>label {
        font-size: 16px;
        color: #4a4a4a;
        font-weight: 500;
    }
    .stSuccess {
        background-color: #e6f4ea;
        color: #2e7d32;
        border: 1px solid #2e7d32;
        border-radius: 5px;
    }
    .stError {
        background-color: #ffebee;
        color: #c62828;
        border: 1px solid #c62828;
        border-radius: 5px;
    }
    .stWarning {
        background-color: #fff3e0;
        color: #ef6c00;
        border: 1px solid #ef6c00;
        border-radius: 5px;
    }
    h1, h2 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

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
    
    # Header
    st.title("Job Description Analyzer")
    st.subheader("Transform Job Descriptions into Actionable Insights")

    # Input Section
    with st.container():
        st.markdown("### Input Your Job Description")
        with st.expander("Enter Details", expanded=True):
            col1, col2 = st.columns([2, 1])
            with col1:
                api_key = st.text_input("Google AI Studio API Key", type="password", help="Enter your API key securely")
            with col2:
                job_input_method = st.radio("Input Method", ["Paste Text", "Upload File"], horizontal=True)
            
            job_description = ""
            if job_input_method == "Paste Text":
                job_description = st.text_area("Job Description", height=200, help="Paste the job description here")
            else:
                uploaded_file = st.file_uploader("Upload Job Description", type=["txt", "md"], help="Upload a text or markdown file")
                if uploaded_file:
                    job_description = uploaded_file.read().decode("utf-8")

    # Process Button
    if st.button("Analyze Job Description"):
        if not api_key or not job_description:
            st.error("Please provide both an API key and a job description.")
        else:
            with st.spinner("Analyzing your job description..."):
                st.session_state.breakdown_result = process_job_description(api_key, job_description)
                st.success("Analysis completed successfully!")

    # Results Section
    if "breakdown_result" in st.session_state:
        analysis, error_message = parse_analysis(st.session_state.breakdown_result)
        
        if error_message:
            st.warning(error_message)
        else:
            st.markdown("### Analysis Results")
            with st.container():
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
