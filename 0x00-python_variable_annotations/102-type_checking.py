#!/usr/bin/env python3
"""Use mypy to validate the following piece of code and apply any necessary changes."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
	"""
	get a sublist of a tuple upto the 'factor' index
	:param lst: given tuple
	:param factor: index to stop
	:return: sublist
	"""
	zoomed_in: List = [
		item for item in lst
		for i in range(factor)
	]
	return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
