
import streamlit as st 
import pandas as pd 

#Title
st.title("Streamlit Form Demo")

with st.form(key="sample_form"):

  # Text input
  st.subheader('Text Inputs')
  name = st.text_input('Enter your name')
  feedback = st.text_area('Provide your feedback')

  # Date and time inputs
  st.subheader('Date and Time Inputs')
  dob = st.date_input("Select your Date of Birth")
  time = st.time_input("Choose a preferred time")

  # Selectors
  st.subheader("Selectors")
  choice = st.radio("Choose an option", ['Option 1', 'Option 2', 'Option 3', 'Option 4'])
  gender = st.selectbox('Select your Gender', ['Male', 'Female', 'Other'])
  slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])

  # Toggles and Checkboxes
  st.subheader("Toggles & Checkboxes")
  notifications = st.checkbox("Recieve Notifications")
  toggle_value = st.checkbox('Enable Dark Mode ?', value=False)

  # Submit button for the form
  submit_button = st.form_submit_button(label='Submit')


# Outside the form
st.subheader("Buttons")
st.button("Submit")
  