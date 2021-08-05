#!/usr/bin/env python3
"""Module containing hash_password function"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash_password function"""

    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid function"""
    check = password.encode()
    if bcrypt.checkpw(check, hashed_password):
        return True
    else:
        return False
