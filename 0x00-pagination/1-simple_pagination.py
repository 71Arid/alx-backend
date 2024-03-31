#!/usr/bin/env python3
"""
The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in
a list for those particular pagination parameters
"""
import csv
import math
from typing import List


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
        """
        get the required number of indexes based on start
        and end indexes if the arguments passsed into the
        function are both ints
        """
        assert isinstance(page, int) and isinstance(page_size, int)\
                and page > 0 and page_size > 0
        indexes = self.index_range(page, page_size)
        st_ind = int(indexes[0])
        end_ind = int(indexes[1])
        ds = self.dataset()
        if (st_ind < len(ds) and end_ind < len(ds)):
            page = ds[st_ind:end_ind]
            return page
        else:
            return list()

    def index_range(self, page: int, page_size: int):
        """
        function named index_range that takes
        two integer arguments page and page_size
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)
