from YougileApi import YougileApi

api = YougileApi(
    "токен") # заменить на реальный


def test_update_positive_project():
    create_resp = api.create_project("Мой проект")
    project_id = create_resp.json()["id"]

    update_resp = api.update_project(project_id, title="Новый проект")

    assert update_resp.status_code == 200

    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Новый проект"


def test_update_negative_project():
    fake_id = "00000000-0000-0000-000000000000"
    get_resp = api.get_project(fake_id)
    assert get_resp.status_code == 404
