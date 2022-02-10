from unittest import TestCase
from unittest.mock import patch

import pytest


@patch("services.task.open_file")
@pytest.mark.usefixtures("app_client")
class TestSuccess(TestCase):

    def test__get_by__empty_params(self, patch_open_file):
        mock_tasks = [
            {
                "user_id": 1,
                "id": 1,
                "title": "delectus",
                "completed": False
            },
        ]
        patch_open_file.return_value = mock_tasks
        expected_respose = '{"total_items":1,"data":[{"user_id":1,"id":1,"title":"delectus","completed":false}]}'
        response = self.client.get("/services/tasks")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_respose, response.text)

    def test__get_by__only_completed(self, patch_open_file):
        mock_tasks = [
            {
                "user_id": 1,
                "id": 1,
                "title": "delectus",
                "completed": False
            },
            {
                "user_id": 2,
                "id": 3,
                "title": "traffic",
                "completed": True
            },
        ]
        patch_open_file.return_value = mock_tasks
        expected_respose = '{"total_items":1,"data":[{"user_id":2,"id":3,"title":"traffic","completed":true}]}'
        response = self.client.get("/services/tasks/?completed=true")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_respose, response.text)

    def test__get_by__only_title(self, patch_open_file):
        mock_tasks = [
            {
                "user_id": 1,
                "id": 1,
                "title": "delectus",
                "completed": False
            },
            {
                "user_id": 2,
                "id": 3,
                "title": "traffic",
                "completed": True
            },
        ]
        patch_open_file.return_value = mock_tasks
        expected_respose = '{"total_items":1,"data":[{"user_id":1,"id":1,"title":"delectus","completed":false}]}'
        response = self.client.get("/services/tasks/?title=delectus")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_respose, response.text)

    def test__get_by__completed_title(self, patch_open_file):
        mock_tasks = [
            {
                "user_id": 1,
                "id": 1,
                "title": "delectus",
                "completed": False
            },
            {
                "user_id": 1,
                "id": 1,
                "title": "delectus two",
                "completed": False
            },
            {
                "user_id": 2,
                "id": 3,
                "title": "traffic",
                "completed": True
            },
        ]
        patch_open_file.return_value = mock_tasks
        expected_respose = '{"total_items":2,"data":[{"user_id":1,"id":1,"title":"delectus","completed":false},' \
                           '{"user_id":1,"id":1,"title":"delectus two","completed":false}]}'
        response = self.client.get("/services/tasks/?completed=false&title=delectus")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_respose, response.text)

    def test__get_by_id(self, patch_open_file):
        mock_tasks = [
            {
                "user_id": 1,
                "id": 1,
                "title": "delectus",
                "completed": False
            },]
        patch_open_file.return_value = mock_tasks
        expected_respose = '{"user_id":1,"id":1,"title":"delectus","completed":false}'
        response = self.client.get("/services/tasks/1")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_respose, response.text)

@pytest.mark.usefixtures("app_client")
class TestFail(TestCase):
    def test__get_by__bad_param_data_type_deleted(self):
        expected_respose = '{"detail":[{"loc":["query","completed"],"msg":"value could not be parsed to a boolean","type":"type_error.bool"}]}'
        response = self.client.get("/services/tasks/?completed=hola")
        self.assertEqual(422, response.status_code)
        self.assertEqual(expected_respose, response.text)

    def test__get_by_id__bad_data_type_param(self):
        expected_respose = '{"detail":[{"loc":["path","id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}'
        response = self.client.get("/services/tasks/a")
        self.assertEqual(422, response.status_code)
        self.assertEqual(expected_respose, response.text)
