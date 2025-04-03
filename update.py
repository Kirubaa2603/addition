import streamlit as st
import random
import datetime

# Define Prompts
motivation_prompts = [
    "Believe in yourself! You are capable of amazing things. 🌟",
    "Every day is a new beginning. Take a deep breath and start again. 🧘‍♀️",
    "Success is the sum of small efforts, repeated daily. 🏆",
    "Keep going. Everything you need will come to you at the perfect time. ⏳",
    "Difficulties in life are intended to make us better, not bitter. 💪",
    "You are stronger than you think. Keep pushing forward! ✨",
    "Your potential is limitless. Never stop exploring your capabilities. 🔄",
    "The only way to achieve the impossible is to believe it is possible. 🤖",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful. ⚡",
    "You are capable, you are strong, and you can do this! 🥳",
    "Stay focused and never give up. Your dreams are within reach! 🌟",
    "Obstacles are just stepping stones to your success. ⭐",
    "Turn setbacks into comebacks. You’ve got this! 🚀",
    "Progress is progress, no matter how small. Keep going! 🌿",
    "Your future self will thank you for not giving up today. 😊",
    "Small consistent actions lead to great results. 📚",
    "You are your only limit. Keep breaking barriers! 🎨",
    "Every day is a second chance. Make the most of it! 🙌",
    "Believe in your dreams and work hard to make them real. 🎉",
    "Your hard work will pay off. Stay patient and persistent. 💪"
]

anxiety_relief_prompts = [
    "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6. 🌬",
    "Close your eyes and picture your happy place. Stay there for a moment. 🌿",
    "Write down what’s bothering you and set it aside for later. 📝",
    "Try progressive muscle relaxation – tense each muscle, then relax it. 🏋️",
    "Listen to calming music or nature sounds to ease your mind. 🎵",
    "Step outside and take a short walk to clear your thoughts. 🌾",
    "Drink a warm cup of tea or water. Hydration helps relaxation. 🍵",
    "Focus on the present. What are five things you can see and hear? 🎨",
    "Talk to someone you trust about what’s making you anxious. 🤝",
    "Remind yourself: You have overcome challenges before, and you will again. 🛡",
    "Stretch your body to release tension. 💪",
    "Write down three things you are grateful for. 📚",
    "Avoid caffeine and opt for a calming herbal tea. 🍼",
    "Take slow, deep breaths and focus on your heartbeat. 💭",
    "Limit your screen time for mental clarity. 🎮",
    "Watch a funny video or read a lighthearted story. 😂",
    "Remind yourself that anxiety is temporary. You will get through this. 💪",
    "Visualize a peaceful scene, like a beach or forest. 🌴",
    "Speak kind words to yourself. You deserve them. 🌟",
    "Light a scented candle or use essential oils to relax. 🌿"
]

# Streamlit Page Configuration
st.set_page_config(page_title="MindEase", layout="wide")
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #E6E6FA !important;
        }
        .st-emotion-cache-1d6wzja p {
            color: black !important;
        }
        .st-emotion-cache-1d6wzja h2 {
            color: black !important;
        }
        .st-emotion-cache-15zrgzn a {
            color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("🧡 Welcome to MindEase")

# Sidebar
st.sidebar.title("🧡 MindEase Tools")
if st.sidebar.button("🌟 Need a boost? Inspire Me!"):
    st.sidebar.write(random.choice(motivation_prompts))

if st.sidebar.button("💡 Feeling anxious? Anxiety Relief"):
    st.sidebar.write(random.choice(anxiety_relief_prompts))

# Emotion-Based Prompt System
st.subheader("😊 How are you feeling today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": random.choice(motivation_prompts),
    "Sad": "It's okay to feel sad. Take it one step at a time. ✨",
    "Anxious": random.choice(anxiety_relief_prompts),
    "Motivated": "Keep up the great work! Stay strong! 🏆",
    "Frustrated": "Take a deep breath. A short break might help. 🤓",
    "Tired": "Rest is just as important as work. Recharge. 🌟"
}
st.write(prompt_mapping[emotion])

# Daily Affirmation
st.subheader("✨ Daily Affirmation")
current_date = datetime.datetime.now().day
affirmation = motivation_prompts[current_date % len(motivation_prompts)]
st.markdown(f"<p style='font-size:16px; color:black;'>{affirmation}</p>", unsafe_allow_html=True)
