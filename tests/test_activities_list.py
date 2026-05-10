def test_get_activities_returns_all_seeded_activities(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == expected_count


def test_get_activities_contains_expected_activity_fields(client):
    # Arrange
    activity_name = "Chess Club"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert activity_name in payload
    assert set(payload[activity_name].keys()) == expected_fields
