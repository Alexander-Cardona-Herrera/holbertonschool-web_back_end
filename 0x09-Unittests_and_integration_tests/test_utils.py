#!/usr/bin/env python3
""" test module """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Testing class for nested map"""

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
    """ Testing class for get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    
    def test_get_json(self, url, test_payload):
        """ test method for get_json """
        class Mocked(Mock):
            """ mocked class """

            def json(self):
                """ json method mocked """
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), test_payload)

class TestMemoize(unittest.TestCase):
    """ Testing class for memoize """

    def test_memoize(self):
        """ test method for nested map """
        class TestClass:
            """ mocked class """
            def a_method(self):
                """ method mocked """
                return 42

            @memoize
            def a_property(self):
                """ method mocked """
                return self.a_method()
        
        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()

if __name__ == '__main__':
    unittest.main()
