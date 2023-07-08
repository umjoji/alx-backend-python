#!/usr/bin/python3
"""
Write a type-annotated function sum_list
which takes a list input_list of floats
as argument and returns their sum as a float.

Author: Akanimoh George
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that takes a list of floats and returns the sum of the floats
    """
    return sum(input_list)
