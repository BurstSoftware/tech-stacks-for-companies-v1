import streamlit as st

# Title and Job Details
st.title("MLOps Architect Application")
st.subheader("Position: Dallas, TX - Remote, Full-time")

# Job Description
st.write("""
This page is designed to help you prepare for the MLOps Architect role. Below are the required and recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- Shell Scripting")
    st.write("- Scripting")
    st.write("- Python")
    st.write("- Power BI")
    st.write("- Kubernetes")
    st.write("- Google Cloud Platform")
    st.write("- Distributed Systems")
    st.write("- Azure")
    st.write("- Analytics")
    st.write("- AWS")
    st.write("- UNIX")

with col2:
    st.success("Recommended Skills")
    st.write("- Terraform")
    st.write("- Tableau")
    st.write("- Spark")
    st.write("- REST")
    st.write("- Model Deployment")
    st.write("- Machine Learning Libraries")
    st.write("- Machine Learning Frameworks")
    st.write("- Machine Learning")
    st.write("- GitHub")
    st.write("- Full-stack Development")
    st.write("- Distributed Computing")
    st.write("- Data Science")
    st.write("- CI/CD")
    st.write("- Ansible")
    st.write("- APIs")
    st.write("- AI")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
