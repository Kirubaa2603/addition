import streamlit as st
import random
import datetime

# Motivational Prompts
motivation_prompts = [
    "🌟 Believe in yourself! You are capable of amazing things.",
    "💪 Every day is a new beginning. Take a deep breath and start again.",
    "🚀 Success is the sum of small efforts, repeated daily.",
    "✨ Keep going. Everything you need will come to you at the perfect time.",
    "🔥 Difficulties in life are intended to make us better, not bitter.",
    "💖 You are stronger than you think. Keep pushing forward!",
    "🌈 Your potential is limitless. Never stop exploring your capabilities.",
    "🎯 The only way to achieve the impossible is to believe it is possible.",
    "⚡ Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "🌻 You are capable, you are strong, and you can do this!"
]

# Anxiety Relief Prompts
anxiety_relief_prompts = [
    "😌 Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
    "🌅 Close your eyes and picture your happy place. Stay there for a moment.",
    "📝 Write down what’s bothering you and set it aside for later.",
    "🧘 Try progressive muscle relaxation – tense each muscle, then relax it.",
    "🎶 Listen to calming music or nature sounds to ease your mind.",
    "🚶 Step outside and take a short walk to clear your thoughts.",
    "☕ Drink a warm cup of tea or water. Hydration helps relaxation.",
    "👀 Focus on the present. What are five things you can see and hear?",
    "🗣️ Talk to someone you trust about what’s making you anxious.",
    "💡 Remind yourself: You have overcome challenges before, and you will again."
]

# Study Tips
study_tips = [
    "📚 Use the Pomodoro technique – study for 25 mins, take a 5-min break.",
    "🧑‍🏫 Teach what you learn to someone else. It helps retain information!",
    "📝 Summarize notes in your own words to enhance understanding.",
    "🔍 Practice active recall – test yourself instead of rereading notes.",
    "🎯 Break large tasks into smaller chunks to avoid feeling overwhelmed.",
    "🧠 Use mnemonic devices to memorize complex concepts.",
    "🔕 Find a distraction-free study environment for better focus.",
    "📊 Use visual aids like mind maps and diagrams to remember better.",
    "😴 Get enough sleep! Rest is crucial for memory retention.",
    "💧 Stay hydrated and take regular breaks to keep your mind fresh."
]

# Self-care Tips
self_care_tips = [
    "🧘 Take a 5-minute stretch break to ease your muscles.",
    "🪑 Maintain a good posture while studying to avoid back pain.",
    "🥑 Eat brain-boosting foods like nuts, fruits, and dark chocolate.",
    "☕ Avoid excessive caffeine; try herbal tea instead.",
    "🌞 Get sunlight exposure to boost your mood and energy levels.",
    "🎉 Set realistic goals and celebrate small achievements.",
    "🎶 Listen to calming music while studying to reduce stress.",
    "🙏 Practice gratitude – write down three things you are grateful for.",
    "💆 Take a deep breath and remind yourself it’s okay to take breaks.",
    "📱 Limit screen time before bed to ensure better sleep quality."
]

st.set_page_config(page_title="MindEase", layout="wide")

# Sidebar Styling
st.markdown(
    """
    <style>
        .css-1d391kg {background-color: #f8c8dc !important;} /* Pale Pink Sidebar */
        .css-1d391kg .stButton>button {color: black !important;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌿 Welcome to MindEase")
st.subheader("Your personal companion for motivation, study tips, and self-care.")

# Sidebar
st.sidebar.title("🌸 MindEase Tools")
if st.sidebar.button("💡 Need a boost? Inspire Me!"):
    st.sidebar.write(random.choice(motivation_prompts))

if st.sidebar.button("😌 Feeling anxious? Anxiety Relief"):
    st.sidebar.write(random.choice(anxiety_relief_prompts))

if st.sidebar.button("📖 Study Tips"):
    st.sidebar.write(random.choice(study_tips))

if st.sidebar.button("💆 Self-care Tips"):
    st.sidebar.write(random.choice(self_care_tips))

# Emotion-Based Prompt System
st.subheader("🎭 How do you feel today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": "😊 Keep spreading the joy! Happiness is contagious.",
    "Sad": "💙 It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": random.choice(anxiety_relief_prompts),
    "Motivated": "🚀 Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "😤 Take a deep breath. A short break might help clear your mind.",
    "Tired": "💤 Rest is just as important as work. Give yourself a moment to recharge."
}
st.markdown(f"<div style='background-color:#fffbf0; padding:10px; border-radius:10px;'><b>{prompt_mapping[emotion]}</b></div>", unsafe_allow_html=True)

# Study Planner Generator
st.subheader("📖 Study Planner Generator")
num_subjects = st.number_input("Number of subjects:", min_value=1, max_value=10, step=1)
study_plan = {}

time_duration = st.number_input("Total study time (in minutes):", min_value=30, step=10)

generate_plan = st.button("📝 Generate Study Plan")
if generate_plan:
    for i in range(1, int(num_subjects) + 1):
        study_plan[f"📚 Subject {i}"] = f"Study for {round(time_duration / num_subjects, 2)} minutes."
    st.write(study_plan)

# Daily Affirmations
st.subheader("✨ Daily Affirmation")
current_date = datetime.datetime.now().day
affirmation = motivation_prompts[current_date % len(motivation_prompts)]
st.markdown(f"<div style='background-color:#e6f7ff; padding:10px; border-radius:10px;'><b>{affirmation}</b></div>", unsafe_allow_html=True)

# Study Timer
st.subheader("⏳ Study Timer")
study_time = st.number_input("Set your study duration (minutes):", min_value=10, max_value=180, step=5)
break_time = st.selectbox("Break duration:", [5, 10, 15])
if st.button("▶️ Start Timer"):
    st.write(f"🕰️ Study for {study_time} minutes, then take a {break_time}-minute break.")
