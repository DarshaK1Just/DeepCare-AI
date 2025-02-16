import streamlit as st
import datetime
from data.doctors import doctors
from data.regions import regions

st.header("📅 Book Your Appointment")
selected_region = st.selectbox("🌎 Choose Region", regions, key="appointment_region")
available_doctors = [doc for doc in doctors if doc['region'] == selected_region]
selected_doctor = st.selectbox("👨‍⚕️ Select a Doctor", [doc['name'] for doc in available_doctors])
selected_date = st.date_input("📆 Select Date", min_value=datetime.date.today())
selected_time = st.time_input("⏰ Select Time")
patient_email = st.text_input("📧 Enter Your Email")
patient_phone = st.text_input("📞 Enter Your Phone Number")

if st.button("✅ Confirm Appointment"):
    if patient_email and patient_phone:
        st.success(f"✅ Appointment confirmed with {selected_doctor} on {selected_date} at {selected_time}.")
        st.markdown(f"📧 Confirmation sent to **{patient_email}**")
        st.markdown(f"📞 Contact: **{patient_phone}**")
    else:
        st.error("Please enter your contact details.")
