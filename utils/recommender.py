import datetime

def get_productivity_recommendation(tasks):
    if not tasks:
        return "Start by adding your first task! Small steps matter 🌱"

    completed_tasks = [t for t in tasks if t['status'] == 'Completed']
    pending_tasks = [t for t in tasks if t['status'] == 'Pending']

    if len(completed_tasks) == 0:
        return "You haven’t completed any tasks yet. Try finishing the smallest one first!"

    if len(completed_tasks) > len(pending_tasks):
        return "Great job! You’re on a productive streak. Consider planning tomorrow’s tasks 📅."

    if len(pending_tasks) > 5:
        return "You have many pending tasks. Try the ‘2-minute rule’ to clear quick items."

    today = datetime.date.today()
    today_tasks = [t for t in tasks if t['date'] == str(today)]

    if len(today_tasks) == 0:
        return "Plan at least 2 tasks for today to maintain momentum."

    return "Keep going! A balanced workload helps you stay consistent."
