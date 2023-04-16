from PIL import Image
import streamlit as st
import numpy as np
import pandas as ps 
# with open('C:/Users/pdv50/Downloads/Fruit_Vegetable_Recognition-master/Fruit_Vegetable_Recognition-master/pages/css/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")
# st.title("Yoga Tutorials")
video_file=open("pexels-tima-miroshnichenko-5319759.mp4", 'rb')
video_bytes=video_file.read()
st.write("---")

with st.container():
    st.title("Yoga Tutorials")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.video(video_bytes)
    with mid_column:
        st.video(video_bytes)
    with right_column:
        st.video(video_bytes)
with st.container():
    st.title("Cardio Tutorials")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.video(video_bytes)
    with mid_column:
        st.video(video_bytes)
    with right_column:
        st.video(video_bytes)
with st.container():
    st.title("Zumba Tutorials")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.video(video_bytes)
    with mid_column:
        st.video(video_bytes)
    with right_column:
        st.video(video_bytes)
with st.container():
    st.title("Aerobics Tutorials")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.video(video_bytes)
    with mid_column:
        st.video(video_bytes)
    with right_column:
        st.video(video_bytes)
    # st.video(video_bytes)