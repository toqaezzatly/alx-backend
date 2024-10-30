#!/usr/bin/python3
""" fifo_cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inherits from BaseCaching"""

    def __init__(self):
        """Initialize the FIFOCache"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.key_order.remove(key)
        self.cache_data[key] = item
        self.key_order.append(key)

        if len(self.key_order) > BaseCaching.MAX_ITEMS:
            first_key = self.key_order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
