#!/usr/bin/env python3
"""Exercise Module"""

from uuid import uuid4
from typing import Union, Callable
import redis


class Cache:
    """Cache class
    """
    def __init__(self):
        """Init constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis hash table"""
        key = uuid4()
        key = str(key)
        self._redis.mset({key: data})
        return key

    def get_str(self):
        """Get string methof"""
        return str

    def get_int(self):
        """Get int method"""
        return int

    def get(self, key: str, fn: Callable):
        """Gets an element from the Redis hash table"""
        ele = self._redis.get(key)
        try:
            val = fn(ele)
            return val
        except Exception:
            pass
        return ele
