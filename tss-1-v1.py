import streamlit as st

# Set page configuration
st.set_page_config(page_title="Technical Support Specialist I - Job Description", layout="wide")

# Title and introduction
st.title("Technical Support Specialist I - Job Description")
st.markdown("""
Are you a tech-savvy problem-solver with a passion for helping others? Spherion Staffing is seeking a **Technical Support Specialist I** for a direct-hire, full-time, hybrid position in Mankato, MN. This is an excellent opportunity to join a dynamic team and make a real impact! Below are the key responsibilities for this role, organized by category.
""")

# Collapsible sections for responsibilities
st.header("Responsibilities")

with st.expander("Technical & Business Analysis"):
    st.markdown("""
    - Become proficient in web technologies and web-based applications.
    - Learn to create and troubleshoot communication within IoT systems.
    - Perform hands-on software setup and configuration.
    - Understand and troubleshoot low voltage control and alarm circuits.
    - Assist with compliance research and monitoring for regulations (e.g., REACH, RoHS, Prop 65, PFAS, TSCA).
    """)

with st.expander("Client Support"):
    st.markdown("""
    - Gather and track client information and data accurately.
    - Provide technical support to external customers via phone, email, or online case management system.
    - Enter support requests into the case management system, update statuses, and log detailed resolutions.
    - Perform hands-on hardware and software application setup and configuration.
    - Communicate hardware/software installation procedures and application configuration tasks clearly.
    - Proactively address customer issues and educate clients.
    - Identify opportunities for additional solutions within customer environments and share with account managers/sales staff.
    - Assist with Return Material Authorizations and field sales calls.
    """)

with st.expander("Testing and Training"):
    st.markdown("""
    - Conduct quality assurance testing for new product releases and client-specific feature requests.
    - Coordinate and support user acceptance testing and issue resolution with clients and the development team.
    - Provide software application training to clients for new features and enhancements.
    """)

# Additional job details section
st.header("Additional Job Details")
if st.button("Show Job Details"):
    st.subheader("Working Hours")
    st.write("7:00 AM - 4:00 PM")

    st.subheader("Skills")
    st.markdown("""
    - Located within 25 miles of Mankato, MN.
    - Familiarity with database management.
    - Knowledge of IoT API.
    - Proficiency with Microsoft Word, Excel, PowerPoint, and Outlook.
    """)

    st.subheader("Education")
    st.write("High School")

    st.subheader("Experience")
    st.write("1-4 years")

    st.subheader("Qualifications")
    st.markdown("""
    - Electronics troubleshooting experience.
    - Ability to provide detailed documentation with troubleshooting steps.
    - Excellent attention to detail and strong follow-through skills.
    - Exceptional written and verbal communication skills.
    - Excellent problem-solving skills.
    - Ability to work both independently and as a member of a team.
    - Flexibility for travel up to 10% of the time.
    """)

# Footer
st.markdown("---")
st.write("For more information, contact Spherion Staffing or visit their career portal.")
