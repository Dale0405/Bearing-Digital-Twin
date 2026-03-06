import streamlit as st
import numpy as np
import pandas as pd

st.markdown("<h1 style='text-align: center;'>BEARING TESTING DIGITAL TWIN</h1>", unsafe_allow_html=True)

# ----------------------------
# Bearing Parameters
# ----------------------------

st.subheader("Bearing Parameters")

bearing_table = pd.DataFrame({
    "ID (mm)": [40.0],
    "OD (mm)": [90.0],
    "Width (mm)": [23.0],
    "Ball Dia (mm)": [15.875],
    "Balls": [8],
    "Dynamic C (N)": [31500],
    "Static Co (N)": [24000]
})

col1, col2 = st.columns([3,2])

with col1:

    bearing_data = st.data_editor(
        bearing_table,
        hide_index=True,
        use_container_width=True,
        column_config={
            "ID (mm)": st.column_config.NumberColumn(),
            "OD (mm)": st.column_config.NumberColumn(),
            "Width (mm)": st.column_config.NumberColumn(),
            "Ball Dia (mm)": st.column_config.NumberColumn(),
            "Balls": st.column_config.NumberColumn(),
            "Dynamic C (N)": st.column_config.NumberColumn(),
            "Static Co (N)": st.column_config.NumberColumn()
        }
    )

    bearing_id = bearing_data["ID (mm)"][0]
    bearing_od = bearing_data["OD (mm)"][0]
    bearing_width = bearing_data["Width (mm)"][0]
    ball_diameter = bearing_data["Ball Dia (mm)"][0]
    number_of_balls = int(bearing_data["Balls"][0])
    dynamic_rating = bearing_data["Dynamic C (N)"][0]
    static_rating = bearing_data["Static Co (N)"][0]

# ----------------------------
# DGBB Front View Diagram
# ----------------------------

st.subheader("Bearing Visualization")

import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:

    fig, ax = plt.subplots(figsize=(2,2))

    # Normalized radii for visualization
    outer_r = 1.0
    inner_r = 0.55
    ball_r = 0.12
    pitch_r = 0.78

    # Outer ring
    ax.add_patch(plt.Circle((0,0), outer_r, fill=False, linewidth=2))

    # Inner ring
    ax.add_patch(plt.Circle((0,0), inner_r, fill=False, linewidth=2))

    # Balls
    angles = np.linspace(0, 2*np.pi, number_of_balls, endpoint=False)

    for a in angles:
        x = pitch_r*np.cos(a)
        y = pitch_r*np.sin(a)

        ball = plt.Circle((x,y), ball_r, fill=False)
        ax.add_patch(ball)

    # Center cross
    ax.axhline(0, linewidth=0.6)
    ax.axvline(0, linewidth=0.6)

    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)

    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)
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

st.subheader("Bearing Internal Clearance")

clearance_table = pd.DataFrame({
    "Min Clearance (mm)": [0.010],
    "Mean Clearance (mm)": [0.020],
    "Max Clearance (mm)": [0.030]
})

clearance_data = st.data_editor(
    clearance_table,
    num_rows="fixed",
    use_container_width=True
)

clearance_min = clearance_data["Min Clearance (mm)"][0]
clearance_mean = clearance_data["Mean Clearance (mm)"][0]
clearance_max = clearance_data["Max Clearance (mm)"][0]

st.subheader("Fit Conditions")

fit_table = pd.DataFrame({
    "Bearing ID Min": [40.000],
    "Bearing ID Max": [40.020],
    "Shaft Min": [40.010],
    "Shaft Max": [40.030],
    "Bearing OD Min": [90.000],
    "Bearing OD Max": [90.020],
    "Housing Min": [89.980],
    "Housing Max": [90.000]
})

fit_data = st.data_editor(
    fit_table,
    num_rows="fixed",
    use_container_width=True
)

bearing_id_min = fit_data["Bearing ID Min"][0]
bearing_id_max = fit_data["Bearing ID Max"][0]
shaft_min = fit_data["Shaft Min"][0]
shaft_max = fit_data["Shaft Max"][0]

bearing_od_min = fit_data["Bearing OD Min"][0]
bearing_od_max = fit_data["Bearing OD Max"][0]
housing_min = fit_data["Housing Min"][0]
housing_max = fit_data["Housing Max"][0]
