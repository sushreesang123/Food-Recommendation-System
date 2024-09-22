import streamlit as st


def app():
    st.html("<h1 style='color:red' >Register<h1>")
    st.text_input("First Name", "")
    st.text_input("Last Name", "")
    st.text_input("Username", "")
    st.text_input("Email", "",placeholder="example@gmail.com")
    st.text_input("Password", "", type="password")
    st.button("Register", type="primary")
        