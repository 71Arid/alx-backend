#!/usr/bin/env python3
"""
You must use self.cache_data - dictionary from the
parent class BaseCaching
This caching system doesn’t have limit
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    inherits from BaseCaching and implements
    put and get methods
    """
    def __init__(self):
        """
        overloading init class
        """
        super().__init__()
        self.items = {}

    def put(self, key, item):
        """
        updates cache_data which is declared in
        super class
        """
        if key is None or item is None:
            return
        if key not in self.items.keys():
            self.items.update({key: 1})
        if len(self.cache_data) == super().MAX_ITEMS:
            if key in self.cache_data.keys():
                if key in self.items.keys():
                    v = self.items.get(key)
                    value = v + 1
                    self.items.update({key: value})
            else:
                items_use = dict.copy(self.items)
                items_use.popitem()
                unique_values = set(items_use.values())
                smallest_value = min(unique_values)
                list_item = None
                for k, v in items_use.items():
                    if v == smallest_value:
                        list_item = k
                        self.items.pop(k)
                        self.cache_data.pop(k)
                        break
                print(f'DISCARD: {list_item}')
        self.cache_data.update({key: item})

    def get(self, key):
        """
        access value stored by a particular key in super class's
        cache_data
        """
        if key is None:
            return None
        if key in self.items:
            v = self.items.get(key)
            value = v + 1
            self.items.update({key: value})
        return self.cache_data.get(key)
