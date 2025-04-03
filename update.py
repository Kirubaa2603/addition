import streamlit as st
import random
import datetime

# Set page config at the very start
st.set_page_config(page_title="MindEase", layout="wide")

# Custom CSS for dark mode and light mode with lavender accents
def apply_custom_css():
    custom_css = """
    <style>
        :root {
            --primary-color: #c3aed6;
            --text-color-light: #333333;
            --text-color-dark: #ffffff;
            --bg-light: #f7f3fc;
            --bg-dark: #1a1a2e;
        }
        body {
            background-color: var(--bg-light);
            color: var(--text-color-light);
            transition: all 0.3s ease-in-out;
        }
        .dark-mode body {
            background-color: var(--bg-dark);
            color: var(--text-color-dark);
        }
        .stButton>button {
            background-color: var(--primary-color);
            color: white;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #a38ac7;
        }
        .toggle-switch {
            position: fixed;
            top: 20px;
            right: 20px;
            cursor: pointer;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

apply_custom_css()

# Toggle button for dark mode
is_dark_mode = st.sidebar.toggle("🌙 Toggle Dark Mode")
if is_dark_mode:
    st.markdown("""<script>
document.body.classList.add('dark-mode');
</script>""", unsafe_allow_html=True)
else:
    st.markdown("""<script>
document.body.classList.remove('dark-mode');
</script>""", unsafe_allow_html=True)

# Motivational Prompts
motivation_prompts = [
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
]

# Anxiety Relief Prompts
anxiety_relief_prompts = [
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
]

# Sidebar Icons with Labels
st.sidebar.title("MindEase Tools")
if st.sidebar.button("✨ Inspire Me!"):
    st.sidebar.write(random.choice(motivation_prompts))

if st.sidebar.button("💆 Anxiety Relief"):
    st.sidebar.write(random.choice(anxiety_relief_prompts))

# Emotion-Based Prompt System
st.subheader("How do you feel today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": "Keep spreading the joy! Happiness is contagious.",
    "Sad": "It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": random.choice(anxiety_relief_prompts),
    "Motivated": "Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "Take a deep breath. A short break might help clear your mind.",
    "Tired": "Rest is just as important as work. Give yourself a moment to recharge."
}
st.write(prompt_mapping[emotion])

# Daily Affirmations
st.subheader("✨ Daily Affirmation")
current_date = datetime.datetime.now().day
affirmation = motivation_prompts[current_date % len(motivation_prompts)]
st.write(affirmation)

# Study Timer
st.subheader("⏳ Study Timer")
study_time = st.number_input("Set your study duration (minutes):", min_value=10, max_value=180, step=5)
break_time = st.selectbox("Break duration:", [5, 10, 15])
if st.button("Start Timer"):
    st.write(f"Study for {study_time} minutes, then take a {break_time}-minute break.")
