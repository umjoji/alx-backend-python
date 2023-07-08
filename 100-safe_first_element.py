#!/usr/bin/env python3
"""
Augmenting a function to have a list as parameters
and return a union of values
Author: Akanimoh George
"""
from typing import Union, Sequence, Any

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    A function that takes a list and returns the first element of the list
    """
    if lst:
        return lst[0]
    else:
        return None