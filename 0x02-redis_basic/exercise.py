#!/usr/bin/env python3

"""
Redis Basic Exercise
"""

import redis
import uuid
from typing import Callable, Union


class Cache:
    """
    A Cache class based on Redis
    """

    def __init__(self):
        """initializes an instance of Cache"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a str"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float,
                                                          None]:
        """get data from cache"""

        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """get data in str format"""

        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """get data in int"""

        return self.get(key, fn=int)
