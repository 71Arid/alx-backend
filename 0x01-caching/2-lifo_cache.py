#!/usr/bin/env python3
"""
You must use self.cache_data - dictionary from the
parent class BaseCaching
This caching system doesn’t have limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and implements
    put and get methods
    """
    def __init__(self):
        """
        overloading init class
        """
        super().__init__()
        self.last_item = 0

    def put(self, key, item):
        """
        updates cache_data which is declared in
        super class
        """
        if key is None and item is None:
            return
        ls = None
        flag = 1
        total_keys = self.cache_data.keys()
        if len(self.cache_data) == super().MAX_ITEMS:
            if key not in total_keys:
                self.last_item = list(self.cache_data)[3]
                ls = self.last_item
                self.cache_data.pop(ls)
            else:
                ls = key
                flag = 0
                self.cache_data.pop(ls)
            if ls is not None and flag != 0:
                print(f"DISCARD: {ls}")
                ls = None
        self.cache_data.update({key: item})

    def get(self, key):
        """
        access value stored by a particular key in super class's
        cache_data
        """
        if key is None:
            return None
        return self.cache_data.get(key)
