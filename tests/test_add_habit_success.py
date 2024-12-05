import pytest
from bot_logic import add_habit

def test_add_habit_success():
    result = add_habit("Медитація")
    assert result == "Звичка 'Медитація' додана!"
