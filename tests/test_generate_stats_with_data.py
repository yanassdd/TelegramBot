from bot_logic import generate_stats

def test_generate_stats_with_data():
    stats = generate_stats([{"habit": "Медитація", "days_completed": 5}])
    assert stats == "Звичка: Медитація, виконано: 5 днів."
