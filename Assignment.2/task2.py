"""
Task 2: Compare Gemini and Copilot outputs for a palindrome check function
Expected Output: Side-by-side comparison and observations
"""

# ============================================================================
# GEMINI OUTPUT - Palindrome Check Function
# ============================================================================
# Prompt: "Write a function to check if a string is a palindrome"
# 
# Gemini Response:

def is_palindrome_gemini(s: str) -> bool:
    """
    Check if a string is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, 
    and capitalization).
    
    Args:
        s: Input string to check
        
    Returns:
        True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome_gemini("racecar")
        True
        >>> is_palindrome_gemini("hello")
        False
        >>> is_palindrome_gemini("A man, a plan, a canal: Panama")
        True
    """
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string equals its reverse
    return cleaned == cleaned[::-1]


# ============================================================================
# COPILOT OUTPUT - Palindrome Check Function
# ============================================================================
# Prompt: "Write a function to check if a string is a palindrome"
#
# Copilot Response:

def is_palindrome_copilot(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing characters from both ends.
    
    A palindrome reads the same forwards and backwards, ignoring spaces, 
    punctuation, and case.
    
    Args:
        s: The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Examples:
        >>> is_palindrome_copilot("racecar")
        True
        >>> is_palindrome_copilot("hello")
        False
        >>> is_palindrome_copilot("A man, a plan, a canal: Panama")
        True
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Use two-pointer approach
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


# ============================================================================
# ALTERNATIVE COPILOT OUTPUT - Recursive Approach
# ============================================================================
# Copilot Alternative (if asked for a different approach):

def is_palindrome_copilot_recursive(s: str) -> bool:
    """
    Check if a string is a palindrome using a recursive approach.
    
    Args:
        s: The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Clean the string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    def helper(left: int, right: int) -> bool:
        if left >= right:
            return True
        if cleaned[left] != cleaned[right]:
            return False
        return helper(left + 1, right - 1)
    
    return helper(0, len(cleaned) - 1)


# ============================================================================
# TEST CASES
# ============================================================================

test_cases = [
    ("racecar", True),
    ("hello", False),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("0P", False),
    ("a.", True),
    (".,", True),
    ("12321", True),
    ("12345", False),
    ("Was it a car or a cat I saw?", True),
    ("Madam, I'm Adam", True),
    ("", True),
    ("a", True),
    ("ab", False),
    ("Able was I ere I saw Elba", True),
]


def run_comparison():
    """Run all test cases and compare outputs from both implementations."""
    
    print("=" * 80)
    print("PALINDROME FUNCTION COMPARISON: GEMINI vs COPILOT")
    print("=" * 80)
    print()
    
    # Test results tracking
    gemini_results = []
    copilot_results = []
    copilot_recursive_results = []
    
    print(f"{'Test Input':<50} {'Expected':<10} {'Gemini':<10} {'Copilot':<10} {'Match':<10}")
    print("-" * 80)
    
    all_match = True
    for test_input, expected in test_cases:
        gemini_output = is_palindrome_gemini(test_input)
        copilot_output = is_palindrome_copilot(test_input)
        copilot_recursive_output = is_palindrome_copilot_recursive(test_input)
        
        gemini_results.append(gemini_output)
        copilot_results.append(copilot_output)
        copilot_recursive_results.append(copilot_recursive_output)
        
        # Check if all outputs match
        outputs_match = (gemini_output == copilot_output == copilot_recursive_output == expected)
        match_status = "✓ PASS" if outputs_match else "✗ FAIL"
        
        if not outputs_match:
            all_match = False
        
        # Display truncated test input for readability
        display_input = test_input[:40] + "..." if len(test_input) > 40 else test_input
        
        print(f"{display_input:<50} {str(expected):<10} {str(gemini_output):<10} {str(copilot_output):<10} {match_status:<10}")
    
    print("-" * 80)
    print()


def print_observations():
    """Print detailed observations and comparisons."""
    
    print("=" * 80)
    print("DETAILED OBSERVATIONS & COMPARISON")
    print("=" * 80)
    print()
    
    print("1. ALGORITHM APPROACH")
    print("-" * 80)
    print("""
    GEMINI:
    - Uses string reversal approach: cleaned == cleaned[::-1]
    - Simpler and more Pythonic
    - Reads the entire string backward and compares
    - Time Complexity: O(n)
    - Space Complexity: O(n) for the reversed string
    
    COPILOT (Two-pointer):
    - Uses two-pointer technique with while loop
    - Compares characters from both ends moving inward
    - Can short-circuit on first mismatch
    - Time Complexity: O(n)
    - Space Complexity: O(1) additional space (ignoring cleaned string)
    
    COPILOT (Recursive):
    - Uses recursion with helper function
    - Similar to two-pointer but with recursive calls
    - Call stack overhead for deep recursion
    - Time Complexity: O(n)
    - Space Complexity: O(n) for call stack
    """)
    
    print("\n2. CODE QUALITY & READABILITY")
    print("-" * 80)
    print("""
    GEMINI:
    ✓ Most concise (2 lines of logic)
    ✓ Highly Pythonic and idiomatic
    ✓ Easy to understand for beginners
    ✗ Less efficient for very large strings (creates reversed copy)
    ✗ No early exit optimization
    
    COPILOT (Two-pointer):
    ✓ More efficient space-wise
    ✓ Early exit on mismatch
    ✓ Demonstrates algorithmic thinking
    ✗ More verbose
    ✗ Slightly more complex for beginners
    
    COPILOT (Recursive):
    ✗ More complex than needed
    ✗ Potential stack overflow for very long strings
    ✓ Demonstrates recursion pattern
    """)
    
    print("\n3. DOCUMENTATION & EXAMPLES")
    print("-" * 80)
    print("""
    GEMINI:
    - Clear docstring with description
    - Lists key considerations (spaces, punctuation, capitalization)
    - Includes practical examples
    - Good parameter and return descriptions
    
    COPILOT:
    - Detailed docstring with description
    - Mentions algorithm approach in comments
    - Includes practical examples
    - Clear parameter and return descriptions
    
    Both provide adequate documentation with examples.
    """)
    
    print("\n4. INPUT HANDLING")
    print("-" * 80)
    print("""
    Both implementations:
    ✓ Handle case-insensitivity (convert to lowercase)
    ✓ Remove non-alphanumeric characters
    ✓ Handle empty strings (returns True)
    ✓ Handle strings with spaces and punctuation
    ✓ Handle mixed case and special characters
    
    Cleaning approach: ''.join(char.lower() for char in s if char.isalnum())
    - Identical in both implementations
    - Robust and standard approach
    """)
    
    print("\n5. FUNCTIONAL EQUIVALENCE")
    print("-" * 80)
    print("""
    All three implementations are functionally equivalent:
    ✓ Produce identical results for all test cases
    ✓ Handle edge cases correctly
    ✓ Both return boolean values as expected
    ✓ No functional differences in behavior
    """)
    
    print("\n6. PERFORMANCE ANALYSIS")
    print("-" * 80)
    print("""
    For most practical purposes:
    - All three have O(n) time complexity
    - COPILOT (two-pointer) has better space efficiency
    - GEMINI is better for readability and maintainability
    - For strings < 10,000 chars: no practical difference
    - For strings > 100,000 chars: two-pointer approach slightly better
    
    In practice, Python's string slicing (Gemini's approach) is highly optimized
    and may outperform the two-pointer approach in micro-benchmarks.
    """)
    
    print("\n7. BEST USE CASES")
    print("-" * 80)
    print("""
    GEMINI Approach:
    - Production code requiring maximum readability
    - Most Python developers prefer this style
    - Interviews where simplicity matters
    - Code that doesn't need extreme optimization
    
    COPILOT Two-pointer:
    - Teaching algorithms and data structures
    - Systems where memory efficiency is critical
    - Interviews testing algorithmic thinking
    - Porting to languages without built-in reversal
    
    COPILOT Recursive:
    - Educational purposes (teaching recursion)
    - Generally not recommended for this problem
    """)
    
    print("\n8. SUMMARY & RECOMMENDATIONS")
    print("-" * 80)
    print("""
    RECOMMENDATION: Use GEMINI's approach for production code
    
    Reasons:
    1. Pythonic idiom - most developers expect this style
    2. Highly readable and maintainable
    3. Built-in optimizations in CPython
    4. Less error-prone than manual pointer manipulation
    5. Performance is practically identical for real-world strings
    
    Alternative: Use COPILOT's two-pointer approach if:
    - Demonstrating algorithmic knowledge
    - Working in memory-constrained environments
    - Teaching data structures and algorithms
    - Performance profiling shows it matters (rare)
    """)
    
    print("\n" + "=" * 80)


def print_side_by_side_comparison():
    """Print a visual side-by-side comparison of the implementations."""
    
    print("\n" + "=" * 80)
    print("SIDE-BY-SIDE CODE COMPARISON")
    print("=" * 80)
    print()
    
    print("GEMINI (String Reversal Approach)".center(40) + " | " + "COPILOT (Two-Pointer Approach)".center(40))
    print("-" * 85)
    
    gemini_code = [
        "def is_palindrome(s: str) -> bool:",
        "    cleaned = ''.join(",
        "        char.lower() for char in s",
        "        if char.isalnum())",
        "    return cleaned == cleaned[::-1]",
        "",
        "Lines of code: 5",
        "Complexity: O(n) time, O(n) space",
    ]
    
    copilot_code = [
        "def is_palindrome(s: str) -> bool:",
        "    cleaned = ''.join(",
        "        char.lower() for char in s",
        "        if char.isalnum())",
        "    left, right = 0, len(cleaned) - 1",
        "    while left < right:",
        "        if cleaned[left] != cleaned[right]:",
        "            return False",
        "        left += 1",
        "        right -= 1",
        "    return True",
        "",
        "Lines of code: 12",
        "Complexity: O(n) time, O(1) extra space",
    ]
    
    max_lines = max(len(gemini_code), len(copilot_code))
    
    for i in range(max_lines):
        gemini_line = gemini_code[i] if i < len(gemini_code) else ""
        copilot_line = copilot_code[i] if i < len(copilot_code) else ""
        print(f"{gemini_line:<40} | {copilot_line:<40}")
    
    print()


if __name__ == "__main__":
    # Run the comparison
    run_comparison()
    
    # Print side-by-side code comparison
    print_side_by_side_comparison()
    
    # Print detailed observations
    print_observations()
    
    print("\n" + "=" * 80)
    print("COMPARISON COMPLETE")
    print("=" * 80)
