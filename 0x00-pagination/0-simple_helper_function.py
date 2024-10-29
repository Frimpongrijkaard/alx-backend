#!/usr/bin/env python3

"""Simple helper function that take two inputs"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function should return a tuple of size"""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    size_of_range = (start_index, end_index)

    return size_of_range
