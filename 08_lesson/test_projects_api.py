class TestProjectsAPI:

    def test_create_project_positive(self, project_api):
        response = project_api.create_project("Новый проект")
        assert response.status_code == 201
        data = response.json()
        assert "id" in data

    def test_create_project_negative_empty_title(self, project_api):
        response = project_api.create_project("")
        assert response.status_code in [400, 422]

    def test_create_project_negative_missing_title(self, project_api):
        response = project_api.create_project(None)
        assert response.status_code in [400, 422]

    def test_update_project_positive(self, test_project, project_api):
        project_id = test_project["id"]
        response = project_api.update_project(
            project_id, "Обновлённое название"
            )
        assert response.status_code == 200

    def test_update_project_negative_invalid_id(self, project_api):
        response = project_api.update_project(
            "invalid_id_123", "Новое название"
            )
        assert response.status_code == 404

    def test_update_project_negative_empty_title(
            self, test_project, project_api
            ):
        project_id = test_project["id"]
        response = project_api.update_project(project_id, "")
        assert response.status_code in [400, 422]

    def test_get_project_positive(self, test_project, project_api):
        project_id = test_project["id"]
        response = project_api.get_project(project_id)
        assert response.status_code == 200
        data = response.json()
        assert "id" in data and data["id"] == project_id

    def test_get_project_negative_invalid_id(self, project_api):
        response = project_api.get_project("nonexistent_id_456")
        assert response.status_code == 404
