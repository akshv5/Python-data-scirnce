import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

st.title('Dashboard')


# Load the Titanic dataset from seaborn  
df  = sns.load_dataset('titanic') 



# Gender Filter 
gender = st.sidebar.multiselect('Gender', 
                                
                                options = df['sex'].unique(),
                                default = df['sex'].unique())

# class Filter
pclass = st.sidebar.multiselect('Class', 
                                 options = df['pclass'].unique(),
                                 default = df['pclass'].unique())



# age Filter
min_age, max_age = st.sidebar.slider('Age', 
                          min_value = int(df['age'].min()), 
                          max_value = int(df['age'].max()), 
                          value = (int(df['age'].min()), 
                                   int(df['age'].max())))


filtered_data = df[
  (df['sex'].isin(gender)) &
  (df['pclass'].isin(pclass)) &
  (df['age'] >= min_age) &
  (df['age'] <= max_age)
]

# Display the filtered dataframe in the Streamlit app
st.dataframe(filtered_data)  

# histogram of age distribution
st.subheader("Age Disstribution")

#  Create a histogram of the 'age' column
fig = px.histogram(df, 
                   x='age', 
                   nbins=20, 
                   title='Age Distribution')  


# Display the histogram in the Streamlit app
st.plotly_chart(fig)  

# pie chart of survival rate by gender
fig = px.pie(df, 
             names= "sex", 
             values= "survived", 
             title="Survival rate by gender", 
             color_discrete_sequence= ['pink', 'blue'], 
             hole = 0.5)

st.plotly_chart(fig)

# # passenger count by class
# fig = px.pie(df, names='sex', values='survived', title='Survival rate by)


# Survival rate by age
fig = px.line(df.groupby('age') ['survived'].mean().reset_index(), 
              x = 'age', 
              y = 'survived', 
              title = 'Survival rate by age', 
              markers=True)

st.plotly_chart(fig)


