def convert_cm_to_inches(cm: float) -> float:
	"""Convert centimeters to inches.

	Args:
		cm: Length in centimeters.

	Returns:
		Length in inches.
	"""
	return cm / 2.54


# One-shot example to guide an AI writing this function:
# Input: 10 (cm)
# Output: 10 / 2.54 = 3.937007874015748 (inches)


if __name__ == "__main__":
	example_cm = 10
	example_inches = convert_cm_to_inches(example_cm)
	print(f"Input: {example_cm} (cm)")
	print(f"Output: {example_inches} (inches)")

