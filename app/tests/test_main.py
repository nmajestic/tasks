"""Tests for the main module entry point functions."""

import datetime

import pytest

from app.main import get_priority, get_due_date
from app.models.priority import Priority


def test_get_priority():
    """Verify that each priority string maps to the correct Priority enum value."""
    assert get_priority("low") == Priority.LOW
    assert get_priority("medium") == Priority.MEDIUM
    assert get_priority("high") == Priority.HIGH


def test_get_priority_error():
    """Verify that an invalid priority string raises a ValueError."""
    with pytest.raises(ValueError):
        get_priority("invalid")


def test_get_due_date():
    """Verify that it returns a correct due date."""
    test_due_date = get_due_date("2026-04-01")
    assert test_due_date == datetime.date(2026, 4, 1)


def test_get_due_date_error():
    """Verify that an invalid due date string raises a ValueError."""
    with pytest.raises(ValueError):
        get_due_date("invalid")
