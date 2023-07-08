#!/usr/bin/python3
"""
Function: make_multiplier
Params: multiplier(float)
Returns: function that multiplies a float by multiplier
Author : Akanimoh George
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """
    A function that takes a float
    and returns a function that multiplies
    a float by multiplier
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
