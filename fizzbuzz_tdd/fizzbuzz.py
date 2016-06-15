def fizz_buzz(n):
	""" returns fizz when n is divisible by 3
	returns buzz when n is divisible by 5
	returns buzz when n is divisible by both 3 and 5
	"""
	if n % 3 == 0 and n % 5 == 0:
		return 'fizzbuzz'
	elif n % 3 == 0:
		return 'fizz'
	elif n % 5 == 0:
		return 'buzz'