import streamlit as st
import random
import time

def allocate_study_time(subjects):
    total_time = 3  # Fixed 3-hour study session
    difficulty_weights = {"Easy": 1, "Medium": 1.5, "Difficult": 2}
    total_weight = sum(difficulty_weights[d] for _, d in subjects)
    
    schedule = {}
    for subject, difficulty in subjects:
        study_time = (difficulty_weights[difficulty] / total_weight) * total_time
        schedule[subject] = round(study_time * 60)  # Convert to minutes
    return schedule

# Page layout
st.set_page_config(page_title="Mindease", layout="wide")
st.title("Mindease")

# Sidebar customization
sidebar_bg_color = "#98FB98"  # Mint Green
st.markdown(
    f'''<style>
        .css-1d391kg {{ background-color: {sidebar_bg_color} !important; }}
        .stSidebar .css-1d391kg {{ color: black !important; }}
    </style>''',
    unsafe_allow_html=True,
)

# Sidebar Prompts (20 each category)
def random_prompt(category):
    prompts = {
        "Inspire Me": [
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
            "Hard work beats talent when talent doesn’t work hard.",
            "Failure is not the opposite of success, it’s part of success.",
            "The best way to predict the future is to create it.",
            "Your mindset determines your future.",
            "Small progress is still progress. Keep moving forward!",
            "You only fail when you stop trying.",
            "Success doesn’t come from what you do occasionally, but what you do consistently.",
            "Push yourself, because no one else is going to do it for you.",
            "Stay positive, work hard, and make it happen!",
            "Great things never come from comfort zones."
        ],
        "Anxiety Relief": [
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
            "Engage in deep breathing exercises to calm your nervous system.",
            "Do a quick 5-minute meditation to reset your thoughts.",
            "Jot down your thoughts in a journal.",
            "Try guided visualization to imagine a peaceful scene.",
            "Laugh! Watch a funny video or talk to a friend who makes you smile.",
            "Hug someone – physical touch reduces stress.",
            "Stretch your body to release tension.",
            "Sing or hum your favorite song.",
            "Use grounding techniques to bring yourself to the present moment.",
            "Affirm: 'I am in control of my thoughts and emotions.'"
        ],
    }
    return random.choice(prompts[category])

st.sidebar.header("💡 Need a boost?")
if st.sidebar.button("Inspire Me!"):
    st.sidebar.write(random_prompt("Inspire Me"))
if st.sidebar.button("🧘 Feeling anxious?"):
    st.sidebar.write(random_prompt("Anxiety Relief"))

# Emotion Selection
t = st.selectbox("💭 How do you feel today?", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])

# Daily Affirmation
affirmations = {
    "Happy": "Keep spreading the joy! Happiness is contagious.",
    "Sad": "It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": "Take a deep breath and remind yourself that you’re in control.",
    "Motivated": "Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "Take a deep breath. A short break might help clear your mind.",
    "Tired": "Rest is just as important as work. Give yourself a moment to recharge."
}
st.write(f"**Daily Affirmation:** {affirmations[t]}")

# Study Planner
st.header("📚 Study Planner")
n = st.number_input("Number of subjects", min_value=1, step=1)
subjects = []
for i in range(n):
    name = st.text_input(f"Subject {i+1} name")
    difficulty = st.selectbox(f"Difficulty for {name}", ["Easy", "Medium", "Difficult"], key=f"diff_{i}")
    subjects.append((name, difficulty))

time_preference = st.radio("Preferred Study Time", ["Morning", "Evening"])

if st.button("Generate Study Plan"):
    schedule = allocate_study_time(subjects)
    for subject, time in schedule.items():
        st.write(f"{subject}: {time} minutes")

# Study Timer
st.header("⏳ Study Timer")
study_duration = st.number_input("Enter study time in minutes", min_value=1, step=1)
if st.button("Start Timer"):
    with st.empty():
        for i in range(study_duration, 0, -1):
            st.write(f"⏳ Time Left: {i} min")
            time.sleep(1)
        st.write("🎉 Time's up! Take a break!")
