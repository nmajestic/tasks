import datetime
import sys

from app.display.renderer import display_startup, display_actions, display_tasks
from app.models.priority import Priority
from app.models.task_item import TaskItem
from app.store.task_store import TaskStore
from app.util.platform_utils import clear

def start():
    store = TaskStore()
    display_startup()

    while True:
        print()
        display_actions()
        action_selected = input("Select an action: ")
        clear()
        match action_selected:
            case "a":
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                priority_selected = ""
                priority = Priority.MEDIUM

                while priority_selected not in Priority:
                    priority_selected = input("Enter task priority(low, medium, high): ")
                    match priority_selected:
                        case "low":
                            priority = Priority.LOW
                        case "medium":
                            priority = Priority.MEDIUM
                        case "high":
                            priority = Priority.HIGH

                while True:
                    try:
                        date_selected = input("Enter task date(YYYY-MM-DD): ")
                        due_date = datetime.datetime.strptime(date_selected, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid date. Try again.")\

                completed = False
                task = TaskItem(name, description, completed, priority, due_date)
                store.add_task(task)
                clear()
            case "d":
                name = input("Enter task name: ")
                store.remove_task(name)
                clear()
            case "c":
                name = input("Enter task name: ")
                store.complete_task(name)
                clear()
            case "l":
                display_tasks(store.get_tasks())
            case "g":
                store.load()
            case "s":
                store.save()
            case "q":
                sys.exit(0)