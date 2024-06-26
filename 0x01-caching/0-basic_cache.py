#!/usr/bin/env python2
'''first time working on cache'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''inherit from base_caching'''

    def put(self, key, item):
        '''some updating going on'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''getting as always'''
        return self.cache_data[key] if key in self.cache_data or\
            key is not None else None
