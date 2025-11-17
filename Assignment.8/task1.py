import re


def is_valid_email(email):
    """
    Validates an email address based on the following requirements:
    - Must contain @ and . characters
    - Must not start or end with special characters
    - Should not allow multiple @
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    # Check if email contains @ and . characters
    if '@' not in email or '.' not in email:
        return False
    
    # Check for multiple @ characters
    if email.count('@') != 1:
        return False
    
    # Check that email does not start or end with special characters
    # Special characters include: @, ., -, _, +, and other non-alphanumeric characters
    # Allow alphanumeric characters (letters and numbers) at start and end
    if not email[0].isalnum() or not email[-1].isalnum():
        return False
    
    return True


# Test cases
def test_is_valid_email():
    """Test cases for is_valid_email function"""
    
    # Valid email addresses
    assert is_valid_email("user@example.com") == True, "Valid email should return True"
    assert is_valid_email("test123@domain.co.uk") == True, "Valid email with numbers should return True"
    assert is_valid_email("john.doe@example.com") == True, "Valid email with dot should return True"
    assert is_valid_email("user_name@example.com") == True, "Valid email with underscore should return True"
    assert is_valid_email("user-name@example.com") == True, "Valid email with hyphen should return True"
    assert is_valid_email("user+tag@example.com") == True, "Valid email with plus should return True"
    assert is_valid_email("a@b.co") == True, "Short valid email should return True"
    
    # Invalid: Missing @
    assert is_valid_email("userexample.com") == False, "Email without @ should return False"
    
    # Invalid: Missing .
    assert is_valid_email("user@examplecom") == False, "Email without . should return False"
    
    # Invalid: Multiple @
    assert is_valid_email("user@@example.com") == False, "Email with multiple @ should return False"
    assert is_valid_email("user@exam@ple.com") == False, "Email with multiple @ should return False"
    
    # Invalid: Starts with special character
    assert is_valid_email("@example.com") == False, "Email starting with @ should return False"
    assert is_valid_email(".user@example.com") == False, "Email starting with . should return False"
    assert is_valid_email("-user@example.com") == False, "Email starting with - should return False"
    assert is_valid_email("_user@example.com") == False, "Email starting with _ should return False"
    assert is_valid_email("+user@example.com") == False, "Email starting with + should return False"
    
    # Invalid: Ends with special character
    assert is_valid_email("user@example.com@") == False, "Email ending with @ should return False"
    assert is_valid_email("user@example.com.") == False, "Email ending with . should return False"
    assert is_valid_email("user@example.com-") == False, "Email ending with - should return False"
    assert is_valid_email("user@example.com_") == False, "Email ending with _ should return False"
    assert is_valid_email("user@example.com+") == False, "Email ending with + should return False"
    
    # Invalid: Edge cases
    assert is_valid_email("") == False, "Empty string should return False"
    assert is_valid_email(None) == False, "None should return False"
    assert is_valid_email("@.") == False, "Only @ and . should return False"
    assert is_valid_email("a@.") == False, "Missing domain should return False"
    assert is_valid_email("@a.com") == False, "Missing local part should return False"
    assert is_valid_email("a@b") == False, "Missing . in domain should return False"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_valid_email()

