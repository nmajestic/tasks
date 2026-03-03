import sys

from app.display.renderer import display_startup, display_actions
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
                completed = False
                task = TaskItem(name, description, completed)
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
                for task in store.get_tasks():
                    print(f"Task: {task.name} | Description: {task.description} | Completion Status: {task.completed}")
            case "q":
                sys.exit(0)