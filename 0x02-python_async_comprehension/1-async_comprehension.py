#!/usr/bin/env python3
from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension over async_generator, then returns the list of numbers."""
    return [i async for i in async_generator()]

