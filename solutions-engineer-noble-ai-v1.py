import streamlit as st

# App title
st.set_page_config(page_title="Solutions Engineer - NobleAI", layout="wide")

st.title("🚀 Solutions Engineer - NobleAI")
st.write("This interactive tool outlines the key technologies and processes used in the role.")

# Tools & Technologies
st.header("🛠️ Key Tools & Technologies")
tools = [
    "Python", "Scikit-learn", "Predictive Analytics", "Software Implementation",
    "Software Deployment", "SaaS", "Pandas", "Machine Learning", "JavaScript",
    "Flask", "Enterprise Software", "Data Science", "Data Analytics",
    "Back-end Development", "AI"
]
selected_tools = st.multiselect("Select the tools you're familiar with:", tools)

# Process Overview
st.header("📌 Key Processes")
st.markdown("""
1. **AI & Data Science Solutions**  
   - Use **Machine Learning** and **Predictive Analytics** to drive AI-powered insights.  
   - Work with **Scikit-learn**, **Pandas**, and **Python** to analyze datasets.  

2. **Software Implementation & Deployment**  
   - Deploy **SaaS** solutions and integrate **enterprise software** into existing workflows.  
   - Use **Flask** and **JavaScript** for back-end and web applications.  

3. **Customer Engagement & Technical Support**  
   - Act as a **technical advisor** for AI solutions.  
   - Support clients in the **Oil & Gas** sector by optimizing workflows.  

4. **Collaboration & Communication**  
   - Work with **Sales, AI Research, and Product Teams** to ensure smooth implementation.  
   - Provide technical demos and support.  
""")

# Feedback Section
st.header("💡 Your Feedback")
feedback = st.text_area("What additional tools or processes would you like to explore?")
if st.button("Submit Feedback"):
    st.success("Thank you for your input!")

# Footer
st.write("---")
st.write("🔗 [Visit NobleAI Website](https://www.noble.ai)")
