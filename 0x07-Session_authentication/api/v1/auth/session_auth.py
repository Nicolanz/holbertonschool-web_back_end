#!/usr/bin/env python3
"""Module containing the SessionAuth subclass"""
import uuid
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """SessionAuth subclass"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create session method"""
        if user_id is None or type(user_id) != str:
            return None
        id = uuid.uuid4()
        id = str(id)
        SessionAuth.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """User id method"""
        if session_id is None or type(session_id) != str:
            return None

        value = SessionAuth.user_id_by_session_id.get(session_id)
        return value

    def current_user(self, request=None):
        """Method to get a user by a cookies"""
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        user = User()
        obj = user.get(user_id)

        return obj

    def destroy_session(self, request=None):
        """Destroy method to delete a session"""
        if request is None:
            return False

        cookie_obj = self.session_cookie(request)
        if cookie_obj is None:
            return False

        user_id = self.user_id_for_session_id(cookie_obj)
        if user_id is None:
            return False

        for key, value in SessionAuth.user_id_by_session_id.items():
            if value == user_id:
                del SessionAuth.user_id_by_session_id[key]
                break
        return True
