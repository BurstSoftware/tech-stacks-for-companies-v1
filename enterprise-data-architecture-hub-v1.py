import streamlit as st
from datetime import datetime

# Set wide layout
st.set_page_config(layout="wide")

# Sidebar setup
st.sidebar.title("Enterprise Data Architecture Hub")
st.sidebar.markdown("[Insert Sidebar Description]: A tool to centralize data strategy, governance, and modeling for enterprise data architects at a large bank.")

# Current date in sidebar
st.sidebar.markdown(f"**Current Date:** {datetime.now().strftime('%B %d, %Y')}")

# Sidebar Tech Stack & Resources
st.sidebar.markdown("### Tech Stack & Resources")
st.sidebar.markdown("""
- Streamlit ([https://docs.streamlit.io/](https://docs.streamlit.io/))  
- Python ([https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/))  
- SQLAlchemy ([https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/))  
- PostgreSQL ([https://www.postgresql.org/docs/](https://www.postgresql.org/docs/))  
- Plotly ([https://plotly.com/python/](https://plotly.com/python/))  
""")

# Navigation (only Guide section)
st.sidebar.markdown("### Navigation")
st.sidebar.markdown("- Guide")

# Main Guide Section
st.title("Enterprise Data Architecture Hub - Guide")

# Key Tasks and Responsibilities
st.header("Key Tasks and Responsibilities")
st.markdown("""
- **Discover, Document, and Classify Data Assets**: Maintain a catalog of data assets across platforms.  
  Resource: [Data Catalog Basics](https://www.datacamp.com/tutorial/data-catalogs)  
- **Develop Data Blueprints and Models**: Create conceptual, logical, and physical data models.  
  Resource: [Data Modeling Tutorial](https://www.guru99.com/data-modelling.html)  
- **Define Architecture Standards and Policies**: Establish guidelines for data governance and consistency.  
  Resource: [Data Governance Guide](https://www.dataversity.net/data-governance-best-practices/)  
- **Manage Technology Landscape**: Plan and roadmap data platforms and tools.  
  Resource: [Enterprise Architecture Basics](https://www.cio.com/article/2439128/enterprise-architecture-basics.html)  
- **Ensure Data Governance and Security**: Implement rules and controls for data access and lifecycle.  
  Resource: [Data Security Best Practices](https://www.imperva.com/learn/data-security/)  
- **Optimize Cloud Data Management**: Enhance performance and cost-effectiveness in cloud environments.  
  Resource: [Cloud Data Management](https://www.talend.com/resources/cloud-data-management/)
""")

# Skills Required
st.header("Skills Required")
st.markdown("""
- **Data Modeling**: Proficiency in designing data structures.  
  Resource: [Learn Data Modeling](https://www.datacamp.com/courses/data-modeling)  
- **Data Governance**: Knowledge of policies and compliance.  
  Resource: [Data Governance Training](https://www.edx.org/learn/data-governance)  
- **Cloud Platforms**: Experience with AWS, Azure, or GCP.  
  Resource: [Cloud Computing Basics](https://aws.amazon.com/training/)  
- **Python Programming**: Backend logic and data manipulation skills.  
  Resource: [Python Tutorial](https://www.w3schools.com/python/)  
- **SQL and Databases**: Querying and managing relational databases.  
  Resource: [SQL Basics](https://www.khanacademy.org/computing/computer-programming/sql)
""")

# Tool Design Overview
st.header("Tool Design Overview")
design_input = st.text_area("Proposed Tool Design", height=200, value="")
if design_input:
    st.markdown(design_input)
else:
    st.markdown("Paste your Proposed Tool Design here to view it.")

st.markdown("""
**Purpose**: Centralize data strategy, governance, and modeling for enterprise data architects, supporting tasks like metadata management, data modeling, and cloud optimization.
""")

# Tech Stack Integration
st.header("Tech Stack Integration")
st.markdown("""
- **Streamlit + Python**: Streamlit provides the UI, while Python handles backend logic and data processing.  
  Resource: [Streamlit with Python](https://docs.streamlit.io/library/get-started)  
- **SQLAlchemy + PostgreSQL**: SQLAlchemy integrates with PostgreSQL for structured data storage and querying.  
  Resource: [SQLAlchemy with PostgreSQL](https://docs.sqlalchemy.org/en/20/orm/)  
- **Plotly**: Enhances visualization of data models and lineage diagrams.  
  Resource: [Plotly Integration](https://plotly.com/python/getting-started/)
""")

# Implementation Notes
st.header("Implementation Notes")
st.markdown("""
- **Construction**: Built with Streamlit for a simple, interactive UI and Python for logic. Uses static links due to limited imports.  
- **Enhancements**: Add authentication, caching, and dynamic data connections with additional libraries like SQLAlchemy or OAuth2.  
- **Limitations**: Current version lacks real-time data fetching or advanced visuals due to import constraints.
""")
