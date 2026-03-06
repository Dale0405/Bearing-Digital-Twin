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
