import datetime
import sys
import json
from dataclasses import asdict
from unittest import case

from app.display.renderer import display_startup, display_actions
from app.models.priority import Priority
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

                sorted_task_priorities = sorted(store.get_tasks(), key=lambda l_task: l_task.priority.get_priority_order())

                for task in sorted_task_priorities:
                    print(f"Task: {task.name} | Description: {task.description} | Completion Status: {task.completed} | Priority: {task.priority} | Due Date: {task.due_date}")
                for task in sorted_task_priorities:
                    if task.due_date < datetime.date.today():
                        print(f"OVERDUE TASK: {task.name} | Due Date: {task.due_date}")
            case "g":
                store.clear_tasks()
                try:
                    with open("data.json", "r") as file:
                        raw_data = json.load(file)
                        for info in raw_data.values():
                            new_task = TaskItem(**info)
                            new_task.priority = Priority(info["priority"])
                            new_task.due_date = datetime.datetime.strptime(info["due_date"], "%Y-%m-%d").date()
                            store.add_task(new_task)
                        print("Tasks loaded.")
                except (FileNotFoundError, json.JSONDecodeError):
                    with open("data.json", "w") as file:
                        json.dump(store_dict, file, indent=4)
                        print("File not found. Creating new data file...")
            case "s":
                for task in store.get_tasks():
                    task_dict = asdict(task)
                    task_dict["due_date"] = task.due_date.strftime("%Y-%m-%d")
                    store_dict[task.name] = task_dict
                with open("data.json", "w") as file:
                    json.dump(store_dict, file, indent=4)
            case "q":
                sys.exit(0)