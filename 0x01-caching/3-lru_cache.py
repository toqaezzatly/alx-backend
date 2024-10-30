#!/usr/bin/python3
"""LRUcaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching"""

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache following LRU replacement policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.order.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
