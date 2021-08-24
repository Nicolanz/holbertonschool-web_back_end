#!/usr/bin/env python3
"""Module containing the test cases for the utils.py module"""

from utils import access_nested_map
import unittest
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
