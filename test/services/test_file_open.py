from unittest import TestCase

import pkg_resources

from services import open_file


class TestOpenFile(TestCase):
    def test__open_file__success_resource_path_tasks(self):
        TASKS_PATH = pkg_resources.resource_filename('resources', 'tasks.json')
        tasks = open_file(TASKS_PATH)
        self.assertIsInstance(tasks, list)

    def test__open_file__success_resource_path_users(self):
        TASKS_PATH = pkg_resources.resource_filename('resources', 'users.json')
        tasks = open_file(TASKS_PATH)
        self.assertIsInstance(tasks, list)
