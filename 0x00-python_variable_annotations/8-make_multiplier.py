#!/usr/bin/env python3
"""Annotate for when a function is returned"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
	"""
	Gives back a function for multiplying by the given multiplier
	:param multiplier: float taken as the index of multiplication
	:return: function that multiplies value with the initially provided multiplier
	"""
	def multiply(n: float) -> float:
		"""
		multiple given value by multiplier provided in 'make_multiplier' function
		:param n: float
		:return: float of multiplied value
		"""
		return n * multiplier
	return multiply
