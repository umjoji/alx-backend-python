#!/usr/bin/env python3
"""
Add annotations to a function
Function: safely_get_value
Parameters: dct: dict, key: Any, default: Union[TypeVar('T'), None]
Return: Union[Any, TypeVar('T')]
Author: Akanimoh George
"""
from typing import Mapping, Optional, Any, Union, TypeVar


# type: ignore
def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[Union[TypeVar('T'), None]]
) -> Union[Any, TypeVar('T')]:
    """
    A function that takes a dictionary and returns the value of the key
    """
    if key in dct:
        return dct[key]
    else:
        return default
