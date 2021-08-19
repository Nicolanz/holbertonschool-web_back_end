#!/usr/bin/env python3
"""Auth module"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method to register a user"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists.'.format(email))
        except NoResultFound:
            my_password = _hash_password(password)
            user = self._db.add_user(email, my_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Method to check credential validation"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(bytes(password, 'utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Method to assign a session_id"""
        try:
            new_user = self._db.find_user_by(email=email)
            u_id = _generate_uuid()
            self._db.update_user(new_user.id, session_id=u_id)
            return u_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Method to get a user from a session id"""
        if session_id is None:
            return None
        try:
            my_user = self._db.find_user_by(session_id=session_id)
            return my_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Method to destroy a session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass
        return None


def _hash_password(password: str) -> bytes:
    """Creates a hash password"""
    new_password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(new_password, salt)

    return hashed


def _generate_uuid() -> str:
    """Generates a unique id"""
    id = uuid.uuid4()
    id = str(id)

    return(id)
