import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the pre-trained model and make it a global variable
loaded_model = joblib.load('C:/Users/moham/OneDrive/Bureau/Financial Inclusion in Africa/Financial Inclusion in Africa.joblib')

def predict_account(features):
    # Convert user input into a DataFrame
    input_data = pd.DataFrame([features])

    # Make predictions
    prediction = loaded_model.predict(input_data)

    return prediction[0]

def main():
    st.title('Bank account Prediction App')
    st.write("Welcome to the Bank account Prediction App!")
    st.markdown("This app allows you to predict whether an is likely to have or not a bank account based on provided features.")

    st.header("Input Features")

    col1,col2 =st.columns(2)

    # Define input fields for features
    country = col1.selectbox(label="country", options=['Kenya', 'Rwanda', 'Uganda', 'Tanzania'])
    location_type = col2.selectbox(label="location_type", options=['Rural', 'Urban'])
    cellphone_access = col1.selectbox(label="cellphone_access", options=['Yes', 'No'])
    gender_of_respondent =  col2.selectbox(label="gender_of_respondent", options=['Female', 'Male'])
    relationship_with_head = col1.selectbox(label="relationship_with_head", options=['Spouse', 'Head of Household', 'Child', 'Parent', 'Other relative',
       'Other non-relatives'])
    marital_status = col2.selectbox(label="marital_status", options=['Married/Living together', 'Single/Never Married', 'Widowed',
       'Divorced/Seperated', 'Dont know'])
    education_level = col1.selectbox(label="education_level", options=['Secondary education', 'Primary education', 'No formal education',
       'Vocational/Specialised training', 'Tertiary education',
       'Other/Dont know/RTA'])
    job_type = col2.selectbox(label="job_type", options=['Farming and Fishing', 'Other Income', 'Self employed',
       'Formally employed Private', 'Remittance Dependent',
       'Informally employed', 'Formally employed Government',
       'Government Dependent', 'No Income', 'Dont Know/Refuse to answer'])
    
    year= col1.number_input("Select survey's year 2018/2019/2020", min_value=2010, max_value=2023)
    household_size= st.slider("Number of people living in one house", min_value=1, max_value=10)
    age_of_respondent= st.slider("Select age", min_value=18, max_value=100)

   # Create a button to trigger prediction
    if st.button("Predict account possession"):
        # Collect user input for features
         user_input = {
            'country': country,
            'location_type': location_type,
            'cellphone_access': cellphone_access,
            'gender_of_respondent': gender_of_respondent,
            'relationship_with_head': relationship_with_head,
            'marital_status': marital_status,
            'education_level': education_level,
            'job_type': job_type,
            'year': year,
            'household_size':household_size,
            'age_of_respondent':age_of_respondent


        }


# Make a prediction
         prediction = predict_account(user_input)

        # Display the prediction result
         if prediction == 1:
            st.write("Prediction: Customer is likely to have a bank account.")
         else:
            st.write("Prediction: Customer is unlikely to have a bank account.")

if __name__ == '__main__':
    main()