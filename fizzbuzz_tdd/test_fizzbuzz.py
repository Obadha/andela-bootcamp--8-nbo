import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase): #test case is inside unittest
	"""Testing the 
	fizzbuzz """

	def test_divisibility_by_three(self): #all tests have to start with test_
		"""Test will return Fizz if input is ndivisible by
		3"""
		self.assertEqual(fizzbuzz.fizz_buzz(3),"fizz")

	def test_divisibility_by_five(self): 
		"""Test will return Fizz if input is divisible by
		3"""
		self.assertEqual(fizzbuzz.fizz_buzz(5),"buzz")






# docstring can be called. 