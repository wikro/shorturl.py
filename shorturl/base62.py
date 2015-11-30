"""Base62 encoding and decoding"""
DIGITS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE = len(DIGITS)

def decode(b62string):
	"""Decode base62 string"""
	try:
		result, multiplier = 0, 1
		for char in reversed(b62string):
			result += multiplier*DIGITS.index(char)
			multiplier *= BASE
		return str(result)
	except ValueError:
		return '0'

def encode(number):
	"""Encode number to base62"""
	number = int(number)
	if number < 0:
		raise Exception("negative number: %s" % number)
	if number == 0:
		return '0'

	result = ''
	while number != 0:
		result = (DIGITS[number%BASE])+result
		number = int(number/BASE)
	return str(result)
