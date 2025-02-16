import streamlit as st

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

    if not st.session_state.logged_in:
        st.stop()
