import streamlit as st
import numpy as np
import pickle

# ----------------------------
# Load Scaler and Model
# ----------------------------
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("svm_model.pkl", "rb") as f:
    model = pickle.load(f)

# ----------------------------
# Feature list (16 features)
# ----------------------------
features = [
    'birth_rate', 'business_tax_rate', 'days_to_start_business',
    'energy_usage', 'gdp', 'health_exp_percentage_gdp',
    'health_exp/capita', 'hours_to_do_tax', 'internet_usage',
    'lending_interest', 'life_expectancy_female', 'mobile_phone_usage',
    'population_15_64', 'population_65plus', 'population_total', 'population_urban'
]

st.title("Global Development Classification")
st.write("Predict whether a country is Developed, Developing, or Least Developed based on 16 features.")

# ----------------------------
# Input form
# ----------------------------
user_input = []
for f in features:
    val = st.number_input(f"Enter {f}:", value=0.0)
    user_input.append(val)

# Convert to numpy and scale
input_array = np.array(user_input).reshape(1, -1)
scaled_input = scaler.transform(input_array)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Country Type"):
    prediction = model.predict(scaled_input)[0]
    st.success(f"Predicted Category: **{prediction}**")
