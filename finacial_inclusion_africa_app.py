import pandas as pd
import numpy as np
import pickle
import streamlit as st

model_file = open('financial-inclusion-africa-clf-model.pkl', 'rb')
model = pickle.load(model_file)

def bank_account_prediction(country, year, location_type, cellphone_access, household_size, age_of_respondent, gender_of_respondent, relationship_with_head, marital_status, education_level, job_type):
    '''Predict if a customer has a bank account based on features values'''
    
    prediction = model.predict([[country, year, location_type, cellphone_access, household_size, age_of_respondent, gender_of_respondent, relationship_with_head, marital_status, education_level, job_type]])
    print(prediction)
    
    return "The predicted value for bank_account is : " + str(prediction)

def main():
    st.title("Financial Inclusion in Africa App")
    html_template = """
        <div style="background-color: DarkSlateGray;padding:10px">
            <h2 style="color:white;text-align:center">Streamlit Bank Account Prediction ML App</h2>
        </div>
        <br>
    """
    st.markdown(html_template, unsafe_allow_html=True)
    country = st.selectbox("country", ["Rwanda", "Tanzania", "Kenya", "Uganda"])
    year = st.selectbox("year", [2016, 2017, 2018])
    location_type = st.selectbox("location_type", ["Rural", "Urban"])
    cellphone_access = st.selectbox("cellphone_access", ["Yes", "No"])
    household_size = st.slider("household_size", 1, 20)
    age_of_respondent = st.slider("age_of_respondent", 1, 100)
    gender_of_respondent = st.selectbox("gender_of_respondent", ["Male", "Female"])
    relationship_with_head = st.selectbox("relationship_with_head", ["Head of Household", "Spouse", "Child", "Parent", "Other relative", "Other non-relatives"])
    marital_status = st.selectbox("marital_status", ["Married/Living together", "Single/Never Married", "Widowed", "Divorced/Seperated, Dont know"])
    education_level = st.selectbox("education_level", ["Secondary education", "No formal education", "Vocational/Specialised training, Primary education", "Tertiary education", "Other/Dont know/RTA"])
    job_type = st.selectbox("job_type", ["Self employed", "Government Dependent", "Formally employed Private", "Informally employed", "Formally employed Government", "Farming and Fishing", "Remittance Dependent", "Other Income", "Dont Know/Refuse to answer", "No Income"])
    
    result= ""
    
    if st.button("Predict"):
        result = bank_account_prediction(country, year, location_type, cellphone_access, household_size, age_of_respondent, gender_of_respondent, relationship_with_head, marital_status, education_level, job_type)
    st.success(f"Result : {result}")

        
if __name__=='__main__':
    main()