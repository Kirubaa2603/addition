import streamlit as st
import random
import datetime

# Motivational Prompts
motivation_prompts = [
    "🌟 Believe in yourself! You are capable of amazing things.",
    "🙌 Every day is a new beginning. Take a deep breath and start again.",
    "💪 Success is the sum of small efforts, repeated daily.",
    "🌈 Keep going. Everything you need will come to you at the perfect time.",
    "✨ Difficulties in life are intended to make us better, not bitter.",
    "💪 You are stronger than you think. Keep pushing forward!",
    "🚀 Your potential is limitless. Never stop exploring your capabilities.",
    "💎 The only way to achieve the impossible is to believe it is possible.",
    "🌟 Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "✨ You are capable, you are strong, and you can do this!"
]

# Anxiety Relief Prompts
anxiety_relief_prompts = [
    "🌱 Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
    "💖 Close your eyes and picture your happy place. Stay there for a moment.",
    "🌿 Write down what’s bothering you and set it aside for later.",
    "💡 Try progressive muscle relaxation – tense each muscle, then relax it.",
    "🎵 Listen to calming music or nature sounds to ease your mind.",
    "🌳 Step outside and take a short walk to clear your thoughts.",
    "🥤 Drink a warm cup of tea or water. Hydration helps relaxation.",
    "🌟 Focus on the present. What are five things you can see and hear?",
    "👤 Talk to someone you trust about what’s making you anxious.",
    "✨ Remind yourself: You have overcome challenges before, and you will again."
]

st.set_page_config(page_title="MindEase", layout="wide")
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #E6E6FA !important; /* Lavender */
        }
        [data-testid="stSidebar"] .css-1d391kg, [data-testid="stSidebar"] .css-1v3fvcr {
            color: black !important;
        }
        [data-testid="stSidebarNav"] button {
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌿 Welcome to MindEase")
st.subheader("Your personal companion for motivation and self-care.")

# Sidebar
st.sidebar.title("🧡 MindEase Tools")
if st.sidebar.button("🌟 Need a boost? Inspire Me!"):
    st.sidebar.write(random.choice(motivation_prompts))

if st.sidebar.button("😊 Feeling anxious? Anxiety Relief"):
    st.sidebar.write(random.choice(anxiety_relief_prompts))

# Emotion-Based Prompt System
st.subheader("😊 How are you feeling today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": "🎉 Keep spreading the joy! Happiness is contagious.",
    "Sad": "❤️ It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": random.choice(anxiety_relief_prompts),
    "Motivated": "💪 Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "🤯 Take a deep breath. A short break might help clear your mind.",
    "Tired": "💤 Rest is just as important as work. Give yourself a moment to recharge."
}
st.write(prompt_mapping[emotion])

# Daily Affirmations
st.subheader("✨ Daily Affirmation")
current_date = datetime.datetime.now().day
affirmation = motivation_prompts[current_date % len(motivation_prompts)]
st.markdown(f"<div style='background-color:#E6E6FA; padding:10px; border-radius:5px; color:black;'><b>{affirmation}</b></div>", unsafe_allow_html=True)
