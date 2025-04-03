import streamlit as st
from datetime import datetime

# Set wide layout
st.set_page_config(layout="wide")

# Sidebar setup
with st.sidebar:
    st.title("Data Architect")
    st.markdown("A tool to help assess and improve skills for Data Architect roles")
    # Navigation
    page = st.radio("Navigation", ["Guide"])
    # Current date in sidebar
    st.markdown(f"**Current Date**: {datetime.now().strftime('%B %d, %Y')}")
    # Tech stack in sidebar
    st.markdown("**Tech Stack**:")
    st.markdown("- Streamlit")
    st.markdown("- datetime")

# Main content
if page == "Guide":
    st.title("Data Architect Guide")
    
    # Key Tasks and Responsibilities section
    st.header("Key Tasks and Responsibilities")
    st.markdown("""
    - **Data Architecture Design**: Create and maintain Snowflake data models aligned with business needs
    - **Master Data Management (MDM)**: Collaborate with MDM team to optimize data architecture
    - **Data Integration & ETL**: Design and manage end-to-end ETL/ELT pipelines
    - **Data Governance & Security**: Establish and enforce data policies
    - **Data Modeling**: Design enterprise-level data models
    - **Performance Optimization**: Monitor and optimize data processes
    - **Issue Resolution**: Investigate and resolve data-related problems
    """)
    
    # Skills Required section
    st.header("Skills Required")
    st.markdown("""
    - **Cloud Platforms**: Expert in Snowflake, Databricks, AWS/Azure/GCP
    - **dbt**: Proficiency in data transformation pipelines
    - **MDM Knowledge**: Understanding of data governance and quality management
    - **Data Warehousing/Data Lake**: Design and management expertise
    - **SQL**: Advanced data manipulation skills
    - **Scripting**: Proficiency in Python, Shell, and Git
    - **Data Modeling**: Expert in dimensional and star/snowflake schemas
    - **Data Integration**: Experience with ETL tools like ADF, Fivetran
    - **Collaboration**: Strong communication and leadership skills
    - **Analytical Thinking**: Problem-solving capabilities
    """)
