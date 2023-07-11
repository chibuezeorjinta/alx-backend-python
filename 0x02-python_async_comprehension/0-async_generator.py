#!/usr/bin/env python3
"""Coroutine that loops ten times to return a value"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate async random values.
    uses the yield keyword.
    Returns a generator."""
    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
