#!/usr/bin/env python3
"""Auth module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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
        """Method to assign a unique id"""
        try:
            user = self._db.find_user_by(email=email)
            u_id = _generate_uuid()
            self._db.update_user(user.id, session_id=u_id)
            return u_id
        except NoResultFound:
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
