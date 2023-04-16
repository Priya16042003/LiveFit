import streamlit as st 
from PIL import Image

st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")
st.title("Calculate Your BMI")

img = Image.open("bmi.jpg")
st.image(img)

# Introduction

st.subheader("Introduction")


# Input

weight = st.number_input("Enter your Weight in KG", step = 0.1)

height = st.number_input("Enter your Height in Meters")
submitted = st.button("Submit")
if submitted:
    bmi = weight/(height)**2
    st.success(f"Your BMI is {bmi}")