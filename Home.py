from PIL import Image
import streamlit as st
import numpy as np
import pandas as ps
from bokeh.plotting import figure

st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")
fit_ness=Image.open("body_building.png")
li_fit=Image.open("LIVEFIT.png")
gym_tech=Image.open("pexels-andrea-piacquadio-3837388.jpg")
dum_bell=Image.open("pexels-victor-freitas-791763.jpg")
ben_press=Image.open("pexels-pixabay-416717.jpg")
video_file=open("pexels-tima-miroshnichenko-5319759.mp4", 'rb')
video_bytes=video_file.read()
with open('./pages/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container(): 
    text_column, empty_column =st.columns((2))
    with text_column:
        st.subheader("Welcome to LiveFit")
        st.write("[Click for Motivation](https://www.youtube.com/watch?v=WE50ZSVQeDs)")
        st.text("Ever felt the need to tranform your body?")
        st.text("Do you want that slim fit look for a occasion?")
        st.subheader("Well here's the solution..")
    with empty_column:
        st.image(li_fit, width=450)
#    with image_column:
#        st.image(fit_ness, width=380, clamp=True)
        
st.write("---")
with st.container():
    st.title("**Our Program provides these exercises**")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image(gym_tech, width=400)
    with mid_column:
        st.image(dum_bell, width=400)
    with right_column:
        st.image(ben_press, width=400)

st.write("---")
with st.container():
    st.title("Our Blog Postings....")
    col1, col2, col3=st.columns(3)
    with col1:
        st.write(" You are the best trainer to teach personal fitness and always bring fire workouts! Since quarantine, I've strictly done your suggested workouts and I'm in the best shape ever! ")
        st.write(":heart:")
    with col2:
        st.write(" Your fitness sessions have been giving me strength (literally and figuratively) Each session I feel excited, motivated and challenged in a good way.")
        st.write(":heart:")
    with col3:
        st.write("The best app for training of mind and body. I have relieved all stress after just two months of fitness sessions")
        st.write(":heart:")
st.write("---")
with st.container():

        x = [1, 2, 3, 4, 5]
        y = [6, 7, 2, 4, 5]

        p = figure(
            title='BMI Chart',
            x_axis_label='x',
            y_axis_label='y')

        p.line(x, y, legend_label='Trend', line_width=2)

        st.bokeh_chart(p, use_container_width=True)

st.write("---")
with st.container():
    st.video(video_bytes)



st.write("---")
with st.container():
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Be The Part Of Something Great:moyai:")
    with mid_column:
        st.subheader("Sign up for a 2-month program:weight_lifter::point_right:")
    with right_column:
        st.markdown("""<a href="http://localhost:8504/"> <button type="button" style="background-color:#FFFFFF"> Click Me </button> </a>""", unsafe_allow_html=True)
        
            
