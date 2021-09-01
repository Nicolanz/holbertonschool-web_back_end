#!/usr/bin/env python3
"""Exercise Module"""

from uuid import uuid4
from typing import Union, Callable
from functools import wraps
import redis


def count_calls(func: Callable) -> Callable:
    """Decorator to count calls of a function"""
    @wraps(func)
    def wrapper(self, data):
        """wrapper fuction with coounter functionality"""
        func(self, data)
        self._redis.incr(func.__qualname__)
    return wrapper


class Cache:
    """Cache class
    """
    def __init__(self):
        """Init constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis hash table"""
        key = uuid4()
        key = str(key)
        self._redis.mset({key: data})
        return key

    def get_str(self, element) -> str:
        """Get string method"""
        ele = element.decode('utf-8')
        return ele

    def get_int(self) -> int:
        """Get int method"""
        return int

    def get(self, key: str, fn: Callable = None):
        """Gets an element from the Redis hash table"""
        ele = self._redis.get(key)

        if not ele:
            return None
        elif fn is None:
            return ele
        else:
            return fn(ele)
