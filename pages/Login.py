# Modules
import pyrebase
import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
import time
from PIL import Image
import numpy as np
import pandas as ps
from bokeh.plotting import figure
st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")

# Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyBIYcy765-mZh8DgeoZ8TVdopwhrq2i8l4",
    'authDomain': "stayfit-a417f.firebaseapp.com",
    'projectId': "stayfit-a417f",
    'databaseURL':"https://stayfit-a417f-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "stayfit-a417f.appspot.com",
    'messagingSenderId': "183972816828",
    'appId': "1:183972816828:web:436869b1b34979987fedb9",
    'measurementId': "G-XP8P436Z9R"
  };

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Live Fit")

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

# App 

# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Please input your app handle name', value='Name')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')
        st.balloons()
        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome  ' + handle)
        st.info('Login via login drop down selection')

# Login Block
if choice == 'Login':
    login = st.sidebar.button('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)
li_fit=Image.open("LIVEFIT.png")
pro_tein=Image.open("whey.png")
with open('./pages/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
with st.container(): 
    left, right=st.columns(2)
    with left:
        st.header("\n\n\n\n\n\nDashBoard")
        
    with right:
        st.image(li_fit, width=340)    
        st.write("")
st.write("---")
    
with st.container():
    st.header("Welcome")
    weg_col, heig_col, bmi_col=st.columns(3)
    with weg_col:
        st.metric(label="Weight", value="75 kg" )
    with heig_col:
        st.metric(label="Height", value="178 m" )
    with bmi_col:
        st.metric(label="BMI", value=27)

st.write("---")

with st.container():
    st.header("Work Out Plans")
    option=st.selectbox('Exercises:',['Select one exercise','Arms','Abs', 'Legs', 'Full Body'])
    if option == 'Select one exercise':
        st.write("Please select one of the four exercises to strat your course")
    if option == 'Arms':
        st.markdown(" **:red[Push Ups x20]  \nInclined Push Ups x 20  \nArm Twists x 15  \n:red[Pull Ups x 20]  \nRope Swinging x 20(each)** ")
        st.write("[Click for Motivation](https://www.youtube.com/watch?v=WE50ZSVQeDs)")
        
        success=st.button("Task Completed")
        if success:
            st.success("Daily Goal Reached!!!")
            st.balloons()
    if option == 'Abs':
        st.markdown(" **:red[Crunches x20]  \nLumbar Dips x 20  \nRussian Twists x 15  \n:red[Leg Raises x 20]  \n:red[Plank x 30(sec)]** ")
        st.write("[Click](https://www.youtube.com/watch?v=WE50ZSVQeDs)")

        success=st.button("Task Completed")
        if success:
            st.success("Daily Goal Reached!!!")
            st.balloons()
    if option == 'Legs':
        st.markdown(" **:red[Squats x20]  \nSumo Squats x 20  \nSide Leg Raises x 15  \n:red[Calf Raises x 20]  \nDonkey Kicks x 20** ")
        st.write("[Click Motivation](https://www.youtube.com/watch?v=WE50ZSVQeDs)")
        
        success=st.button("Task Completed")
        if success:
            st.success("Daily Goal Reached!!!")
            st.balloons()
    if option == 'Full Body':
        st.write("Get ready to sweat like Hell  \nAs the Gains are Maximum :fire:")
        l_col, m_col, r_col=st.columns(3)
        with l_col:
            st.subheader("SET 1")
            st.markdown(" **:red[Push Ups x20]  \nInclined Push Ups x 20  \nArm Twists x 15  \n:red[Pull Ups x 20]  \nRope Swinging x 20(each)** ")
        with m_col:
            st.subheader("SET 2")
            st.markdown(" **:red[Crunches x20]  \nLumbar Dips x 20  \nRussian Twists x 15  \n:red[Leg Raises x 20]  \n:red[Plank x 30(sec)]** ")
        with r_col:
            st.subheader("SET 3")
            st.markdown(" **:red[Squats x20]  \nSumo Squats x 20  \nSide Leg Raises x 15  \n:red[Calf Raises x 20]  \nDonkey Kicks x 20** ")
        st.write("[Click for Motivation](https://www.youtube.com/watch?v=WE50ZSVQeDs)")

        success=st.button("Task Completed")
        if success:
            st.success("Daily Goal Reached!!!")
            st.balloons()

st.write("---")

with st.container():
    st.subheader("Recommended Diet")
    l_col, m_col, r_col=st.columns(3)
    with l_col:
        st.image(pro_tein, width=150)
        # st.write("")
    with m_col:
        st.image(pro_tein, width=150)
        # st.write("")
    with r_col:
        st.image(pro_tein, width=150)
        # st.write("")

st.write("---")


with st.container():
    st.header("Recommnded Activity")
    l_col, m_col, r_col=st.columns(3)
    with l_col:
        st.markdown(" **Walking  \n:red[Running]  \n:yellow[Jogging] \n:orange[Cycling]** ")
        
    with m_col:
        st.markdown(" **700 kcal  \n1300 kcal  \n900 kcal  \n2000 kcal** ")
        
st.write("---")







