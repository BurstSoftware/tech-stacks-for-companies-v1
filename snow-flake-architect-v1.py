import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px

# --- Streamlit App Title ---
st.set_page_config(page_title="Snowflake Architect Dashboard", layout="wide")
st.title("❄️ Snowflake Data Engineering & Strategy Dashboard")

# --- Snowflake Connection Function ---
@st.cache_resource
def connect_snowflake():
    return snowflake.connector.connect(
        user="your_username",
        password="your_password",
        account="your_account"
    )

conn = connect_snowflake()

# --- Fetch Data Function ---
def fetch_data(query):
    cur = conn.cursor()
    cur.execute(query)
    return pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])

# --- Sidebar Navigation ---
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to", ["User Activity", "Warehouse Utilization", "Data Governance", "RBAC Monitoring"])

# --- User Activity & Credit Consumption ---
if menu == "User Activity":
    st.subheader("📊 User Activity & Credit Consumption")
    query = "SELECT user_name, query_text, execution_time, warehouse_size FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY ORDER BY start_time DESC LIMIT 50"
    df = fetch_data(query)
    st.dataframe(df)

    fig = px.bar(df, x="user_name", y="execution_time", title="Query Execution Time by User", color="warehouse_size")
    st.plotly_chart(fig)

# --- Warehouse Utilization & Workload Analysis ---
elif menu == "Warehouse Utilization":
    st.subheader("🏢 Warehouse Utilization & Workload Analysis")
    query = "SELECT warehouse_name, avg_load_percent, total_queries, credits_used FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_LOAD_HISTORY ORDER BY start_time DESC LIMIT 50"
    df = fetch_data(query)
    st.dataframe(df)

    fig = px.pie(df, values="credits_used", names="warehouse_name", title="Credits Used by Warehouse")
    st.plotly_chart(fig)

# --- Data Governance & Security ---
elif menu == "Data Governance":
    st.subheader("🔒 Data Governance & Security")
    query = "SELECT table_name, policy_name, policy_type FROM SNOWFLAKE.ACCOUNT_USAGE.POLICY_REFERENCES"
    df = fetch_data(query)
    st.dataframe(df)

    fig = px.bar(df, x="table_name", y="policy_type", title="Data Masking & Governance Policies", color="policy_name")
    st.plotly_chart(fig)

# --- Role-Based Access Control (RBAC) Monitoring ---
elif menu == "RBAC Monitoring":
    st.subheader("🔑 Role-Based Access Control (RBAC) Monitoring")
    query = "SELECT role_name, granted_to, privilege FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES"
    df = fetch_data(query)
    st.dataframe(df)

    fig = px.bar(df, x="role_name", y="privilege", title="RBAC Privileges by Role", color="granted_to")
    st.plotly_chart(fig)

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.markdown("🚀 **Developed by ChatGPT** | Snowflake Data Engineering")
