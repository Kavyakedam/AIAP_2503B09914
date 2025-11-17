"""
Age Group Classification System
Demonstrates various conditional statements including nested if-else, elif, match-case, and ternary operators.
"""


# ============================================================================
# METHOD 1: NESTED IF-ELSE CONDITIONALS
# ============================================================================
def classify_age_nested_if_else(age):
    """
    Classify age groups using nested if-else conditionals.
    
    Explanation:
    - Nested if-else means having if-else statements inside other if-else blocks
    - This allows for hierarchical decision-making
    - Each level of nesting checks a more specific condition
    
    Args:
        age (int): The age to classify
        
    Returns:
        str: Age group classification
    """
    if age >= 0:
        if age < 13:
            return "Child"
        else:
            if age < 18:
                return "Teenager"
            else:
                if age < 65:
                    if age < 30:
                        return "Young Adult"
                    else:
                        if age < 50:
                            return "Adult"
                        else:
                            return "Middle-aged Adult"
                else:
                    if age < 80:
                        return "Senior"
                    else:
                        return "Elderly"
    else:
        return "Invalid Age"


# ============================================================================
# METHOD 2: ELIF CHAIN (MORE READABLE ALTERNATIVE)
# ============================================================================
def classify_age_elif(age):
    """
    Classify age groups using elif (else-if) chain.
    
    Explanation:
    - elif is a cleaner alternative to nested if-else
    - It checks conditions sequentially until one is true
    - More readable and easier to maintain than deeply nested structures
    - Only the first matching condition is executed
    
    Args:
        age (int): The age to classify
        
    Returns:
        str: Age group classification
    """
    if age < 0:
        return "Invalid Age"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 30:
        return "Young Adult"
    elif age < 50:
        return "Adult"
    elif age < 65:
        return "Middle-aged Adult"
    elif age < 80:
        return "Senior"
    else:
        return "Elderly"


# ============================================================================
# METHOD 3: MATCH-CASE STATEMENT (Python 3.10+)
# ============================================================================
def classify_age_match_case(age):
    """
    Classify age groups using match-case statement (Python 3.10+).
    
    Explanation:
    - match-case is similar to switch-case in other languages
    - Uses pattern matching for cleaner code
    - Can match ranges using guards (if conditions)
    - More modern and Pythonic approach
    
    Args:
        age (int): The age to classify
        
    Returns:
        str: Age group classification
    """
    if age < 0:
        return "Invalid Age"
    
    # Match-case with range guards
    match age:
        case n if n < 13:
            return "Child"
        case n if n < 18:
            return "Teenager"
        case n if n < 30:
            return "Young Adult"
        case n if n < 50:
            return "Adult"
        case n if n < 65:
            return "Middle-aged Adult"
        case n if n < 80:
            return "Senior"
        case _:  # Default case (catch-all)
            return "Elderly"


# ============================================================================
# METHOD 4: TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ============================================================================
def classify_age_ternary(age):
    """
    Classify age groups using nested ternary operators.
    
    Explanation:
    - Ternary operator: value_if_true if condition else value_if_false
    - Allows inline conditional expressions
    - Can be nested for multiple conditions
    - More compact but can become hard to read if over-nested
    
    Args:
        age (int): The age to classify
        
    Returns:
        str: Age group classification
    """
    return ("Invalid Age" if age < 0 else
            "Child" if age < 13 else
            "Teenager" if age < 18 else
            "Young Adult" if age < 30 else
            "Adult" if age < 50 else
            "Middle-aged Adult" if age < 65 else
            "Senior" if age < 80 else
            "Elderly")


