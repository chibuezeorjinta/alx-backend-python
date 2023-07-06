#!/usr/bin/env python3
"""Complex annotation for lists"""


def sum_list(input_list: list[float]) -> float:
    """
    collect each float in input_list
    :param input_list: list of floats
    :return: sum of list
    """
    list_sum: float = 0
    for item in input_list:
        list_sum += item
    return list_sum
