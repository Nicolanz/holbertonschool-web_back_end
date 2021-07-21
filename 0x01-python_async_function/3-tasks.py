#!/usr/bin/env python3
"""Module to create task_wait_random function"""


import asyncio
from typing import Coroutine
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """Function to return new task

    Args:
        max_delay (int): [max num for the range]

    Returns:
        Coroutine: [new task]
    """
    new_task = asyncio.create_task(wait_random(max_delay))
    return new_task
