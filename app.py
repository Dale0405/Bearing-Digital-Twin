# ----------------------------
# Bearing Parameters (Horizontal Panel)
# ----------------------------

st.subheader("Bearing Parameters")

c1,c2,c3,c4,c5,c6,c7 = st.columns(7)

c1.metric("ID (mm)", bearing_id)
c2.metric("OD (mm)", bearing_od)
c3.metric("Width (mm)", bearing_width)
c4.metric("Ball Dia (mm)", ball_diameter)
c5.metric("Balls", number_of_balls)
c6.metric("Dynamic C (N)", dynamic_rating)
c7.metric("Static Co (N)", static_rating)
