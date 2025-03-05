
import streamlit as st
import pandas as pd 


st.title("Streamlit Elements Demo")

st.subheader('DataFrame')
df = pd.DataFrame({
  'Name': ['Alice', 'Bob', 'Charlie', 'David'],
  'Age': [25, 32, 37, 45],
  'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef'],
})

st.dataframe(df)


# Data Editor Section (Editable Dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)


# Static Table Section 
st.subheader("Static Table")
st.table(df)


# Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label='Average Age', value=round(df['Age'].mean(), 1))


# Json and Dict Section
st.subheader("Json and Dictionary")
sample_dict = {
  "name": "Alice",
  "age": 25,
  "skills": ["Python", "Data Science", "GenAI"],
}
st.json(sample_dict)

# Also show it as dictionary
st.subheader("Dictionary View")
st.write(sample_dict)

