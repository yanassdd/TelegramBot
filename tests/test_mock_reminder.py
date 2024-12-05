from bot_logic import create_reminder

def test_mock_reminder(mocker):
    mock_scheduler = mocker.patch('bot_logic.scheduler.add_job', return_value=True)
    result = create_reminder("08:00", "Медитація")
    assert result == "Нагадування для 'Медитація' встановлено на 08:00."
    mock_scheduler.assert_called_once()
