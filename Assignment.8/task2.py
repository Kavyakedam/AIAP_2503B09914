def assign_grade(score):
    """
    Assigns a letter grade based on the numerical score.
    
    Grade ranges:
    - 90-100: A
    - 80-89: B
    - 70-79: C
    - 60-69: D
    - <60: F
    
    Args:
        score (int/float): The numerical score (0-100)
        
    Returns:
        str: The letter grade (A, B, C, D, or F)
        
    Raises:
        ValueError: If score is outside valid range (0-100) or invalid type
        TypeError: If score is not a numeric type
    """
    # Check if score is boolean (explicitly exclude since bool is a subclass of int)
    if isinstance(score, bool):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    
    # Check if score is numeric
    if not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    
    # Check if score is within valid range
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    
    # Assign grade based on score ranges
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def test_assign_grade():
    """Test cases for assign_grade function"""
    
    print("Running test cases for assign_grade function...\n")
    
    # Test cases for Grade A (90-100)
    print("Testing Grade A range (90-100)...")
    assert assign_grade(100) == "A", "Score 100 should return A"
    assert assign_grade(95) == "A", "Score 95 should return A"
    assert assign_grade(90) == "A", "Score 90 (boundary) should return A"
    assert assign_grade(90.5) == "A", "Score 90.5 should return A"
    print("✓ Grade A tests passed")
    
    # Test cases for Grade B (80-89)
    print("\nTesting Grade B range (80-89)...")
    assert assign_grade(89) == "B", "Score 89 (boundary) should return B"
    assert assign_grade(89.9) == "B", "Score 89.9 should return B"
    assert assign_grade(85) == "B", "Score 85 should return B"
    assert assign_grade(80) == "B", "Score 80 (boundary) should return B"
    assert assign_grade(80.1) == "B", "Score 80.1 should return B"
    print("✓ Grade B tests passed")
    
    # Test cases for Grade C (70-79)
    print("\nTesting Grade C range (70-79)...")
    assert assign_grade(79) == "C", "Score 79 (boundary) should return C"
    assert assign_grade(79.9) == "C", "Score 79.9 should return C"
    assert assign_grade(75) == "C", "Score 75 should return C"
    assert assign_grade(70) == "C", "Score 70 (boundary) should return C"
    assert assign_grade(70.1) == "C", "Score 70.1 should return C"
    print("✓ Grade C tests passed")
    
    # Test cases for Grade D (60-69)
    print("\nTesting Grade D range (60-69)...")
    assert assign_grade(69) == "D", "Score 69 (boundary) should return D"
    assert assign_grade(69.9) == "D", "Score 69.9 should return D"
    assert assign_grade(65) == "D", "Score 65 should return D"
    assert assign_grade(60) == "D", "Score 60 (boundary) should return D"
    assert assign_grade(60.1) == "D", "Score 60.1 should return D"
    print("✓ Grade D tests passed")
    
    # Test cases for Grade F (<60)
    print("\nTesting Grade F range (<60)...")
    assert assign_grade(59) == "F", "Score 59 (boundary) should return F"
    assert assign_grade(59.9) == "F", "Score 59.9 should return F"
    assert assign_grade(50) == "F", "Score 50 should return F"
    assert assign_grade(0) == "F", "Score 0 (boundary) should return F"
    assert assign_grade(30) == "F", "Score 30 should return F"
    print("✓ Grade F tests passed")
    
    # Test cases for boundary values
    print("\nTesting critical boundary values...")
    assert assign_grade(90) == "A", "Boundary 90 should be A"
    assert assign_grade(89.999) == "B", "Boundary 89.999 should be B"
    assert assign_grade(80) == "B", "Boundary 80 should be B"
    assert assign_grade(79.999) == "C", "Boundary 79.999 should be C"
    assert assign_grade(70) == "C", "Boundary 70 should be C"
    assert assign_grade(69.999) == "D", "Boundary 69.999 should be D"
    assert assign_grade(60) == "D", "Boundary 60 should be D"
    assert assign_grade(59.999) == "F", "Boundary 59.999 should be F"
    print("✓ Boundary value tests passed")
    
    # Test cases for invalid inputs - Negative numbers
    print("\nTesting invalid inputs - Negative numbers...")
    try:
        assign_grade(-5)
        assert False, "Should raise ValueError for negative score"
    except ValueError as e:
        assert "Score must be between 0 and 100" in str(e), "Error message should mention valid range"
        print("✓ Negative score (-5) correctly raised ValueError")
    
    try:
        assign_grade(-1)
        assert False, "Should raise ValueError for negative score"
    except ValueError:
        print("✓ Negative score (-1) correctly raised ValueError")
    
    # Test cases for invalid inputs - Scores over 100
    print("\nTesting invalid inputs - Scores over 100...")
    try:
        assign_grade(105)
        assert False, "Should raise ValueError for score > 100"
    except ValueError as e:
        assert "Score must be between 0 and 100" in str(e), "Error message should mention valid range"
        print("✓ Score > 100 (105) correctly raised ValueError")
    
    try:
        assign_grade(100.1)
        assert False, "Should raise ValueError for score > 100"
    except ValueError:
        print("✓ Score > 100 (100.1) correctly raised ValueError")
    
    try:
        assign_grade(150)
        assert False, "Should raise ValueError for score > 100"
    except ValueError:
        print("✓ Score > 100 (150) correctly raised ValueError")
    
    # Test cases for invalid inputs - Non-numeric types
    print("\nTesting invalid inputs - Non-numeric types...")
    try:
        assign_grade("eighty")
        assert False, "Should raise TypeError for string input"
    except TypeError as e:
        assert "Score must be a number" in str(e), "Error message should mention numeric type"
        print("✓ String input ('eighty') correctly raised TypeError")
    
    try:
        assign_grade("85")
        assert False, "Should raise TypeError for string numeric input"
    except TypeError:
        print("✓ String numeric input ('85') correctly raised TypeError")
    
    try:
        assign_grade(None)
        assert False, "Should raise TypeError for None input"
    except TypeError:
        print("✓ None input correctly raised TypeError")
    
    try:
        assign_grade([85])
        assert False, "Should raise TypeError for list input"
    except TypeError:
        print("✓ List input correctly raised TypeError")
    
    try:
        assign_grade({"score": 85})
        assert False, "Should raise TypeError for dict input"
    except TypeError:
        print("✓ Dictionary input correctly raised TypeError")
    
    try:
        assign_grade(True)
        assert False, "Should raise TypeError for boolean input"
    except TypeError:
        print("✓ Boolean input correctly raised TypeError")
    
    print("\n" + "="*50)
    print("All test cases passed successfully! ✓")
    print("="*50)


if __name__ == "__main__":
    test_assign_grade()

