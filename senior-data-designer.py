import streamlit as st

# Title and Job Details
st.title("Senior Data Designer Application")
st.subheader("Position: Charlotte, NC - Remote")
st.write("Salary Range: $125,000 - $145,000 per year")

# Job Description
st.write("""
This page is designed to help you prepare for the Senior Data Designer role. Below are the required and recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- Power BI")
    st.write("- Microsoft Excel")
    st.write("- JavaScript")
    st.write("- Data Analysis")

with col2:
    st.success("Recommended Skills")
    st.write("- TypeScript")
    st.write("- Tableau")
    st.write("- Statistical Analysis")
    st.write("- SQL")
    st.write("- R")
    st.write("- Python")
    st.write("- Presentation Skills")
    st.write("- Google Cloud Platform")
    st.write("- Flask")
    st.write("- ETL")
    st.write("- Design Patterns")
    st.write("- Data Warehouse")
    st.write("- Data Governance")
    st.write("- D3.js")
    st.write("- Communication Skills")
    st.write("- Color Theory")
    st.write("- Cloud Infrastructure")
    st.write("- Cataloging")
    st.write("- Analytics")
    st.write("- Analysis Skills")
    st.write("- AWS")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
