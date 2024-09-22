import streamlit as st


def app():
    #st.header("input page")
    col1, col2 = st.columns(2)
    col1.number_input("Age", step=1)
    col1.number_input("Weight", step=1)
    col1.selectbox("Eating Preference", ["Veg", "Non-Veg"])
    col1.text_input("Region")

    col2.selectbox("Gender", ["MALE", "FEMALE", "OTHERS"])
    col2.number_input("Height(in m)")
    col2.text_input("Generic Disease")
    col2.text_input("Allergies")

    st.text_input("Food Type")
    st.button("Next")
    
        