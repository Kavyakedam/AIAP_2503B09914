import re


def is_sentence_palindrome(sentence):
    """
    Checks if a sentence is a palindrome, ignoring case, punctuation, and spaces.
    
    Args:
        sentence (str): The sentence to check
        
    Returns:
        bool: True if the sentence is a palindrome (ignoring case, punctuation, spaces), False otherwise
    """
    if not sentence or not isinstance(sentence, str):
        return False
    
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence.lower())
    
    # Check if cleaned string is empty or a palindrome
    if not cleaned:
        return False
    
    return cleaned == cleaned[::-1]


def test_is_sentence_palindrome():
    """Test cases for is_sentence_palindrome function - Takes input from keyboard"""
    
    print("="*60)
    print("Test Cases for is_sentence_palindrome()")
    print("="*60)
    print("Enter test cases from keyboard.")
    print("Enter a sentence and (optionally) expected result (True/False)")
    print("Type 'quit' or 'exit' to stop entering test cases\n")
    
    test_count = 0
    passed_count = 0
    failed_count = 0
    
    while True:
        print("-" * 60)
        # Get sentence input
        sentence = input("Enter sentence (or 'quit' to exit): ").strip()
        
        if sentence.lower() in ['quit', 'exit', 'q']:
            break
        
        if not sentence:
            print("Please enter a valid sentence.")
            continue
        
        # Get expected result (optional)
        expected_input = input("Enter expected result (True/False, or press Enter to skip): ").strip().lower()
        expected = None
        if expected_input:
            if expected_input in ['true', 't', '1']:
                expected = True
            elif expected_input in ['false', 'f', '0']:
                expected = False
            else:
                print(f"Warning: Invalid expected result '{expected_input}'. Will only show actual result.")
        
        # Test the function
        result = is_sentence_palindrome(sentence)
        test_count += 1
        
        # Display result
        print(f"\nTest Case #{test_count}:")
        print(f"  Input: \"{sentence}\"")
        print(f"  Result: {result}")
        
        if expected is not None:
            status = "✓ PASS" if result == expected else "✗ FAIL"
            print(f"  Expected: {expected}")
            print(f"  Status: {status}")
            if result == expected:
                passed_count += 1
            else:
                failed_count += 1
        else:
            print(f"  Status: Tested (no expected result provided)")
        
        # Show cleaned version for debugging
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence.lower())
        print(f"  Cleaned (ignoring case, spaces, punctuation): \"{cleaned}\"")
        print()
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"Total test cases: {test_count}")
    if passed_count + failed_count > 0:
        print(f"Passed: {passed_count}")
        print(f"Failed: {failed_count}")
    print("="*60)


if __name__ == "__main__":
    test_is_sentence_palindrome()

