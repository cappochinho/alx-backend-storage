#!/usr/bin/env python3

"""
Redis Basic Exercise
"""

import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator for Cache
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, int]:
        """
        Wrapper to increment the count for key when called
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Keeps records of input parameters and results of functions
    """

    @wraps(method)
    def wrapper(self, *args) -> Union[str, int]:
        '''wrapper to add the call history'''
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        op = method(self, *args)
        self._redis.rpush(f"{key}:outputs", op)
        return op

    return wrapper

    return wrapper


class Cache:
    """
    A Cache class based on Redis
    """

    def __init__(self):
        """initializes an instance of Cache"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
