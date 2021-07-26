#!/usr/bin/env python3
"""Module containing LIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class

    Args:
        BaseCaching ([class]): [BaseCaching class]
    """
    def __init__(self):
        """Init method
        """
        super().__init__()

    def put(self, key, item):
        """Put function to put new item by using LIFO algorythm

        Args:
            key ([type]): [Key argument]
            item ([type]): [Value argument]
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS or \
                                    key in self.cache_data.keys():
                self.last_item = key
            else:
                print("DISCARD: {}".format(self.last_item))
                self.cache_data.pop(self.last_item)
                self.last_item = key

            self.cache_data[key] = item

    def get(self, key):
        """Get function to get new item by key

        Args:
            key ([type]): [Key argument]

        Returns:
            [type]: [value]
        """
        if key is None:
            return None
        try:
            value = self.cache_data[key]
        except KeyError:
            return None
        return value
