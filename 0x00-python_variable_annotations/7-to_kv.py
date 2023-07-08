#!/usr/bin/env python3
"""
Function: to_kv
Params: k(str), v(int or float)
Returns: tuple
Author: Akanimoh George
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes a string and an int or float and returns a tuple
    """
    return (k, v * v)
