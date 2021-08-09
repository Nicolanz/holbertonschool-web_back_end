#!/usr/bin/env python3
"""Module containing the BasicAuth class that inherirs from Auth class"""
from .auth import Auth
from models.user import User
from typing import TypeVar
import base64
import binascii


class BasicAuth(Auth):
    """Basic Auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract base_64 method"""
        if authorization_header is None or \
            type(authorization_header) != str or \
                authorization_header[:5] != 'Basic':
            return None
        else:
            values = authorization_header.split()
            if len(values) <= 1:
                return None
            return values[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
            ) -> str:
        """Base64 decode method"""
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None
        try:
            s = base64.b64decode(base64_authorization_header)
            return s.decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user method"""
        if decoded_base64_authorization_header is None or \
            type(decoded_base64_authorization_header) != str or \
                ':' not in decoded_base64_authorization_header:
            return None, None

        my_str = decoded_base64_authorization_header
        idx = my_str.find(":")
        my_str = my_str[:idx] + " " + my_str[idx+1:]

        values = my_str.split()
        return values[0], values[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Method to get a User object"""

        if user_email is None or type(user_email) != str or \
                user_pwd is None or type(user_pwd) != str:
            return None

        user = User()
        objs = user.search()
        obj = None

        for i in objs:
            if i.__dict__['email'] == user_email:
                obj = i

        if not obj or obj.is_valid_password(user_pwd) is False:
            return None

        return obj

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user and basic authentication"""

        auth_header = self.authorization_header(request)
        my_base64 = self.extract_base64_authorization_header(auth_header)
        new_base64 = self.decode_base64_authorization_header(my_base64)
        user, password = self.extract_user_credentials(new_base64)
        obj = self.user_object_from_credentials(user, password)

        return obj
