#!/usr/bin/env python3
"""Module containing LRUCacheclass"""

from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class

    Args:
        BaseCaching ([class]): [parent class]
    """
    def __init__(self):
        """Init method
        """
        super().__init__()
        self.my_dict = {}

    def put(self, key, item):
        """Module to put new items with
        LRU algorythm

        Args:
            key ([type]): [Key argument]
            item ([type]): [Value argument]
        """
        if key is None or item is None:
            pass
        else:
            self.my_dict[key] = datetime.now()
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                my_value = list(self.my_dict.values())[0]
                idx = list(self.my_dict.keys())[0]

                for key, value in self.my_dict.items():
                    if value < my_value:
                        my_value = value
                        idx = key
                print("DISCARD: {}".format(idx))
                self.cache_data.pop(idx)
                self.my_dict.pop(idx)

    def get(self, key):
        """Module to get a value of the dict

        Args:
            key ([type]): [key argument]

        Returns:
            [type]: [Value]
        """
        if key is None:
            return None
        try:
            value = self.cache_data[key]
            self.my_dict[key] = datetime.now()
        except KeyError:
            return None
        return value
