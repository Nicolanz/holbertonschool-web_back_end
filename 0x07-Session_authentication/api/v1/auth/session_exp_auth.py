#!/usr/bin/env python3
"""Module containing the SessionExpAuth subclass"""
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Session Exp Auth"""

    user_id_by_session_id = {}

    def __init__(self):
        """Init method"""
        value = getenv('SESSION_DURATION')

        if value:
            try:
                self.session_duration = int(value)
            except TypeError:
                self.session_duration = 0
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Method to create a new session"""
        session = super().create_session(user_id)

        print(session)
        if session is None:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        SessionExpAuth.user_id_by_session_id[session] = session_dictionary
        return session

    def user_id_for_session_id(self, session_id=None):
        """Method to get a user id for a session id"""

        my_dict = SessionExpAuth.user_id_by_session_id.get(session_id)
        if session_id is None or my_dict is None:
            return None

        create_at = SessionExpAuth.user_id_by_session_id[session_id].get(
            'created_at')
        user_id = SessionExpAuth.user_id_by_session_id[session_id].get(
            'user_id')

        if self.session_duration <= 0:
            return user_id

        if not create_at:
            return None

        if (create_at + timedelta(seconds=self.session_duration)) \
                < datetime.now():
            return None
        return user_id
