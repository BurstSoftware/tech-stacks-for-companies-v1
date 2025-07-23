import streamlit as st

# Title and Job Details
st.title("Data Scientist Application")
st.subheader("Position: Remote")
st.write("Salary Range: $145,000 - $180,000 per year")

# Job Description
st.write("""
This page is designed to help you prepare for the Data Scientist role. Below are the recommended skills and education requirements.
""")

# Skills Section
st.header("Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- Teaching")
    st.write("- Software Deployment")
    st.write("- SQL")
    st.write("- R")
    st.write("- Python")

with col2:
    st.write("- Public Speaking")
    st.write("- MLOps")
    st.write("- JavaScript")
    st.write("- Data Visualization")
    st.write("- Data Science")
    st.write("- APIs")
    st.write("- AI")

# Education Section
st.header("Education Requirements")
st.write("- Master's Degree")
st.write("- Bachelor's Degree")

# Apply Button
st.button("Apply on company site")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack and education above!")
