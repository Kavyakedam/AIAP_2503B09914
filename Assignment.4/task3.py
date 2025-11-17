def format_name(full_name):
    """
    Formats a full name as "Last, First"
    
    Args:
        full_name: A string containing the full name
        
    Returns:
        A string formatted as "Last, First"
    """
    # Split the name into parts
    name_parts = full_name.strip().split()
    
    if len(name_parts) == 0:
        return ""
    elif len(name_parts) == 1:
        # Only one name provided, return as is
        return name_parts[0]
    else:
        # Multiple parts: last name is the last part, first name(s) are the rest
        last_name = name_parts[-1]
        first_name = " ".join(name_parts[:-1])
        return f"{last_name}, {first_name}"


def main():
    """
    Main function to take 4 names from keyboard and format them
    """
    print("Name Formatter - Format names as 'Last, First'")
    print("Enter 4 names:\n")
    
    formatted_names = []
    
    # Prompt for exactly 4 names
    for i in range(1, 5):
        # Get input from keyboard
        name = input(f"Enter name {i}: ").strip()
        
        # Format the name
        formatted = format_name(name)
        formatted_names.append(formatted)
        print(f"Formatted: {formatted}\n")
    
    # Display all formatted names
    print("\n--- All Formatted Names ---")
    for formatted_name in formatted_names:
        print(formatted_name)


if __name__ == "__main__":
    main()

