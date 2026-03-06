# ----------------------------
# Bearing Parameters Table
# ----------------------------

bearing_table = pd.DataFrame({
    "Parameter":[
        "Bearing ID",
        "Bearing OD",
        "Width",
        "Ball Diameter",
        "Number of Balls",
        "Dynamic Load Rating C",
        "Static Load Rating Co"
    ],
    "Value":[
        bearing_id,
        bearing_od,
        bearing_width,
        ball_diameter,
        number_of_balls,
        dynamic_rating,
        static_rating
    ],
    "Unit":[
        "mm",
        "mm",
        "mm",
        "mm",
        "-",
        "N",
        "N"
    ]
})

st.subheader("Bearing Parameters")
st.table(bearing_table)
