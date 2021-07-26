#!/usr/bin/env python3
"""FIFOcache module"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class

    Args:
        BaseCaching ([class]): [BaseCaching parent class]
    """

    def __init__(self):
        """Init attributes
        """
        super().__init__()

    def put(self, key, item):
        """Funtion to put new element considering
        FIFO algorythm

        Args:
            key ([type]): [Key argument]
            item ([type]): [Value argument]
        """

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))

    def get(self, key):
        """Funtion to get a value

        Args:
            key ([type]): [key argument]

        Returns:
            [type]: [Value]
        """
        if key is None:
            return None
        try:
            value = self.cache_data[key]
        except KeyError:
            return None
        return value
