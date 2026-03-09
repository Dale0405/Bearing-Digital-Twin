import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# GLOBAL STYLE
# ----------------------------------------------------

st.markdown("""
<style>

/* Wrap header text like Excel */
[data-testid="stDataEditor"] th {
    white-space: normal !important;
    text-align: center !important;
    line-height: 1.2em;
    font-weight: 600;
}

/* Center editable values */
[data-testid="stDataEditor"] td {
    text-align: center !important;
}

/* Force columns to share space evenly */
[data-testid="stDataEditor"] table {
    table-layout: fixed !important;
}

/* Allow header line breaks */
[data-testid="stDataEditor"] th div {
    white-space: normal !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>BEARING TESTING DIGITAL TWIN</h1>", unsafe_allow_html=True)
# ----------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    ["Test Setup", "Test Data", "Test Results"]
)


# ====================================================
# TEST SETUP PAGE
# ====================================================

if page == "Test Setup":

    st.title("Test Setup")

    # ----------------------------
    # Bearing Parameters
    # ----------------------------

    st.markdown("<h3 style='text-align:center;'>Bearing Parameters</h3>", unsafe_allow_html=True)

    st.markdown("""
    <style>

    .param-header{
        text-align:center;
        font-weight:bold;
        margin-bottom:5px;
    }

    .param-row{
        border:1px solid #555;
        padding:6px;
    }

    </style>
    """, unsafe_allow_html=True)


    left, right = st.columns([1,1])


    # ----------------------------
    # PARAMETER TABLE
    # ----------------------------

    with left:

        h1, h2 = st.columns([1,1])
        h1.markdown('<div class="param-header">Parameters</div>', unsafe_allow_html=True)
        h2.markdown('<div class="param-header">Values</div>', unsafe_allow_html=True)

        r1c1, r1c2 = st.columns([1,1])
        r1c1.markdown('<div class="param-row">ID (mm)</div>', unsafe_allow_html=True)
        bearing_id = float(r1c2.text_input("", "40", label_visibility="collapsed"))

        r2c1, r2c2 = st.columns([1,1])
        r2c1.markdown('<div class="param-row">OD (mm)</div>', unsafe_allow_html=True)
        bearing_od = float(r2c2.text_input("", "90", label_visibility="collapsed"))

        r3c1, r3c2 = st.columns([1,1])
        r3c1.markdown('<div class="param-row">Width (mm)</div>', unsafe_allow_html=True)
        bearing_width = float(r3c2.text_input("", "23", label_visibility="collapsed"))

        r4c1, r4c2 = st.columns([1,1])
        r4c1.markdown('<div class="param-row">Ball Diameter (mm)</div>', unsafe_allow_html=True)
        ball_diameter = float(r4c2.text_input("", "15.88", label_visibility="collapsed"))

        r5c1, r5c2 = st.columns([1,1])
        r5c1.markdown('<div class="param-row">Number of Balls</div>', unsafe_allow_html=True)
        number_of_balls = int(r5c2.text_input("", "8", label_visibility="collapsed"))

        r6c1, r6c2 = st.columns([1,1])
        r6c1.markdown('<div class="param-row">Dynamic Load Cr (N)</div>', unsafe_allow_html=True)
        dynamic_rating = float(r6c2.text_input("", "31500", label_visibility="collapsed"))

        r7c1, r7c2 = st.columns([1,1])
        r7c1.markdown('<div class="param-row">Static Load Co (N)</div>', unsafe_allow_html=True)
        static_rating = float(r7c2.text_input("", "24000", label_visibility="collapsed"))


    # ----------------------------
    # BEARING VISUALIZATION
    # ----------------------------

    with right:

        fig, ax = plt.subplots(figsize=(6,6))

        fig.patch.set_alpha(0)
        ax.set_facecolor("none")

        outer_r = 1.0
        inner_r = bearing_id / bearing_od
        pitch_r = (outer_r + inner_r) / 2
        ball_r = ball_diameter / bearing_od * 0.5

        ax.add_patch(plt.Circle((0,0), outer_r, fill=False, linewidth=3, color="#8c8f94"))
        ax.add_patch(plt.Circle((0,0), outer_r-0.07, fill=False, linewidth=2, color="#8c8f94"))

        ax.add_patch(plt.Circle((0,0), inner_r, fill=False, linewidth=3, color="#8c8f94"))
        ax.add_patch(plt.Circle((0,0), inner_r+0.07, fill=False, linewidth=2, color="#8c8f94"))

        angles = np.linspace(0, 2*np.pi, number_of_balls, endpoint=False)

        for a in angles:

            x = pitch_r * np.cos(a)
            y = pitch_r * np.sin(a)

            ax.add_patch(plt.Circle((x,y), ball_r, color="#cfd3d6", ec="#2b2b2b", linewidth=1.2))

        ax.set_xlim(-1.4,1.4)
        ax.set_ylim(-1.4,1.4)

        ax.set_aspect("equal")
        ax.axis("off")

        st.pyplot(fig)

        st.markdown("<div style='text-align:center;'>Front View</div>", unsafe_allow_html=True)



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
    lubrication = st.selectbox("Lubrication Type", ["Grease", "Oil"])
    

# ====================================================
# TEST DATA PAGE
# ====================================================
elif page == "Test Data":

    st.title("Test Data")

    # ----------------------------
    # Initialize session storage
    # ----------------------------
    if "raw_test_data" not in st.session_state:
        st.session_state.raw_test_data = None

    if "twin_data_table" not in st.session_state:
        st.session_state.twin_data_table = None

    # ----------------------------
    # Standard Digital Twin columns
    # ----------------------------

    standard_columns = [
        "Test Time (hr)",
        "Speed (RPM)",
        "Radial Load (N)",
        "Axial Load (N)",
        "Temp 1# (°C)",
        "Temp 2# (°C)",
        "Temp 3# (°C)",
        "Temp 4# (°C)",
        "Vibration (g)"
    ]

    # ----------------------------
    # Upload Test Machine Data
    # ----------------------------

    uploaded_file = st.file_uploader(
        "Upload Test Machine Data",
        type=["xlsx", "xls", "csv"]
    )

    if uploaded_file is not None:

        # ----------------------------
        # Read uploaded file
        # ----------------------------

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Store raw data in session
        st.session_state.raw_test_data = df

        # ----------------------------
        # Keyword recognition dictionary
        # ----------------------------

        column_map = {
            "Test Time (hr)": ["Time", "Time (hr)", "Test Time (hr)", "Duration"],
            "Speed (RPM)": ["RPM", "Speed"],
            "Radial Load (N)": ["Radial Load", "Fr"],
            "Axial Load (N)": ["Axial Load", "Fa"],
            "Temp 1# (°C)": ["Temp 1# (°C)", "Temp 1#", "Temp 1", "Temperature 1", "Temp1"],
            "Temp 2# (°C)": ["Temp 2# (°C)", "Temp 2#", "Temp 2", "Temperature 2", "Temp2"],
            "Temp 3# (°C)": ["Temp 3# (°C)", "Temp 3#", "Temp 3", "Temperature 3", "Temp3"],
            "Temp 4# (°C)": ["Temp 4# (°C)", "Temp 4#", "Temp 4", "Temperature 4", "Temp4"],
            "Vibration (g)": ["Vibration", "Vib"]
        }

        # ----------------------------
        # Create Digital Twin table
        # ----------------------------

        data_table = pd.DataFrame(index=df.index, columns=standard_columns)

        for standard_col, keywords in column_map.items():

            found_series = None

            for col in df.columns:
                for key in keywords:
                    if key in col:
                        found_series = df[col]
                        break

                if found_series is not None:
                    break

            data_table[standard_col] = found_series

        # ----------------------------
        # Apply formatting rules
        # ----------------------------

        if "Speed (RPM)" in data_table:
            data_table["Speed (RPM)"] = pd.to_numeric(
                data_table["Speed (RPM)"], errors="coerce"
            ).round(0)

        if "Radial Load (N)" in data_table:
            data_table["Radial Load (N)"] = pd.to_numeric(
                data_table["Radial Load (N)"], errors="coerce"
            ).round(0)

        if "Axial Load (N)" in data_table:
            data_table["Axial Load (N)"] = pd.to_numeric(
                data_table["Axial Load (N)"], errors="coerce"
            ).round(0)

        for temp_col in ["Temp 1# (°C)", "Temp 2# (°C)", "Temp 3# (°C)", "Temp 4# (°C)"]:
            if temp_col in data_table:
                data_table[temp_col] = pd.to_numeric(
                    data_table[temp_col], errors="coerce"
                ).round(1)

        if "Vibration (g)" in data_table:
            data_table["Vibration (g)"] = pd.to_numeric(
                data_table["Vibration (g)"], errors="coerce"
            ).round(2)

        # Store processed twin table
        st.session_state.twin_data_table = data_table

    # ----------------------------
    # Display stored table
    # ----------------------------

    if st.session_state.twin_data_table is not None:

        st.subheader("Test Data Table")
        st.dataframe(st.session_state.twin_data_table, use_container_width=True)

    else:

        st.info("Upload a test data file to display the table.")



# ====================================================
# TEST RESULTS PAGE
# ====================================================

if page == "Test Results":

    st.title("Test Results")

    st.write("Engineering results will appear here.")




