import streamlit as st
import pandas as pd
from services.deepseek_api import analyze_text
from utils.disease_mapping import disease_to_specialist
from data.doctors import doctors
from data.regions import regions

def get_best_doctor(disease, region):
    specialty = disease_to_specialist.get(disease.lower(), "General Medicine")
    return [doc for doc in doctors if doc['specialty'] == specialty and doc['region'] == region]

st.header("🏥 Health Analysis & Recommendations")
user_input = st.text_area("📝 Enter symptoms or medical query:")
selected_region = st.selectbox("🌎 Choose Region", regions, key="analysis_region")

if st.button("🔍 Analyze & Suggest"):
    if user_input:
        result = analyze_text(user_input)
        disease_detected = result.get("disease", "Unknown condition")
        suggestion = f"Try consulting a specialist in {disease_to_specialist.get(disease_detected.lower(), 'General Medicine')}"

        st.markdown(f"### 🩺 Detected Condition: **{disease_detected}**")
        st.markdown(f"### 💡 Suggestion: {suggestion}")

        matched_doctors = get_best_doctor(disease_detected, selected_region)
        if matched_doctors:
            df = pd.DataFrame(matched_doctors)
            st.dataframe(df[['name', 'specialty', 'availability']], hide_index=True)

        if "important_links" in result:
            st.markdown("### 🔗 Important Links for Reference")
            for link in result["important_links"]:
                st.markdown(f"- [{link}]({link})")
    else:
        st.error("Please enter a query.")
