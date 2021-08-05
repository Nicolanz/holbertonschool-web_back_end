#!/usr/bin/env python3
"""Module containing the auth class"""
from flask import request
from typing import TypeVar, List


class Auth:
    """Auth Main Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function to require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """function to get the auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user"""
        return None
