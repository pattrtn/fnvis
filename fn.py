import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into a DataFrame
data = {
    'CNTSCHID': [76400001, 76400001, 76400001, 76400001, 76400001],
    'CNTSTUID': [76400396, 76400632, 76400865, 76400936, 76401306],
    'ST001D01T': [11, 10, 10, 10, 10],
    'ST003D02T': [8, 1, 11, 2, 7],
    'ST003D03T': [2006, 2007, 2006, 2007, 2006],
    'ST004D01T': [2, 1, 1, 2, 1],
    'ST250D06JA': [7640001, 7640002, 7640001, 7640001, 7640001],
    'ST250D07JA': [7640002, 7640002, 7640002, 7640002, 7640002],
    'PV1MATH': [376.167, 374.905, 439.850, 430.583, 279.361],
    'PV1READ': [255.171, 453.844, 423.108, 444.154, 320.895],
    'PV1SCIE': [391.449, 385.540, 481.047, 413.090, 315.831]
}
df = pd.DataFrame(data)

# Streamlit app layout
st.title('Educational Data Analysis Dashboard')

# Display raw data table
st.subheader('Raw Data')
st.write(df)

# Data Exploration Section
st.subheader('Explore Data')
year_filter = st.selectbox('Select Year', df['ST003D03T'].unique())
filtered_data = df[df['ST003D03T'] == year_filter]
st.write(f"Data for the year {year_filter}:")
st.write(filtered_data)

# Statistics Section
st.subheader('Basic Statistics')
st.write("Summary Statistics:")
st.write(df.describe())

# Scatter Plot of PV1MATH vs PV1READ
st.subheader('Scatter Plot of PV1MATH vs PV1READ')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='PV1MATH', y='PV1READ', ax=ax)
ax.set_title('PV1MATH vs PV1READ')
st.pyplot(fig)

# Bar plot of PV1MATH, PV1READ, and PV1SCIE
st.subheader('Bar Plot of PV1MATH, PV1READ, and PV1SCIE')
df_long = pd.melt(df, id_vars=['CNTSTUID'], value_vars=['PV1MATH', 'PV1READ', 'PV1SCIE'], var_name='Subject', value_name='Score')
fig, ax = plt.subplots()
sns.barplot(x='CNTSTUID', y='Score', hue='Subject', data=df_long, ax=ax)
ax.set_title('Scores by Subject')
st.pyplot(fig)

# Correlation heatmap
st.subheader('Correlation Heatmap')
corr = df[['PV1MATH', 'PV1READ', 'PV1SCIE']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)

# Sidebar for interaction
st.sidebar.header('Filters')
selected_student = st.sidebar.selectbox('Select Student', df['CNTSTUID'].unique())
student_data = df[df['CNTSTUID'] == selected_student]
st.sidebar.write(f"Data for Student {selected_student}:")
st.sidebar.write(student_data)
