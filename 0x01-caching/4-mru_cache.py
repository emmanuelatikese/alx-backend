#!/usr/bin/env python3
'''least recently used'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''the MRU class begins here'''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''discard the most recently item'''
        if not key or item is None:
            return
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            _key = list(self.cache_data.keys())[self.MAX_ITEMS - 1]
            self.cache_data.pop(_key)
            print("DISCARD: {}".format(_key))

    def get(self, key):
        '''getting as always'''
        if key not in self.cache_data or key is None:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
