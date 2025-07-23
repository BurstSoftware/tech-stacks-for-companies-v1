import streamlit as st
from datetime import datetime

# Title and Job Details
st.title("Senior Machine Learning Engineer Application")
st.subheader("Position: Atlanta, GA - Remote, Full-time")
st.write("Salary Range: $160,000 - $220,000 per year")
st.write(f"Last Updated: {datetime.now().strftime('%I:%M %p CDT, %B %d, %Y')}")

# Job Description
st.write("""
This page is designed to help you prepare for the Senior Machine Learning Engineer role. Below are the recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- Terraform")
    st.write("- TensorFlow")
    st.write("- SQL")
    st.write("- Rust Programming Language")
    st.write("- Redis")
    st.write("- Python")
    st.write("- PyTorch")

with col2:
    st.write("- PostgreSQL")
    st.write("- NoSQL")
    st.write("- Machine Learning")
    st.write("- Kubernetes")
    st.write("- Google Cloud Platform")
    st.write("- Go")
    st.write("- Git")
    st.write("- Docker")
    st.write("- Data Science")
    st.write("- Communication Skills")
    st.write("- APIs")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
