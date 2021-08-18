#!/usr/bin/env python3
"""Auth module"""

import bcrypt
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


def _hash_password(password: str) -> bytes:
    """Creates a hash password"""
    new_password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(new_password, salt)

    return hashed
