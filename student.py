import streamlit as st
import pandas as pd

# ----------------------
# Sample Data Creation
# ----------------------
data = {
    "Student Name": ["Vyas chandrasekar", "Joshika", "Aravind", "Susweatha", "Taran", "Sanjay"],
    "Course": ["AI & ML", "Data Science", "Data Analytics", "Data Analytics", "Data Science", "Data Analytics"],
    "Mode": ["OFFLINE", "OFFLINE", "OFFLINE", "OFFLINE", "ONLINE", "OFFLINE"],
    "Difficulty": ["MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM"],
    "Performance (%)": [75, 85, 85, 70, 80, 75]
}

df = pd.DataFrame(data)

# ----------------------
# Streamlit UI
# ----------------------
st.set_page_config(page_title="Student Dashboard", layout="wide")

st.title("📊 Student Performance Dashboard")

# ----------------------
# Sidebar Filters
# ----------------------
st.sidebar.header("Filters")

course_filter = st.sidebar.multiselect("Select Course", df["Course"].unique(), default=df["Course"].unique())
mode_filter = st.sidebar.multiselect("Select Mode", df["Mode"].unique(), default=df["Mode"].unique())

filtered_df = df[(df["Course"].isin(course_filter)) & (df["Mode"].isin(mode_filter))]

# ----------------------
# KPI Metrics
# ----------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(filtered_df))
col2.metric("Average Performance", f"{filtered_df['Performance (%)'].mean():.2f}%" if filtered_df['Performance (%)'].notna().any() else "N/A")
col3.metric("Top Performance", f"{filtered_df['Performance (%)'].max()}%" if filtered_df['Performance (%)'].notna().any() else "N/A")

# ----------------------
# Table View
# ----------------------
st.subheader("📋 Student Data")
st.dataframe(filtered_df)

# ----------------------
# Charts
# ----------------------
st.subheader("📈 Performance by Student")
st.bar_chart(filtered_df.set_index("Student Name")["Performance (%)"])

st.subheader("📊 Course Distribution")
st.bar_chart(filtered_df["Course"].value_counts())

# ----------------------
# Student Insights
# ----------------------
st.subheader("🏆 Top Performers")
top_students = filtered_df.sort_values(by="Performance (%)", ascending=False).head(3)
st.write(top_students)

st.subheader("⚠️ Needs Improvement")
low_students = filtered_df.sort_values(by="Performance (%)", ascending=True).head(3)
st.write(low_students)

# ----------------------
# Individual Student View
# ----------------------
st.subheader("🔍 Student Detail View")
student = st.selectbox("Select Student", df["Student Name"])

student_data = df[df["Student Name"] == student]
st.write(student_data)
