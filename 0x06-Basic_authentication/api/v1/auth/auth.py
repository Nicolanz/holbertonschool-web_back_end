#!/usr/bin/env python3
"""Module containing the auth class"""
import flask
from typing import TypeVar, List


class Auth:
    """Auth Main Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function to require auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1:] != '/':
            path = path + '/'

        for i in excluded_paths:

            if '*' in i:
                idx = i.find("*") - 1
                my_list = []
                my_str = ""

                while i[idx] != '/':
                    my_list.insert(0, i[idx])
                    idx -= 1

                my_str = my_str.join(my_list)

                if my_str in path:
                    return False

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """function to get the auth header"""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return flask.request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user"""
        return None
