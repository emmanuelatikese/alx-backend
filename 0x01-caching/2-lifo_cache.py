#!/usr/bin/env python3
'''last in first out algo'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''the Lifo class begins here'''
    def put(self, key, item):
        '''discard the last item'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            _key = list(self.cache_data.keys())[self.MAX_ITEMS - 1]
            self.cache_data.pop(_key)
            print("DISCARD: {}".format(_key))

    def get(self, key):
        '''this get value by returning'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
