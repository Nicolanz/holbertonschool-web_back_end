#!/usr/bin/env python3
"""Module containing the test cases for the utils.py module"""

import unittest
import requests
from unittest import mock
from utils import access_nested_map, get_json
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
        mock_requests.return_value = test_payload
        mock_requests.assert_called_once()
        self.assertEqual(mock_requests(), get_json(test_url))
