from app.models.priority import Priority


def test_get_priority_order():
    assert Priority.LOW.get_priority_order() == 0
    assert Priority.MEDIUM.get_priority_order() == 1
    assert Priority.HIGH.get_priority_order() == 2
