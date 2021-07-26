#!/usr/bin/env python3
"""Basic cache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache module that inherits from BaseCaching

    Args:
        BaseCaching ([BaseCaching]): [Parent class]
    """

    def put(self, key, item):
        """Function to put a new item

        Args:
            key ([type]): [Key]
            item ([type]): [Value]
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Funtion to get a value element

        Args:
            key ([type]): [Key of the value]

        Returns:
            [type]: [value0]
        """
        if key is None:
            return None
        try:
            value = self.cache_data[key]
        except KeyError:
            return None
        return value
