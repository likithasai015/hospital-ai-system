import streamlit as st
import pandas as pd
import time
from model import predict_patients

time.sleep(2)

st.title("🏥 AI Hospital Resource Allocation System")

# Inputs
time = st.slider("Select Time", 1, 24, 5)
beds = st.number_input("Available Beds", min_value=0, value=20)
oxygen = st.number_input("Available Oxygen Units", min_value=0, value=15)
staff = st.number_input("Available Staff", min_value=0, value=10)

# Prediction
predicted_patients = predict_patients(time, beds, oxygen, staff)

st.subheader(f"Predicted Patients: {int(predicted_patients)}")

# Resource check
if predicted_patients > beds:
    st.error("⚠️ Not enough beds!")

if predicted_patients > oxygen:
    st.error("⚠️ Oxygen shortage predicted!")

if predicted_patients > staff:
    st.error("⚠️ Staff shortage predicted!")

if predicted_patients <= beds and predicted_patients <= oxygen and predicted_patients <= staff:
    st.success("✅ Resources are sufficient")

# Show data
data = pd.read_csv("data.csv")
st.line_chart(data[['patients']])