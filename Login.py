import streamlit as st

def app():
    st.html("<h1 style='color:red' >Log in<h1>")
    st.text_input("Email", "",placeholder="example@gmail.com")
    st.text_input("Password", "", type="password")
    st.button("Log In", type="primary")