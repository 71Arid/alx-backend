#!/usr/bin/env python3
"""
The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in
a list for those particular pagination parameters
"""

def index_range(page: int, page_size: int):
    """
    function named index_range that takes
    two integer arguments page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
