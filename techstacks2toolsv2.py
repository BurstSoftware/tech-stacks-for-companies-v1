# techstacks2toolsv2.py
import streamlit as st
import requests
import json
import base64
from io import BytesIO

def process_job_description(api_key, job_description):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [{
            "parts": [{
                "text": """Analyze this job description and provide a detailed Streamlit tool design:
                - Required features
                - Suggested UI components
                - Proposed functionality
                Job Description: """ + job_description
            }]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        response.raise_for_status()
        result = response.json()
        generated_text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response generated")
        return generated_text
    except requests.exceptions.Timeout:
        return "Error: API request timed out"
    except requests.exceptions.RequestException as e:
        return f"Error calling API: {str(e)}"

def generate_reportlab_code(tool_design):
    # Escape the content separately to avoid f-string backslash issues
    escaped_content = tool_design.replace('"', '\\"').replace('\n', '\\n')
    
    return """from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(output_filename="tool_design.pdf"):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph("Proposed Tool Design", styles['Title']))
    story.append(Spacer(1, 12))
    
    # Content
    content = "{}"
    for paragraph in content.split('\\n\\n'):
        story.append(Paragraph(paragraph, styles['BodyText']))
        story.append(Spacer(1, 12))
    
    doc.build(story)

if __name__ == "__main__":
    create_pdf()
""".format(escaped_content)

def main():
    st.set_page_config(page_title="TechStack2Tools", layout="wide")
    st.title("TechStack2Tools")
    st.header("Job Description to Tool Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        api_key = st.text_input(
            "Google AI Studio API Key",
            type="password",
            help="Enter your API key to process job descriptions"
        )
        job_description = st.text_area(
            "Job Description",
            height=400,
            help="Paste the job description you want to convert into a tool"
        )
    
    with col2:
        if st.button("Generate Tool Design", key="process"):
            if not api_key:
                st.error("Please provide an API key")
            elif not job_description:
                st.error("Please provide a job description")
            else:
                with st.spinner("Generating tool design..."):
                    result = process_job_description(api_key, job_description)
                    
                    st.subheader("Proposed Tool Design")
                    st.markdown(result)
                    
                    # Generate filename from first line of analysis
                    first_line = result.split('\n')[0].strip().lower().replace(' ', '_')
                    filename = f"{first_line}.txt"
                    
                    # Download button
                    st.download_button(
                        label="Download Tool Design",
                        data=result,
                        file_name=filename,
                        mime="text/plain"
                    )
                    
                    # Generate and display ReportLab code
                    st.subheader("ReportLab PDF Generation Code")
                    reportlab_code = generate_reportlab_code(result)
                    st.code(reportlab_code, language="python")
                    
                    # Copy to clipboard button
                    st.button(
                        "Copy Code to Clipboard",
                        on_click=lambda: st.write(
                            '<script>navigator.clipboard.writeText(`' + reportlab_code + '`)</script>',
                            unsafe_allow_html=True
                        )
                    )
        
        if st.button("Clear", key="clear"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
