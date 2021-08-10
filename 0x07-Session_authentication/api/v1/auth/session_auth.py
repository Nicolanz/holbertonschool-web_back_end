#!/usr/bin/env python3
"""Module containing the SessionAuth subclass"""
import uuid
from .auth import Auth


class SessionAuth(Auth):
    """SessionAuth subclass"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create session method"""
        if user_id is None or type(user_id) != str:
            return None
        id = uuid.uuid4()
        SessionAuth.user_id_by_session_id[str(id)] = user_id
        return id
