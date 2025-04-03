import streamlit as st
import requests
import json
from collections import defaultdict

# Set page config as the first Streamlit command
st.set_page_config(page_title="Job Description Analyzer", layout="wide")

# Custom CSS for a clean, beautiful look without redundant dashes/dots
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 40px;
        max-width: 1200px;
        margin: 0 auto;
    }
    .header-title {
        font-size: 36px;
        font-weight: 700;
        color: #1a3c34;
        margin-bottom: 10px;
        text-align: center;
    }
    .header-subtitle {
        font-size: 20px;
        color: #5e6e66;
        margin-bottom: 40px;
        text-align: center;
    }
    .input-container {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        margin-bottom: 40px;
    }
    .section-container {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        transition: transform 0.2s;
    }
    .section-container:hover {
        transform: translateY(-5px);
    }
    .section-title {
        font-size: 22px;
        font-weight: 600;
        color: #1a3c34;
        margin-bottom: 15px;
    }
    .section-content {
        font-size: 16px;
        color: #34495e;
        line-height: 1.8;
        margin-left: 0; /* Removed offset to avoid redundancy */
    }
    .section-content ul {
        list-style-type: none; /* Remove default bullets */
        padding-left: 0;
    }
    .section-content li {
        margin-bottom: 10px;
        padding-left: 20px; /* Space for custom bullet */
    }
    .section-content li::before {
        content: "•";
        color: #2ecc71;
        font-size: 16px;
        position: absolute;
        margin-left: -20px;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border-radius: 8px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #27ae60;
    }
    .stTextInput>label, .stRadio>label, .stFileUploader>label {
        font-size: 16px;
        color: #1a3c34;
        font-weight: 500;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        padding: 12px;
        background-color: #f9f9f9;
    }
    .stSuccess {
        background-color: #e8f5e9;
        color: #2e7d32;
        border-radius: 8px;
        padding: 12px;
        margin-top: 10px;
    }
    .stError {
        background-color: #ffebee;
        color: #c62828;
        border-radius: 8px;
        padding: 12px;
        margin-top: 10px;
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
            for section, keywords in section_keywords.items():
                if any(keyword in lower_line for keyword in keywords) and section != current_section:
                    current_section = section
                    break
            sections[current_section].append(line)
        else:
            for section, keywords in section_keywords.items():
                if any(keyword in lower_line for keyword in keywords):
                    current_section = section
                    sections[current_section].append(line)
                    break
    
    if not any(sections.values()):
        return sections, "Error: Could not extract meaningful sections from the response"
    
    return sections, None

def main():
    # Main container for centering
    with st.container():
        # Header
        st.markdown("<h1 class='header-title'>Job Description Analyzer</h1>", unsafe_allow_html=True)
        st.markdown("<div class='header-subtitle'>Unlock Insights from Job Descriptions with Ease</div>", unsafe_allow_html=True)

        # Input Section
        with st.container():
            st.markdown("<div class='input-container'>", unsafe_allow_html=True)
            st.markdown("### Provide Your Details")
            col1, col2 = st.columns([3, 1])
            with col1:
                api_key = st.text_input("API Key", type="password", help="Enter your Google AI Studio API key")
            with col2:
                job_input_method = st.radio("Input Method", ["Text", "File"], horizontal=True)
            
            job_description = ""
            if job_input_method == "Text":
                job_description = st.text_area("Job Description", height=150, placeholder="Paste your job description here...")
            else:
                uploaded_file = st.file_uploader("Upload File", type=["txt", "md"], help="Upload a text or markdown file")
                if uploaded_file:
                    job_description = uploaded_file.read().decode("utf-8")
            st.markdown("</div>", unsafe_allow_html=True)

        # Process Button
        if st.button("Analyze Now"):
            if not api_key or not job_description:
                st.error("Please provide both an API key and a job description.")
            else:
                with st.spinner("Analyzing..."):
                    st.session_state.breakdown_result = process_job_description(api_key, job_description)
                    st.success("Analysis Complete!")

        # Results Section
        if "breakdown_result" in st.session_state:
            analysis, error_message = parse_response(st.session_state.breakdown_result)
            
            if error_message:
                st.error(error_message)
            else:
                st.markdown("<h2 class='header-title'>Your Analysis</h2>", unsafe_allow_html=True)
                for section in ["Key Tasks and Responsibilities", "Skills Required", "Tool Design Overview", "Tech Stack Integration", "Implementation Notes"]:
                    with st.container():
                        st.markdown(f"<div class='section-container'><div class='section-title'>{section}</div><div class='section-content'><ul>", unsafe_allow_html=True)
                        content = "\n".join(f"<li>{item}</li>" for item in analysis[section]) if analysis[section] else "<li>No details identified</li>"
                        st.markdown(content, unsafe_allow_html=True)
                        st.markdown("</ul></div></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
