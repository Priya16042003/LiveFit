from PIL import Image
import streamlit as st
import numpy as np
from PIL import Image
import streamlit as st
import numpy as np
import pandas as ps 
# with open('C:/Users/pdv50/Downloads/Fruit_Vegetable_Recognition-master/Fruit_Vegetable_Recognition-master/pages/css/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")
# st.title("Yoga Tutorials")
profile=Image.open("profile.png")
# video_file=open("pexels-tima-miroshnichenko-5319759.mp4", 'rb')
# =video_file.read()
st.write("---")

with st.container():
    st.title("5 star Dietician")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image(profile)
        st.write("Priya Jain")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
    with mid_column:
        st.image(profile)
        st.write("Stalen Ferreira")
        st.markdown("""<a href="https://call.whatsapp.com/video/IY4KlPCP1cblKIqGizSkU0"> phno:8879603443 </a>""", unsafe_allow_html=True)
    with right_column:
        st.image(profile)
        st.write("Lanish Fernandes")
        st.markdown("""<a href="https://wa.me/919049296030"> phno:9049296030 </a>""", unsafe_allow_html=True)
    
with st.container():
    st.title("4 star Dietician")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image(profile)
        st.write("Aaron Fernandes")
        st.markdown("""<a href="https://wa.me/917718827314"> phno:7718827314 </a>""", unsafe_allow_html=True)
    with mid_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
    with right_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
with st.container():
    st.title("3 star Dietician")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
    with mid_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
    with right_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
with st.container():
    st.title("2 star dietician")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
    with mid_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://wa.me/917506210598"> phno:7506210598 </a>""", unsafe_allow_html=True)
    with right_column:
        st.image(profile)
        st.write("Name")
        st.markdown("""<a href="https://call.whatsapp.com/video/MO5PCARS1Hnru5Yj09Td9t"> phno:7506210598 </a>""", unsafe_allow_html=True)
    # st.image(profile)