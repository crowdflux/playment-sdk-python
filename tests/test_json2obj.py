from playment.utilities import JSON2Obj, Decodable
from collections import namedtuple
import unittest
import json


class TestJson2Obj(unittest.TestCase):
    def test_json2obj(self):
        test_data = JSON2Obj(obj=URL(), data=json.dumps({"url": "yo_1"})).json2obj()
        self.assertEqual(test_data.url, URL().url)


class URL(Decodable):
    def __init__(self):
        self.url = "yo_1"

    def json_object_hook(self, d):
        return namedtuple(self.__class__.__name__, d.keys())(*d.values())



