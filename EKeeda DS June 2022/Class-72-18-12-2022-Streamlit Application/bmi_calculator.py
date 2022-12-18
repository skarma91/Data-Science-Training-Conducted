import streamlit as st
import numpy as np

st.title("Welcome to BMI calculator")

st.write("Body Mass Index (BMI) is calculated using following formula")

st.latex(r'''
    BMI = \frac{weight}{height^2}
    ''')

weight = st.number_input("Enter your weight (in kg)")

unit = st.radio("Select your height format: ", ['cms', 'meters', 'feet'])

height = st.number_input(f"Enter your height in {unit}")

# height conversion (convrting the height is meters)

if unit == 'cms':
    height = height / 100
elif unit == 'feet':
    height = height / 3.28  # 3.28 feet = 1 meter

# bmi calculation

if (st.button("Calculate BMI")):

    bmi = np.round(weight / (height**2), 3)

    st.write(f"Your BMI is {bmi}")

    if (bmi < 16):
        st.error("You are extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("You are Overweight")
    elif (bmi >= 30):
        st.error("You are extremely Overweight")