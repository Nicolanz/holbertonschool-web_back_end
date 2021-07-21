#!/usr/bin/env python3
"""4. Tasks Module"""


from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine to execute multiple things

    Args:
        n (int): [Number of nums in lit]
        max_delay (int): [Max delay of the range  generated]

    Returns:
        List[float]: [List sorted of the generated floats]
    """
    float_list = []
    sorted_list = []

    for i in range(n):
        result = task_wait_random(max_delay)
        task = await result
        float_list.append(task)

    while float_list:
        min_num = float_list[0]
        for item in float_list:
            if item < min_num:
                min_num = item
        sorted_list.append(min_num)
        float_list.remove(min_num)

    return sorted_list
