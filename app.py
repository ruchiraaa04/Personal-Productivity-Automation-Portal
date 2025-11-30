import streamlit as st
import json
import os
from datetime import date
from utils.recommender import get_productivity_recommendation

DATA_FILE = "data/tasks.json"

st.set_page_config(page_title="Productivity Portal", layout="wide")

# Load tasks
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if content == "":
                return []   # empty file → return empty list
            return json.loads(content)
    except json.JSONDecodeError:
        return []


# Save tasks
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Main UI
st.title("📌 FocusFlow")
st.write("A simple dashboard for task tracking, automation utilities and smart insights.")

tasks = load_tasks()

# ---- SIDEBAR ----
st.sidebar.header("➕ Add New Task")
task_title = st.sidebar.text_input("Task Title")
task_priority = st.sidebar.selectbox("Priority", ["Low", "Medium", "High"])
task_date = st.sidebar.date_input("Due Date", date.today())

if st.sidebar.button("Add Task"):
    if task_title.strip() != "":
        tasks.append({
            "title": task_title,
            "priority": task_priority,
            "date": str(task_date),
            "status": "Pending"
        })
        save_tasks(tasks)
        st.sidebar.success("Task added!")
    else:
        st.sidebar.error("Task title cannot be empty.")

# ---- MAIN UI ----
st.subheader("📋 Your Tasks")

for idx, task in enumerate(tasks):
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

    with col1:
        st.write(f"**{task['title']}**")

    with col2:
        st.write(f"Priority: `{task['priority']}`")

    with col3:
        st.write(f"Due: {task['date']}")

    with col4:
        if st.button("Complete", key=f"complete_{idx}"):
            task['status'] = "Completed"
            save_tasks(tasks)
            st.success("Task marked complete!")

# -------------------------
# 📊 TASK STATISTICS
# -------------------------

completed = len([t for t in tasks if t["status"] == "Completed"])
pending = len([t for t in tasks if t["status"] == "Pending"])
total = len(tasks)

st.markdown("---")
st.markdown("### 📊 Task Overview")

colA, colB, colC = st.columns(3)

with colA:
    st.metric("✔ Completed", completed)

with colB:
    st.metric("⏳ Pending", pending)

with colC:
    st.metric("📌 Total Tasks", total)


# -------------------------
# 🔥 SMART PRODUCTIVITY MESSAGE
# -------------------------

st.markdown("### 🎯 Productivity Insight")

if total == 0:
    st.info("Add your first task and kickstart your productivity journey! 🚀")

elif completed == 0:
    st.warning("No tasks completed yet — start with a small one to build momentum 💪")

elif completed > pending:
    st.success("🔥 Great! You're completing more tasks than remaining — high productivity!")

elif pending > completed:
    st.info("📌 Keep going! Try finishing 1–2 tasks to boost your progress.")

elif pending == completed:
    st.info("✨ Balanced workload — you're managing your tasks well!")

# Optional fun extra message
if completed >= 5 and completed > pending:
    st.success("🌟 Amazing! 5+ tasks completed — you’re on a roll!")


st.markdown("---")
st.subheader("⚡ Productivity Automation Tools")

col1, col2 = st.columns(2)

with col1:
    import time
    import streamlit as st

    st.subheader("⏱️Timer")

    # Timer durations
    durations = {
        "Focus (25 min)": 25 * 60,
        "Short Break (5 min)": 5 * 60,
        "Long Break (15 min)": 15 * 60
    }

    mode = st.selectbox("Mode", list(durations.keys()))

    # Initialize session state
    if "remaining" not in st.session_state:
        st.session_state.remaining = 0
    if "running" not in st.session_state:
        st.session_state.running = False
    if "paused" not in st.session_state:
        st.session_state.paused = False


    # ---------- BUTTON ROW 1 (Start / Pause / Resume) ----------
    btn_css = """
    <style>

    /* Make all 3 buttons same size & inline */
    .uniform-btn > button {
        width: 120px !important;
        height: 42px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    /* Add spacing between buttons */
    .uniform-btn {
        display: flex;
        justify-content: center;
        gap: 12px;
    }

    </style>
    """
    st.markdown(btn_css, unsafe_allow_html=True)

    # Layout container
    with st.container():
        colA, colB, colC = st.columns([1, 1, 1])

        with colA:
            start = st.container()
            with start:
                st.markdown('<div class="uniform-btn">', unsafe_allow_html=True)
                if st.button("▶️ Start", key="start_btn"):
                    st.session_state.remaining = durations[mode]
                    st.session_state.running = True
                    st.session_state.paused = False
                st.markdown('</div>', unsafe_allow_html=True)

        with colB:
            pause = st.container()
            with pause:
                st.markdown('<div class="uniform-btn">', unsafe_allow_html=True)
                if st.button("⏸ Pause", key="pause_btn"):
                    if st.session_state.running:
                        st.session_state.paused = True
                        st.session_state.running = False
                st.markdown('</div>', unsafe_allow_html=True)

        with colC:
            resume = st.container()
            with resume:
                st.markdown('<div class="uniform-btn">', unsafe_allow_html=True)
                if st.button("⏯ Resume", key="resume_btn"):
                    if st.session_state.paused:
                        st.session_state.running = True
                        st.session_state.paused = False
                st.markdown('</div>', unsafe_allow_html=True)


    # ---------- STOP BUTTON (RED, FULL WIDTH) ----------
    stop_css = """
    <style>
    .stop-btn > button {
        background-color: #ff4b4b !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        height: 45px !important;
        width: 100% !important;
        margin-top: 10px;
        font-size: 16px !important;
    }
    </style>
    """
    st.markdown(stop_css, unsafe_allow_html=True)

    st.markdown('<div class="stop-btn">', unsafe_allow_html=True)
    if st.button("⏹ Stop", key="stop_btn2"):
        st.session_state.running = False
        st.session_state.paused = False
        st.session_state.remaining = 0
    st.markdown('</div>', unsafe_allow_html=True)



    # ----- TIMER LOGIC -----

    timer_placeholder = st.empty()

    if st.session_state.running and not st.session_state.paused:
        start_time = time.time()

        while st.session_state.remaining > 0 and st.session_state.running:
            elapsed = time.time() - start_time
            st.session_state.remaining -= elapsed
            start_time = time.time()

            mins, secs = divmod(int(st.session_state.remaining), 60)
            timer_placeholder.markdown(f"### ⏳ **{mins:02d}:{secs:02d}** remaining")

            time.sleep(1)

        if st.session_state.remaining <= 0:
            st.session_state.running = False
            st.balloons()
            st.success("🎉 Time's up!")

    else:
        # Display current remaining time (while paused or stopped)
        mins, secs = divmod(int(st.session_state.remaining), 60)
        timer_placeholder.markdown(f"### ⏳ **{mins:02d}:{secs:02d}** remaining")


with col2:
    # Text Summarizer
    st.write("### 📝 Text Summarizer")
    text_in = st.text_area("Enter text")
    if st.button("Summarize Text"):
        if len(text_in.split()) < 20:
            st.warning("Enter at least 20+ words.")
        else:
            lines = text_in.split(".")
            summary = " ".join(lines[:2])
            st.success(summary)

