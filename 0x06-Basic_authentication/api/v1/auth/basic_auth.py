#!/usr/bin/env python3
"""Module containing the BasicAuth class that inherirs from Auth class"""
from .auth import Auth


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
