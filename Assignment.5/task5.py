"""
Code Snippet - Greet User Function
This function demonstrates conditional logic for greeting users based on gender.
"""

def greet_user(name, gender):
    """Greet a user with an appropriate title based on gender"""
    if gender.lower() == "male":
        title = "Mr."
    elif gender.lower() == "female":
        title = "Mrs."
    elif gender.lower() == "neutral":
        # Neutral gender - use gender-neutral title "Mx."
        title = "Mx."
    else:
        # Default case for any other gender input
        title = "Mx."
    return f"Hello, {title} {name}! Welcome."


def main():
    """Main function to demonstrate the greet_user function"""
    print("=" * 60)
    print("Greet User Function Demo")
    print("=" * 60)
    print()
    
    # Example usage
    print("Example 1:")
    result1 = greet_user("John", "male")
    print(result1)
    print()
    
    print("Example 2:")
    result2 = greet_user("Sarah", "female")
    print(result2)
    print()
    
    print("Example 3:")
    result3 = greet_user("Alex", "neutral")
    print(result3)
    print()
    
    # Interactive mode
    print("-" * 60)
    print("Interactive Mode:")
    print("-" * 60)
    
    while True:
        name = input("\nEnter name (or 'q' to quit): ").strip()
        if name.lower() == 'q':
            break
        
        gender = input("Enter gender (male/female/neutral): ").strip()
        if not gender:
            print("Error: Gender cannot be empty!")
            continue
        
        greeting = greet_user(name, gender)
        print(f"\n{greeting}")
    
    print("\nThank you for using the Greet User function!")


if __name__ == "__main__":
    main()
