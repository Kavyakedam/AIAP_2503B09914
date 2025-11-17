"""
Small utility: is_prime() implementation and quick tests.
s
This file provides a compact, efficient primality check using the
6k ± 1 optimization and integer square root from the standard library.
"""
from math import isqrt

def is_prime(n: int) -> bool:
	"""Return True if n is a prime number, otherwise False.

	Implementation notes:
	- Accepts only integers (raises TypeError for other types).
	- Numbers < 2 are not prime.
	- Uses simple checks for small primes and divisibility by 2 and 3,
	  then tests potential divisors of the form 6k-1 and 6k+1 up to sqrt(n).

	Examples:
	>>> is_prime(2)
	True
	>>> is_prime(15)
	False
	>>> is_prime(17)
	True
	"""
	if not isinstance(n, int):
		raise TypeError("is_prime() only accepts integers")

	if n < 2:
		return False
	if n in (2, 3):
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False

	limit = isqrt(n)
	i = 5
	while i <= limit:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True


if __name__ == "__main__":
	# Quick self-checks (happy path + a few edge cases)
	test_cases = [
		(0, False),
		(1, False),
		(2, True),
		(3, True),
		(4, False),
		(17, True),
		(18, False),
		(19, True),
		(7919, True),  # known prime
		(7920, False),
		(-7, False),
	]

	for n, expected in test_cases:
		assert is_prime(n) == expected, f"is_prime({n}) should be {expected}"

	print("Sample primes up to 30:", [p for p in range(2, 31) if is_prime(p)])
	print("All tests passed")

