import streamlit as st
import numpy as np
import pandas as pd

st.markdown("<h1 style='text-align: center;'>BEARING TESTING DIGITAL TWIN</h1>", unsafe_allow_html=True)

# ----------------------------
# Bearing Parameters
# ----------------------------

st.subheader("Bearing Parameters")

# CSS to wrap header text and center values
st.markdown("""
<style>
[data-testid="stDataEditor"] th {
    white-space: normal !important;
    text-align: center !important;
}
[data-testid="stDataEditor"] td {
    text-align: center !important;
}
</style>
""", unsafe_allow_html=True)


bearing_table = pd.DataFrame({
    "ID<br>(mm)": [40.0],
    "OD<br>(mm)": [90.0],
    "Width<br>(mm)": [23.0],
    "Ball Dia<br>(mm)": [15.875],
    "Balls": [8],
    "Dynamic C<br>(N)": [31500],
    "Static Co<br>(N)": [24000]
})

bearing_data = st.data_editor(
    bearing_table,
    hide_index=True,
    use_container_width=True,
    column_config={
        col: st.column_config.NumberColumn()
        for col in bearing_table.columns
    }
)

# Extract values
bearing_id = float(bearing_data.iloc[0]["ID<br>(mm)"])
bearing_od = float(bearing_data.iloc[0]["OD<br>(mm)"])
bearing_width = float(bearing_data.iloc[0]["Width<br>(mm)"])
ball_diameter = float(bearing_data.iloc[0]["Ball Dia<br>(mm)"])
number_of_balls = int(bearing_data.iloc[0]["Balls"])
dynamic_rating = float(bearing_data.iloc[0]["Dynamic C<br>(N)"])
static_rating = float(bearing_data.iloc[0]["Static Co<br>(N)"])

# ----------------------------
# Dynamic DGBB Visualization
# ----------------------------

st.subheader("Bearing Visualization")

import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:

    fig, ax = plt.subplots(figsize=(6,6))

    # transparent background
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # normalized geometry
    outer_r = 1.0
    inner_r = bearing_id / bearing_od
    pitch_r = (outer_r + inner_r)/2
    ball_r = ball_diameter / bearing_od * 0.5

    # outer ring
    ax.add_patch(plt.Circle((0,0), outer_r, fill=False, linewidth=3, color="#6f6f6f"))
    ax.add_patch(plt.Circle((0,0), outer_r-0.07, fill=False, linewidth=2, color="#6f6f6f"))

    # inner ring
    ax.add_patch(plt.Circle((0,0), inner_r, fill=False, linewidth=3, color="#6f6f6f"))
    ax.add_patch(plt.Circle((0,0), inner_r+0.07, fill=False, linewidth=2, color="#6f6f6f"))

    # balls
    angles = np.linspace(0, 2*np.pi, number_of_balls, endpoint=False)

    for a in angles:
        x = pitch_r*np.cos(a)
        y = pitch_r*np.sin(a)

        ball = plt.Circle((x,y), ball_r,
                          color="#cfd3d6",
                          ec="#2b2b2b",
                          linewidth=1)

        ax.add_patch(ball)

    # ----------------------------
    # Red broken line labels
    # ----------------------------

    # OD reference point
    od_x = -outer_r * 0.7
    od_y = outer_r * 0.7

    ax.plot([od_x, -1.2], [od_y, 1.1],
            linestyle="--", color="red", linewidth=0.5)

    ax.scatter([od_x], [od_y], color="red", s=15)

    ax.text(-1.22, 1.12,
            f"OD = {bearing_od} mm",
            color="white",
            fontsize=20,
            ha="right")


    # ID reference point
    id_x = -inner_r * 0.7
    id_y = -inner_r * 0.7

    ax.plot([id_x, -1.2], [id_y, -1.1],
            linestyle="--", color="red", linewidth=0.5)

    ax.scatter([id_x], [id_y], color="red", s=15)

    ax.text(-1.22, -1.13,
            f"ID = {bearing_id} mm",
            color="white",
            fontsize=20,
            ha="right")


    # Ball reference point
    bx = pitch_r*np.cos(angles[0])
    by = pitch_r*np.sin(angles[0])

    ax.plot([bx+ball_r, 1.15], [by, by],
            linestyle="--", color="red", linewidth=0.5)

    ax.scatter([bx+ball_r], [by], color="red", s=15)

    ax.text(1.18, by,
            f"Ball = {ball_diameter} mm",
            color="white",
            fontsize=20,
            va="center")


    ax.set_xlim(-1.4,1.4)
    ax.set_ylim(-1.4,1.4)

    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)

    st.markdown("<div style='text-align:center;'>Front View</div>",
                unsafe_allow_html=True)
    
