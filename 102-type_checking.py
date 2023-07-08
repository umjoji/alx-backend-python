#!/usr/bin/env python3
"""
102-type_checking.py
Function: zoom_array
Params: lst(Tuple), factor(int)
Returns: Tuple
Author: Akanimoh George
"""
from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    A function that takes a tuple and returns a tuple
    """
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in