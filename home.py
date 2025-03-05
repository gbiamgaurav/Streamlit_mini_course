
import streamlit as st
import pandas as pd
import numpy as np


# Define page functions
def intro():
  st.title("Welcome to my multi-page App")
  st.write("This is the introduction page, use thr dropdown to navigate to different demos")

def plotting_demo():
  st.title("Plotting Demo")
  st.write("Here, we create a simple plot")

  chart_data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
  st.line_chart(chart_data)
  
  st.header('Bar Chart')
  st.bar_chart(chart_data)

  st.header('Area Chart')
  st.area_chart(chart_data)


def mapping_demo():
  st.title("Mapping Demo")
  st.write("This page shows a map with random points")

  map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [12.9716, 77.5946], columns=["lat", "lon"])

  st.map(map_data)


def data_frame_demo():
  st.title("Dataframe Demo")
  st.write("Here we display a sample data frame")

  data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]}

  df = pd.DataFrame(data)
  st.dataframe(df)


# Dictionary to map page names to functions
page_names_to_funcs = {
  "Introduction Demo": intro,
  "Plotting Demo": plotting_demo,
  "Mapping Demo": mapping_demo,
  "Dataframe Demo": data_frame_demo
}


# Sidebar for page navigation
selected_page = st.sidebar.selectbox("Choose a Page", options=page_names_to_funcs.keys())


# Run the functions associated with the selected page
page_names_to_funcs[selected_page]()