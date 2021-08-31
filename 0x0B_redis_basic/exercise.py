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

    def get_str(self, element) -> str:
        """Get string methof"""
        ele = element.decode('utf-8')
        return ele

    def get_int(self, element) -> int:
        """Get int method"""
        return int(element)

    def get(self, key: str, fn: Callable = None):
        """Gets an element from the Redis hash table"""
        ele = self._redis.get(key)

        if not ele:
            return None
        elif fn is None:
            return ele

        try:
            val = fn(ele)
            return val
        except Exception:
            return ele
