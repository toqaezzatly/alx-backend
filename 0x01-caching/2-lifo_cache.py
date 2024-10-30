#!/usr/bin/python3
"""LIFO caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using LIFO replacement policy"""
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data):
            # Get the last key added
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
