import streamlit as st
from datetime import datetime

# Set page configuration to wide layout
st.set_page_config(layout="wide")

# Sidebar setup
st.sidebar.title("Enterprise Data Architecture Hub")
st.sidebar.write("A centralized guide for data architects to manage strategy, governance, and modeling.")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Guide"])

# Sidebar current date
current_date = datetime.now().strftime("%B %d, %Y")
st.sidebar.write(f"**Current Date:** {current_date}")

# Sidebar tech stack
st.sidebar.write("**Tech Stack:**")
st.sidebar.write("- Python: [Learn More](https://docs.python.org/3/)")
st.sidebar.write("- SQL: [Learn More](https://www.w3schools.com/sql/)")
st.sidebar.write("- Cloud Platforms (AWS/Azure/GCP): [Learn More](https://aws.amazon.com/what-is-cloud-computing/)")
st.sidebar.write("- Streamlit: [Learn More](https://docs.streamlit.io/)")
st.sidebar.write("- Data Modeling Tools: [Learn More](https://www.erwin.com/data-modeling/)")

# Main content: Guide section
if page == "Guide":
    st.title("Enterprise Data Architecture Hub - Guide")
    
    # Key Tasks and Responsibilities
    st.header("1. Key Tasks and Responsibilities")
    st.markdown("""
    - **Develop Data Strategy**: Define long-term data architecture goals. [Resource](https://www.dataversity.net/data-strategy/)
    - **Data Governance**: Establish policies for data quality and security. [Resource](https://www.collibra.com/data-governance/)
    - **Data Modeling**: Create and manage conceptual, logical, and physical data models. [Resource](https://www.datamodel.com/)
    - **Cloud Integration**: Optimize data systems for cloud platforms. [Resource](https://aws.amazon.com/cloud-data-management/)
    - **Metadata Management**: Document and classify data assets. [Resource](https://www.alation.com/what-is-metadata-management/)
    """)
    
    # Skills Required
    st.header("2. Skills Required")
    st.markdown("""
    - **Data Architecture**: Expertise in designing scalable data systems. [Resource](https://www.coursera.org/learn/data-architecture)
    - **SQL Proficiency**: Advanced querying and database management. [Resource](https://www.sqlcourse.com/)
    - **Cloud Knowledge**: Familiarity with AWS, Azure, or GCP. [Resource](https://cloud.google.com/learn)
    - **Data Governance**: Understanding of compliance and policy frameworks. [Resource](https://www.isaca.org/resources/data-governance)
    - **Communication**: Ability to collaborate with stakeholders. [Resource](https://www.linkedin.com/learning/business-communication/)
    """)
    
    # Tool Design Overview
    st.header("3. Tool Design Overview")
    st.markdown("""
    The **Enterprise Data Architecture Hub** is a Streamlit-based tool designed to assist Enterprise Data Architects at a large bank. It provides a centralized guide for managing data strategy, governance, and modeling tasks. The tool is structured as a single-page application with a sidebar for navigation and a main 'Guide' section to outline key responsibilities, skills, and technical details.
    """)
    
    # Tech Stack Integration
    st.header("4. Tech Stack Integration")
    st.markdown("""
    - **Python**: Core language for scripting and automation, integrates with Streamlit for UI. [Resource](https://realpython.com/python-streamlit/)
    - **SQL**: Used for querying and managing relational databases, foundational for data modeling. [Resource](https://www.w3schools.com/sql/sql_intro.asp)
    - **Cloud Platforms**: Enable scalable data storage and processing, integrated via APIs. [Resource](https://azure.microsoft.com/en-us/services/)
    - **Streamlit**: Provides an interactive interface for data architects. [Resource](https://streamlit.io/gallery)
    - **Data Modeling Tools**: Support creation of ER diagrams and schemas, often integrated with SQL outputs. [Resource](https://www.visual-paradigm.com/guide/data-modeling/)
    """)
    
    # Implementation Notes
    st.header("5. Implementation Notes")
    st.markdown("""
    - **Construction**: Built with basic Streamlit tools (`st.write`, `st.markdown`, `st.sidebar`) and `datetime` for date display. No additional libraries are used to keep it lightweight.
    - **Potential Enhancements**: Add tabs for Data Asset Catalog, Data Modeling, and Governance (requires advanced Streamlit features like `st.tabs` in future iterations). Integrate with a database for dynamic data (requires libraries like SQLAlchemy). Enhance interactivity with user inputs (e.g., skill ratings) if imports are expanded.
    - **Limitations**: Static content due to limited imports; links are hardcoded markdown URLs.
    """)
