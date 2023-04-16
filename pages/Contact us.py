from PIL import Image
import streamlit as st
import numpy as np
st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")

st.title("Contact Us")
st.write("\n\n")
with st.container():
    st.subheader("Instagram")
    st.markdown("""<a href="https://instagram.com/livefit_inc?igshid=ZWIzMWE5ZmU3Zg=="> @livefit_inc </a>""", unsafe_allow_html=True)
    
    st.write("---")
    
    st.subheader("LinkedIn")
    st.markdown("""<a href="https://in.linkedin.com/in/lanish-fernandes-07a749234"> @Lanish Fernandes </a>""", unsafe_allow_html=True)
    