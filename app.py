import streamlit as st
import numpy as np
import pandas as pd

st.markdown("<h1 style='text-align: center;'>BEARING TESTING DIGITAL TWIN</h1>", unsafe_allow_html=True)

st.header("Bearing Parameters")

col1,col2,col3,col4 = st.columns(4)

with col1:
    bearing_id = float(st.text_input("Bearing ID (mm)", "40"))

with col2:
    bearing_od = float(st.text_input("Bearing OD (mm)", "90"))

with col3:
    bearing_width = float(st.text_input("Bearing Width (mm)", "23"))

with col4:
    ball_diameter = float(st.text_input("Ball Diameter (mm)", "15.875"))

col5,col6,col7 = st.columns(3)

with col5:
    number_of_balls = int(st.text_input("Number of Balls", "8"))

with col6:
    dynamic_rating = float(st.text_input("Dynamic Load Rating C (N)", "31500"))

with col7:
    static_rating = float(st.text_input("Static Load Rating Co (N)", "24000"))

# ----------------------------
# Test Conditions
# ----------------------------
st.header("Test Conditions")

radial_load = float(st.text_input("Radial Load (N)", "14000"))
axial_load = float(st.text_input("Axial Load (N)", "0"))
rpm = float(st.text_input("RPM", "3000"))
ambient_temperature = float(st.text_input("Ambient Temperature (°C)", "25"))

lubrication = st.selectbox(
    "Lubrication Type",
    ["Grease", "Oil"]
)

# ----------------------------
# Bearing Parameter Table
# ----------------------------
st.subheader("Bearing Parameters")

table_html = f"""
<table style="width:100%; text-align:center; border-collapse:collapse;">
<tr>
<th>ID (mm)</th>
<th>OD (mm)</th>
<th>Width (mm)</th>
<th>Ball Dia (mm)</th>
<th>Balls</th>
<th>Dynamic C (N)</th>
<th>Static Co (N)</th>
</tr>
<tr>
<td>{bearing_id}</td>
<td>{bearing_od}</td>
<td>{bearing_width}</td>
<td>{ball_diameter}</td>
<td>{number_of_balls}</td>
<td>{dynamic_rating}</td>
<td>{static_rating}</td>
</tr>
</table>
"""

st.markdown(table_html, unsafe_allow_html=True)

# ----------------------------
# Derived Geometry
# ----------------------------

pitch_diameter = (bearing_id + bearing_od) / 2
ball_spacing = 360 / number_of_balls

st.subheader("Derived Geometry")

col1, col2 = st.columns(2)

with col1:
    st.metric("Pitch Diameter (mm)", round(pitch_diameter,3))

with col2:
    st.metric("Ball Angular Spacing (deg)", round(ball_spacing,3))

# ----------------------------
# Internal Clearance
# ----------------------------

st.subheader("Internal Clearance")

col1, col2 = st.columns(2)

with col1:
    initial_clearance = float(st.text_input("Initial Radial Clearance (mm)", "0.020"))

with col2:
    fit_reduction = float(st.text_input("Clearance Reduction from Fit (mm)", "0.0124"))

effective_clearance = initial_clearance - fit_reduction


# Horizontal table display
clearance_table = f"""
<table style="width:100%; text-align:center; border-collapse:collapse;">
<tr>
<th>Initial Clearance (mm)</th>
<th>Fit Reduction (mm)</th>
<th>Effective Clearance (mm)</th>
</tr>
<tr>
<td>{initial_clearance}</td>
<td>{fit_reduction}</td>
<td>{round(effective_clearance,6)}</td>
</tr>
</table>
"""

st.markdown(clearance_table, unsafe_allow_html=True)
