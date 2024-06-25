#!/usr/bin/env python3
'''first time working on fifo cache I guess...'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''Here we go!!! with this, I guess ...'''
    cache_data = {}

    def put(self, key, item):
        '''not going to lie this is my first'''

        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            _key = list(self.cache_data.keys())[0]
            del self.cache_data[_key]
            print("DISCARD: {}".format(_key))

    def get(self, key):
        '''getting as always'''
        return self.cache_data[key] if key in self.cache_data or\
            key is not None else None
