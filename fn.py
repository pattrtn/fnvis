import streamlit as st
import pandas as pd
import plotly.express as px

# Data Preparation
data = {
    "CNTSCHID": [76400001, 76400001, 76400001, 76400001, 76400001],
    "CNTSTUID": [76400396, 76400632, 76400865, 76400936, 76401306],
    "ST004D01T": [2, 1, 1, 2, 1],  # Gender: 1 = Female, 2 = Male
    "PV1MATH": [376.167, 374.905, 439.850, 430.583, 279.361],
    "PV1READ": [255.171, 453.844, 423.108, 444.154, 320.895],
    "PV1SCIE": [391.449, 385.540, 481.047, 413.090, 315.831],
}
df = pd.DataFrame(data)
df['Gender'] = df['ST004D01T'].map({1: 'Female', 2: 'Male'})

# Streamlit App
st.title("PISA Score Dashboard")

# Dropdown to Select Gender
gender = st.selectbox("Select Gender", options=["All", "Male", "Female"])
if gender != "All":
    filtered_df = df[df['Gender'] == gender]
else:
    filtered_df = df

# Average Scores Bar Chart
st.subheader("Average Scores by Subject")
avg_scores = filtered_df[['PV1MATH', 'PV1READ', 'PV1SCIE']].mean()
bar_fig = px.bar(
    x=avg_scores.index,
    y=avg_scores.values,
    labels={"x": "Subjects", "y": "Average Score"},
    title="Average Scores by Subject",
)
st.plotly_chart(bar_fig)

# Scatter Plot for Math vs Reading
st.subheader("Mathematics vs Reading Scores")
scatter_fig = px.scatter(
    filtered_df,
    x="PV1MATH",
    y="PV1READ",
    color="Gender",
    labels={"PV1MATH": "Mathematics Score", "PV1READ": "Reading Score"},
    title="Math vs Reading Scores",
)
st.plotly_chart(scatter_fig)

# Data Table
st.subheader("Raw Data")
st.dataframe(filtered_df)
