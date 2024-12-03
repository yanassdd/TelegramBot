import pytest
from bot_logic import add_habit, create_reminder, generate_stats

def test_add_habit_success():
    result = add_habit("Читання книги")
    assert result == "Звичка 'Читання книги' додана!"

def test_add_habit_empty_name():
    with pytest.raises(ValueError):
        add_habit("")

def test_create_reminder_valid():
    result = create_reminder("08:00", "Читання книги")
    assert result == "Нагадування для 'Читання книги' встановлено на 08:00."

def test_generate_stats_empty():
    stats = generate_stats([])
    assert stats == "У вас немає активних звичок."

def test_generate_stats_with_data():
    stats = generate_stats([{"habit": "Читання книги", "days_completed": 5}])
    assert stats == "Звичка: Читання книги, виконано: 5 днів."
