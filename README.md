# 📌 **FocusFlow – Personal Productivity Automation Portal**

> A modern productivity dashboard built with **Python + Streamlit** that helps you track tasks, automate routines, and maintain focus using built-in tools like a Pomodoro timer and text summarizer.

---

## 🚀 **Overview**

**FocusFlow** is a lightweight and interactive productivity app designed to simplify your workflow.
It provides task tracking, productivity analytics, and quick automation tools — all inside one sleek interface.

This project was built as a practical tool to improve daily efficiency while showcasing UI development and logical structuring using Streamlit.

---

## ✨ **Features**

### ✅ **Task Management**

* Add new tasks with priority & due date
* Mark tasks as completed
* Tasks saved locally in JSON
* View stats: **Completed / Pending / Total**
* Smart productivity insights based on task progress

### ⏱️ **Pomodoro Timer**

* Focus / Short Break / Long Break modes
* Accurate countdown
* **Start, Pause, Resume, Stop** controls
* Red Stop button for emphasis
* Balloons animation when timer finishes 🎉

### ⚡ **Automation Tools**

* 📝 **Text Summarizer**
* More tools can be added easily

### 📊 **Extra Logic**

* Recommendation engine (`utils/recommender.py`)
* Dynamic motivational messages
* Clean UI layout with responsive buttons

---

## 🛠 **Tech Stack**

* **Python 3.x**
* **Streamlit**
* JSON (Local Storage)
* PyPDF2 (optional for future tools)

---

## 📂 **Project Structure**

```
FocusFlow/
│── app.py
│── data/
│   └── tasks.json
│── utils/
│   └── recommender.py
│── requirements.txt
│── README.md
```

---

## ▶️ **Run Locally**

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/focusflow.git
cd focusflow
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit server

```bash
streamlit run app.py
```

---

## 📸 **Screenshots**

<img src="https://github.com/ruchiraaa04/Personal-Productivity-Automation-Portal/blob/main/focusflow.png">

<img src="https://github.com/ruchiraaa04/Personal-Productivity-Automation-Portal/blob/main/focusflow2.png">

---

## 🔧 **How It Works**

### 🎯 Task Manager

Stores tasks in `tasks.json`.
Stats are auto-calculated:

* `completed`
* `pending`
* `total`

### ⏱ Pomodoro Timer Logic

Uses:

* `st.session_state.running`
* `st.session_state.paused`
* `st.session_state.remaining`

Includes:

* Start
* Pause
* Resume
* Stop (red button)

### ⚡ Automation Tools

Includes:

* Text summarizer
* Any future tool can be added under this section

---

## 🚀 **Future Improvements**

Planned enhancements:

* Productivity charts & weekly stats
* Habit tracker
* Authentication (login system)
* Cloud database support
* Notes section
* AI-powered suggestions
* Theme customization

---

## 🤝 **Contributing**

Contributions are always welcome!
Feel free to open issues or submit PRs.

---

## 📝 **License**

This project is released under the **MIT License**.

---

## 👤 **Author**

**Ruchira More**
📌 Aspiring Data Scientist & Developer
🔗 Add your LinkedIn: *[https://www.linkedin.com/in/](https://www.linkedin.com/in/ruchira-more/)...*


