
import streamlit as st 

# Sidebar layout
st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements like sidebars, buttons, and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# Tabs Layout
tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
  st.write("You are in Tab 1")

with tab2:
  st.write("You are in Tab 2")

with tab3:
  st.write("You are in Tab 3")


# Columns Layout
col1, col2 = st.columns(2)

with col1:
  st.header('Column 1')
  st.write('Content for column 1')

with col2:
  st.header('Column 2')
  st.write('Content for column 2')


# Containers example
with st.container(border=True):
  st.write("Sample Container 1")
  st.write("Sample SubContainer")


# Empty Placeholder
placeholder = st.empty()
placeholder.write("This is an sample placeholder")

if st.button("Update Placeholder"):
  placeholder.write("Updated Placeholder")


# Expander
with st.expander("This is an sample Expander"):
  st.write("Sample Sub expander")


# Popover (Tooltip)
st.write("Hover over this button for a tooltip")
st.button("Button with tooltip", help="This is a tooltip or popover on hover")


# Sidebar input handling
if sidebar_input:
  st.write(f"You entered in the sidebar: {sidebar_input}")