import streamlit as st
import langchain_helper

st.title("Restaurant Name & Menu Generator")

menu_type = st.sidebar.selectbox("Pick any one", ("Gujarati", "South Indian", "Chinese", "Punjabi", "Italian"))

if menu_type:
    response = langchain_helper.generate_name_and_menu(menu_type)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items...")
    for item in menu_items:
        st.write("- ", item)
