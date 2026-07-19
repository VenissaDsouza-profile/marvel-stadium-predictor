import streamlit as st
import pandas as pd
import joblib
from datetime import date
import matplotlib.pyplot as plt

# ── Load model and features ──────────────────────────────────────
rf = joblib.load("data/model_random_forest.pkl")
feature_cols = joblib.load("data/feature_cols.pkl")

# ── Page config ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Marvel Stadium Traffic Predictor",
    page_icon="🏟️",
    layout="centered"
)

# ── Header ───────────────────────────────────────────────────────
st.title("🏟️ Marvel Stadium Traffic Predictor")
st.markdown("*Predict whether a game day will be high traffic based on date and weather conditions.*")
st.divider()

# ── Sidebar inputs ───────────────────────────────────────────────
st.sidebar.header("🎯 Enter Game Details")

selected_date = st.sidebar.date_input("Game Date", value=date.today())
temperature = st.sidebar.slider("Max Temperature (°C)", 5, 40, 15)
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 30, 0)
windspeed = st.sidebar.slider("Wind Speed (km/h)", 0, 80, 20)

# ── Auto-calculate date features ─────────────────────────────────
day_of_week = selected_date.weekday()        # 0=Mon, 6=Sun
month = selected_date.month
is_weekend = 1 if day_of_week in [5, 6] else 0
is_friday_night = 1 if day_of_week == 4 else 0
is_finals_month = 1 if month in [8, 9] else 0
is_rainy = 1 if rainfall > 2 else 0
is_cold = 1 if temperature < 14 else 0
is_public_holiday = 0  # simplified for demo

# ── Build input dataframe ─────────────────────────────────────────
input_data = pd.DataFrame([{
    "day_of_week": day_of_week,
    "month": month,
    "is_weekend": is_weekend,
    "is_friday_night": is_friday_night,
    "is_public_holiday": is_public_holiday,
    "is_rainy": is_rainy,
    "is_cold": is_cold,
    "is_finals_month": is_finals_month,
    "temperature_2m_max": temperature,
    "precipitation_sum": rainfall,
    "windspeed_10m_max": windspeed
}])[feature_cols]

# ── Prediction ────────────────────────────────────────────────────
prediction = rf.predict(input_data)[0]
probability = rf.predict_proba(input_data)[0][1]

# ── Display results ───────────────────────────────────────────────
st.subheader("📅 Selected Game Details")

col1, col2, col3 = st.columns(3)
col1.metric("Day", selected_date.strftime("%A"))
col2.metric("Month", selected_date.strftime("%B"))
col3.metric("Season", "Finals 🏆" if is_finals_month else "Regular")

st.divider()
st.subheader("🔮 Prediction Result")

if prediction == 1:
    st.success("🔴 HIGH TRAFFIC DAY — Expect big crowds!")
else:
    st.info("🟢 NORMAL DAY — Quieter than usual.")

# ── Probability bar ───────────────────────────────────────────────
st.markdown(f"**Confidence: {probability * 100:.1f}% chance of high traffic**")
st.progress(float(probability))

st.divider()

# ── Weather summary ───────────────────────────────────────────────
st.subheader("🌦️ Weather Conditions")
col4, col5, col6 = st.columns(3)
col4.metric("Temperature", f"{temperature}°C", delta="Cold ❄️" if is_cold else "Mild ☀️")
col5.metric("Rainfall", f"{rainfall}mm", delta="Rainy 🌧️" if is_rainy else "Dry ☀️")
col6.metric("Wind", f"{windspeed} km/h")

st.divider()

# ── Key insight ───────────────────────────────────────────────────
st.subheader("💡 Key Insight")
st.markdown("""
> *Day of week is the single strongest predictor of busy days at Marvel Stadium —
> accounting for 55% of the model's decisions. Saturday games are almost always
> high traffic regardless of weather.*
""")

st.caption("Built by Nissa | Master of Analytics, RMIT | Data: Ticketmaster API, Open-Meteo, AFL Tables")