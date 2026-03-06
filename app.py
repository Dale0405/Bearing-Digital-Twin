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
# Bearing Internal Clearance
# ----------------------------

st.subheader("Bearing Internal Clearance")

col1,col2,col3 = st.columns(3)

with col1:
    clearance_min = float(st.text_input("Minimum Clearance (mm)", "0.010"))

with col2:
    clearance_mean = float(st.text_input("Mean Clearance (mm)", "0.020"))

with col3:
    clearance_max = float(st.text_input("Maximum Clearance (mm)", "0.030"))


clearance_table = f"""
<table style="width:100%; text-align:center; border-collapse:collapse;">
<tr>
<th>Minimum Clearance</th>
<th>Mean Clearance</th>
<th>Maximum Clearance</th>
</tr>
<tr>
<td>{clearance_min}</td>
<td>{clearance_mean}</td>
<td>{clearance_max}</td>
</tr>
</table>
"""

st.markdown(clearance_table, unsafe_allow_html=True)

# ----------------------------
# Fit Conditions
# ----------------------------

st.subheader("Fit Conditions")

col1,col2,col3,col4 = st.columns(4)

with col1:
    bearing_id_min = float(st.text_input("Bearing ID Min (mm)", "40.000"))

with col2:
    bearing_id_max = float(st.text_input("Bearing ID Max (mm)", "40.020"))

with col3:
    shaft_min = float(st.text_input("Shaft Min (mm)", "40.010"))

with col4:
    shaft_max = float(st.text_input("Shaft Max (mm)", "40.030"))


col5,col6,col7,col8 = st.columns(4)

with col5:
    bearing_od_min = float(st.text_input("Bearing OD Min (mm)", "90.000"))

with col6:
    bearing_od_max = float(st.text_input("Bearing OD Max (mm)", "90.020"))

with col7:
    housing_min = float(st.text_input("Housing Min (mm)", "89.980"))

with col8:
    housing_max = float(st.text_input("Housing Max (mm)", "90.000"))


fit_table = f"""
<table style="width:100%; text-align:center; border-collapse:collapse;">
<tr>
<th>Bearing ID Min</th>
<th>Bearing ID Max</th>
<th>Shaft Min</th>
<th>Shaft Max</th>
<th>Bearing OD Min</th>
<th>Bearing OD Max</th>
<th>Housing Min</th>
<th>Housing Max</th>
</tr>
<tr>
<td>{bearing_id_min}</td>
<td>{bearing_id_max}</td>
<td>{shaft_min}</td>
<td>{shaft_max}</td>
<td>{bearing_od_min}</td>
<td>{bearing_od_max}</td>
<td>{housing_min}</td>
<td>{housing_max}</td>
</tr>
</table>
"""

st.markdown(fit_table, unsafe_allow_html=True)
