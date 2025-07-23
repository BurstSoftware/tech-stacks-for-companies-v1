import streamlit as st

# Title and Job Details
st.title("Sr Software Engineer Application")
st.subheader("Position: Brisbane, CA 94005 - Remote, Full-time")
st.write("Salary Range: $140,000 - $175,000 per year")

# Job Description
st.write("""
This page is designed to help you prepare for the Sr Software Engineer role. Below are the recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- Vulnerability Management")
    st.write("- Terraform")
    st.write("- Snowflake")
    st.write("- SQL")
    st.write("- Redshift")
    st.write("- Python")
    st.write("- PostgreSQL")
    st.write("- Plotly")
    st.write("- Natural Language Processing")
    st.write("- Metadata & Access Management")

with col2:
    st.write("- MLOps")
    st.write("- Microsoft SQL Server")
    st.write("- Kafka")
    st.write("- Jenkins")
    st.write("- Kubernetes")
    st.write("- HIPAA")
    st.write("- Google Cloud Platform")
    st.write("- GitHub")
    st.write("- Flask")
    st.write("- Encryption")
    st.write("- Docker")
    st.write("- DevOps")
    st.write("- Data Visualization")
    st.write("- Data Governance")
    st.write("- Continuous Improvement")
    st.write("- Computer Science")
    st.write("- CI/CD")
    st.write("- Big Data")
    st.write("- Azure")
    st.write("- Agile")
    st.write("- AWS")
    st.write("- AI")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
