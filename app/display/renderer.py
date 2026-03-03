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
    print("Quit: q")
    print("------------------")