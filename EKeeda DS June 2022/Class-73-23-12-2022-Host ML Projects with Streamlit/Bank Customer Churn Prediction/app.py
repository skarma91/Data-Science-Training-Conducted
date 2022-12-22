
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import yaml
import joblib
import matplotlib.pyplot as plt

# Load the details file
with open('./details.yml', 'r') as readfile:
    details_dict = yaml.load(readfile, Loader=yaml.SafeLoader)
readfile.close()

# Load the model
model = joblib.load(details_dict['model_filename'])

# Streamlit app header and subheader

st.title("Welcome to Bank Customer Churn Prediction App")
st.markdown("""---""")
st.subheader("This app predcts the chances of churning of a customer based on following features")

# Take input from the user

st.markdown("""---""")

col1, col2, col3 = st.columns([4,1,4])

with col1:
    credit_score = st.slider("Credit score of the customer", min_value=350, max_value=850)

with col3:
    age = st.slider("Age of the customer", min_value=18, max_value=92)

col4, col5, col6 = st.columns([4, 1, 4])

with col4:
    balance = st.number_input("Account balance of the customer", min_value=0, max_value=250000, step=100)

with col6:
    estimated_salary = st.number_input("Salary of the customer", min_value=0, max_value=200000, step=100)

col7, col8, col9 = st.columns([4, 1, 4])

with col7:
    tenure = st.slider("How many years the customer is having account?", min_value=0, max_value=10)

with col9:
    products_number = st.slider("Number of banking products the customer used.", min_value=1, max_value=4)

col10, col11, col12 = st.columns([4, 1, 4])

with col10:
    country = st.selectbox("Country of the account location", ['France', 'Spain', 'Germany'])

with col12:
    gender = st.selectbox("Gender of the customer", ['Male', 'Female'])

col13, col14, col15 = st.columns([4, 1, 4])

with col13:
    if (st.checkbox("The customer using a credit card")):
        credit_card = 1
    else:
        credit_card = 0

with col15:
    if (st.checkbox("The customer is an active member of the bank")):
        active_member = 1
    else:
        active_member = 0

# prediction from the model

values = np.array([credit_score, age, balance, estimated_salary, tenure, products_number, country, gender, credit_card, active_member]).reshape(1,-1)

test_df = pd.DataFrame(values, columns=details_dict['feature_list'])

prediction = float(model.predict_proba(test_df)[:,1])

st.markdown("""---""")

st.write("Based on the inputs provided above")

if prediction < details_dict['threshold']:
    st.success("The customer has low probability to churn.")
elif prediction >= details_dict['threshold'] and prediction < 2*details_dict['threshold']:
    st.warning("The customer is moderately likely to churn.")
else:
    st.error("The customer has high probability to churn.")