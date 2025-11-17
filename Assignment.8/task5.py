from datetime import datetime


def convert_date_format(date_str):
    """
    Converts a date string from "YYYY-MM-DD" format to "DD-MM-YYYY" format.
    
    Args:
        date_str (str): Date string in "YYYY-MM-DD" format
        
    Returns:
        str: Date string in "DD-MM-YYYY" format
        
    Raises:
        ValueError: If the date string is not in the correct format or is invalid
        TypeError: If the input is not a string
    """
    if not isinstance(date_str, str):
        raise TypeError(f"Date must be a string, got {type(date_str).__name__}")
    
    if not date_str:
        raise ValueError("Date string cannot be empty")
    
    # Try to parse the date to validate it
    try:
        # Parse the date to ensure it's valid
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format or date value: {date_str}. Expected format: YYYY-MM-DD")
    
    # Split the date string
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")
    
    year, month, day = parts
    
    # Return in DD-MM-YYYY format
    return f"{day}-{month}-{year}"


def test_convert_date_format():
    """Test cases for convert_date_format function"""
    
    print("Running test cases for convert_date_format function...\n")
    
    # Test cases for valid date conversions
    print("Testing valid date conversions...")
    assert convert_date_format("2023-10-15") == "15-10-2023", "Should convert 2023-10-15 to 15-10-2023"
    assert convert_date_format("2024-01-01") == "01-01-2024", "Should convert 2024-01-01 to 01-01-2024"
    assert convert_date_format("2023-12-31") == "31-12-2023", "Should convert 2023-12-31 to 31-12-2023"
    assert convert_date_format("2000-02-29") == "29-02-2000", "Should convert leap year date 2000-02-29 to 29-02-2000"
    assert convert_date_format("2024-02-29") == "29-02-2024", "Should convert leap year date 2024-02-29 to 29-02-2024"
    assert convert_date_format("2023-02-28") == "28-02-2023", "Should convert 2023-02-28 to 28-02-2023"
    print("✓ Valid date conversion tests passed")
    
    # Test cases for different months
    print("\nTesting different months...")
    assert convert_date_format("2023-01-15") == "15-01-2023", "January date should convert correctly"
    assert convert_date_format("2023-06-15") == "15-06-2023", "June date should convert correctly"
    assert convert_date_format("2023-09-15") == "15-09-2023", "September date should convert correctly"
    assert convert_date_format("2023-12-25") == "25-12-2023", "December date should convert correctly"
    print("✓ Different months tests passed")
    
    # Test cases for single-digit days and months
    print("\nTesting single-digit days and months...")
    assert convert_date_format("2023-01-05") == "05-01-2023", "Single-digit day and month should preserve leading zeros"
    assert convert_date_format("2023-05-01") == "01-05-2023", "Single-digit day should preserve leading zero"
    assert convert_date_format("2023-09-09") == "09-09-2023", "Single-digit day and month should preserve leading zeros"
    print("✓ Single-digit days and months tests passed")
    
    # Test cases for boundary dates
    print("\nTesting boundary dates...")
    assert convert_date_format("2000-01-01") == "01-01-2000", "First day of year 2000 should convert correctly"
    assert convert_date_format("1999-12-31") == "31-12-1999", "Last day of year 1999 should convert correctly"
    assert convert_date_format("2100-01-01") == "01-01-2100", "Future date should convert correctly"
    assert convert_date_format("1900-01-01") == "01-01-1900", "Past date should convert correctly"
    print("✓ Boundary dates tests passed")
    
    # Test cases for leap years
    print("\nTesting leap year dates...")
    assert convert_date_format("2020-02-29") == "29-02-2020", "Leap year 2020 should convert correctly"
    assert convert_date_format("2016-02-29") == "29-02-2016", "Leap year 2016 should convert correctly"
    assert convert_date_format("2004-02-29") == "29-02-2004", "Leap year 2004 should convert correctly"
    print("✓ Leap year dates tests passed")
    
    # Test cases for invalid format - wrong separator
    print("\nTesting invalid format - wrong separator...")
    try:
        convert_date_format("2023/10/15")
        assert False, "Should raise ValueError for wrong separator"
    except ValueError as e:
        assert "Invalid date format" in str(e) or "Expected format" in str(e), "Error message should mention format"
        print("✓ Wrong separator (/) correctly raised ValueError")
    
    try:
        convert_date_format("2023.10.15")
        assert False, "Should raise ValueError for wrong separator"
    except ValueError:
        print("✓ Wrong separator (.) correctly raised ValueError")
    
    # Test cases for invalid format - missing parts
    print("\nTesting invalid format - missing parts...")
    try:
        convert_date_format("2023-10")
        assert False, "Should raise ValueError for missing day"
    except ValueError as e:
        assert "Invalid date format" in str(e) or "Expected format" in str(e), "Error message should mention format"
        print("✓ Missing day part correctly raised ValueError")
    
    try:
        convert_date_format("2023")
        assert False, "Should raise ValueError for missing month and day"
    except ValueError:
        print("✓ Missing month and day correctly raised ValueError")
    
    # Test cases for invalid format - wrong order
    print("\nTesting invalid format - wrong order...")
    try:
        convert_date_format("15-10-2023")
        assert False, "Should raise ValueError for DD-MM-YYYY format (wrong input format)"
    except ValueError:
        print("✓ Wrong order (DD-MM-YYYY) correctly raised ValueError")
    
    try:
        convert_date_format("10-15-2023")
        assert False, "Should raise ValueError for MM-DD-YYYY format"
    except ValueError:
        print("✓ Wrong order (MM-DD-YYYY) correctly raised ValueError")
    
    # Test cases for invalid dates
    print("\nTesting invalid dates...")
    try:
        convert_date_format("2023-13-01")
        assert False, "Should raise ValueError for invalid month (13)"
    except ValueError as e:
        assert "Invalid date format" in str(e) or "Invalid date" in str(e), "Error message should mention invalid date"
        print("✓ Invalid month (13) correctly raised ValueError")
    
    try:
        convert_date_format("2023-00-01")
        assert False, "Should raise ValueError for invalid month (00)"
    except ValueError:
        print("✓ Invalid month (00) correctly raised ValueError")
    
    try:
        convert_date_format("2023-02-30")
        assert False, "Should raise ValueError for invalid day (Feb 30)"
    except ValueError:
        print("✓ Invalid day (Feb 30) correctly raised ValueError")
    
    try:
        convert_date_format("2023-04-31")
        assert False, "Should raise ValueError for invalid day (April 31)"
    except ValueError:
        print("✓ Invalid day (April 31) correctly raised ValueError")
    
    try:
        convert_date_format("2023-02-29")
        assert False, "Should raise ValueError for invalid leap day (2023 is not a leap year)"
    except ValueError:
        print("✓ Invalid leap day (2023-02-29) correctly raised ValueError")
    
    try:
        convert_date_format("2023-01-32")
        assert False, "Should raise ValueError for invalid day (32)"
    except ValueError:
        print("✓ Invalid day (32) correctly raised ValueError")
    
    try:
        convert_date_format("2023-01-00")
        assert False, "Should raise ValueError for invalid day (00)"
    except ValueError:
        print("✓ Invalid day (00) correctly raised ValueError")
    
    # Test cases for empty string
    print("\nTesting empty string...")
    try:
        convert_date_format("")
        assert False, "Should raise ValueError for empty string"
    except ValueError as e:
        assert "cannot be empty" in str(e) or "Invalid date format" in str(e), "Error message should mention empty string"
        print("✓ Empty string correctly raised ValueError")
    
    # Test cases for non-string inputs
    print("\nTesting non-string inputs...")
    try:
        convert_date_format(None)
        assert False, "Should raise TypeError for None"
    except TypeError as e:
        assert "must be a string" in str(e), "Error message should mention string type"
        print("✓ None input correctly raised TypeError")
    
    try:
        convert_date_format(20231015)
        assert False, "Should raise TypeError for integer"
    except TypeError as e:
        assert "must be a string" in str(e), "Error message should mention string type"
        print("✓ Integer input correctly raised TypeError")
    
    try:
        convert_date_format(["2023", "10", "15"])
        assert False, "Should raise TypeError for list"
    except TypeError:
        print("✓ List input correctly raised TypeError")
    
    try:
        convert_date_format({"date": "2023-10-15"})
        assert False, "Should raise TypeError for dictionary"
    except TypeError:
        print("✓ Dictionary input correctly raised TypeError")
    
    # Test cases for malformed strings
    print("\nTesting malformed strings...")
    try:
        convert_date_format("2023-10-15-extra")
        assert False, "Should raise ValueError for extra parts"
    except ValueError:
        print("✓ Extra parts correctly raised ValueError")
    
    try:
        convert_date_format("2023-10")
        assert False, "Should raise ValueError for incomplete date"
    except ValueError:
        print("✓ Incomplete date correctly raised ValueError")
    
    try:
        convert_date_format("abc-def-ghi")
        assert False, "Should raise ValueError for non-numeric date"
    except ValueError:
        print("✓ Non-numeric date correctly raised ValueError")
    
    try:
        convert_date_format("23-10-15")
        assert False, "Should raise ValueError for 2-digit year"
    except ValueError:
        print("✓ 2-digit year correctly raised ValueError")
    
    print("\n" + "="*50)
    print("All test cases passed successfully! ✓")
    print("="*50)


def main():
    """Main function to get date input from keyboard and convert it"""
    print("="*60)
    print("Date Format Converter: YYYY-MM-DD to DD-MM-YYYY")
    print("="*60)
    print("\nEnter dates in YYYY-MM-DD format (e.g., 2023-10-15)")
    print("Type 'test' to run test cases, 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            # Get input from keyboard
            date_input = input("Enter a date (YYYY-MM-DD): ").strip()
            
            # Check for exit commands
            if date_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Date Format Converter!")
                break
            
            # Check for test command
            if date_input.lower() == 'test':
                print("\n" + "="*60)
                test_convert_date_format()
                print("="*60 + "\n")
                continue
            
            # Skip empty input
            if not date_input:
                print("Please enter a valid date.\n")
                continue
            
            # Convert the date
            converted_date = convert_date_format(date_input)
            print(f"Converted: {date_input} → {converted_date}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except TypeError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}\n")


if __name__ == "__main__":
    # Uncomment the line below to run interactive mode (keyboard input)
    main()
    
    # Uncomment the line below to run test cases only
    # test_convert_date_format()

