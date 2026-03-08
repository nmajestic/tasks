"""Tests for the TaskStore class."""

import datetime
import json
from unittest.mock import patch, mock_open

import pytest

from app.models.priority import Priority
from app.models.task_item import TaskItem
from app.store.task_store import TaskStore


@pytest.fixture
def store():
    """Return an empty TaskStore instance."""
    return TaskStore()


@pytest.fixture
def task():
    """Return a default medium-priority TaskItem due today."""
    name = "Test Task"
    description = "This is just a test task"
    completed = False
    priority = Priority.MEDIUM
    due_date = datetime.date.today()

    return TaskItem(name, description, completed, priority, due_date)


def test_add_task(task, store):
    """Verify that adding a task increases the store size by one."""
    store.add_task(task)
    length_of_task_list = len(store.get_tasks())
    assert length_of_task_list == 1


def test_remove_task(task, store):
    """Verify that removing a task by name leaves the store empty."""
    store.add_task(task)
    store.remove_task(task.name)
    length_of_task_list = len(store.get_tasks())
    assert length_of_task_list == 0


def test_complete_task(task, store):
    """Verify that completing a task sets its completed flag to True."""
    store.add_task(task)
    store.complete_task(task.name)
    assert task.completed is True


def test_get_tasks(task, store):
    """Verify that tasks are returned sorted by priority ascending."""
    second_task = TaskItem(
        "Second Test Task",
        "This is just a second test task",
        False,
        Priority.HIGH,
        datetime.date.today(),
    )
    store.add_task(task)
    store.add_task(second_task)

    sorted_tasks = store.get_tasks()

    assert sorted_tasks[0].priority == Priority.MEDIUM
    assert sorted_tasks[1].priority == Priority.HIGH


def test_clear_tasks(task, store):
    """Verify that clearing the store results in an empty task list."""
    store.add_task(task)
    store.clear_tasks()
    assert store.get_tasks() == []


def test_load(store):
    fake_data = json.dumps(
        {
            "Test Task": {
                "name": "Test Task",
                "description": "This is just a test task",
                "completed": False,
                "priority": "medium",
                "due_date": "2026-04-01",
            }
        }
    )

    with patch("builtins.open", mock_open(read_data=fake_data)):
        store.load()

        assert len(store.get_tasks()) == 1


def test_save(store, task):
    store.add_task(task)

    with patch("builtins.open", mock_open()):
        with patch("json.dump") as mocked_dump:
            store.save()
            mocked_dump.assert_called_once()
