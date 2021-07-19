#!/usr/bin/env python3
"""Module conataining a function that returns a function that
multiplies float with given number"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to get a function to multiply a value

    Args:
        multiplier (float): [first num]

    Returns:
        Callable[[float], float]: [Function returned]
    """
    def new_func(num: float) -> float:
        """Function to get the result of a num multiplied by multiplier

        Args:
            num (float): [second num]

        Returns:
            float: [result]
        """
        return num * multiplier
    return new_func
