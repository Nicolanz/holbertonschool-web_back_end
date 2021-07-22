#!/usr/bin/env python3
"""Module containing comprehension"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension

    Returns:
        List[float]: [list of generated random value]
    """
    new_list = [i async for i in async_generator()]
    return new_list
