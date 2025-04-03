import streamlit as st
import random

# Set Page Configuration
st.set_page_config(page_title="MindEase", layout="wide")

# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

def toggle_theme():
    st.session_state["dark_mode"] = not st.session_state["dark_mode"]

st.sidebar.button("🌗 Toggle Dark Mode", on_click=toggle_theme)

theme_bg = "#1E1E1E" if st.session_state["dark_mode"] else "#E6E6FA"  # Black for dark mode, Lavender for light mode
st.markdown(f"""
    <style>
        .stApp {{ background-color: {theme_bg}; }}
    </style>
""", unsafe_allow_html=True)

# Sidebars
if st.sidebar.button("💡 Need a boost? Inspire Me!"):
    st.sidebar.write(random.choice([
        "Believe in yourself! You are capable of amazing things.",
        "Every day is a new beginning. Take a deep breath and start again.",
        "Success is the sum of small efforts, repeated daily.",
        "Keep going. Everything you need will come to you at the perfect time.",
        "Difficulties in life are intended to make us better, not bitter.",
        "You are stronger than you think. Keep pushing forward!",
        "Your potential is limitless. Never stop exploring your capabilities.",
        "The only way to achieve the impossible is to believe it is possible.",
        "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
        "You are capable, you are strong, and you can do this!"
    ]))

if st.sidebar.button("🧘 Feeling anxious? Anxiety Relief"):
    st.sidebar.write(random.choice([
        "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
        "Close your eyes and picture your happy place. Stay there for a moment.",
        "Write down what’s bothering you and set it aside for later.",
        "Try progressive muscle relaxation – tense each muscle, then relax it.",
        "Listen to calming music or nature sounds to ease your mind.",
        "Step outside and take a short walk to clear your thoughts.",
        "Drink a warm cup of tea or water. Hydration helps relaxation.",
        "Focus on the present. What are five things you can see and hear?",
        "Talk to someone you trust about what’s making you anxious.",
        "Remind yourself: You have overcome challenges before, and you will again."
    ]))

if st.sidebar.button("📚 Study Tips"):
    st.sidebar.write(random.choice([
        "Use the Pomodoro technique – study for 25 mins, take a 5-min break.",
        "Teach what you learn to someone else. It helps retain information!",
        "Summarize notes in your own words to enhance understanding.",
        "Practice active recall – test yourself instead of rereading notes.",
        "Break large tasks into smaller chunks to avoid feeling overwhelmed.",
        "Use mnemonic devices to memorize complex concepts.",
        "Find a distraction-free study environment for better focus.",
        "Use visual aids like mind maps and diagrams to remember better.",
        "Get enough sleep! Rest is crucial for memory retention.",
        "Stay hydrated and take regular breaks to keep your mind fresh."
    ]))

if st.sidebar.button("💆‍♀️ Self-care Tips"):
    st.sidebar.write(random.choice([
        "Take a 5-minute stretch break to ease your muscles.",
        "Maintain a good posture while studying to avoid back pain.",
        "Eat brain-boosting foods like nuts, fruits, and dark chocolate.",
        "Avoid excessive caffeine; try herbal tea instead.",
        "Get sunlight exposure to boost your mood and energy levels.",
        "Set realistic goals and celebrate small achievements.",
        "Listen to calming music while studying to reduce stress.",
        "Practice gratitude – write down three things you are grateful for.",
        "Take a deep breath and remind yourself it’s okay to take breaks.",
        "Limit screen time before bed to ensure better sleep quality."
    ]))

# 🎭 Emotion-Based Prompt System
st.subheader("💭 How do you feel today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": "Keep spreading the joy! Happiness is contagious.",
    "Sad": "It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": random.choice([
        "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
        "Close your eyes and picture your happy place. Stay there for a moment.",
        "Write down what’s bothering you and set it aside for later."
    ]),
    "Motivated": "Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "Take a deep breath. A short break might help clear your mind.",
    "Tired": "Rest is just as important as work. Give yourself a moment to recharge."
}
st.write(prompt_mapping[emotion])

# 📅 Study Planner
st.subheader("📅 Plan Your Study Schedule")
num_subjects = st.number_input("Enter the number of subjects:", min_value=1, step=1)
subjects = []
for i in range(num_subjects):
    subject = st.text_input(f"Enter Subject {i+1}:")
    subjects.append(subject)

time_pref = st.selectbox("Preferred Study Time:", ["Morning", "Evening"])
study_time = st.time_input("Enter study start time:")

if st.button("Generate Study Plan"):
    st.write("### Your Study Plan")
    for subject in subjects:
        if subject:
            st.write(f"- Study {subject} in the {time_pref} at {study_time}")
