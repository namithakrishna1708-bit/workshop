import streamlit as st

#Take a userinput\
name= st.text_input("Enter your name")

st.title("take the input")

if st.button("submit"):
  st.write(f"print the name: {name}")