# ============================================================================
# METHOD 5: LOGICAL OPERATORS (AND, OR, NOT)
# ============================================================================
def classify_age_logical_operators(age):
    """
    Classify age groups using logical operators (and, or, not).
    
    Explanation:
    - Logical operators combine multiple conditions
    - 'and': both conditions must be true
    - 'or': at least one condition must be true
    - 'not': negates a condition
    - Useful for checking ranges and complex conditions
    
    Args:
        age (int): The age to classify
        
    Returns:
        str: Age group classification
    """
    if age < 0:
        return "Invalid Age"
    elif age >= 0 and age < 13:
        return "Child"
    elif age >= 13 and age < 18:
        return "Teenager"
    elif age >= 18 and age < 30:
        return "Young Adult"
    elif age >= 30 and age < 50:
        return "Adult"
    elif age >= 50 and age < 65:
        return "Middle-aged Adult"
    elif age >= 65 and age < 80:
        return "Senior"
    else:  # age >= 80
        return "Elderly"


# ============================================================================
# METHOD 6: DICTIONARY-BASED CLASSIFICATION
# ============================================================================
def classify_age_dictionary(age):
    """
    Classify age groups using dictionary with lambda functions.
    
    Explanation:
    - Uses dictionary to map conditions to results
    - Lambda functions create anonymous functions for conditions
    - More functional programming style
    - Can be extended easily by adding new entries
    
    Args:
        age (int): The age to classify
        
    Returns:
        str: Age group classification
    """
    if age < 0:
        return "Invalid Age"
    
    age_classifiers = {
        lambda a: a < 13: "Child",
        lambda a: a < 18: "Teenager",
        lambda a: a < 30: "Young Adult",
        lambda a: a < 50: "Adult",
        lambda a: a < 65: "Middle-aged Adult",
        lambda a: a < 80: "Senior",
        lambda a: a >= 80: "Elderly"
    }
    
    for condition, classification in age_classifiers.items():
        if condition(age):
            return classification
    
    return "Unknown"


# ============================================================================
# METHOD 7: COMPLEX NESTED CONDITIONS WITH MULTIPLE CRITERIA
# ============================================================================
def classify_age_detailed(age, has_license=False, is_student=False):
    """
    Classify age groups with additional context using nested conditionals.
    
    Explanation:
    - Demonstrates nested if-else with multiple conditions
    - Shows how to combine age with other attributes
    - More realistic example of nested decision-making
    - Each nested level adds more specificity
    
    Args:
        age (int): The age to classify
        has_license (bool): Whether person has a driver's license
        is_student (bool): Whether person is a student
        
    Returns:
        str: Detailed age group classification
    """
    if age < 0:
        return "Invalid Age"
    elif age < 13:
        if age < 5:
            return "Toddler"
        else:
            return "Child"
    elif age < 18:
        if is_student:
            return "Teenager (Student)"
        else:
            return "Teenager"
    elif age < 30:
        if has_license:
            if is_student:
                return "Young Adult (Student with License)"
            else:
                return "Young Adult (Licensed Driver)"
        else:
            return "Young Adult"
    elif age < 50:
        if has_license:
            return "Adult (Licensed Driver)"
        else:
            return "Adult"
    elif age < 65:
        return "Middle-aged Adult"
    elif age < 80:
        return "Senior"
    else:
        return "Elderly"


