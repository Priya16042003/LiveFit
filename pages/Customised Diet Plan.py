from click import Option
import pyrebase
import streamlit as st
st.set_page_config(page_title="LiveFIT", page_icon=":running:", layout="wide")
firebaseConfig = {
  'apiKey': "AIzaSyBIYcy765-mZh8DgeoZ8TVdopwhrq2i8l4",
  'authDomain': "stayfit-a417f.firebaseapp.com",
  'databaseURL': "https://stayfit-a417f-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "stayfit-a417f",
  'storageBucket': "stayfit-a417f.appspot.com",
  'messagingSenderId': "183972816828",
  'appId': "1:183972816828:web:e8f4a30413b8c4097fedb9",
  'measurementId': "G-BQ0WLMMGJZ"
};
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

st.write("LiveFit User Details")
with st.form("Details"):
   name=st.text_input("Enter your Name:")
   sname=st.text_input("Enter your Surname:")
   no=st.text_input("Contact Number:")
   eid=st.text_input("Email Id:")
   height=st.text_input("Height: (In Feet)")
   weight=st.text_input("Weight: (In kilograms)")
   st.write("Inside the form")
   age = st.slider("Age")
   
   gen = st.selectbox(
    'Gender:',
    ('Male', 'Female','Others'))
   
   st.write("Activity")
   
   option1 = st.selectbox(
    'How often do you exercise:',
    ('Daily', 'Moderately','Sometimes', 'Rarely' , 'Do not exercise'))
#    st.write("How often do you exercise")
#    checkbox_vall = st.checkbox("Daily")
#    checkbox_vall = st.checkbox("Moderately")
#    checkbox_vall = st.checkbox("Sometimes")
#    checkbox_vall = st.checkbox("Rarely")
#    checkbox_vall = st.checkbox("Do not exercise")
   st.write("Food Preferences")
   food=st.selectbox('Food Preference:',('Non-Vegeterian', 'Vegetarian','Jain', 'Vegan' ))
    
#    if option is 'Non-Vegeterian':

#     checkbox_food1 = st.checkbox("Chicken")
#     checkbox_food1 = st.checkbox("Mutton")
#     checkbox_food1 = st.checkbox("Fish")
#     checkbox_food2 = st.checkbox("Eggs")
#     checkbox_food2 = st.checkbox("Beef")
#     checkbox_food2 = st.checkbox("Pork")

   condition=st.text_input("Any Medical Condition:")
   st.write("eg. Diabeties, Blood pressue, etc.")

   contact = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Mobile phone'))

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("Age : ", age, "Gender", gen,"Activity", option1)
       data = {'name': name, 'surname':sname,'contact number':no,'email id':eid,'height':height,'weight':weight, 'age': age, 'gender': gen,'Activity':option1,'Food':food,'condition':condition,'contacton':contact}
       database.push(data)




st.write("Thank you For your time.")
st.write("A customised Diet & Exercie plan will be shared with you shortly.")