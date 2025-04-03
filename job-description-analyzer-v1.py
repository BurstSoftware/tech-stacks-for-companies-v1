import streamlit as st
import requests
import json
from collections import defaultdict

# Set page config as the first Streamlit command
st.set_page_config(page_title="Job Description Analyzer", layout="wide")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 20px;
        border-radius: 10px;
    }
    .section-container {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .section-title {
        font-size: 18px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .section-content {
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
    h1, h2 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

def process_job_description(api_key, job_description):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"""Provide a detailed analysis of this job description, covering:
    1. Key tasks and responsibilities
    2. Skills required
    3. A brief overview of a tool design to support the role
    4. How the tech stack integrates
    5. Notes on implementation
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

def parse_response(response):
    sections = defaultdict(list)
    lines = response.split('\n')
    current_section = None
    
    # Keywords to identify sections
    section_keywords = {
        "Key Tasks and Responsibilities": ["tasks", "responsibilities", "duties", "perform"],
        "Skills Required": ["skills", "required", "qualifications", "abilities"],
        "Tool Design Overview": ["tool", "design", "overview", "support"],
        "Tech Stack Integration": ["tech", "stack", "integration", "integrates"],
        "Implementation Notes": ["implementation", "notes", "how to", "approach"]
    }
    
    if response.startswith("Error:"):
        return sections, response
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for numbered sections (e.g., "1.", "2.") or keywords
        lower_line = line.lower()
        if any(lower_line.startswith(f"{i}.") for i in range(1, 6)):
            if "tasks" in lower_line or "responsibilities" in lower_line:
                current_section = "Key Tasks and Responsibilities"
            elif "skills" in lower_line or "required" in lower_line:
                current_section = "Skills Required"
            elif "tool" in lower_line or "design" in lower_line:
                current_section = "Tool Design Overview"
            elif "tech" in lower_line or "stack" in lower_line or "integration" in lower_line:
                current_section = "Tech Stack Integration"
            elif "implementation" in lower_line or "notes" in lower_line:
                current_section = "Implementation Notes"
            sections[current_section].append(line.lstrip("12345.").strip())
        elif current_section:
            # Add to current section if it’s a continuation
            for section, keywords in section_keywords.items():
                if any(keyword in lower_line for keyword in keywords) and section != current_section:
                    current_section = section
                    break
            sections[current_section].append(line)
        else:
            # Fallback: Look for keywords to start a section
            for section, keywords in section_keywords.items():
                if any(keyword in lower_line for keyword in keywords):
                    current_section = section
                    sections[current_section].append(line)
                    break
    
    if not any(sections.values()):
        return sections, "Warning: Could not extract meaningful sections from the response"
    
    return sections, None

def main():
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
        analysis, error_message = parse_response(st.session_state.breakdown_result)
        
        if error_message:
            st.error(error_message)
        else:
            st.markdown("### Analysis Results")
            with st.container():
                for section in ["Key Tasks and Responsibilities", "Skills Required", "Tool Design Overview", "Tech Stack Integration", "Implementation Notes"]:
                    st.markdown(f"<div class='section-container'><div class='section-title'>{section}</div><div class='section-content'>", unsafe_allow_html=True)
                    content = "\n".join(f"- {item}" for item in analysis[section]) or "No details identified"
                    st.markdown(content)
                    st.markdown("</div></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
