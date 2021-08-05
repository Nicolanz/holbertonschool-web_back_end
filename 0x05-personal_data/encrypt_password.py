#!/usr/bin/env python3
"""Module containing hash_password function"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash_password function"""

    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
