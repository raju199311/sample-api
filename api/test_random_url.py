import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from api.app import *
import json


class BasicTests(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data).get('type'), "success")


if __name__ == '__main__':
    unittest.main()