import os
import unittest
from run_api import api_run
import subprocess
import sys
import os
from run_api import api_run

class TestRunApi(unittest.TestCase):

    def setUp(self):
        print('\nsetUp')
        filepath = "db.json"
        if not os.path.isfile(filepath):
            print("The file {} doesn't exist".format(filepath))
        else:
            os.remove("db.json")
            print("File {} Revoved".format(filepath))
        self.process = subprocess.Popen([sys.executable,  "server.py"])
        self.init()

    def init(self):
        pload = {'username': 'test', 'password': '1234'}
        basic_url = 'http://localhost:8000'
        self.api = api_run(i_url=basic_url, i_pload=pload)

    def tearDown(self):
        print('tearDown\n')
        self.process.kill()

    def test_get_list_of_polydata_empty_list(self):
        lst = self.api.get_list_of_polydata()
        self.assertEqual(lst,[])

    def test_get_list_of_polydata_list_not_empty(self):
        self.api.create_new_object()
        act = self.api.get_list_of_polydata()
        exp = [{'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}], 'object_id': 1}]
        self.assertEqual(exp,act)

    def test_create_new_object(self):
        act = self.api.create_new_object()
        exp = {'id': 1, 'values': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}
        self.assertEqual(exp,act)

    def test_create_10_object(self):
        for i in range(10):
            self.api.create_new_object()
        act = len(self.api.get_list_of_polydata())
        exp = 10
        self.assertEqual(exp, act)

    def test_get_object_by_id_number(self):
        self.api.create_new_object()
        act = self.api.get_object_by_id_number(1)
        exp = {'object_id': 1, 'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}
        self.assertEqual(exp,act)

    def test_delete_object_by_id_number_while_list_is_empty(self):
        act = self.api.delete_object_by_id_number(1)
        exp = ''
        self.assertEqual(exp,act)

    def test_delete_object_by_id_number_while_list_is_not_empty(self):
        self.api.create_new_object()
        self.api.delete_object_by_id_number(1)
        act = self.api.get_object_by_id_number(1)
        exp = {'error': 'Not Found', 'message': 'Resource with id 1 was not found'}
        self.assertEqual(exp,act)