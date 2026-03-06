import streamlit as st

st.title("Bearing Digital Twin")

radial_load = st.number_input("Radial Load (N)", value=14000)
rpm = st.number_input("RPM", value=3000)
temperature = st.number_input("Temperature (C)", value=60)

st.write("Current Inputs:")
st.write("Radial Load:", radial_load)
st.write("RPM:", rpm)
st.write("Temperature:", temperature)
