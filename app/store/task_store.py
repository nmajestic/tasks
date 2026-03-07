import datetime
import json
from dataclasses import asdict

from app.models.priority import Priority
from app.models.task_item import TaskItem


class TaskStore:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task: TaskItem):
        self.__tasks.append(task)

    def remove_task(self, task_name):
        for task in self.__tasks:
            if task_name.lower() == task.name.lower():
                self.__tasks.remove(task)

    def complete_task(self, task_name):
        for task in self.__tasks:
            if task_name.lower() == task.name.lower():
                task.completed = True

    def get_tasks(self):
        sorted_tasks = sorted(
            self.__tasks, key=lambda l_task: l_task.priority.get_priority_order()
        )
        return sorted_tasks

    def clear_tasks(self):
        self.__tasks.clear()

    def save(self):
        store_dict = {}
        for task in self.__tasks:
            task_dict = asdict(task)
            task_dict["due_date"] = task.due_date.strftime("%Y-%m-%d")
            store_dict[task.name] = task_dict
        with open("data.json", "w") as file:
            json.dump(store_dict, file, indent=4)

    def load(self):
        self.clear_tasks()
        try:
            with open("data.json", "r") as file:
                raw_data = json.load(file)
                for info in raw_data.values():
                    new_task = TaskItem(**info)
                    new_task.priority = Priority(info["priority"])
                    new_task.due_date = datetime.datetime.strptime(
                        info["due_date"], "%Y-%m-%d"
                    ).date()
                    self.add_task(new_task)
                print("Tasks loaded.")
        except FileNotFoundError, json.JSONDecodeError:
            with open("data.json", "w") as file:
                store_dict = {}
                json.dump(store_dict, file, indent=4)
                print("File not found. Creating new data file...")
