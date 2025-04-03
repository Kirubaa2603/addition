import streamlit as st
import random
import time

def get_study_schedule(subjects, difficulties, total_hours):
    difficulty_weights = {'Easy': 1, 'Medium': 1.5, 'Difficult': 2}
    weighted_hours = [difficulty_weights[d] for d in difficulties]
    total_weight = sum(weighted_hours)
    allocated_hours = [(h / total_weight) * total_hours for h in weighted_hours]
    return dict(zip(subjects, allocated_hours))

st.set_page_config(page_title="Mindease", layout="wide")
st.markdown("""
    <style>
        body { background-color: white; color: black; }
        .sidebar .sidebar-content { background-color: #98FB98; }
    </style>
""", unsafe_allow_html=True)

# Sidebars with 20 prompts each
sidebars = {
    "💡 Need a boost? Inspire Me!": [...],  # Add 20 prompts
    "🧘 Feeling anxious? Anxiety Relief": [...],
    "📚 Study Tips": [...],
    "💆‍♀️ Self-care Tips": [...]
}
for title, prompts in sidebars.items():
    if st.sidebar.button(title):
        st.sidebar.write(random.choice(prompts))

# Title
st.title("Mindease")

# Emotion-Based Dropdown
st.subheader("💭 How do you feel today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": "Keep spreading the joy! Happiness is contagious.",
    "Sad": "It’s okay to feel sad. Be kind to yourself.",
    "Anxious": "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
    "Motivated": "Keep up the great work! Stay focused on your goals.",
    "Frustrated": "A short break might help clear your mind.",
    "Tired": "Rest is just as important as work. Recharge."
}
st.write(prompt_mapping[emotion])

# Daily Affirmation
st.subheader("🌟 Daily Affirmation")
st.write(random.choice(["You are enough.", "You are capable of great things.", "Believe in yourself."]))

# Study Planner
st.subheader("📅 Study Planner")
num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)
subjects, difficulties = [], []
for i in range(num_subjects):
    subjects.append(st.text_input(f"Enter subject {i+1}:", ""))
    difficulties.append(st.select_slider(f"Select difficulty for {subjects[i]}", ["Easy", "Medium", "Difficult"]))
study_hours = st.number_input("Total study hours available:", min_value=1, step=1)
if st.button("Generate Study Plan"):
    schedule = get_study_schedule(subjects, difficulties, study_hours)
    for subject, hours in schedule.items():
        st.write(f"{subject}: {round(hours, 2)} hours")

# Study Timer
st.subheader("⏳ Study Timer")
study_time = st.number_input("Enter study duration (minutes):", min_value=1, step=1)
if st.button("Start Timer"):
    with st.empty():
        for remaining in range(study_time, 0, -1):
            st.write(f"⏳ Time left: {remaining} min")
            time.sleep(60)
        st.success("🎉 Time's up! Take a break and refresh yourself.")
