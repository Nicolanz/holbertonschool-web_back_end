#!/usr/bin/env python3
"""Module containing async generator"""

import asyncio
import random


async def async_generator():
    """Async generator

    Yields:
        [type]: [yields numbers]
    """
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
