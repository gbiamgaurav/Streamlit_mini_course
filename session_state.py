
#import streamlit as st 
#
#
## A simple counter variable, without session state
#counter = 0
#
#st.write(f"Counter Value: {counter}")
#
#
## Button to increment the counter
#if st.button("Increment Counter"):
#  counter += 1
#  st.write(f"Counter incremented to {counter}")
#else:
#  st.write(f"Counter stays at {counter}")


## Using Session State
import streamlit as st

if "counter" not in st.session_state:
  st.session_state.counter = 0 

if st.button("Increment Counter"):
  st.session_state.counter += 1
  st.write(f"Counter incremented to {st.session_state.counter}")


if st.button("Reset"):
  st.session_state.counter = 0
else:
  st.write(f"Counter did not reset")

st.write(f"Counter Value: {st.session_state.counter}")