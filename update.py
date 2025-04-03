import streamlit as st
import random
import datetime

# Motivational Prompts
motivation_prompts = [
    "Believe in yourself! You are capable of amazing things. 🌟",
    "Every day is a new beginning. Take a deep breath and start again. 🌅",
    "Success is the sum of small efforts, repeated daily. 📈",
    "Keep going. Everything you need will come to you at the perfect time. ⏳",
    "Difficulties in life are intended to make us better, not bitter. 💪",
    "You are stronger than you think. Keep pushing forward! 🔥",
    "Your potential is limitless. Never stop exploring your capabilities. 🚀",
    "The only way to achieve the impossible is to believe it is possible. 🎯",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful. 🏆",
    "You are capable, you are strong, and you can do this! 💖"
]

# Anxiety Relief Prompts
anxiety_relief_prompts = [
    "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6. 🌬️",
    "Close your eyes and picture your happy place. Stay there for a moment. 🌄",
    "Write down what’s bothering you and set it aside for later. ✍️",
    "Try progressive muscle relaxation – tense each muscle, then relax it. 🧘",
    "Listen to calming music or nature sounds to ease your mind. 🎵",
    "Step outside and take a short walk to clear your thoughts. 🚶",
    "Drink a warm cup of tea or water. Hydration helps relaxation. 🍵",
    "Focus on the present. What are five things you can see and hear? 👀👂",
    "Talk to someone you trust about what’s making you anxious. 💬",
    "Remind yourself: You have overcome challenges before, and you will again. 🌟"
]

# Study Tips
study_tips = [
    "Use the Pomodoro technique – study for 25 mins, take a 5-min break. ⏳",
    "Teach what you learn to someone else. It helps retain information! 🗣️",
    "Summarize notes in your own words to enhance understanding. 📝",
    "Practice active recall – test yourself instead of rereading notes. 📚",
    "Break large tasks into smaller chunks to avoid feeling overwhelmed. 🏗️",
    "Use mnemonic devices to memorize complex concepts. 🧠",
    "Find a distraction-free study environment for better focus. 🎧",
    "Use visual aids like mind maps and diagrams to remember better. 🖼️",
    "Get enough sleep! Rest is crucial for memory retention. 😴",
    "Stay hydrated and take regular breaks to keep your mind fresh. 💧"
]

# Self-care Tips
self_care_tips = [
    "Take a 5-minute stretch break to ease your muscles. 🏋️",
    "Maintain a good posture while studying to avoid back pain. 🪑",
    "Eat brain-boosting foods like nuts, fruits, and dark chocolate. 🍫",
    "Avoid excessive caffeine; try herbal tea instead. ☕",
    "Get sunlight exposure to boost your mood and energy levels. ☀️",
    "Set realistic goals and celebrate small achievements. 🎉",
    "Listen to calming music while studying to reduce stress. 🎶",
    "Practice gratitude – write down three things you are grateful for. 💖",
    "Take a deep breath and remind yourself it’s okay to take breaks. 🌿",
    "Limit screen time before bed to ensure better sleep quality. 📵"
]

st.set_page_config(page_title="MindEase", layout="wide")
st.title("🍃 Welcome to MindEase")
st.subheader("Your personal companion for motivation, study tips, and self-care.")

# Sidebar
st.sidebar.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #E6E6FA;
        }
        .sidebar-title {
            color: black;
            font-size: 20px;
            font-weight: bold;
        }
        .sidebar-text {
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<span class='sidebar-title'>💜 MindEase Tools</span>", unsafe_allow_html=True)

if st.sidebar.button("💡 Need a boost? Inspire Me!"):
    st.sidebar.markdown(f"<span class='sidebar-text'>{random.choice(motivation_prompts)}</span>", unsafe_allow_html=True)

if st.sidebar.button("😌 Feeling anxious? Anxiety Relief"):
    st.sidebar.markdown(f"<span class='sidebar-text'>{random.choice(anxiety_relief_prompts)}</span>", unsafe_allow_html=True)

if st.sidebar.button("📖 Study Tips"):
    st.sidebar.markdown(f"<span class='sidebar-text'>{random.choice(study_tips)}</span>", unsafe_allow_html=True)

if st.sidebar.button("💆 Self-care Tips"):
    st.sidebar.markdown(f"<span class='sidebar-text'>{random.choice(self_care_tips)}</span>", unsafe_allow_html=True)

# Emotion-Based Prompt System
st.subheader("How are you feeling today?")

total_emotion_prompts = {
    "Happy": ["Keep spreading the joy! Happiness is contagious. 😊", "Enjoy the little things in life! 🌼", "Happiness shared is happiness doubled. 💕", "Smile more, worry less. 😊", "Every moment is a fresh beginning. 🌟"],
    "Sad": ["It’s okay to feel sad. Take it one step at a time. 💙", "This too shall pass. 🌈", "You are stronger than you think. 💪", "Tough times never last, but tough people do. 🏆", "Let yourself feel, then let yourself heal. 💖"],
    "Anxious": anxiety_relief_prompts,
    "Motivated": ["Keep up the great work! Channel your motivation into your goals. 🚀", "Your hard work will pay off. 💰", "Success is built on consistency. 📈", "You’ve got this! 🔥", "Dream big, work hard, stay focused. 🎯"],
    "Frustrated": ["Take a deep breath. A short break might help clear your mind. 🌬️", "Let go of what you can’t control. 🍃", "One step at a time, you’ll get there. 🏁", "Obstacles are stepping stones to growth. ⛰️", "Frustration is temporary, progress is permanent. 💡"],
    "Tired": ["Rest is just as important as work. Recharge yourself. 💤", "Listen to your body, it’s okay to slow down. 🛌", "Energy comes from balance. Take care of yourself. ⚖️", "Small breaks can make a big difference. ⏳", "You deserve to rest and recover. 🌙"]
}

emotion = st.selectbox("Select your emotion:", list(total_emotion_prompts.keys()))
st.write(random.choice(total_emotion_prompts[emotion]))

# Daily Affirmations
st.subheader("✨ Daily Affirmation")
current_date = datetime.datetime.now().day
affirmation = motivation_prompts[current_date % len(motivation_prompts)]
st.markdown(f'<div style="color:black; font-size:18px; padding:10px; border-radius:10px; background-color:#F5F5F5;">{affirmation}</div>', unsafe_allow_html=True)
