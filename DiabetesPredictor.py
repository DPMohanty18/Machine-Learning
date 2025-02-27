import streamlit as st
import pickle
import numpy as np
import os

# Define model paths
model_path = r"C:\Users\ts280\Documents\GitHub\Machine-Learning\TrainedModels\diabetesmodel.pkl"
scaler_path = r"C:\Users\ts280\Documents\GitHub\Machine-Learning\TrainedModels\scaler.pkl"

# Load the model and scaler with error handling
if os.path.exists(model_path) and os.path.exists(scaler_path):
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    with open(scaler_path, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
else:
    st.error("🔴 Model or Scaler file is missing! Please check the file paths.")
    st.stop()  # Stops execution if model files are missing

# Streamlit UI
st.title("Diabetes Prediction App 🏥")
st.write("Enter your health details to check the risk of diabetes.")

# Input fields for user data
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1, step=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=80)
insulin = st.number_input("Insulin Level", min_value=0, max_value=1000, value=30)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, format="%.2f")
age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)

# Predict button
if st.button("Predict Diabetes Risk 🚀"):
    # Prepare input data
    user_input = np.array([[pregnancies, glucose, blood_pressure, insulin, bmi, dpf, age]])

    # Scale the input data
    user_input_scaled = scaler.transform(user_input)

    # Make prediction
    prediction = model.predict(user_input_scaled)

    # Display result
    if prediction[0] == 1:
        st.error("⚠️ High risk of diabetes! Please consult a doctor.")
    else:
        st.success("✅ No risk detected. Keep maintaining a healthy lifestyle!")

st.write("Made with ❤️ using Streamlit")
