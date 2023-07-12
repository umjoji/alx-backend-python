#!/usr/bin/env python3
"""
Async basics
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random number of seconds
    """
    max_delay *= random.random()  # type: ignore
    await asyncio.sleep(max_delay)
    return max_delay
