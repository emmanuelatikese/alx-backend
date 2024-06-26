#!/usr/bin/env python3
'''first time working on fifo cache I guess...'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''functions fifo begins'''
    cache_data = {}

    def put(self, key, item):
        '''this function is from parent class'''
        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            _key = list(self.cache_data.keys())[0]
            del self.cache_data[_key]
            print("DISCARD: {}".format(_key))

    def get(self, key):
        '''get function from cache'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
