#!/usr/bin/env python3
"""Module containing index_range function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index range function

    Args:
        page (int): [Number of page]
        page_size (int): [Number of page size]

    Returns:
        Tuple[int, int]: [Tuple with two values]
    """
    my_page = page_size * (page - 1)
    my_page_size = page * page_size
    return my_page, my_page_size
