import streamlit as st
name = st.text_input("Enter your name")
age = st.slider("Enter your age", 0, 100)
st.write(f'Your name is {name}, and your age is {age}')
