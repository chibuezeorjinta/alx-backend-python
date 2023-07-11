#!/usr/bin/env python3
"""Calculate runtime"""
import time
from typing import List
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    tasks: List[asyncio.Task] = []
    start: float = time.time()
    for _ in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end: float = time.time()
    return end - start
