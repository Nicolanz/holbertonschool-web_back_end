#!/usr/bin/env python3
"""Module with correct annotation"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the length of the tuples inside a list

    Args:
        lst (Sequence[Iterable]): [List]

    Returns:
        List[Tuple[Sequence, int]]: [New list with the length of the tupes]
    """
    return [(i, len(i)) for i in lst]
