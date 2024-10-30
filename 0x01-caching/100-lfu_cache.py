#!/usr/bin/python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = {}  # key: frequency count
        self.order = []  # for tracking access order within same frequency

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items()if v == min_freq]
            if len(lfu_keys) == 1:
                lfu_key = lfu_keys[0]
            else:
                # If multiple items have same frequency,
                # remove the least recently used among them
                for k in self.order:
                    if k in lfu_keys:
                        lfu_key = k
                        break
            print("DISCARD:", lfu_key)
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            self.order.remove(lfu_key)

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
