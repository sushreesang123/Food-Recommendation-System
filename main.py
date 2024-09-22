import streamlit as st
from streamlit_option_menu import option_menu
import Login, Register, InputPage

st.set_page_config(
    page_title="Food recommendation system"
)

class Pages:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Nav Bar",
                options=["Register","Login","InputPage"],
                #icons=["house-fill","house-fill","house-fill"],
                default_index=0
            )
        if app == "Register":
            Register.app()
        if app == "Login":
            Login.app()
        if app == "InputPage":
            InputPage.app()
            
    run()