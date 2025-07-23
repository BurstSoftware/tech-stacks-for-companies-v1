import streamlit as st

# Title and Job Details
st.title("Software Engineer III - Data Applications Application")
st.subheader("Position: Remote, Full-time")

# Job Description
st.write("""
This page is designed to help you prepare for the Software Engineer III - Data Applications role. Below are the required and recommended skills and education requirements.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- Debugging")
    st.write("- Communication Skills")

with col2:
    st.success("Recommended Skills")
    st.write("- TypeScript")
    st.write("- SQL")
    st.write("- Python")
    st.write("- Plotly")
    st.write("- Node.js")
    st.write("- Integration Testing")
    st.write("- Google Cloud Platform")
    st.write("- Docker")
    st.write("- Distributed Systems")
    st.write("- Computer Science")
    st.write("- Cloud Infrastructure")
    st.write("- Azure")
    st.write("- Agile")
    st.write("- AI")

# Education Section
st.header("Education Requirements")
st.write("- Master's Degree")
st.write("- Bachelor's Degree")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack and education above!")
