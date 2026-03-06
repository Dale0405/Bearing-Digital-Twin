# Inputs first
bearing_id = st.sidebar.number_input("Bearing ID (mm)", value=40.0)
bearing_od = st.sidebar.number_input("Bearing OD (mm)", value=90.0)
bearing_width = st.sidebar.number_input("Bearing Width (mm)", value=23.0)

ball_diameter = st.sidebar.number_input("Ball Diameter (mm)", value=15.875)
number_of_balls = st.sidebar.number_input("Number of Balls", value=8)

dynamic_rating = st.sidebar.number_input("Dynamic Load Rating C (N)", value=31500)
static_rating = st.sidebar.number_input("Static Load Rating Co (N)", value=24000)


# THEN show horizontal panel
st.subheader("Bearing Parameters")

c1,c2,c3,c4,c5,c6,c7 = st.columns(7)

c1.metric("ID (mm)", bearing_id)
c2.metric("OD (mm)", bearing_od)
c3.metric("Width (mm)", bearing_width)
c4.metric("Ball Dia (mm)", ball_diameter)
c5.metric("Balls", number_of_balls)
c6.metric("Dynamic C (N)", dynamic_rating)
c7.metric("Static Co (N)", static_rating)
