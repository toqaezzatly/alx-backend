#!/usr/bin/python3
"""lifo caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """first in first out"""
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """add item in the cache following LIFo replac. policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        return self.cache_data.get(key, None)
