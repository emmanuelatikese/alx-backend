#!/usr/bin/env python3
'''this is where it continues from file 1'''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''this is the page'''
    first = (page - 1) * page_size
    return (first, first + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''this function return list'''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        first, last = index_range(page, page_size)
        ans = self.dataset()
        if first > len(ans):
            return []
        return ans[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> object:
        '''this is an improve version'''
        res = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": res,
            "next_page": page + 1,
            "prev_page": page - 1 if page != 1 else None,
            "total_pages": total_pages
        }
