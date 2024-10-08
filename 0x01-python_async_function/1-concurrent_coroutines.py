#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine
    wait_n
    """
    ls = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    end = [await task for task in asyncio.as_completed(ls)]
    return end
