
import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model/trained_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.title("🧪 Doping Bandgap Shift Predictor")

# Input fields
atomic_number = st.number_input("Atomic Number", 1, 100, step=1)
electronegativity = st.number_input("Electronegativity", 0.0, 4.0, step=0.01)

# Predict on button click
if st.button("Predict Bandgap Shift"):
    X_input = scaler.transform([[atomic_number, electronegativity]])
    prediction = model.predict(X_input)
    st.success(f"📉 Predicted Bandgap Shift: {prediction[0]:.3f} eV")
