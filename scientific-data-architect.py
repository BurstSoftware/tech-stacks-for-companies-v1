import streamlit as st

# Title and Job Details
st.title("Scientific Data Architect - Bay Area Application")
st.subheader("Position: San Francisco, CA - Remote, Full-time")

# Job Description
st.write("""
This page is designed to help you prepare for the Scientific Data Architect - Bay Area role. Below are the required and recommended skills and education requirements.
""")

# Skills Section
st.header("Required and Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.success("Required Skills")
    st.write("- AI")

with col2:
    st.success("Recommended Skills")
    st.write("- Software Troubleshooting")
    st.write("- Python")
    st.write("- JSON")
    st.write("- Drug Discovery")
    st.write("- AWS")
    st.write("- APIs")

# Education Section
st.header("Education Requirements")
st.write("- Master's Degree")
st.write("- Doctoral Degree (Required)")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack and education above!")
