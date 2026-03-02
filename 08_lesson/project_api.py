import requests


class ProjectAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, title=None):
        url = self.base_url + "/projects"
        payload = {"title": title} if title is not None else {}
        return requests.post(url, headers=self.headers, json=payload)

    def update_project(self, project_id, title=None):
        url = self.base_url + "/projects/" + project_id
        payload = {"title": title} if title is not None else {}
        return requests.put(url, headers=self.headers, json=payload)

    def get_project(self, project_id):
        url = self.base_url + "/projects/" + project_id
        return requests.get(url, headers=self.headers)
