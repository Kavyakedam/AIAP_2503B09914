class ShoppingCart:
    """
    A Shopping Cart class that allows adding items, removing items, and calculating total cost.
    
    Methods:
        add_item(name, price): Adds an item with given name and price to the cart
        remove_item(name): Removes an item with given name from the cart
        total_cost(): Returns the total cost of all items in the cart
    """
    
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items = {}  # Dictionary to store items: {name: price}
    
    def add_item(self, name, price):
        """
        Adds an item to the shopping cart.
        
        Args:
            name (str): Name of the item
            price (float): Price of the item
            
        Returns:
            str: Confirmation message
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        
        self.items[name] = price
        return f"Added '{name}' (${price:.2f}) to cart"
    
    def remove_item(self, name):
        """
        Removes an item from the shopping cart.
        
        Args:
            name (str): Name of the item to remove
            
        Returns:
            str: Confirmation message
            
        Raises:
            KeyError: If item is not in the cart
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in cart")
        
        price = self.items.pop(name)
        return f"Removed '{name}' (${price:.2f}) from cart"
    
    def total_cost(self):
        """
        Calculates and returns the total cost of all items in the cart.
        
        Returns:
            float: Total cost of all items
        """
        return sum(self.items.values())
    
    def get_items(self):
        """
        Returns a copy of all items in the cart.
        
        Returns:
            dict: Dictionary of items {name: price}
        """
        return self.items.copy()
    
    def clear(self):
        """Clears all items from the cart"""
        self.items.clear()
        return "Cart cleared"


def generate_test_cases():
    """
    Interactive test case generator for ShoppingCart class.
    Takes methods and test inputs from keyboard.
    """
    print("="*70)
    print("Shopping Cart Test Case Generator")
    print("="*70)
    print("\nAvailable methods:")
    print("  1. add_item(name, price) - Add an item to cart")
    print("  2. remove_item(name) - Remove an item from cart")
    print("  3. total_cost() - Get total cost of all items")
    print("  4. show_cart() - Display all items in cart")
    print("  5. clear() - Clear all items from cart")
    print("\nType 'quit' or 'exit' to stop testing\n")
    
    cart = ShoppingCart()
    test_count = 0
    passed_count = 0
    failed_count = 0
    
    while True:
        print("-" * 70)
        print(f"Current cart: {dict(cart.get_items()) if cart.get_items() else 'Empty'}")
        print(f"Total cost: ${cart.total_cost():.2f}")
        print("-" * 70)
        
        # Get method choice
        method_input = input("\nEnter method (add_item/remove_item/total_cost/show_cart/clear/quit): ").strip().lower()
        
        if method_input in ['quit', 'exit', 'q']:
            break
        
        test_count += 1
        
        try:
            if method_input == 'add_item':
                # Test add_item
                print("\n--- Testing add_item(name, price) ---")
                name = input("Enter item name: ").strip()
                price_input = input("Enter item price: ").strip()
                
                try:
                    price = float(price_input)
                    result = cart.add_item(name, price)
                    print(f"✓ Result: {result}")
                    passed_count += 1
                except ValueError as e:
                    print(f"✗ Error: {e}")
                    failed_count += 1
                except Exception as e:
                    print(f"✗ Unexpected error: {e}")
                    failed_count += 1
            
            elif method_input == 'remove_item':
                # Test remove_item
                print("\n--- Testing remove_item(name) ---")
                name = input("Enter item name to remove: ").strip()
                
                try:
                    result = cart.remove_item(name)
                    print(f"✓ Result: {result}")
                    passed_count += 1
                except KeyError as e:
                    print(f"✗ Error: {e}")
                    failed_count += 1
                except ValueError as e:
                    print(f"✗ Error: {e}")
                    failed_count += 1
                except Exception as e:
                    print(f"✗ Unexpected error: {e}")
                    failed_count += 1
            
            elif method_input == 'total_cost':
                # Test total_cost
                print("\n--- Testing total_cost() ---")
                result = cart.total_cost()
                print(f"✓ Result: ${result:.2f}")
                passed_count += 1
            
            elif method_input == 'show_cart':
                # Show cart contents
                print("\n--- Cart Contents ---")
                items = cart.get_items()
                if items:
                    print("Items in cart:")
                    for name, price in items.items():
                        print(f"  - {name}: ${price:.2f}")
                else:
                    print("Cart is empty")
                passed_count += 1
            
            elif method_input == 'clear':
                # Clear cart
                print("\n--- Testing clear() ---")
                result = cart.clear()
                print(f"✓ Result: {result}")
                passed_count += 1
            
            else:
                print(f"✗ Unknown method: {method_input}")
                print("Available methods: add_item, remove_item, total_cost, show_cart, clear")
                test_count -= 1  # Don't count invalid method as a test
                continue
        
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            failed_count += 1
        
        print()
    
    # Summary
    print("\n" + "="*70)
    print("Test Summary")
    print("="*70)
    print(f"Total test cases executed: {test_count}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Final cart state: {dict(cart.get_items()) if cart.get_items() else 'Empty'}")
    print(f"Final total cost: ${cart.total_cost():.2f}")
    print("="*70)


