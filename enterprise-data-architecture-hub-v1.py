import streamlit as st
from datetime import datetime

# Set wide layout
st.set_page_config(layout="wide")

# Sidebar setup
st.sidebar.title("Enterprise Data Architecture Hub")
st.sidebar.markdown("A centralized tool for data strategy, governance, and modeling across enterprise platforms.")

# Current date in sidebar
st.sidebar.markdown(f"**Current Date:** {datetime.now().strftime('%B %d, %Y')}")

# Sidebar navigation
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio("Go to", ["Guide"])

# Tech Stack & Resources in sidebar
st.sidebar.markdown("### Tech Stack & Resources")
st.sidebar.markdown("""
- Streamlit ([https://docs.streamlit.io](https://docs.streamlit.io))
- Python ([https://docs.python.org/3/](https://docs.python.org/3/))
- SQLAlchemy ([https://docs.sqlalchemy.org](https://docs.sqlalchemy.org))
- PostgreSQL ([https://www.postgresql.org/docs/](https://www.postgresql.org/docs/))
- Plotly ([https://plotly.com/python/](https://plotly.com/python/))
""")

# Main content - Guide section
if page == "Guide":
    st.title("Enterprise Data Architecture Hub - Guide")

    # Key Tasks and Responsibilities
    st.header("Key Tasks and Responsibilities")
    st.markdown("""
    - **Discover and document data assets**: Manage data asset catalog and metadata ([Streamlit Data Display](https://docs.streamlit.io/library/api-reference/data)).
    - **Develop data models**: Create and manage conceptual, logical, and physical data models ([SQLAlchemy Models](https://docs.sqlalchemy.org/en/20/orm/)).
    - **Define architecture standards**: Establish data governance and policies ([Data Governance Basics](https://www.dataversity.net/data-governance-basics/)).
    - **Plan technology roadmap**: Assess and integrate data platforms ([Enterprise Architecture Guide](https://www.gartner.com/en/information-technology/insights/enterprise-architecture)).
    - **Ensure data security**: Implement governance and access controls ([Python Security Best Practices](https://docs.python.org/3/library/security.html)).
    """)

    # Skills Required
    st.header("Skills Required")
    st.markdown("""
    - **Data Modeling**: Proficiency in ER and UML modeling ([ERD Tutorial](https://www.lucidchart.com/pages/er-diagrams)).
    - **Python Programming**: Backend logic and scripting ([Python Tutorial](https://docs.python.org/3/tutorial/)).
    - **SQL/Database Management**: Querying and schema design ([PostgreSQL Docs](https://www.postgresql.org/docs/)).
    - **Cloud Platforms**: Knowledge of AWS, Azure, or GCP ([AWS Data Services](https://aws.amazon.com/big-data/)).
    - **Data Governance**: Understanding policies and compliance ([Data Governance Framework](https://www.collibra.com/data-governance-what-it-is/)).
    """)

    # Tool Design Overview
    st.header("Tool Design Overview")
    design_input = st.text_area("Proposed Tool Design", height=200, value="")
    if design_input:
        st.markdown(design_input)
    else:
        st.markdown("Paste your Proposed Tool Design here to view it.")

    # Tech Stack Integration
    st.header("Tech Stack Integration")
    st.markdown("""
    - **Streamlit + Python**: Builds the UI and handles logic ([Streamlit with Python](https://docs.streamlit.io)).
    - **SQLAlchemy + PostgreSQL**: Manages data models and metadata storage ([SQLAlchemy Integration](https://docs.sqlalchemy.org/en/20/orm/)).
    - **Plotly**: Visualizes data models and lineage ([Plotly Python](https://plotly.com/python/)).
    - **Authentication**: Integrates with OAuth2 or LDAP for security ([Python OAuth2](https://oauthlib.readthedocs.io/)).
    """)

    # Implementation Notes
    st.header("Implementation Notes")
    st.markdown("""
    - **Construction**: Built with Streamlit for rapid UI development and Python for backend logic. Uses a simple layout with sidebar navigation.
    - **Enhancements**: Add tabs for each core functionality (e.g., Data Asset Catalog, Data Modeling) using st.tabs when available in basic Streamlit. Integrate with a database for persistent storage and caching for performance ([Streamlit Caching](https://docs.streamlit.io/library/api-reference/performance)).
    - **Future Steps**: Incorporate interactive visualizations and authentication for enterprise use.
    """)
