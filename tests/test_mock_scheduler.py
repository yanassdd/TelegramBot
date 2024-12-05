def test_mock_scheduler(mocker):
    mock_scheduler = mocker.patch('bot_logic.scheduler.add_job', return_value=True)
    create_reminder("09:00", "Спорт")
    mock_scheduler.assert_called_with("Спорт", "09:00")
