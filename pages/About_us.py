from PIL import Image
import streamlit as st
import numpy as np
st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")

photo=Image.open("profile.png")

with st.container():
    left_col, right_col=st.columns((1,2))
    with left_col:
        st.image(photo, width=184)
        st.write("---")
        st.image(photo, width=184)
        st.write("---")
        st.image(photo, width=184)
    with right_col:
        st.header("Aaron Fernandes")
        st.subheader("Tech Innovator")
        st.write("Student studying in second year of INFT department of St. Francis College of Engineering, having amazing skills in team projects manages this team with ease") 
        st.write("---")       
        st.header("Priya Jain")
        st.subheader("Back-End Developer")
        st.write("Student studying in second year of INFT department of St. Francis College of Engineering, having exceptional skills in coding and data management is the core member of our team project")
        st.write("---")
        st.header("Lanish Fernandes")
        st.subheader("Front-End Developer")
        st.write("Student studying in second year of INFT department of St. Francis College of Engineering, having the creativity of graphics helps in designing the UI")
