#!/usr/bin/python3
"""Defines an add_integer function."""

def add_integer(a, b=98):
	"""return the addition of integers a and b.

	float args are typecasted to ints before the operation.

	Raises:
		TypeError: if either of a or b are not ints or floats.
	"""
	if ((not isinstance(a, int) and not isinstance(a,float))):
		raise TypeError("a must be an int")
	if ((not isinstance(b, int) and not isinstance(b,float))):
		raise TypeError("b must be an int")
	return (int(a) + int(b))
