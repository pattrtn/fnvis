import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data for mapping
geo_data_path = 'pisa-pisa.csv'  # Adjust the path if necessary
try:
    df = pd.read_csv(geo_data_path, encoding='utf-8')
except FileNotFoundError:
    st.error(f"The file '{geo_data_path}' was not found. Please check the file path.")
    st.stop()  # Stop further execution

# Display columns in the data to ensure proper loading
st.write("Columns in the dataset:", df.columns)

# Check for missing values
st.write("Missing values in the dataset:", df.isnull().sum())

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
