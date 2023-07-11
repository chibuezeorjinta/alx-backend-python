#!/usr/bin/env python3
"""Calculate runtime"""
import time
from typing import List
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the time taken for the four
    generated tasks to run asynchronously

    the result will always be within 10 seconds as the primary
    task takes roughly 10 seconds to complete. hence,
    as the new 4 instances are ran using the gather methods,
    they all return at roughly the same time.
    """
    tasks: List[asyncio.Task] = []
    start: float = time.time()
    for _ in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end: float = time.time()
    return end - start
