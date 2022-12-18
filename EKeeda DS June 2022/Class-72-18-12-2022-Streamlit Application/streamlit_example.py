import streamlit as st
import numpy as np
import pandas as pd

st.header("Examples of streamlit inputs.")

st.markdown("""---""")

# text input

name = st.text_input("Enter your name")
surname = st.text_input("Enter your surname")

# button
status = st.button("Submit")

st.markdown("""---""")

if status:
    st.subheader(f"Welcome {name} {surname}")

# bootstrap like status output box

#st.success("Success message")
#st.info("Information message")
#st.warning("This is a warning")
#st.error("This is an error")

st.markdown("""---""")
st.write("Now enter some details about you.")

# Radio Button
gender = st.radio("Select Gender: ", ('Male', 'Female', 'Prefer not to disclose'))

# Selection Box
education_level = st.selectbox("Highest Educational Qualification",
                               ['Higher Secondary', 'Bachelors', 'Masters', 'PhD', 'Others'])

if education_level == 'Others':
    education_level = st.text_input("Please enter your other educational qualification")

# Multi-selection box
hobbies = st.multiselect("Hobbies", ['Dancing', 'Photography', 'Painting', 'Sketching/Drawing', 'Singing'])

st.info(f"You have selected {len(hobbies)} hobbies.")

# Slider
age = st.slider("Select your age in years",18, 60)
st.info(f"Your age is {age} years")

weight = st.slider("Select your weight in kg", min_value=40.0, max_value=120.0, step=0.5)
st.warning(f"Your weight is {weight} kg")

# Checkbox
watching = st.checkbox("Watching Qatar WC 2022/ Not watching")

if watching:
    st.success(f"Good! You are watching Qatar WC 2022")
