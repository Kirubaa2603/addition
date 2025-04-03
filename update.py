import streamlit as st
import random
import time

# Set page background color and sidebar style
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
        color: #000000;
    }
    .stSidebar {
        background-color: #CFF5E7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar - Inspiration
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
        "You are capable, you are strong, and you can do this!",
        "Dream big, work hard, and stay consistent.",
        "Opportunities don't happen. You create them.",
        "Your only limit is your mind.",
        "Be a warrior, not a worrier.",
        "You are enough just as you are.",
        "Strive for progress, not perfection.",
        "Doubt kills more dreams than failure ever will.",
        "Your future is created by what you do today, not tomorrow.",
        "Every expert was once a beginner. Keep learning!"
    ]))

# Sidebar - Anxiety Relief
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
        "Remind yourself: You have overcome challenges before, and you will again.",
        "Practice deep breathing exercises to calm your nervous system.",
        "Take a few minutes to stretch and relax your body.",
        "Limit screen time and avoid negative news before sleeping.",
        "Try journaling to process your thoughts.",
        "Practice gratitude – list three things you’re grateful for today.",
        "Disconnect from social media for a while and focus on yourself.",
        "Listen to uplifting or relaxing podcasts.",
        "Engage in a hobby that relaxes your mind.",
        "Visualize a peaceful and calming scene in your mind.",
        "Remind yourself that feelings are temporary and will pass."
    ]))

# Sidebar - Study Tips
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
        "Stay hydrated and take regular breaks to keep your mind fresh.",
        "Set clear study goals before each session.",
        "Take handwritten notes to improve retention.",
        "Use spaced repetition for better long-term memory.",
        "Group study can help reinforce learning.",
        "Make flashcards for quick revision.",
        "Stay consistent with your study routine.",
        "Avoid multitasking; focus on one subject at a time.",
        "Keep a study journal to track progress.",
        "Take short walks between study sessions to refresh your mind.",
        "Reward yourself after completing a difficult topic."
    ]))

# Sidebar - Self-care Tips
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
        "Limit screen time before bed to ensure better sleep quality.",
        "Stay hydrated and drink enough water throughout the day.",
        "Disconnect from work or study for a few minutes every hour.",
        "Try a new hobby that makes you happy.",
        "Write down your thoughts in a journal.",
        "Light a scented candle or use essential oils for relaxation.",
        "Make time for friends and loved ones.",
        "Take a short nap if you feel exhausted.",
        "Treat yourself with something you love – a book, food, or music.",
        "Engage in mindful breathing or short meditation.",
        "Celebrate small victories every day!"
    ]))

st.subheader("💭 How do you feel today?")
emotion = st.selectbox("Select your emotion:", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
prompt_mapping = {
    "Happy": "Keep spreading the joy! Happiness is contagious.",
    "Sad": "It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": "Take a deep breath and find a moment of calm.",
    "Motivated": "Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "Take a break and clear your mind before getting back to work.",
    "Tired": "Rest is just as important as work. Give yourself time to recharge."
}
st.write(prompt_mapping[emotion])
