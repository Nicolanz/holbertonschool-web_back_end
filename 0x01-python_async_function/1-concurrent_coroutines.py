#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine to execute multiple things

    Args:
        n (int): [Number of nums in lit]
        max_delay (int): [Max delay of the range  generated]

    Returns:
        List[float]: [List sorted of the generated floats]
    """
    float_list = []

    for i in range(n):
        float_list.append(await wait_random(max_delay))

    for j in range(len(float_list)):
        for n in range(j+1, len(float_list)):
            if float_list[j] > float_list[n]:
                float_list[j] = float_list[n]
                float_list[n] = float_list[j]
    return float_list
