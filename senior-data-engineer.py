import streamlit as st
from datetime import datetime

# Title and Job Details
st.title("Senior Data Engineer Application")
st.subheader("Position: Atlanta, GA - Remote, Full-time")
st.write("Salary Range: $145,000 - $200,000 per year")
st.write(f"Last Updated: {datetime.now().strftime('%I:%M %p CDT, %B %d, %Y')}")  # Updated to 07:45 PM CDT, July 22, 2025

# Job Description
st.write("""
This page is designed to help you prepare for the Senior Data Engineer role. Below are the required and recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- Data Classification")
    st.success("Recommended Skills")
    st.write("- Terraform")
    st.write("- Spark")
    st.write("- SQL")
    st.write("- Redis")
    st.write("- Quality Assurance")
    st.write("- Python")

with col2:
    st.success("Recommended Skills")
    st.write("- PostgreSQL")
    st.write("- Organizational Skills")
    st.write("- NoSQL")
    st.write("- Model Training")
    st.write("- Kubernetes")
    st.write("- Kafka")
    st.write("- Google Cloud Platform")
    st.write("- Go")
    st.write("- DevOps")
    st.write("- Data Governance")
    st.write("- Communication Skills")
    st.write("- CI/CD")
    st.write("- APIs")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
