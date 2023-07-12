#!/usr/bin/python3
"""
Execute multiple coroutines
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Args:
        n: number of times to execute wait_random()
        max_delay: max wait time
    Returns:
        float: average wait time
    """
    # create tasks using list comprehension
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in
             range(n)]
    return [await task for task in asyncio.as_completed(tasks)]  # type: ignore
