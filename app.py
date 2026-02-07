import streamlit as st
import json
import random
from datetime import date

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="DailyDose 🌸",
    page_icon="🌸",
    layout="centered"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>
    body {
        background-color: #f7f9fc;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #222;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 25px;
    }
    .card {
        background: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# ---------------- QUOTES ----------------
quotes = [
    "You are doing better than you think 🌱",
    "One day at a time. You’ve got this 💪",
    "Your presence matters more than you know ✨",
    "Progress, not perfection 🌸",
    "Even small steps are still steps forward 💖"
]

# ---------------- UI ----------------
st.markdown("<div class='title'>DailyDose 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your daily check-in & motivation</div>", unsafe_allow_html=True)

username = st.text_input("What should I call you?", placeholder="e.g. Munachi")

if username:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader(f"{username}, how are you doing today? 💭")
    st.info(random.choice(quotes))

    mood = st.radio(
        "Rate your mood today",
        ["😞 Very Low", "😐 Low", "🙂 Okay", "😊 Good", "🤩 Amazing"],
        horizontal=True
    )

    if st.button("Save My Mood 💾"):
        today = str(date.today())

        if username not in data:
            data[username] = {}

        data[username][today] = mood
        save_data(data)

        st.success("Your mood has been saved 🌷")

    st.markdown("</div>", unsafe_allow_html=True)

    if username in data:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Your Mood History 📅")

        for d, m in reversed(list(data[username].items())):
            st.write(f"**{d}** — {m}")

        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Enter your name to begin 🌼")
