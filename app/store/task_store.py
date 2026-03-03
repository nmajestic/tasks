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
        return self.__tasks