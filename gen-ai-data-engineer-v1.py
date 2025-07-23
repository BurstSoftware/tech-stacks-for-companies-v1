import streamlit as st

# Title and Job Details
st.title("Gen AI Data Engineer Application")
st.subheader("Position: Remote")

# Job Description
st.write("""
This page is designed to help you prepare for the Gen AI Data Engineer role. Below are the required and recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- Neo4j")
    st.write("- Snowflake")
    st.write("- SQL")
    st.write("- Python")
    st.write("- Operating Systems")
    st.write("- NoSQL")
    st.write("- Linux")
    st.write("- Data Warehouse")
    st.write("- Communication Skills")
    st.write("- Apache")

with col2:
    st.success("Recommended Skills")
    st.write("- Ontology")
    st.write("- Graph Databases")
    st.write("- Disaster Recovery")
    st.write("- Terraform")
    st.write("- Spark")
    st.write("- Software Development")
    st.write("- Scalability")
    st.write("- SI")
    st.write("- Machine Learning")
    st.write("- Kubernetes")
    st.write("- Jenkins")
    st.write("- Hadoop")
    st.write("- Google Cloud Platform")
    st.write("- GitHub")
    st.write("- Generative AI")
    st.write("- Docker")
    st.write("- DevOps")
    st.write("- Databases")
    st.write("- Data Visualization")
    st.write("- Data Science")
    st.write("- Data Pipelines")
    st.write("- Data Management")
    st.write("- CI/CD")
    st.write("- Big Data")
    st.write("- Analytics")
    st.write("- Elasticsearch")
    st.write("- Algorithms")
    st.write("- AWS")
    st.write("- APIs")
    st.write("- AI")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
