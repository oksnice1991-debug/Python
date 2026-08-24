import requests


class YougileApi:
    def __init__(self, api_key):
        self.base_url = "https://ru.yougile.com/api-v2"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        url = self.base_url + "/projects"
        resp = requests.post(url, json={"title": title}, headers=self.headers)
        return resp

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        resp = requests.get(url, headers=self.headers)
        return resp

    def update_project(self, project_id, title=None, deleted=None):
        url = f"{self.base_url}/projects/{project_id}"
        data = {}
        if title is not None:
            data["title"] = title
        if deleted is not None:
            data["deleted"] = deleted
        resp = requests.put(url, json=data, headers=self.headers)
        return resp
