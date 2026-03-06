import datetime

from app.config.config import APP_NAME, APP_VERSION

def display_startup():
    print(f"Welcome to {APP_NAME}: {APP_VERSION}")
    print("-----------------------")
    print()

def display_actions():
    print("Available actions:")
    print("------------------")
    print("Add Task: a")
    print("Delete Task: d")
    print("Complete Task: c")
    print("List Tasks: l")
    print("Load Tasks: g")
    print("Save Tasks: s")
    print("Quit: q")
    print("------------------")

def display_tasks(sorted_tasks):
        for task in sorted_tasks:
            print(
                f"Task: {task.name} | Description: {task.description} | Completion Status: {task.completed} | Priority: {task.priority} | Due Date: {task.due_date}")
        for task in sorted_tasks:
            if task.due_date < datetime.date.today():
                print(f"OVERDUE TASK: {task.name} | Due Date: {task.due_date}")