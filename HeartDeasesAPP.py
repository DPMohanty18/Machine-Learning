import streamlit as st
import pandas as pd
import pickle
import joblib

# Title of the Streamlit app
st.title("Heart Disease Prediction")

# Upload model file
#uploaded_model = st.file_uploader("Upload your model file", type=["pkl"])

# if uploaded_model is not None:
#     # Load the model
model = joblib.load('random_forest_model.joblib')

# Define the feature names based on your dataset
feature_names = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 
        'ca', 'thal'
    ]
    
# Input feature values for prediction
input_data = {}
for feature in feature_names:
    value = st.text_input(f"Enter value for {feature}")
    input_data[feature] = float(value) if value else 0
    
    # Convert input data to DataFrame
input_df = pd.DataFrame([input_data])
    
    # Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
        
    # Display the prediction
    st.write("Prediction:", "Heart Disease" if prediction[0] else "No Heart Disease")
    st.write("Prediction Probability:", prediction_proba)

