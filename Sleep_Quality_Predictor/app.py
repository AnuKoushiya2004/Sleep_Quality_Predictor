import streamlit as st
import pandas as pd
from datetime import datetime
import random
# --- Session State for History ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Page Layout ---
st.set_page_config(page_title="Sleep Quality Predictor", page_icon="🌙", layout="wide")
st.title("🌙 Sleep Quality Predictor")
st.subheader("Monitor and improve your sleep with personalized tips")

# --- Input Section ---
with st.container():
    st.markdown("### 🛌 Enter Your Sleep & Lifestyle Data")
    col1, col2 = st.columns(2)
    
    with col1:
        sleep_hours = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
        bedtime = st.time_input("Bedtime", value=datetime.strptime("22:30", "%H:%M").time())
        wakeup_time = st.time_input("Wake-up Time", value=datetime.strptime("06:30", "%H:%M").time())
        caffeine = st.selectbox("Caffeine Intake", ["None", "Low", "Moderate", "High"])
    
    with col2:
        exercise = st.number_input("Exercise Duration (minutes)", min_value=0, max_value=180, value=30)
        screen_time = st.number_input("Screen Time Before Bed (minutes)", min_value=0, max_value=300, value=60)
        stress = st.slider("Stress Level (0-10)", 0, 10, 5)
        mood = st.selectbox("Mood Before Sleep", ["Happy", "Neutral", "Sad", "Anxious"])
        interruptions = st.radio("Sleep Interruptions?", ["No", "Yes"])

# --- Predict Button ---
if st.button("Predict Sleep Quality 🌟"):
    
    # --- Innovative Prediction Logic (Mock ML model for demo) ---
    score = 0
    
    # Sleep duration factor
    if sleep_hours >= 7 and sleep_hours <= 9:
        score += 3
    elif sleep_hours >= 5 and sleep_hours < 7:
        score += 2
    else:
        score += 1
    # Caffeine factor
    
    caffeine_dict = {"None":3, "Low":2, "Moderate":1, "High":0}
    score += caffeine_dict[caffeine]
    # Exercise factor

    if exercise >= 30:
        score += 2
    else:
        score += 1
    # Screen time factor

    if screen_time <= 60:
        score += 2
    else:
        score += 1
    # Stress factor

    score += max(0, 3 - stress//3)
    # Mood factor

    mood_dict = {"Happy":2, "Neutral":1, "Sad":0, "Anxious":0}
    score += mood_dict[mood]

    # Interruptions
    if interruptions == "No":
        score += 2
    else:
        score += 0

    # Determine Sleep Quality
    if score >= 11:
        prediction = "Good"
        advice = "🎉 Excellent! Keep maintaining your healthy sleep routine."
    elif score >= 7:
        prediction = "Average"
        advice = "⚡ Average sleep. Try reducing screen time before bed or moderate caffeine."
    else:
        prediction = "Poor"
        advice = "💤 Poor sleep. Increase exercise, reduce stress, and avoid caffeine before bed."
    
    st.markdown(f"### Predicted Sleep Quality: **{prediction}**")
    st.info(advice)
    # --- Store in Session History ---
    st.session_state.history.append({
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Sleep Hours": sleep_hours,
        "Stress": stress,
        "Mood": mood,
        "Prediction": prediction
    })
# --- View History ---
if st.checkbox("📊 View Past Predictions"):
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.line_chart(df[["Sleep Hours", "Stress"]])
        st.table(df)
    else:
        st.write("No history yet. Make a prediction first!")
# --- Reset Inputs ---
if st.button("🔄 Reset History"):
    st.session_state.history = []
    st.success("History cleared successfully!")
# --- Footer ---
st.markdown("---")
st.markdown("Designed with 💜 for better sleep habits.")
