# Function to reverse a string
def reverse_string(s: str) -> str:
	"""
	Reverses the input string and returns it.

	This function was generated in a Copilot-style suggestion. It handles None
	by returning an empty string and preserves empty-string behavior.
	"""
	if s is None:
		return ""
	# Use Python slicing to reverse the string (concise and fast)
	return s[::-1]


if __name__ == "__main__":
	# Quick demo / self-test
	examples = ["hello", "", "A", None]
	for ex in examples:
		print(f"Input: {ex!r} -> Reversed: {reverse_string(ex)!r}")

