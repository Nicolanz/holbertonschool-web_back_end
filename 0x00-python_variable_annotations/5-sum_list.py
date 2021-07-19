#!/usr/bin/env python3
"""Module to obtain the sum of floats elements inside a list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function so sum list float elements

    Args:
        input_list (List[float]): [List of floats]

    Returns:
        float: [Sum of list of floats]
    """
    num: float = 0
    for i in input_list:
        num += i
    return num
