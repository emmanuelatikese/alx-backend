#!/usr/bin/env python3
'''last in first out algo'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''the class begins here'''
    def put(self, key, item):
        '''discard the last item'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            _key = list(self.cache_data.keys())[3]
            self.cache_data.pop(_key)
            print("DISCARD: {}".format(_key))

    def get(self, key):
        '''getting as always'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
