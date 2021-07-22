#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""


import asyncio
import timeit
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime

    Returns:
        float: [total time]
    """
    start_time = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    total_time = timeit.default_timer() - start_time

    return total_time
