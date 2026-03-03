import sys
import json
from dataclasses import asdict

from app.display.renderer import display_startup, display_actions
from app.models.task_item import TaskItem
from app.store.task_store import TaskStore
from app.util.platform_utils import clear

def start():
    store = TaskStore()
    store_dict = dict()

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
            case "g":
                try:
                    with open("data.json", "r") as file:
                        raw_data = json.load(file)
                        for info in raw_data.values():
                            new_task = TaskItem(**info)
                            store.add_task(new_task)
                        print("Tasks loaded.")
                except (FileNotFoundError, json.JSONDecodeError):
                    with open("data.json", "w") as file:
                        json.dump(store_dict, file, indent=4)
                        print("File not found. Creating new data file...")
            case "s":
                for task in store.get_tasks():
                    store_dict[task.name] = asdict(task)
                with open("data.json", "w") as file:
                    json.dump(store_dict, file, indent=4)
            case "q":
                for task in store.get_tasks():
                    store_dict[task.name] = asdict(task)
                with open("data.json", "w") as file:
                    json.dump(store_dict, file, indent=4)
                sys.exit(0)