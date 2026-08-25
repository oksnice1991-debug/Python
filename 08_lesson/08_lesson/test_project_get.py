from YougileApi import YougileApi

api = YougileApi(
    "токен") #заменить на реальный


def test_get_project_positive():
    create_resp = api.create_project("Мой тест")
    project_id = create_resp.json()["id"]
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200

    data = get_resp.json()
    assert data["id"] == project_id
    assert "title" in data
    assert "timestamp" in data


def test_get_project_negative():
    fake_id = "00000000-0000-0000-000000000000"
    get_resp = api.get_project(fake_id)
    assert get_resp.status_code == 404
