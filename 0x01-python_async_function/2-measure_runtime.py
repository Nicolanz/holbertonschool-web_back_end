#!/usr/bin/env python3
"""Module to create a measure_time function with integers n and max_delay"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function o measure time

    Args:
        n (int): [number of items]
        max_delay (int): [max delay of the range]

    Returns:
        float: [total time]
    """
    start_time = time.time()
    new_list = asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
