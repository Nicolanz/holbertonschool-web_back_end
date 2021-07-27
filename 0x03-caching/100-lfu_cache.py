#!/usr/bin/env python3
"""Module containing LFUCache class class"""

from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Init method
        """
        super().__init__()
        self.lru_dict = {}
        self.lfu_dict = {}

    def lfu_item(self):
        """lfu item

        Returns:
            [list]: [list]
        """
        minimum = min(self.lfu_dict, key=self.lfu_dict.get)
        my_list = []
        my_list.append(minimum)

        for lfu_key, lfu_val in self.lfu_dict.items():
            if lfu_key not in my_list:
                if lfu_val == self.lfu_dict[minimum]:
                    my_list.append(lfu_key)

        return my_list

    def put(self, key, item):
        """put function

        Args:
            key ([type]): [key argument]
            item ([type]): [item argument]
        """
        if key is None or item is None:
            pass
        else:
            if key in self.lfu_dict.keys():
                self.lfu_dict[key] += 1
            else:
                self.lfu_dict[key] = 1
            self.lru_dict[key] = datetime.now()
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                new_list = self.lfu_item()

                if len(new_list) > 1:
                    my_value = self.lru_dict[new_list[0]]
                    idx = new_list[0]

                    for keys, values in self.lru_dict.items():
                        if values < my_value and keys in new_list:
                            my_value = values
                            idx = keys

                    print("DISCARD: {}".format(idx))
                    self.cache_data.pop(idx)
                    self.lfu_dict.pop(idx)
                    self.lru_dict.pop(idx)

                else:
                    print("DISCARD: {}".format(new_list[0]))
                    self.cache_data.pop(new_list[0])
                    self.lfu_dict.pop(new_list[0])
                    self.lru_dict.pop(new_list[0])
                

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
            self.lfu_dict[key] += 1
            self.lru_dict[key] = datetime.now()
        except KeyError:
            return None
        return value
