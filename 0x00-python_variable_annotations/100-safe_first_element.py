#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element from an
    inputted iterable if it exists
    :param lst: input iterable
    :return: first element of lst
    """
    if lst:
        return lst[0]
    else:
        return None
