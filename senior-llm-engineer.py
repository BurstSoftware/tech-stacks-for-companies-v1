import streamlit as st
from datetime import datetime

# Title and Job Details
st.title("Senior LLM Engineer Application")
st.subheader("Position: New York, NY - Remote")
st.write("Salary Range: $175,000 - $250,000 per year")
st.write(f"Last Updated: {datetime.now().strftime('%I:%M %p CDT, %B %d, %Y')}")  # Updated to 07:46 PM CDT, July 22, 2025

# Job Description
st.write("""
This page is designed to help you prepare for the Senior LLM Engineer role. Below are the required and recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- Python")
    st.success("Recommended Skills")
    st.write("- Terraform")
    st.write("- Prompt Engineering")
    st.write("- Organizational Skills")
    st.write("- MongoDB")
    st.write("- Kubernetes")
    st.write("- Google Cloud Platform")

with col2:
    st.success("Recommended Skills")
    st.write("- GitLab")
    st.write("- Docker")
    st.write("- DevOps")
    st.write("- Databases")
    st.write("- Data Science")
    st.write("- Continuous Integration")
    st.write("- Communication Skills")
    st.write("- CI/CD")
    st.write("- Azure")
    st.write("- AWS")
    st.write("- AI")

# Apply Button
st.button("Apply on company site")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
