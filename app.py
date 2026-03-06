import streamlit as st
import numpy as np
import pandas as pd

st.title("Bearing Digital Twin")

# ----------------------------
# Bearing Parameters
# ----------------------------
st.sidebar.header("Bearing Parameters")

bearing_id = st.sidebar.number_input("Bearing ID (mm)", value=40.0)
bearing_od = st.sidebar.number_input("Bearing OD (mm)", value=90.0)
bearing_width = st.sidebar.number_input("Bearing Width (mm)", value=23.0)

ball_diameter = st.sidebar.number_input("Ball Diameter (mm)", value=15.875)
number_of_balls = st.sidebar.number_input("Number of Balls", value=8)

dynamic_rating = st.sidebar.number_input("Dynamic Load Rating C (N)", value=31500)
static_rating = st.sidebar.number_input("Static Load Rating Co (N)", value=24000)

# ----------------------------
# Test Conditions
# ----------------------------
st.header("Test Conditions")

radial_load = st.number_input("Radial Load (N)", value=14000)
rpm = st.number_input("RPM", value=3000)
temperature = st.number_input("Temperature (C)", value=60)

# ----------------------------
# Horizontal Bearing Table
# ----------------------------
st.subheader("Bearing Parameters")

param_table = pd.DataFrame({
    "ID (mm)": [bearing_id],
    "OD (mm)": [bearing_od],
    "Width (mm)": [bearing_width],
    "Ball Dia (mm)": [ball_diameter],
    "Balls": [number_of_balls],
    "Dynamic C (N)": [dynamic_rating],
    "Static Co (N)": [static_rating]
})

st.table(param_table)

# ----------------------------
# Test Input Display
# ----------------------------
st.subheader("Current Test Inputs")

st.write("Radial Load:", radial_load)
st.write("RPM:", rpm)
st.write("Temperature:", temperature)
