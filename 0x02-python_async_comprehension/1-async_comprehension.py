#!/usr/bin/env python3
"""Use an async for loop"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Learn to use async list comprehension.
    the for loop runs all the async generator,
    until all is yielded"""
    return [x async for x in async_generator()]
