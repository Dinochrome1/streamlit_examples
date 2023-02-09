import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.write(f.read())

# css = r'''
#     div.css-1r6slb0.e1tzin5v2 {
#     background-color: #EEEEEE;
#     border: 10px solid #CCCCCC;
#     padding: 5% 5% 5% 10%;
#     border-radius: 5px;
#     }
# '''
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
