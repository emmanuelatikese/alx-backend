#!/usr/bin/env python3
'''this is where it begins'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''this is the page'''
    first = page - 1
    return tuple(first, first + page_size)
