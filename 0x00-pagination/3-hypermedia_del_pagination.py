#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The goal here is that if between two queries, certain rows are removed
        from the dataset, the user does not miss items
        from dataset when changing page.
        """
        data = []
        ids = self.indexed_dataset()
        assert index < int(len(ids)) and index > -1
        while index not in ids.keys():
            index += 1
        st = index
        end = st + page_size - 1
        for k, v in ids.items():
            if k >= st and k <= end:
                data.append(v)
        dict_store = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": end+1
        }
        return dict_store
