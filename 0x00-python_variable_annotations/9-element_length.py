#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values with the appropriate types"""
from typing import Any, Tuple, List


def element_length(lst) -> List[Tuple[Any, int]]:
    """
    Gives one a modified list which has a tuple for each element in 'lst'.
    this tuple contains the element and the first entry followed by the length of the element.
    :param lst: list to be counter
    :return: list of tuple.
    """
    return [(i, len(i)) for i in lst]
