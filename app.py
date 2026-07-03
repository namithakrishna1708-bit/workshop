import streamlit as st

#Take a userinput\
st.title("take the input")

name= st.text_input("Enter your name")


if st.button("submit"):
  st.write(f"print the name: {name}")
