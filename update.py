import streamlit as st
import random

def set_theme():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    return "black" if st.session_state.dark_mode else "white"

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

st.set_page_config(page_title="MindEase", layout="wide")

background_color = set_theme()
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: {'white' if background_color == 'black' else 'black'};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.button("🌗 Toggle Dark Mode", on_click=toggle_theme)

# Sidebar Sections
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

# 📖 Study Planner
st.subheader("📅 Study Planner")
num_subjects = st.number_input("How many subjects do you have?", min_value=1, max_value=10, step=1)
subjects = [st.text_input(f"Enter subject {i+1} name:") for i in range(num_subjects)]

study_time_preference = st.selectbox("When do you prefer studying?", ["Morning", "Evening"])
total_study_hours = st.number_input("Enter total study hours per day:", min_value=1, max_value=12, step=1)

if st.button("Generate Study Plan"):
    hours_per_subject = total_study_hours / num_subjects
    st.write("Your Study Plan:")
    for subject in subjects:
        if subject:
            st.write(f"{subject}: {hours_per_subject:.2f} hours in the {study_time_preference.lower()}.")
