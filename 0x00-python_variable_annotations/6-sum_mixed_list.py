#!/usr/bin/env python3
"""Return the sum of a list int and float elements"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to return the sum of a the
    list elements of type int and float

    Args:
        mxd_lst (List[int, float]): [List with mixed elements]

    Returns:
        float: [Sum of the mixed list elements]
    """
    num: float = 0
    for i in mxd_lst:
        num += i
    return num
