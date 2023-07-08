#!/usr/bin/env python3
"""
Write a type-annotated function element_length
which takes a list input_list of strings
and returns a list containing the length of each string.
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that takes a list of strings and returns a list of integers
    """
    return [(list_, len(list_)) for list_ in lst]
