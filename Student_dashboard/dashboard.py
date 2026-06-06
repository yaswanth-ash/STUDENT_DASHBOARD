import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Dashboard")

st.title("📊 Student Performance Dashboard")

df = pd.read_csv("students.csv")

st.subheader("Student Data")
st.dataframe(df)

avg_marks = df["Marks"].mean()
avg_attendance = df["Attendance"].mean()

col1, col2 = st.columns(2)

with col1:
    st.metric("Average Marks", round(avg_marks, 2))

with col2:
    st.metric("Average Attendance", round(avg_attendance, 2))

st.subheader("Marks Analysis")

fig1 = px.bar(
    df,
    x="Name",
    y="Marks",
    title="Student Marks"
)

st.plotly_chart(fig1)

st.subheader("Attendance Analysis")

fig2 = px.pie(
    df,
    values="Attendance",
    names="Name",
    title="Attendance Distribution"
)

st.plotly_chart(fig2)

student = st.selectbox(
    "Select Student",
    df["Name"]
)

selected = df[df["Name"] == student]

st.write(selected)