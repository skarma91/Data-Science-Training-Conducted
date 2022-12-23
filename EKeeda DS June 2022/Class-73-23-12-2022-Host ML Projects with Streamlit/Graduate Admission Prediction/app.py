import streamlit as st
import pickle
import numpy as np
import pandas as pd
import yaml
import seaborn as sns

# Load the preprocessing file

with open('./preprocessing.yml', 'r') as readfile:
    preproc_dict = yaml.load(readfile, Loader=yaml.SafeLoader)
readfile.close()

# Load the model

pickle_file = open("./model/linear_reg_model.pkl","rb")
regressor = pickle.load(pickle_file)
pickle_file.close()

# Putting header and subheader

st.title("Welcome to Graduate Admission Prediction App")
st.markdown("""---""")
st.subheader("This app predcts the chances of Graduate Admission based on following features")
st.markdown("""
    - GRE Score (between 290 to 340)
    - TOEFL Score (between 92 to 120)
    - University Ranking (between 1 to 5)
    - Cumulative Grade Point Average [CGPA] (between 6.8 to 10)
""")

# Take input from the user

st.markdown("""---""")
st.subheader("Please provide your inputs")

col1, col2, col3 = st.columns([8,2,8])

with col1:
    GRE_score = st.slider("Provide your GRE Score", min_value=preproc_dict['GRE_Score_min'], max_value=preproc_dict['GRE_Score_max'])

with col3:
    TOEFL_score = st.slider("Provide your TOEFL Score",min_value=preproc_dict['TOEFL_Score_min'], max_value=preproc_dict['TOEFL_Score_max'])

col4, col5, col6 = st.columns([8,2,8])

with col4:
    university_rating = st.selectbox("University rating", [1, 2, 3, 4, 5])

with col6:
    cgpa = st.slider("Provide your CGPA", min_value=preproc_dict['CGPA_min'], max_value=np.round(preproc_dict['CGPA_max']))

st.markdown("""---""")

st.write(f"Based on your selection of GRE Score: {GRE_score}, TOEFL Score: {TOEFL_score}, University rating: {university_rating} and CGPA: {cgpa}")

# Scaling the inputs to fit into the model

gre_score_scaled = ((GRE_score - preproc_dict['GRE_Score_min'])/(preproc_dict['GRE_Score_max']-preproc_dict['GRE_Score_min']))
toefl_score_scaled = ((TOEFL_score - preproc_dict['TOEFL_Score_min'])/(preproc_dict['TOEFL_Score_max']-preproc_dict['TOEFL_Score_min']))
rating_scaled = ((university_rating - preproc_dict['University_Rating_min'])/(preproc_dict['University_Rating_max']-preproc_dict['University_Rating_min']))
cgpa_scaled = ((cgpa - preproc_dict['CGPA_min'])/(preproc_dict['CGPA_max']-preproc_dict['CGPA_min']))

input_data = np.array([gre_score_scaled, toefl_score_scaled, rating_scaled, cgpa_scaled]).reshape(1,-1)

prediction = np.round(100*regressor.predict(input_data)[0], 2)

if prediction > 100:
    prediction = 100

if prediction >= 75:
    st.success(f"Probability of getting admission is {prediction}%")
elif prediction < 75 and prediction >= 50:
    st.warning(f"Probability of getting admission is {prediction}%")
elif prediction < 50:
    st.error(f"Probability of getting admission is {prediction}%")

st.markdown("""---""")

if (st.checkbox("See analysis")):
    data = pd.read_csv("./data/Admission_Prediction.csv")
    columns = ['GRE Score', 'TOEFL Score', 'University Rating', 'CGPA', 'Chance of Admit ']
    st.subheader("Analysis")
    
    st.markdown("#### Univariate Analysis")
    st.write("Univariate analysis let you examine the distributions of the feature/predictor variables and also the target/response variable one at a time.")
    variable = st.selectbox("Select the variable:",options = columns)
    if variable != "University Rating":
        g = sns.displot(data=data, x=variable)
        st.pyplot(g)
    else:
        g = sns.countplot(data=data, x=variable)
        st.pyplot(g.figure)
    
    st.markdown("""---""")
    st.markdown("#### Bivariate Analysis")
    st.write("Bivariate analysis let you examine the relationship among two variables at a time.")
    col1, col2, col3 = st.columns([8,2,8])
    with col1:
        variable1 = st.selectbox("Select the variable X:",options = columns)
    
    with col3:
        variable2 = st.selectbox("Select the variable Y:",options = columns[::-1])

    g = sns.jointplot(x = data[variable1], y=data[variable2], kind='reg')
    st.pyplot(g)

   
