from enum import StrEnum


class Priority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def get_priority_order(self):
        priority_order = ["low", "medium", "high"]
        index_of_priority = priority_order.index(self)
        return index_of_priority
