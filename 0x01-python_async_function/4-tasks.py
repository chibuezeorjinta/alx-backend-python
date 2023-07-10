#!/usr/bin/env python3
"""Call async function multiple times"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call a set of async functions, return their outputs
    in the order of completion"""
    task_list: List[asyncio.Task] = []
    for call in range(n):
        task_list.append(task_wait_random(max_delay))
    sorted_task_list = asyncio.as_completed(task_list)
    return await asyncio.gather(*sorted_task_list)
