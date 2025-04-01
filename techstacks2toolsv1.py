# techstacks2toolsv1.py
import streamlit as st
import requests
import json

def process_job_description(api_key, job_description):
    """Process job description using Google Gemini API"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"Analyze this job description and suggest a Streamlit tool design to accomplish the tasks described: {job_description}"
            }]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        
        # Parse the API response
        result = response.json()
        generated_text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response generated")
        return generated_text
    
    except requests.exceptions.RequestException as e:
        return f"Error calling API: {str(e)}"

def main():
    # Title and header
    st.title("TechStack2Tools")
    st.header("Job Description to Tool Converter")
    
    # API Key input
    api_key = st.text_input(
        "Paste your Google AI Studio API Key here",
        type="password",
        help="Enter your API key to process job descriptions"
    )
    
    # Job description input
    job_description = st.text_area(
        "Paste Job Description here",
        height=300,
        help="Enter the job description you want to convert into a tool"
    )
    
    # Process button
    if st.button("Process"):
        if not api_key:
            st.error("Please provide an API key")
        elif not job_description:
            st.error("Please provide a job description")
        else:
            with st.spinner("Processing job description..."):
                try:
                    # Call the API and get the result
                    result = process_job_description(api_key, job_description)
                    
                    st.success("Job description processed successfully!")
                    
                    # Display the results
                    st.subheader("Proposed Tool Design")
                    st.write(result)
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
