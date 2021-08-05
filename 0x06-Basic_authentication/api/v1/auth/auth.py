#!/usr/bin/env python3
"""Module containing the auth class"""
from flask import request
from typing import TypeVar, List


class Auth:
    """Auth Main Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function to require auth"""
        if path is None:
            return True
        if len(excluded_paths) == 0 or excluded_paths is None:
            return True
        if path[-1:] != '/':
            new_path = path + '/'
        else:
            new_path = path

        if new_path in excluded_paths or path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """function to get the auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user"""
        return None
