#!/usr/bin/env python3

"""
Redis Basic Exercise
"""

import redis
from uuid import uuid4
from typing import Union

class Cache:
    """
    A Cache class based on Redis
    """

    def __init__(self):
        """initializes an instance of Cache"""

        self._redis = redis.Redis().flushdb()

    def store(data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a str"""

        key = str(uuid4())
        self._redis.set(key, data)
        return key
