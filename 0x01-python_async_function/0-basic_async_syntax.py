#!/usr/bin/env python3
"""Module to understand the async basis"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a rand after waiting some time

    Args:
        max_delay (int, optional): [max number of the rand]. Defaults to 10.

    Returns:
        [float]: [Number between the rand 0, max_delay]
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
