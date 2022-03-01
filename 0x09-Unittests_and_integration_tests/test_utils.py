#!/usr/bin/env python3
""" test module """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Testing class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    
    def test_access_nested_map(self, nested_map, path, expected):
        """ test method for nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    
    def test_access_nested_map_exception(self, nested_map, path):
        """ test method for nested map exceptions """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)

class TestGetJson(unittest.TestCase):
    """ Testing class """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    
    def test_get_json(self, url, test_payload):
        """ test method for nested map """
        class Mocked(Mock):
            ''' mocked class'''

            def json(self):
                ''' json method mocked'''
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), test_payload)

if __name__ == '__main__':
    unittest.main()
