#!/usr/bin/env python3
"""
You must use self.cache_data - dictionary from the
parent class BaseCaching
This caching system doesn’t have limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and implements
    put and get methods
    """
    def put(self, key, item):
        """
        updates cache_data whic is declared in
        super class
        """
        if key is None and item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """
        access value stored by a particular key in super class's
        cache_data
        """
        if key is None:
            return None
        return self.cache_data.get(key)
