from dataclasses import dataclass

@dataclass
class TaskItem:
    name: str
    description: str
    completed: bool