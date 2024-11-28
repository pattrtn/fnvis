import streamlit as st
import pandas as pd
import plotly.express as px

# Prepare the data
data = {
    "CNTSCHID": [76400001, 76400001, 76400001, 76400001, 76400001],
    "CNTSTUID": [76400396, 76400632, 76400865, 76400936, 76401306],
    "ST004D01T": [2, 1, 1, 2, 1],  # Gender: 1 = Female, 2 = Male
    "PV1MATH": [376.167, 374.905, 439.850, 430.583, 279.361],
    "PV1READ": [255.171, 453.844, 423.108, 444.154, 320.895],
    "PV1SCIE": [391.449, 385.540, 481.047, 413.090, 315.831],
    "ST003D03T": [2006, 2007, 2006, 2007, 2006],  # Year of birth
}
df = pd.DataFrame(data)
df['Gender'] = df['ST004D01T'].map({1: 'Female', 2: 'Male'})

# Streamlit App
st.title("Interactive Streamlit Dashboard")
st.markdown("This dashboard visualizes PISA scores by gender and subjects.")

# Sidebar Filters
st.sidebar.header("Filters")
selected_gender = st.sidebar.radio("Select Gender", options=["All", "Male", "Female"])
selected_subjects = st.sidebar.multiselect(
    "Select Subjects to Display",
    options=["PV1MATH", "PV1READ", "PV1SCIE"],
    default=["PV1MATH", "PV1READ", "PV1SCIE"],
)

# Apply Filters
filtered_df = df if selected_gender == "All" else df[df["Gender"] == selected_gender]

# Interactive Box Plot
st.subheader("Box Plot of Scores by Gender")
if selected_subjects:
    melted_df = filtered_df.melt(
        id_vars=["Gender"],
        value_vars=selected_subjects,
        var_name="Subject",
        value_name="Score",
    )
    box_fig = px.box(
        melted_df,
        x="Subject",
        y="Score",
        color="Gender",
        color_discrete_sequence=px.colors.qualitative.Safe,
        title="Box Plot of Selected Subjects by Gender",
    )
    st.plotly_chart(box_fig)
else:
    st.warning("Please select at least one subject to display the box plot.")

# Scatter Plot
st.subheader("Scatter Plot of Mathematics vs Reading")
scatter_fig = px.scatter(
    filtered_df,
    x="PV1MATH",
    y="PV1READ",
    color="Gender",
    size="PV1SCIE",
    hover_data=["CNTSTUID"],
    labels={"PV1MATH": "Mathematics Score", "PV1READ": "Reading Score"},
    title="Scatter Plot of Math vs Reading (Size = Science Score)",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
st.plotly_chart(scatter_fig)

# Average Scores Bar Chart
st.subheader("Average Scores by Subject")
if selected_subjects:
    avg_scores = filtered_df[selected_subjects].mean()
    bar_fig = px.bar(
        x=avg_scores.index,
        y=avg_scores.values,
        labels={"x": "Subject", "y": "Average Score"},
        color=avg_scores.index,
        title="Average Scores for Selected Subjects",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    st.plotly_chart(bar_fig)

# Data Table
st.subheader("Raw Data Table")
st.dataframe(filtered_df)

# Download Button
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv",
)
