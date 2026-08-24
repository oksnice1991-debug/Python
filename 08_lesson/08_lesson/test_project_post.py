from YougileApi import YougileApi

api = YougileApi(
    "токен") #заменить на реальный


def test_positiv_project():
    title = "Мой проект"
    resp = api.create_project(title)

    assert resp.status_code == 201

    data = resp.json()

    assert "id" in data


def test_negativ_project():
    title = ""
    resp = api.create_project(title)

    assert resp.status_code != 201

    data = resp.json()

    assert "error" in data or "detail" in data
    assert "id" not in data
