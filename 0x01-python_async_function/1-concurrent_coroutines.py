#!/usr/bin/env python3
"""Call async function multiple times"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn the wait random function 'n' times."""
    task_list: List[asyncio.Task] = []
    for event in range(n):
        task_list.append(asyncio.create_task(wait_random(max_delay)))
    sorted_task = asyncio.as_completed(task_list)
    return await asyncio.gather(*sorted_task)
