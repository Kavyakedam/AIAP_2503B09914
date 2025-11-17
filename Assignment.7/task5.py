# Code to demonstrate accessing an invalid list index and handling IndexError

# Create a sample list
my_list = [10, 20, 30, 40, 50]

print("Original list:", my_list)
print("List length:", len(my_list))
print("\n" + "="*50)

# Attempt to access an invalid index (this will cause IndexError)
try:
    # Trying to access index 10, but list only has indices 0-4
    invalid_index = 10
    print(f"\nAttempting to access index {invalid_index}...")
    value = my_list[invalid_index]
    print(f"Value at index {invalid_index}: {value}")
    
except IndexError as e:
    # Handle the IndexError
    print(f"IndexError caught: {e}")
    print(f"List indices are valid from 0 to {len(my_list) - 1}")
    print("The error has been resolved by catching it with try-except block")
    
print("\n" + "="*50)

# Another example: accessing negative index that's out of range
try:
    print(f"\nAttempting to access index -10...")
    value = my_list[-10]
    print(f"Value at index -10: {value}")
    
except IndexError as e:
    print(f"IndexError caught: {e}")
    print(f"Negative indices are valid from -1 to -{len(my_list)}")
    print("The error has been resolved!")

print("\n" + "="*50)
print("Program continues to execute after handling the errors.")
