#!/usr/bin/env python3
"""Auth module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Creates a hash password"""
    new_password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(new_password, salt)

    return hashed