# ----------------------------
# Derived Geometry
# ----------------------------

st.subheader("Derived Geometry")

pitch_diameter = (bearing_id + bearing_od) / 2
ball_spacing = 360 / number_of_balls

import matplotlib.pyplot as plt
import numpy as np

col1, col2 = st.columns(2)

# ----------------------------
# Pitch Diameter
# ----------------------------

with col1:

    metric_col, img_col = st.columns([1,1])

    with metric_col:
        st.metric("Pitch Diameter (mm)", f"{pitch_diameter:.3f}")

    with img_col:

        fig, ax = plt.subplots(figsize=(2.4,2.4))

        # transparent background
        fig.patch.set_alpha(0)
        ax.set_facecolor("none")

        outer_r = 1.0
        inner_r = bearing_id / bearing_od
        pitch_r = (outer_r + inner_r)/2

        # OD
        ax.add_patch(plt.Circle((0,0), outer_r,
                                fill=False,
                                linewidth=2,
                                color="white"))

        # Pitch Diameter
        ax.add_patch(plt.Circle((0,0), pitch_r,
                                fill=False,
                                linestyle=":",
                                linewidth=2,
                                color="red"))

        # ID
        ax.add_patch(plt.Circle((0,0), inner_r,
                                fill=False,
                                linewidth=2,
                                color="white"))

        ax.set_xlim(-1.2,1.2)
        ax.set_ylim(-1.2,1.2)

        ax.set_aspect("equal")
        ax.axis("off")

        st.pyplot(fig)



# ----------------------------
# Ball Angular Spacing
# ----------------------------

with col2:

    metric_col, img_col = st.columns([1,1])

    with metric_col:
        st.metric("Ball Angular Spacing (deg)", f"{ball_spacing:.3f}")

    with img_col:

        fig, ax = plt.subplots(figsize=(2.4,2.4))

        fig.patch.set_alpha(0)
        ax.set_facecolor("none")

        outer_r = 1.0
        inner_r = 0.6
        pitch_r = (outer_r + inner_r)/2

        # rings
        ax.add_patch(plt.Circle((0,0), outer_r,
                                fill=False,
                                linewidth=2,
                                color="white"))

        ax.add_patch(plt.Circle((0,0), inner_r,
                                fill=False,
                                linewidth=2,
                                color="white"))

        # two balls showing spacing
        angles = [0, np.deg2rad(ball_spacing)]

        ball_r = 0.08

        for a in angles:

            x = pitch_r*np.cos(a)
            y = pitch_r*np.sin(a)

            ball = plt.Circle((x,y), ball_r,
                              color="#cfd3d6",
                              ec="#222222")

            ax.add_patch(ball)

        # angular arc
        theta = np.linspace(0, np.deg2rad(ball_spacing), 100)

        ax.plot(
            pitch_r*np.cos(theta),
            pitch_r*np.sin(theta),
            color="red",
            linewidth=2
        )

        ax.text(
            pitch_r*0.7*np.cos(np.deg2rad(ball_spacing/2)),
            pitch_r*0.7*np.sin(np.deg2rad(ball_spacing/2)),
            f"{ball_spacing:.1f}°",
            color="red",
            fontsize=8,
            ha="center"
        )

        ax.set_xlim(-1.2,1.2)
        ax.set_ylim(-1.2,1.2)

        ax.set_aspect("equal")
        ax.axis("off")

        st.pyplot(fig)

