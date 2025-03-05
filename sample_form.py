
import streamlit as st
import pandas as pd 
from datetime import datetime

st.title('User Information Form')


form_values = {
  'name': None,
  'height': None,
  'gender': None, 
  'dob': None,
  'location': None
}

min_date = datetime(1950, 1, 1)
max_date = datetime.now()


with st.form(key="user_info_form"):
  form_values["name"] = st.text_input("Enter your name: ")
  form_values["height"] = st.number_input("Enter your height (cm): ")
  form_values["gender"] = st.selectbox("Gender:", ['Male', 'Female'])
  form_values["dob"] = st.date_input("Enter your Birthdate: ", max_value=max_date, min_value=min_date)

  submit_button = st.form_submit_button(label="Submit")
  print("after submit")
  if submit_button:
    if not all(form_values.values()):
      st.warning("Please fill in all of the fields")
    else:
      st.balloons()
      st.write("### Info")
      for (key, value) in form_values.items():
        st.write(f"{key}: {value}")
