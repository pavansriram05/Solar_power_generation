# -*- coding: utf-8 -*-
"""spg.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SOWjshzQFYG66pXJQHk9W2FyBshiAdx5
"""

import numpy as np #importing the numerical python to perform the required numerical steps
import streamlit as st # streamlit library
import pickle# pickle library to read the model
import warnings# to ignore warnings

warnings.filterwarnings("ignore")

# User Interface
st.set_page_config(page_title="Solar Power Generation Prediction", page_icon=':sun_with_face:', layout='centered')# to name the tab where the application opens
st.markdown(""" <style>.stApp {background-color: #696969;} </style>""", unsafe_allow_html=True)
st.title(" ________________________________ Solar Power Generation Prediction :sun_with_face:") # giving title for the page inside it
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Inputs
Distance_to_solar_noon = st.number_input('distance_to_solar_noon', min_value=0.0, max_value=1.0, value=0.5, format="%.6f")# distance to solar noon as an input box
st.write(f"Current Distance to Solar Noon: {Distance_to_solar_noon}")
Temperature = st.slider('temperature', min_value=0, max_value=80, step=1)# temperature input as  a slider
st.write(f"Current Temperature: {Temperature}°C")
WindDirection = st.number_input('wind_direction', min_value=0, max_value=40, value=0)# windDirection as input box
st.write(f"Current Wind Direction: {WindDirection}°")
WindSpeed = st.number_input('wind_speed', min_value=0, max_value=30, value=0)#windSpeed as input box
st.write(f"Current Wind Speed: {WindSpeed} m/s")
Skycover = st.slider('skycover', min_value=0, max_value=4, step=1)#skycover input as slider
st.write(f"Current Sky Cover: {Skycover}")
Visibility = st.slider('visibility', min_value=0, max_value=20, step=2)#visibility input as slider
st.write(f"Current Visibility: {Visibility} km")
Humidity = st.slider('humidity', min_value=0, max_value=100, step=1)#humidity input as slider
st.write(f"Current Humidity: {Humidity}%")
Averagewindspeed = st.number_input("average_wind_speed", min_value=0, max_value=40, value=0)#Average wind speed as input box
st.write(f"Current Average Wind Speed: {Averagewindspeed} m/s")
AveragePressure = st.number_input("average_pressure", min_value=0, max_value=40, value=0)#average pressure as input box
st.write(f"Current Average Pressure: {AveragePressure} Mercury Inches")

# Load models
model = pickle.load(open('spg.pkl', 'rb'))  # Gradient Boost Regressor
model1 = pickle.load(open('treemodel1.pkl', 'rb'))  # Tree Regressor
model2 = pickle.load(open('rfmodel1.pkl', 'rb'))  # Random Forest Regressor

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

    return f"The power generated will be between {min(predictions)} and {max(predictions)}"

# Create input data for prediction
input_data = [Distance_to_solar_noon, Skycover, Humidity]

# Prediction
if st.button('Power generation'):
    result = Solar_power_generation(input_data)
    st.write(result)
