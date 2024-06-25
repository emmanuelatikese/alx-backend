#!/usr/bin/env python2
'''first time working on cache'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''inherit from base_caching'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''some updating going on'''
        self.cache_data[key] = item

    def get(self, key):
        '''all we doing is getting'''
        return self.cache_data.get(key)
