#!/usr/bin/env python3
"""Module containing the test cases for the utils.py module"""

import unittest
import requests
from unittest import mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Tuple,
    Any,
    Dict
)


class TestAccessNestedMap(unittest.TestCase):
    """Class to test utils functions"""
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {'b': 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, a: Dict, b: Tuple, out: Any):
        """Function to test utils.access_nested_map function"""
        self.assertEqual(access_nested_map(a, b), out)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, a: Dict, b: Tuple, out: Any):
        """Method to handle and test utils.access_nested_map raises"""
        self.assertRaises(out, access_nested_map, a, b)


class TestGetJson(unittest.TestCase):
    """Class to test the utils.get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_requests: mock.MagicMock):
        """Method to test get_json function"""
        mock_requests(test_url)
        mock_requests.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class to test memoize"""
    def test_memoize(self):
        """Method to test the memoize function"""
        class TestClass:
            """Class definition"""
            def a_method(self):
                """a_method method"""
                return 42

            @memoize
            def a_property(self):
                """a_property method"""
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_method:
            mock_method()
            mock_method.assert_called_once()
