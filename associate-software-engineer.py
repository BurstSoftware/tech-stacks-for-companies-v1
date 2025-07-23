import streamlit as st
from datetime import datetime

# Title and Job Details
st.title("Associate Software Engineer - Data Intelligence Application")
st.subheader("Position: New York, NY - Remote")
st.write("Salary Range: $93,000 - $145,000 per year")
st.write(f"Last Updated: {datetime.now().strftime('%I:%M %p CDT, %B %d, %Y')}")

# Job Description
st.write("""
This page is designed to help you prepare for the Associate Software Engineer - Data Intelligence role. Below are the recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- Python")
    st.write("- Data Science")

with col2:
    st.write("- Big Data")
    st.write("- AI")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
