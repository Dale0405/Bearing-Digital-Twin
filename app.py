import streamlit as st
import numpy as np
import pandas as pd

st.title("Bearing Digital Twin")

# ----------------------------
# Bearing Parameters
# ----------------------------
st.sidebar.header("Bearing Parameters")

bearing_id = float(st.sidebar.text_input("Bearing ID (mm)", "40"))
bearing_od = float(st.sidebar.text_input("Bearing OD (mm)", "90"))
bearing_width = float(st.sidebar.text_input("Bearing Width (mm)", "23"))

ball_diameter = float(st.sidebar.text_input("Ball Diameter (mm)", "15.875"))
number_of_balls = int(st.sidebar.text_input("Number of Balls", "8"))

dynamic_rating = float(st.sidebar.text_input("Dynamic Load Rating C (N)", "31500"))
static_rating = float(st.sidebar.text_input("Static Load Rating Co (N)", "24000"))

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
