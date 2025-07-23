import streamlit as st

# Title and Job Details
st.title("Staff Data Scientist Application")
st.subheader("Position: Brisbane, CA 94005 - Remote, Full-time")
st.write("Salary Range: $161,000 - $185,000 per year")

# Job Description
st.write("""
This page is designed to help you prepare for the Staff Data Scientist role. Below are the recommended skills to align with the job qualifications.
""")

# Skills Section
st.header("Recommended Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- Signal Processing")
    st.write("- SQL")
    st.write("- Research")
    st.write("- Regression Analysis")
    st.write("- Pandas")
    st.write("- Organizational Skills")

with col2:
    st.write("- Model Deployment")
    st.write("- Machine Learning")
    st.write("- Hidden Markov Models")
    st.write("- Data Science")
    st.write("- Communication Skills")
    st.write("- AI")

# Apply Button
st.button("Apply Now")

# Footer
st.write("Prepare your profile and showcase your expertise in the tech stack above!")
