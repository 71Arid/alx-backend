#!/usr/bin/env python3
"""
You must use self.cache_data - dictionary from the
parent class BaseCaching
This caching system doesn’t have limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    inherits from BaseCaching and implements
    put and get methods
    """
    def __init__(self):
        """
        overloading init class
        """
        super().__init__()
        self.least_items = []

    def put(self, key, item):
        """
        updates cache_data which is declared in
        super class
        """
        if key is None or item is None:
            return
        if key not in self.least_items:
            self.least_items.append(key)
        if len(self.cache_data) == super().MAX_ITEMS:
            if key in self.cache_data:
                index = self.least_items.index(key)
                rem = self.least_items.pop(index)
                self.least_items.append(rem)
            else:
                list_item = self.least_items.pop(-2)
                self.cache_data.pop(list_item)
                print(f'DISCARD: {list_item}')
        self.cache_data.update({key: item})

    def get(self, key):
        """
        access value stored by a particular key in super class's
        cache_data
        """
        if key is None:
            return None
        if key in self.least_items:
            index = self.least_items.index(key)
            rem = self.least_items.pop(index)
            self.least_items.append(rem)
        return self.cache_data.get(key)