st.subheader("Bearing Internal Clearance")

col1, col2, col3 = st.columns(3)

with col1:
    clearance_min = st.number_input(
        "Min Clearance (mm)",
        value=0.01000,
        format="%.5f"
    )

with col2:
    clearance_max = st.number_input(
        "Max Clearance (mm)",
        value=0.03000,
        format="%.5f"
    )

# automatic calculation
clearance_mean = (clearance_min + clearance_max) / 2

with col3:
    st.text_input(
        "Mean Clearance (mm)",
        value=f"{clearance_mean:.5f}",
        disabled=True
    )
# ----------------------------
# Fit Conditions
# ----------------------------

st.subheader("Fit Conditions")

# Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    bearing_id_min = st.number_input(
        "Bearing ID Min (mm)",
        value=40.00000,
        format="%.5f"
    )

with col2:
    bearing_id_max = st.number_input(
        "Bearing ID Max (mm)",
        value=40.02000,
        format="%.5f"
    )

with col3:
    shaft_min = st.number_input(
        "Shaft Min (mm)",
        value=40.01000,
        format="%.5f"
    )

with col4:
    shaft_max = st.number_input(
        "Shaft Max (mm)",
        value=40.03000,
        format="%.5f"
    )


# Row 2
col5, col6, col7, col8 = st.columns(4)

with col5:
    bearing_od_min = st.number_input(
        "Bearing OD Min (mm)",
        value=90.00000,
        format="%.5f"
    )

with col6:
    bearing_od_max = st.number_input(
        "Bearing OD Max (mm)",
        value=90.02000,
        format="%.5f"
    )

with col7:
    housing_min = st.number_input(
        "Housing Min (mm)",
        value=89.98000,
        format="%.5f"
    )

with col8:
    housing_max = st.number_input(
        "Housing Max (mm)",
        value=90.00000,
        format="%.5f"
    )


# ----------------------------
# Calculations
# ----------------------------

# Shaft interference
min_shaft_fit = shaft_min - bearing_id_max
max_shaft_fit = shaft_max - bearing_id_min

effective_shaft_interference = (min_shaft_fit + max_shaft_fit) / 2

# RIC reduction assumption
ric_reduction = effective_shaft_interference * 0.8

effective_radial_clearance = clearance_mean - ric_reduction


# ----------------------------
# Fit Results
# ----------------------------

st.markdown("---")
st.subheader("Fit Results")

st.markdown(f"""
<table style="width:100%; border-collapse:collapse; text-align:center;">
<tr>
<th style="border:1px solid gray; padding:8px; width:20%;">Minimum<br>Shaft Fit<br>(mm)</th>
<th style="border:1px solid gray; padding:8px; width:20%;">Maximum<br>Shaft Fit<br>(mm)</th>
<th style="border:1px solid gray; padding:8px; width:20%;">Effective Shaft<br>Interference<br>(mm)</th>
<th style="border:1px solid gray; padding:8px; width:20%;">RIC Reduction<br>due to Shaft Fit<br>(mm)</th>
<th style="border:1px solid gray; padding:8px; width:20%;">Effective Radial<br>Clearance<br>(mm)</th>
</tr>
<tr>
<td style="border:1px solid gray; padding:8px;">{min_shaft_fit:.5f}</td>
<td style="border:1px solid gray; padding:8px;">{max_shaft_fit:.5f}</td>
<td style="border:1px solid gray; padding:8px;">{effective_shaft_interference:.5f}</td>
<td style="border:1px solid gray; padding:8px;">{ric_reduction:.5f}</td>
<td style="border:1px solid gray; padding:8px;">{effective_radial_clearance:.5f}</td>
</tr>
</table>
""", unsafe_allow_html=True)

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