# ============================================================================
# MAIN FUNCTION - DEMONSTRATION
# ============================================================================
def main():
    """
    Main function to demonstrate all conditional statement methods.
    """
    print("=" * 70)
    print("AGE GROUP CLASSIFICATION SYSTEM")
    print("Demonstrating Various Conditional Statements")
    print("=" * 70)
    
    # List to store all entered ages
    ages_list = []
    
    # Loop to get multiple ages from keyboard
    print("\nEnter ages to classify (enter 'done' or 'quit' to finish):")
    print("-" * 70)
    
    while True:
        try:
            age_input = input(f"\nEnter age #{len(ages_list) + 1} (or 'done' to finish): ").strip().lower()
            
            # Check if user wants to quit
            if age_input in ['done', 'quit', 'exit', 'q', 'd']:
                if len(ages_list) == 0:
                    print("No ages entered. Please enter at least one age.")
                    continue
                break
            
            # Try to convert to integer
            age = int(age_input)
            ages_list.append(age)
            print(f"✓ Age {age} added successfully!")
            
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'done' to finish.")
    
    # Optional additional information for detailed classification
    print("\n" + "-" * 70)
    has_license_input = input("Does this person have a driver's license? (yes/no): ").lower()
    has_license = has_license_input in ['yes', 'y']
    
    is_student_input = input("Is this person a student? (yes/no): ").lower()
    is_student = is_student_input in ['yes', 'y']
    
    # Display results for each age using all methods
    print("\n" + "=" * 70)
    print(f"CLASSIFICATION RESULTS FOR {len(ages_list)} AGE(S):")
    print("=" * 70)
    
    # Process each age entered
    for idx, age in enumerate(ages_list, 1):
        print(f"\n{'=' * 70}")
        print(f"AGE #{idx}: {age} years old")
        print("-" * 70)
        
        print(f"1. Nested If-Else:        {classify_age_nested_if_else(age)}")
        print(f"2. Elif Chain:            {classify_age_elif(age)}")
        print(f"3. Match-Case:            {classify_age_match_case(age)}")
        print(f"4. Ternary Operator:      {classify_age_ternary(age)}")
        print(f"5. Logical Operators:     {classify_age_logical_operators(age)}")
        print(f"6. Dictionary-Based:      {classify_age_dictionary(age)}")
        print(f"7. Detailed (Nested):     {classify_age_detailed(age, has_license, is_student)}")
    
    # Summary table of all ages
    print("\n" + "=" * 70)
    print("SUMMARY TABLE - All Entered Ages:")
    print("=" * 70)
    print(f"\n{'Age':<6} {'Nested If-Else':<20} {'Elif':<20} {'Ternary':<20}")
    print("-" * 70)
    
    for age in ages_list:
        nested = classify_age_nested_if_else(age)
        elif_result = classify_age_elif(age)
        ternary = classify_age_ternary(age)
        print(f"{age:<6} {nested:<20} {elif_result:<20} {ternary:<20}")
    
    print("\n" + "=" * 70)
    print("EXPLANATION OF CONDITIONAL STATEMENTS:")
    print("=" * 70)
    print("""
1. NESTED IF-ELSE:
   - If-else statements inside other if-else blocks
   - Allows hierarchical decision-making
   - Can become hard to read if too deeply nested
   - Example: if condition1: if condition2: action1 else: action2

2. ELIF (ELSE-IF):
   - Cleaner alternative to nested if-else
   - Checks conditions sequentially
   - More readable and maintainable
   - Example: if condition1: action1 elif condition2: action2 else: action3

3. MATCH-CASE (Python 3.10+):
   - Pattern matching similar to switch-case
   - Modern Pythonic approach
   - Can use guards for range matching
   - Example: match value: case n if n < 10: action1

4. TERNARY OPERATOR:
   - Inline conditional expression
   - Syntax: value_if_true if condition else value_if_false
   - Compact but can be hard to read if over-nested
   - Example: result = "Yes" if age >= 18 else "No"

5. LOGICAL OPERATORS:
   - 'and': both conditions must be true
   - 'or': at least one condition must be true
   - 'not': negates a condition
   - Example: if age >= 18 and age < 65: action

6. DICTIONARY-BASED:
   - Uses dictionary to map conditions to results
   - More functional programming style
   - Easily extensible
   - Example: {lambda x: x < 10: "Small", lambda x: x >= 10: "Large"}

7. COMPLEX NESTED CONDITIONS:
   - Combines multiple criteria
   - Each nested level adds specificity
   - More realistic decision-making scenarios
   - Example: if age >= 18: if has_license: if is_student: action
    """)
    
    print("=" * 70)
    print("Thank you for using the Age Classification System!")
    print("=" * 70)


# Run the program
if __name__ == "__main__":
    main()

