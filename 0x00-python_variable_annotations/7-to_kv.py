#!/usr/bin/env python3
"""Module to get a tuple with the square of a num and a str"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to return a tuple with the squae of a num and a string

    Args:
        k (str): [satrin]
        v (Union[int, float]): [Argument of type int or float]

    Returns:
        Tuple[str, float]: [my_tuple]
    """
    my_tuple = (k, v*v)

    return my_tuple
