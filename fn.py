import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sample DataFrame with the data structure
data = {
    'ST001D01T': [11, 10, 10, 10, 10],  # Grade level (7-12)
    'ST003D02T': [8, 1, 11, 2, 7],  # Month of birth
    'ST003D03T': [2006, 2007, 2006, 2007, 2006],  # Year of birth (AD)
    'ST004D01T': [2, 1, 2, 2, 1],  # Gender (1 = Female, 2 = Male)
    'ST250D06JA': [7640001, 7640002, 7640001, 7640002, 7640001],  # Smart TV ownership (1 = Yes, 2 = No)
    'ST250D07JA': [7640001, 7640002, 7640001, 7640002, 7640001],  # Air purifier ownership (1 = Yes, 2 = No)
    'PV1MATH': [376.167, 374.905, 439.850, 430.583, 279.361],  # Math score (out of 1000)
    'PV1READ': [255.171, 453.844, 423.108, 444.154, 320.895],  # Reading score (out of 1000)
    'PV1SCIE': [391.449, 385.540, 481.047, 413.090, 315.831]  # Science score (out of 1000)
}

df = pd.DataFrame(data)

# Streamlit App Layout
st.title('Colorblind-Friendly Educational Data Analysis Dashboard')

# Display raw data
st.subheader('Raw Data')
st.write(df)

# 1. Interactive Scatter Plot of Math vs Reading Scores
st.subheader('Math vs Reading Scores by Year of Birth')
fig_scatter = px.scatter(df, x='PV1MATH', y='PV1READ', color='ST003D03T', 
                         title='Math vs Reading Scores by Year of Birth', 
                         labels={'PV1MATH': 'Math Scores', 'PV1READ': 'Reading Scores'},
                         color_continuous_scale='Viridis')  # Colorblind-friendly color scale
st.plotly_chart(fig_scatter)

# 2. Bar Plot of Math, Reading, and Science Scores by Student
st.subheader('Scores by Subject for Each Year of Birth')
df_long = pd.melt(df, id_vars=['ST003D03T'], value_vars=['PV1MATH', 'PV1READ', 'PV1SCIE'], 
                  var_name='Subject', value_name='Score')

fig_bar = px.bar(df_long, x='ST003D03T', y='Score', color='Subject', 
                 title='Scores by Subject for Each Year of Birth', 
                 labels={'ST003D03T': 'Year of Birth', 'Score': 'Score'},
                 color_discrete_sequence=px.colors.qualitative.Set2)  # Colorblind-friendly palette
st.plotly_chart(fig_bar)

# 3. Correlation Heatmap
st.subheader('Correlation Heatmap of Scores')
corr = df[['PV1MATH', 'PV1READ', 'PV1SCIE']].corr()

fig_heatmap = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.columns,
    colorscale='Cividis'  # Colorblind-friendly color scale
))
fig_heatmap.update_layout(title='Correlation Heatmap of Scores',
                          xaxis_title='Subjects',
                          yaxis_title='Subjects')
st.plotly_chart(fig_heatmap)

# 4. Interactive Filtering by Gender
st.subheader('Interactive Gender Filter: Math vs Reading Scores')
fig_gender_filter = px.scatter(df, x='PV1MATH', y='PV1READ', color='ST004D01T', 
                               title='Interactive Gender Filter: Math vs Reading Scores',
                               labels={'ST004D01T': 'Gender (1=Female, 2=Male)', 
                                       'PV1MATH': 'Math Scores', 'PV1READ': 'Reading Scores'},
                               color_discrete_sequence=px.colors.qualitative.Set2)  # Colorblind-friendly palette
st.plotly_chart(fig_gender_filter)

# 5. Interactive Filtering by Year of Birth (ST003D03T) and Air Purifier Ownership
st.subheader('Interactive Year Filter: Math vs Science Scores')
fig_year_filter = px.scatter(df, x='PV1MATH', y='PV1SCIE', color='ST003D03T', 
                             title='Interactive Year Filter: Math vs Science Scores',
                             labels={'PV1MATH': 'Math Scores', 'PV1SCIE': 'Science Scores'},
                             color_continuous_scale='Viridis')  # Colorblind-friendly color scale
st.plotly_chart(fig_year_filter)

# 6. Ownership of Smart TV vs Air Purifier for Each Student
st.subheader('Smart TV vs Air Purifier Ownership by Year of Birth')
fig_tv_air_filter = px.scatter(df, x='ST250D06JA', y='ST250D07JA', color='ST003D03T', 
                               title='Smart TV vs Air Purifier Ownership by Year of Birth',
                               labels={'ST250D06JA': 'Smart TV (1=Yes, 2=No)', 
                                       'ST250D07JA': 'Air Purifier (1=Yes, 2=No)'},
                               color_continuous_scale='Viridis')  # Colorblind-friendly color scale
st.plotly_chart(fig_tv_air_filter)
