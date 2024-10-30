#!/usr/bin/python3
"""MRUCache class"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.order.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
