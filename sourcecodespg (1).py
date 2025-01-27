# -*- coding: utf-8 -*-
"""sourcecodeSPG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SOWjshzQFYG66pXJQHk9W2FyBshiAdx5
"""

import numpy as np
import streamlit as st
import pickle
import warnings

warnings.filterwarnings("ignore")

# User Interface
st.set_page_config(page_title="Solar Power Generation Prediction", page_icon=':sun_with_face:', layout='centered')
st.subheader("Solar Power Generation Prediction")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Inputs
Distance_to_solar_noon = st.number_input('distance_to_solar_noon', min_value=0.0, max_value=1.0, value=0.5, format="%.6f")
Temperature = st.slider('temperature', min_value=0, max_value=80, step=1)
WindDirection = st.number_input('wind_direction', min_value=0, max_value=40, value=0)
WindSpeed = st.number_input('wind_speed', min_value=0, max_value=30, value=0)
Skycover = st.slider('skycover', min_value=0, max_value=4, step=1)
Visibility = st.slider('visibility', min_value=0, max_value=10, step=2)
Humidity = st.slider('humidity', min_value=0, max_value=100, step=1)
Averagewindspeed = st.number_input("average_wind_speed", min_value=0, max_value=40, value=0)
AveragePressure = st.number_input("average_pressure", min_value=0, max_value=40, value=0)

# Load models
model = pickle.load(open('spg.pkl', 'rb'))  # Gradient Boost Regressor
model1 = pickle.load(open('lassomodel1.pkl', 'rb'))  # Lasso Regressor
model2 = pickle.load(open('treemodel1.pkl', 'rb'))  # Tree Regressor
model3 = pickle.load(open('rfmodel1.pkl', 'rb'))  # Random Forest Regressor

# Prediction function
def Solar_power_generation(input_data):
    predictions = []
    input_array = np.asarray(input_data).reshape(1, -1)

    prediction = model.predict(input_array)
    predictions.append(prediction[0])

    prediction1 = model1.predict(input_array)
    predictions.append(prediction1[0])

    prediction2 = model2.predict(input_array)
    predictions.append(prediction2[0])

    prediction3 = model3.predict(input_array)
    predictions.append(prediction3[0])

    return f"The power generated will be between {min(predictions)} and {max(predictions)}"

# Create input data for prediction
input_data = [Distance_to_solar_noon, Skycover, Humidity]

# Prediction
if st.button('Power generation'):
    result = Solar_power_generation(input_data)
    st.write(result)