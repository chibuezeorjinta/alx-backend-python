#!/usr/bin/env python3
"""List with mixed input"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums each value of mxd_lst
    :param mxd_lst: list of floats and ints
    :return: sum in float
    """
    list_sum: float = 0
    for item in mxd_lst:
        list_sum += item
    return list_sum
