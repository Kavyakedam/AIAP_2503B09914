"""Utilities for finding the largest element in a list.

This file provides two small helpers:
- `find_largest` — an explicit O(n) scan that works with any iterable of
  comparable items and gives clear error messages for empty/invalid inputs.
- `find_largest_builtin` — thin wrapper around Python's built-in `max`
  (concise, also O(n)).

Both functions raise ValueError on empty input (matching `max`), and
TypeError for non-iterable/None inputs.

Complexity: O(n) time, O(1) extra space for the loop version.
"""

from typing import Iterable, TypeVar

T = TypeVar("T")


def find_largest(items: Iterable[T]) -> T:
	"""Return the largest element from `items`.

	This uses a simple linear scan so it works for any iterable and
	runs in O(n) time with O(1) extra space.

	Raises:
		TypeError: if `items` is None or not iterable.
		ValueError: if `items` is empty.
	"""
	if items is None:
		raise TypeError("find_largest() expects an iterable, got None")

	# Use an iterator so we can support any iterable (not just sequences)
	it = iter(items)
	try:
		max_val = next(it)
	except StopIteration:
		raise ValueError("find_largest() arg is an empty iterable")

	for x in it:
		# relies on the elements being mutually comparable via '>'
		if x > max_val:
			max_val = x

	return max_val


def find_largest_builtin(items: Iterable[T]) -> T:
	"""Return the largest element using Python's built-in `max`.

	This is the concise, idiomatic approach; `max` already raises
	TypeError/ValueError for invalid/empty inputs so we don't duplicate
	those checks here.
	"""
	return max(items)


if __name__ == "__main__":
	# Quick self-tests (happy path + edge cases)
	tests = [
		([3, 1, 4, 1, 5, 9], 9),
		((-10, -20, -3, -4), -3),
		([7], 7),
		([1.5, 2.5, 2.499], 2.5),
	]

	for data, expected in tests:
		assert find_largest(data) == expected, f"find_largest failed for {data}"
		assert find_largest_builtin(data) == expected, f"builtin max failed for {data}"

	# empty iterable should raise ValueError
	try:
		find_largest([])
	except ValueError:
		pass
	else:
		raise AssertionError("find_largest([]) should raise ValueError")

	try:
		find_largest_builtin([])
	except ValueError:
		pass
	else:
		raise AssertionError("find_largest_builtin([]) should raise ValueError")

	print("All quick tests passed for find_largest implementations")

	# Interactive prompt: read a line of numbers from keyboard and show the largest.
	# The prompt accepts numbers separated by spaces and/or commas (e.g. "1 2 3" or "1,2,3").
	import re
	import sys


	def parse_number_list(s: str):
		"""Parse a string of numbers separated by spaces or commas into a list of numbers.

		Integers are returned as int when possible; otherwise floats are used.
		Raises ValueError for empty input or invalid tokens.
		"""
		if not s or not s.strip():
			raise ValueError("no input provided")

		tokens = re.split(r"[\s,]+", s.strip())
		nums = []
		for tok in tokens:
			if not tok:
				continue
			# try integer first
			if re.fullmatch(r"[+-]?\d+", tok):
				nums.append(int(tok))
				continue
			# otherwise try float
			try:
				nums.append(float(tok))
			except ValueError:
				raise ValueError(f"invalid number token: {tok!r}")

		if not nums:
			raise ValueError("no numeric tokens found")
		return nums


	def interactive_find_largest():
		"""Prompt the user once for a list of numbers and print the largest."""
		try:
			prompt = "Enter numbers separated by spaces or commas (empty to skip): "
			# Use input() which works in console; catch EOFError for non-interactive runs
			line = input(prompt)
		except EOFError:
			print("No interactive input available; skipping interactive demo")
			return

		if not line.strip():
			print("No numbers entered; skipping")
			return

		try:
			numbers = parse_number_list(line)
		except ValueError as exc:
			print(f"Could not parse numbers: {exc}", file=sys.stderr)
			return

		largest = find_largest(numbers)
		print(f"Largest value: {largest!r}")


	# Only run interactive prompt when the script is executed directly from a terminal
	# (prevents blocking when the module is imported).
	try:
		if sys.stdin and sys.stdin.isatty():
			interactive_find_largest()
		else:
			# Non-interactive environment (e.g. tests); skip prompt.
			pass
	except Exception:
		# Be tolerant: don't crash the script if the environment doesn't support tty checks.
		try:
			interactive_find_largest()
		except Exception:
			pass


