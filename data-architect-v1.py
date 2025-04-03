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
    # Tech stack related to Skills Required
    st.markdown("**Tech Stack**:")
    st.markdown("- Snowflake")
    st.markdown("- Databricks")
    st.markdown("- dbt")
    st.markdown("- AWS/Azure/GCP")
    st.markdown("- SQL")
    st.markdown("- Python")
    st.markdown("- Git")

# Main content
if page == "Guide":
    st.title("Data Architect Guide")
    
    # Key Tasks and Responsibilities section
    st.header("Key Tasks and Responsibilities")
    st.markdown("""
    - **Data Architecture Design**: Create and maintain Snowflake data models aligned with business needs  
      *Resource*: [Snowflake Documentation](https://docs.snowflake.com/)
    - **Master Data Management (MDM)**: Collaborate with MDM team to optimize data architecture  
      *Resource*: [MDM Basics](https://www.informatica.com/resources-mdm.html)
    - **Data Integration & ETL**: Design and manage end-to-end ETL/ELT pipelines  
      *Resource*: [dbt Learn](https://docs.getdbt.com/docs/introduction)
    - **Data Governance & Security**: Establish and enforce data policies  
      *Resource*: [AWS Data Governance](https://aws.amazon.com/data-governance/)
    - **Data Modeling**: Design enterprise-level data models  
      *Resource*: [Data Modeling Tutorial](https://www.datacamp.com/tutorial/data-modeling)
    - **Performance Optimization**: Monitor and optimize data processes  
      *Resource*: [Snowflake Performance Tuning](https://docs.snowflake.com/en/user-guide/performance-optimizing)
    - **Issue Resolution**: Investigate and resolve data-related problems  
      *Resource*: [Python Debugging](https://realpython.com/python-debugging-pdb/)
    """)
    
    # Skills Required section
    st.header("Skills Required")
    st.markdown("""
    - **Cloud Platforms**: Expert in Snowflake, Databricks, AWS/Azure/GCP  
      *Resource*: [Snowflake Training](https://www.snowflake.com/training/), [Databricks Academy](https://www.databricks.com/learn/training)
    - **dbt**: Proficiency in data transformation pipelines  
      *Resource*: [dbt Fundamentals](https://courses.getdbt.com/)
    - **MDM Knowledge**: Understanding of data governance and quality management  
      *Resource*: [Informatica MDM Guide](https://www.informatica.com/products/master-data-management.html)
    - **Data Warehousing/Data Lake**: Design and management expertise  
      *Resource*: [AWS Data Lake](https://aws.amazon.com/big-data/datalakes-and-analytics/)
    - **SQL**: Advanced data manipulation skills  
      *Resource*: [SQL Tutorial](https://www.w3schools.com/sql/)
    - **Scripting**: Proficiency in Python, Shell, and Git  
      *Resource*: [Python for Data](https://www.coursera.org/learn/python-for-data-science), [Git Docs](https://git-scm.com/doc)
    - **Data Modeling**: Expert in dimensional and star/snowflake schemas  
      *Resource*: [Star Schema Guide](https://www.datacamp.com/tutorial/introduction-to-star-schema)
    - **Data Integration**: Experience with ETL tools like ADF, Fivetran  
      *Resource*: [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/)
    - **Collaboration**: Strong communication and leadership skills  
      *Resource*: [Leadership Skills](https://www.coursera.org/learn/leadership-skills)
    - **Analytical Thinking**: Problem-solving capabilities  
      *Resource*: [Problem Solving](https://www.edx.org/learn/problem-solving)
    """)
    
    # Tool Design Overview section
    st.header("Tool Design Overview")
    st.markdown("""
    This tool is designed to help aspiring Data Architects:
    - Assess their proficiency across key skills
    - Access targeted learning resources
    - Understand job responsibilities and required technologies
    - The interface uses a simple sidebar for navigation and tech stack reference
    """)
    
    # Tech Stack Integration section
    st.header("Tech Stack Integration")
    st.markdown("""
    The tech stack integrates seamlessly for Data Architect tasks:
    - **Snowflake + Databricks**: Core data warehousing and processing  
      *Resource*: [Snowflake-Databricks Integration](https://www.databricks.com/solutions/data-warehousing/snowflake)
    - **dbt + SQL**: Data transformation and querying  
      *Resource*: [dbt with SQL](https://docs.getdbt.com/docs/building-a-dbt-project)
    - **AWS/Azure/GCP**: Cloud infrastructure and services  
      *Resource*: [AWS for Data](https://aws.amazon.com/big-data/)
    - **Python + Git**: Automation and version control  
      *Resource*: [Python with Git](https://realpython.com/python-git-github-intro/)
    """)
    
    # Implementation Notes section
    st.header("Implementation Notes")
    st.markdown("""
    - Built using only Streamlit and datetime for simplicity
    - Static links provided due to limited import constraints
    - Future enhancements could include:
      - Interactive skill assessment sliders
      - Dynamic resource fetching
      - Job description analysis
    - Current version focuses on educational content delivery
    """)
