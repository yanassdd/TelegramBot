from bot_logic import create_reminder

def test_create_reminder():
    result = create_reminder("08:00", "Медитація")
    assert result == "Нагадування для 'Медитація' встановлено на 08:00."
