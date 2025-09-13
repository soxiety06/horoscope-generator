import streamlit as st
import requests
import hashlib
import time

# API endpoint
API_URL = "https://horoscopefree.herokuapp.com/daily/"

st.set_page_config(page_title="Daily Horoscope", layout="centered")

# Title
st.markdown(
    """
    <h1 style='text-align: center;'>🔮 Daily Horoscope Generator</h1>
    <p style='text-align: center;'>Enter your name to reveal your destiny</p>
    """,
    unsafe_allow_html=True,
)

# Input form
with st.form("horoscope_form"):
    name = st.text_input("Enter your name")
    submitted = st.form_submit_button("Confirm")

if submitted and name.strip():
    # Custom animation (falling stars)
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <svg width="200" height="200" viewBox="0 0 200 200">
                <circle cx="50" cy="40" r="4" fill="gold">
                    <animateTransform attributeName="transform" type="translate" from="0 0" to="0 200" dur="2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="120" cy="20" r="3" fill="white">
                    <animateTransform attributeName="transform" type="translate" from="0 0" to="0 200" dur="3s" repeatCount="indefinite"/>
                </circle>
                <circle cx="180" cy="60" r="5" fill="yellow">
                    <animateTransform attributeName="transform" type="translate" from="0 0" to="0 200" dur="4s" repeatCount="indefinite"/>
                </circle>
            </svg>
            <p style="font-size:18px; color:gray;">Consulting the stars...</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Delay for effect
    time.sleep(3)

    try:
        # Hash name → zodiac sign
        zodiac_index = int(hashlib.md5(name.encode()).hexdigest(), 16) % 12
        zodiac_signs = [
            "aries", "taurus", "gemini", "cancer", "leo", "virgo",
            "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
        ]
        sign = zodiac_signs[zodiac_index]

        # Fetch horoscope
        response = requests.get(API_URL, timeout=5)
        data = response.json()
        horoscope = data.get(sign, "The stars are quiet today. Try again later.")
    except Exception as e:
        horoscope = f"⚠️ Could not fetch horoscope. Error: {e}"

    # Display result
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 30vh; flex-direction: column;">
            <h2 style="text-align: center;">{name}</h2>
            <p style="text-align: center; font-size: 20px;">{horoscope}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
