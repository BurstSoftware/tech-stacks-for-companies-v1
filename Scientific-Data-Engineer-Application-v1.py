import streamlit as st

# Title and Job Details
st.title("Scientific Data Engineer Application")
st.subheader("Position: Remote, Full-time")

# Job Description
st.write("""
This page is designed to help you prepare for the Scientific Data Engineer role. Below are the required and recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- SQL")
    st.write("- Python")

with col2:
    st.success("Recommended Skills")
    st.write("- Tableau")
    st.write("- Product Management")
    st.write("- Jupyter")
    st.write("- Data Modeling")
    st.write("- Data Analytics")
    st.write("- Communication Skills")
    st.write("- AI")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
