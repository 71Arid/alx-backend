#!/usr/bin/env python3
"""
You must use self.cache_data - dictionary from the
parent class BaseCaching
This caching system doesn’t have limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching and implements
    put and get methods
    """
    def __init__(self):
        """
        overloading init class
        """
        super().__init__()

    def put(self, key, item):
        """
        updates cache_data whic is declared in
        super class
        """
        if key is None or item is None:
            return
        total_keys = self.cache_data.keys()
        if len(self.cache_data) == super().MAX_ITEMS and key not in total_keys:
            total_keys = list(self.cache_data.keys())
            first = total_keys[0]
            self.cache_data.pop(first)
            print(f"DISCARD: {first}")
        self.cache_data.update({key: item})

    def get(self, key):
        """
        access value stored by a particular key in super class's
        cache_data
        """
        if key is None:
            return None
        return self.cache_data.get(key)
