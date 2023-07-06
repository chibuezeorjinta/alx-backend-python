#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function.
Hint: look into TypeVar.
Turns out TypeVar is like in interface for Typescript"""
from typing import Mapping, Any, Union, TypeVar

X = TypeVar('X')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[X, None]) -> Union[Any, X]:
    """
    Check if key is in dct. if not return default which is
    either new type 'X' or none.
    :param dct: Dictionary
    :param key: Any type to index dictionary
    :param default:
    :return: item at key or default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
