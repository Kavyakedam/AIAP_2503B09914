def is_leap_year(year: int) -> bool:
	"""Return True if `year` is a leap year under the Gregorian rules.

	Rules:
	- Years divisible by 4 are leap years,
	- except years divisible by 100 are not leap years,
	- except years divisible by 400 are leap years.
	"""
	if year % 4 != 0:
		return False
	if year % 100 != 0:
		return True
	return year % 400 == 0


if __name__ == "__main__":
	# Prompt the user for a year, validate input, and print the result.
	try:
		s = input("Enter a year: ").strip()
		year = int(s)
	except ValueError:
		print("Invalid input: please enter an integer year.")
		raise SystemExit(1)

	if is_leap_year(year):
		print(f"{year} is a leap year")
	else:
		print(f"{year} is not a leap year")

