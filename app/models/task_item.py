import datetime
from dataclasses import dataclass

from app.models.priority import Priority


@dataclass
class TaskItem:
    name: str
    description: str
    completed: bool
    priority: Priority
    due_date: datetime.date
