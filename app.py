import streamlit as st
import numpy as np
import pandas as pd

st.title("Bearing Digital Twin")

# ----------------------------
# Bearing Parameters Table (Horizontal)
# ----------------------------

bearing_table = pd.DataFrame({
    "Bearing ID (mm)": [bearing_id],
    "Bearing OD (mm)": [bearing_od],
    "Width (mm)": [bearing_width],
    "Ball Diameter (mm)": [ball_diameter],
    "No. of Balls": [number_of_balls],
    "Dynamic Rating C (N)": [dynamic_rating],
    "Static Rating Co (N)": [static_rating]
})

st.subheader("Bearing Parameters")
st.dataframe(bearing_table)

# ----------------------------
# Test Conditions
# ----------------------------
st.header("Test Conditions")

radial_load = st.number_input("Radial Load (N)", value=14000)
rpm = st.number_input("RPM", value=3000)
temperature = st.number_input("Temperature (C)", value=60)


# ----------------------------
# Display Inputs
# ----------------------------
st.subheader("Bearing Parameters")

st.write("ID:", bearing_id)
st.write("OD:", bearing_od)
st.write("Width:", bearing_width)
st.write("Ball Diameter:", ball_diameter)
st.write("Number of Balls:", number_of_balls)
st.write("Dynamic Rating:", dynamic_rating)
st.write("Static Rating:", static_rating)


st.subheader("Current Test Inputs")

st.write("Radial Load:", radial_load)
st.write("RPM:", rpm)
st.write("Temperature:", temperature)

# ----------------------------
# Derived Bearing Geometry
# ----------------------------

pitch_diameter = (bearing_id + bearing_od) / 2

angular_spacing = 360 / number_of_balls


st.subheader("Derived Geometry")

st.write("Pitch Diameter (mm):", round(pitch_diameter,3))
st.write("Ball Angular Spacing (deg):", round(angular_spacing,3))
# ----------------------------
# Internal Clearance
# ----------------------------

st.sidebar.header("Internal Clearance")

initial_clearance = st.sidebar.number_input("Initial Radial Clearance (mm)", value=0.020)
fit_reduction = st.sidebar.number_input("Clearance Reduction due to Fit (mm)", value=0.0124)

effective_clearance = initial_clearance - fit_reduction
st.subheader("Internal Clearance")

st.write("Initial Clearance (mm):", initial_clearance)
st.write("Fit Reduction (mm):", fit_reduction)
st.write("Effective Clearance (mm):", round(effective_clearance,6))
