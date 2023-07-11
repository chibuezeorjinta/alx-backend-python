#!/usr/bin/env python3
"""Coroutine that loops ten times to return a value"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """Generate async timers"""
    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