def run_predefined_tests():
    """
    Run a set of predefined test cases to verify ShoppingCart functionality.
    """
    print("="*70)
    print("Running Predefined Test Cases for ShoppingCart")
    print("="*70)
    
    test_count = 0
    passed_count = 0
    failed_count = 0
    
    # Test 1: Create empty cart
    print("\nTest 1: Create empty cart")
    cart = ShoppingCart()
    test_count += 1
    try:
        assert cart.total_cost() == 0, "Empty cart shouSld have total cost 0"
        assert len(cart.get_items()) == 0, "Empty cart should have no items"
        print("✓ PASS: Empty cart created successfully")
        passed_count += 1
    except AssertionError as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Test 2: Add single item
    print("\nTest 2: Add single item")
    test_count += 1
    try:
        result = cart.add_item("Apple", 1.50)
        assert "Apple" in cart.get_items(), "Apple should be in cart"
        assert cart.get_items()["Apple"] == 1.50, "Apple price should be 1.50"
        assert cart.total_cost() == 1.50, "Total cost should be 1.50"
        print("✓ PASS: Single item added successfully")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Test 3: Add multiple items
    print("\nTest 3: Add multiple items")
    test_count += 1
    try:
        cart.add_item("Banana", 0.75)
        cart.add_item("Orange", 2.00)
        assert len(cart.get_items()) == 3, "Cart should have 3 items"
        assert cart.total_cost() == 4.25, "Total cost should be 4.25"
        print("✓ PASS: Multiple items added successfully")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Test 4: Remove item
    print("\nTest 4: Remove item")
    test_count += 1
    try:
        result = cart.remove_item("Banana")
        assert "Banana" not in cart.get_items(), "Banana should be removed"
        assert len(cart.get_items()) == 2, "Cart should have 2 items"
        assert cart.total_cost() == 3.50, "Total cost should be 3.50"
        print("✓ PASS: Item removed successfully")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Test 5: Remove non-existent item
    print("\nTest 5: Remove non-existent item")
    test_count += 1
    try:
        cart.remove_item("Grape")
        print("✗ FAIL: Should raise KeyError for non-existent item")
        failed_count += 1
    except KeyError:
        print("✓ PASS: Correctly raised KeyError for non-existent item")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: Unexpected error: {e}")
        failed_count += 1
    
    # Test 6: Add item with same name (update price)
    print("\nTest 6: Add item with same name (updates price)")
    test_count += 1
    try:
        cart.add_item("Apple", 2.00)  # Update price
        assert cart.get_items()["Apple"] == 2.00, "Apple price should be updated to 2.00"
        assert cart.total_cost() == 4.00, "Total cost should be 4.00"
        print("✓ PASS: Item price updated successfully")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Test 7: Total cost with empty cart
    print("\nTest 7: Total cost with empty cart")
    test_count += 1
    try:
        cart.clear()
        assert cart.total_cost() == 0, "Empty cart total should be 0"
        print("✓ PASS: Empty cart total cost is 0")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Test 8: Invalid price (negative)
    print("\nTest 8: Add item with negative price")
    test_count += 1
    try:
        cart.add_item("Item", -5.00)
        print("✗ FAIL: Should raise ValueError for negative price")
        failed_count += 1
    except ValueError:
        print("✓ PASS: Correctly raised ValueError for negative price")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: Unexpected error: {e}")
        failed_count += 1
    
    # Test 9: Invalid name (empty string)
    print("\nTest 9: Add item with empty name")
    test_count += 1
    try:
        cart.add_item("", 5.00)
        print("✗ FAIL: Should raise ValueError for empty name")
        failed_count += 1
    except ValueError:
        print("✓ PASS: Correctly raised ValueError for empty name")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: Unexpected error: {e}")
        failed_count += 1
    
    # Test 10: Add items with decimal prices
    print("\nTest 10: Add items with decimal prices")
    test_count += 1
    try:
        cart.add_item("Milk", 3.99)
        cart.add_item("Bread", 2.49)
        assert abs(cart.total_cost() - 6.48) < 0.01, "Total should be approximately 6.48"
        print("✓ PASS: Decimal prices handled correctly")
        passed_count += 1
    except Exception as e:
        print(f"✗ FAIL: {e}")
        failed_count += 1
    
    # Summary
    print("\n" + "="*70)
    print("Predefined Test Summary")
    print("="*70)
    print(f"Total test cases: {test_count}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print("="*70)


if __name__ == "__main__":
    print("Choose test mode:")
    print("1. Interactive test case generator (input from keyboard)")
    print("2. Run predefined test cases")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        generate_test_cases()
    elif choice == "2":
        run_predefined_tests()
    else:
        print("Invalid choice. Running interactive test case generator...")
        generate_test_cases()

