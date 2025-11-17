"""
Task 5: Few-Shot Prompting for File Line Counting
This script demonstrates few-shot prompting to generate a function that reads a .txt file
and returns the number of lines. The filename is taken from keyboard input.
"""


def create_few_shot_prompt() -> str:
    """
    Creates a few-shot prompt (with examples provided) for counting lines in a file
    """
    prompt = """Write a Python function that reads a .txt file and returns the number of lines.

Examples:
1. File: "example1.txt" contains:
   Line 1
   Line 2
   Line 3
   -> Output: 3 lines

2. File: "example2.txt" contains:
   Hello
   World
   -> Output: 2 lines

3. File: "example3.txt" contains:
   Single line
   -> Output: 1 line

4. File: "example4.txt" is empty
   -> Output: 0 lines

The function should:
- Take a filename (string) as input
- Open and read the .txt file
- Count the number of lines in the file
- Handle empty files (return 0)
- Handle file not found errors gracefully
- Return the total line count as an integer

Provide only the function code."""
    return prompt


def count_lines_in_file(filename: str) -> int:
    """
    Reads a .txt file and returns the number of lines.
    This is the implementation we expect from the few-shot prompt.
    
    Args:
        filename: Path to the .txt file to read
        
    Returns:
        Number of lines in the file (0 if empty or file not found)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return 0


def demonstrate_few_shot_prompt():
    """
    Demonstrates the few-shot prompt for line counting
    """
    print("=" * 70)
    print("FEW-SHOT PROMPT (With Examples)")
    print("=" * 70)
    few_shot = create_few_shot_prompt()
    print(few_shot)
    print("\n")


def test_line_counting():
    """
    Tests the line counting function with user input from keyboard
    """
    print("\n" + "=" * 70)
    print("TESTING FILE LINE COUNTING FUNCTION")
    print("=" * 70)
    
    # Get filename from keyboard
    filename = input("\nEnter the path to the .txt file: ").strip()
    
    if not filename:
        print("No filename provided. Using default: 'sample.txt'")
        filename = "sample.txt"
    
    # Ensure it's a .txt file (add extension if missing)
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    # Count lines
    line_count = count_lines_in_file(filename)
    
    # Display results
    print(f"\nFile: '{filename}'")
    print(f"Number of lines: {line_count}")
    
    # Show file contents if file exists and is not too large
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip():
                print(f"\nFile contents:")
                print("-" * 70)
                print(content)
                print("-" * 70)
            else:
                print("\nFile is empty.")
    except FileNotFoundError:
        print(f"\nNote: File '{filename}' was not found.")
    except Exception as e:
        print(f"\nNote: Could not display file contents: {e}")


def simulate_llm_response():
    """
    Simulates what an LLM might generate from the few-shot prompt
    """
    print("\n" + "=" * 70)
    print("SIMULATED LLM RESPONSE FROM FEW-SHOT PROMPT")
    print("=" * 70)
    
    simulated_code = '''def count_lines_in_file(filename):
    """
    Reads a .txt file and returns the number of lines.
    
    Examples:
    - "example1.txt" with 3 lines -> returns 3
    - "example2.txt" with 2 lines -> returns 2
    - "example3.txt" with 1 line -> returns 1
    - "example4.txt" (empty) -> returns 0
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0'''
    
    print("\n--- Generated Code (Simulated) ---")
    print(simulated_code)
    
    print("\n--- Analysis ---")
    print("The few-shot prompt helped the model understand:")
    print("  - How to handle different file sizes (1, 2, 3 lines)")
    print("  - How to handle empty files (0 lines)")
    print("  - The expected return type (integer)")
    print("  - Error handling for file not found cases")


def create_sample_file():
    """
    Creates a sample .txt file for testing if it doesn't exist
    """
    sample_filename = "sample.txt"
    try:
        with open(sample_filename, 'r', encoding='utf-8') as file:
            # File exists, no need to create
            pass
    except FileNotFoundError:
        # Create a sample file
        sample_content = """This is line 1
This is line 2
This is line 3
This is line 4
This is line 5"""
        with open(sample_filename, 'w', encoding='utf-8') as file:
            file.write(sample_content)
        print(f"\nCreated sample file '{sample_filename}' for testing.")


def main():
    """
    Main function to run the few-shot prompting demonstration
    """
    print("\n" + "=" * 70)
    print("FEW-SHOT PROMPTING FOR FILE LINE COUNTING")
    print("Task: Generate a function to count lines in a .txt file")
    print("=" * 70)
    
    # Show the few-shot prompt
    demonstrate_few_shot_prompt()
    
    # Simulate LLM response
    simulate_llm_response()
    
    # Create a sample file if needed
    create_sample_file()
    
    # Test with user input from keyboard
    test_line_counting()
    
    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("""
Few-shot prompting for this task provides:
- Clear examples showing different scenarios (1, 2, 3, 0 lines)
- Pattern for handling edge cases (empty files)
- Expected output format (integer)
- Better understanding of error handling requirements
    """)


if __name__ == "__main__":
    main()

