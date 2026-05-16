import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="Automation Dashboard",
    layout="wide"
)

# TITLE
st.title("📊 Automation Pipeline Dashboard")

# LOAD DATA
df = pd.read_csv("data/automation_logs.csv")

# METRICS
total = len(df)

success = len(df[df["status"] == "success"])

errors = len(df[df["status"] == "error"])

success_rate = (success / total) * 100

# CARDS
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Products", total)

col2.metric("Success", success)

col3.metric("Errors", errors)

col4.metric("Success Rate", f"{success_rate:.2f}%")

# Line visual
st.divider()

# ERRORS TABLE
st.subheader("❌ Error Logs")

errors_df = df[df["status"] == "error"]

st.dataframe(errors_df)