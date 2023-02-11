import streamlit as st


def f1():
    st.session_state['show_button'] = True


def f2():
    st.session_state['show_button'] = False


st.write("Hello World!!!")

if 'show_button' not in st.session_state:
    st.session_state['show_button'] = True

if st.session_state['show_button']:
    st.button("Main Button", on_click=f2)

st.button("Show Button", on_click=f1)
