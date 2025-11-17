"""
Task 4: Compare Zero-Shot and Few-Shot Prompts for Vowel Counting Function
This script demonstrates the difference between zero-shot and few-shot prompting
for generating a function that counts vowels in a string.
"""

import os
import json
from typing import Dict, Any


def create_zero_shot_prompt() -> str:
    """
    Creates a zero-shot prompt (no examples provided)
    """
    prompt = """Write a Python function that counts the number of vowels in a string.
The function should:
- Take a string as input
- Count all vowels (a, e, i, o, u) in both uppercase and lowercase
- Return the total count

Provide only the function code."""
    return prompt


def create_few_shot_prompt() -> str:
    """
    Creates a few-shot prompt (with examples provided)
    """
    prompt = """Write a Python function that counts the number of vowels in a string.

Examples:
1. Input: "Hello" -> Output: 2 (e, o)
2. Input: "Python" -> Output: 1 (o)
3. Input: "AEIOU" -> Output: 5 (all vowels)
4. Input: "Programming" -> Output: 3 (o, a, i)

The function should:
- Take a string as input
- Count all vowels (a, e, i, o, u) in both uppercase and lowercase
- Return the total count

Provide only the function code."""
    return prompt


def count_vowels_simple(text: str) -> int:
    """
    Simple implementation: counts vowels in a string
    This is what we expect the LLM to generate
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_vowels_advanced(text: str) -> int:
    """
    Alternative implementation using list comprehension
    This could be another valid solution
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def demonstrate_prompts():
    """
    Demonstrates the zero-shot and few-shot prompts
    """
    print("=" * 70)
    print("ZERO-SHOT PROMPT (No Examples)")
    print("=" * 70)
    zero_shot = create_zero_shot_prompt()
    print(zero_shot)
    print("\n")
    
    print("=" * 70)
    print("FEW-SHOT PROMPT (With Examples)")
    print("=" * 70)
    few_shot = create_few_shot_prompt()
    print(few_shot)
    print("\n")


def compare_approaches():
    """
    Compares zero-shot vs few-shot approaches with analysis
    """
    print("=" * 70)
    print("COMPARISON: Zero-Shot vs Few-Shot Prompting")
    print("=" * 70)
    
    comparison = {
        "Zero-Shot Prompting": {
            "Definition": "No examples provided in the prompt",
            "Advantages": [
                "Faster to write (no need to create examples)",
                "More concise prompts",
                "Good for simple, well-defined tasks"
            ],
            "Disadvantages": [
                "May produce less accurate results",
                "Might miss edge cases",
                "Less context for the model to understand requirements"
            ],
            "Best For": "Simple, straightforward tasks with clear requirements"
        },
        "Few-Shot Prompting": {
            "Definition": "Includes examples in the prompt to guide the model",
            "Advantages": [
                "Better accuracy and understanding",
                "Handles edge cases better",
                "Provides clear pattern for the model to follow",
                "More likely to produce desired output format"
            ],
            "Disadvantages": [
                "Longer prompts (more tokens)",
                "Requires creating good examples",
                "Slightly more expensive (if using paid APIs)"
            ],
            "Best For": "Complex tasks, tasks requiring specific formatting, or when accuracy is critical"
        }
    }
    
    for approach, details in comparison.items():
        print(f"\n{approach}:")
        print(f"  Definition: {details['Definition']}")
        print(f"  Advantages:")
        for adv in details['Advantages']:
            print(f"    - {adv}")
        print(f"  Disadvantages:")
        for dis in details['Disadvantages']:
            print(f"    - {dis}")
        print(f"  Best For: {details['Best For']}")


def test_vowel_counting():
    """
    Tests the vowel counting function with user input
    """
    print("\n" + "=" * 70)
    print("TESTING VOWEL COUNTING FUNCTION")
    print("=" * 70)
    
    # Get input from keyboard
    user_input = input("\nEnter a string to count vowels: ")
    
    if not user_input:
        print("No input provided. Using default: 'Hello World'")
        user_input = "Hello World"
    
    # Count vowels
    count = count_vowels_simple(user_input)
    
    # Show which vowels were found
    vowels_found = [char for char in user_input if char.lower() in "aeiou"]
    
    print(f"\nInput string: '{user_input}'")
    print(f"Number of vowels: {count}")
    if vowels_found:
        print(f"Vowels found: {', '.join(vowels_found)}")
    else:
        print("No vowels found in the string.")


def simulate_llm_responses():
    """
    Simulates what an LLM might generate for each prompt type
    """
    print("\n" + "=" * 70)
    print("SIMULATED LLM RESPONSES")
    print("=" * 70)
    
    print("\n--- Zero-Shot Response (Simulated) ---")
    zero_shot_code = '''def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return cousnt'''
    print(zero_shot_code)
    
    print("\n--- Few-Shot Response (Simulated) ---")
    few_shot_code = '''def count_vowels(text):
    """
    Counts the number of vowels in a string.
    Examples:
    - "Hello" -> 2
    - "Python" -> 1
    - "AEIOU" -> 5
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)'''
    print(few_shot_code)
    
    print("\n--- Analysis ---")
    print("Zero-Shot: Produced a basic for-loop implementation")
    print("Few-Shot: Produced a more concise solution with docstring,")
    print("          showing the model learned from the examples")


def main():
    """
    Main function to run the comparison
    """
    print("\n" + "=" * 70)
    print("ZERO-SHOT vs FEW-SHOT PROMPT COMPARISON")
    print("Task: Generate a function to count vowels in a string")
    print("=" * 70)
    
    # Show the prompts
    demonstrate_prompts()
    
    # Show comparison
    compare_approaches()
    
    # Simulate LLM responses
    simulate_llm_responses()
    
    # Test with user input
    test_vowel_counting()
    
    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("""
For this specific task (counting vowels):
- Zero-shot is sufficient for simple, well-defined tasks
- Few-shot provides better guidance and may produce more elegant solutions
- Both approaches can work, but few-shot is more reliable for complex scenarios
    """)


if __name__ == "__main__":
    main()

