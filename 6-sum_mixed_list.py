#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
If the input is empty, it should return 0.0. Here's an example:
>>> sum_mixed_list([5, 4, 3])
12
>>> sum_mixed_list([5.4, 4.3, 3.1])
12.8
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that takes a list of integers and floats
    and returns the sum of the integers and floats
    """
    return sum(mxd_lst)