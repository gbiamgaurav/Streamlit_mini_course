


import streamlit as st
import os
import pandas as pd 

st.write("Hello World 1234")
st.write({"key": "value"})
button = st.button("Press me!")
print(button)
# Text Elements 
st.title("Super Simple Title")
st.header("This is an Header")
st.subheader("This is Subheader")
st.markdown("This is Markdown")
st.caption("Small Text")

code_example = """
def greet(name):
  print('Hello', name)
      """

st.code(code_example, language="python")

st.divider()

st.image(os.path.join(os.getcwd(), "static", "business woman.jpg"), width=200)

