"""
Few-Shot Prompting: Read a .txt file and return the number of lines
This script demonstrates few-shot prompting to count lines in a text file.
The file content is taken from keyboard input.
"""


def create_few_shot_prompt() -> str:
    """
    Creates a few-shot prompt with examples to guide the line counting logic.
    This demonstrates how few-shot prompting works with examples.
    """
    prompt = """Count the number of lines in a text file.

Examples:
1. File contains:
   Line 1
   Line 2
   Line 3
   -> Output: 3 lines

2. File contains:
   Hello
   World
   -> Output: 2 lines

3. File is empty
   -> Output: 0 lines

4. File contains:
   Single line
   -> Output: 1 line

Rules:
- Count each line in the file (including empty lines)
- Return the total number of lines
- Handle empty files (return 0)
"""
    return prompt


def get_lines_from_keyboard() -> list:
    """
    Gets lines from keyboard input until user enters an empty line or 'done'.
    
    Returns:
        List of strings entered by the user
    """
    print("\nEnter lines of text (press Enter twice or type 'done' to finish):")
    print("(You can also press Enter on an empty line to finish)\n")
    
    lines = []
    while True:
        try:
            line = input()
            if line.lower() == 'done':
                break
            if line == '' and lines:  # Allow empty line to finish if at least one line entered
                # Check if user wants to finish (double Enter)
                break
            lines.append(line)
        except EOFError:
            # Handle Ctrl+Z (Windows) or Ctrl+D (Unix)
            break
        except KeyboardInterrupt:
            print("\nInput interrupted.")
            break
    
    return lines


def save_lines_to_file(lines: list, filename: str = "input.txt") -> str:
    """
    Saves the lines to a .txt file.
    
    Args:
        lines: List of strings to write to the file
        filename: Name of the file to create
        
    Returns:
        The filename where the lines were saved
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')
    
    return filename


def count_lines_in_file(file_path: str) -> int:
    """
    Reads a .txt file and returns the number of lines.
    
    This function is designed based on the few-shot prompt examples.
    The examples guide the implementation to handle various cases.
    
    Args:
        file_path: Path to the .txt file to read
        
    Returns:
        Number of lines in the file (0 if file is empty or doesn't exist)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Following the few-shot examples:
            # Example 1: 3 lines -> count all lines
            # Example 2: 2 lines -> count all lines
            # Example 3: 0 lines -> handle empty file
            # Example 4: 1 line -> count single line
            
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return 0


def demonstrate_few_shot_approach():
    """
    Demonstrates the few-shot prompting approach
    """
    print("=" * 70)
    print("FEW-SHOT PROMPTING APPROACH")
    print("=" * 70)
    few_shot_prompt = create_few_shot_prompt()
    print(few_shot_prompt)
    print("\n" + "=" * 70)
    print("Based on these examples, the function will:")
    print("  - Count all lines in the file")
    print("  - Handle empty files (return 0)")
    print("  - Handle various line counts correctly")
    print("=" * 70 + "\n")


def main():
    """
    Main function that uses few-shot prompting to count lines from keyboard input
    """
    print("\n" + "=" * 70)
    print("FEW-SHOT PROMPTING: Count Lines in Text File")
    print("=" * 70)
    
    # Show the few-shot prompt approach
    demonstrate_few_shot_approach()
    
    # Get lines from keyboard
    lines = get_lines_from_keyboard()
    
    if not lines:
        print("\nNo lines entered. Creating empty file...")
    
    # Save to file
    filename = "input.txt"
    save_lines_to_file(lines, filename)
    print(f"\n✓ Lines saved to '{filename}'")
    
    # Count lines using the few-shot prompted function
    print(f"\nCounting lines using few-shot prompted function...")
    line_count = count_lines_in_file(filename)
    
    # Display result
    print("\n" + "=" * 70)
    print("RESULT")
    print("=" * 70)
    print(f"File: {filename}")
    print(f"Number of lines: {line_count}")
    
    if lines:
        print(f"\nContent preview (first 5 lines):")
        for i, line in enumerate(lines[:5], 1):
            print(f"  {i}. {line}")
        if len(lines) > 5:
            print(f"  ... and {len(lines) - 5} more line(s)")
    
    print("=" * 70)
    
    # Ask if user wants to keep the file
    try:
        keep_file = input("\nKeep the file? (y/n): ").strip().lower()
        if keep_file != 'y':
            import os
            if os.path.exists(filename):
                os.remove(filename)
                print(f"✓ File '{filename}' deleted.")
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()

