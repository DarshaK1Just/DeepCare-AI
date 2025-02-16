import streamlit as st
from pages import analysis, appointment
from services.auth import login

# Configure Streamlit page
st.set_page_config(page_title="DeepCare AI 🤖", page_icon="🩺", layout="wide")

# Custom CSS for better UI
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {background-color: #f8f9fa;}
        .stButton>button {width: 100%;}
        .title-text {
        font-size: 40px; /* Adjust size as needed */
        font-weight: bold;
        text-align: center;
        color: #2E3B55; /* Custom color */
        padding: 10px;
    }
        .subtitle-text {font-size: 18px; color: #555;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with enhanced styling
st.header("DeepCare AI 🤖 - Smart Healthcare Assistant")
st.markdown('<p class="subtitle-text">Your AI-powered health companion.</p>', unsafe_allow_html=True)

# Authentication
if not login():
    st.stop()

# Sidebar Navigation
st.sidebar.header("🌍 **Navigation**")
page = st.sidebar.radio(
    "🔍 **Go to**", 
    ["🩺 Health Analysis & Suggestions", "📅 Schedule an Appointment"],
    format_func=lambda x: x.split(" ")[1]
)

# Dynamic Page Rendering
if page == "🩺 Health Analysis & Suggestions":
    analysis.show()
elif page == "📅 Schedule an Appointment":
    appointment.show()
