class BankAccount:
    """
    A Bank Account class that simulates a simple bank account.
    
    This class provides functionality to:
    - Create a bank account with account holder name and initial balance
    - Deposit money into the account
    - Withdraw money from the account
    - Check the current balance
    - Display account information
    """
    
    def __init__(self, account_holder_name, initial_balance=0.0):
        """
        Initialize a Bank Account object.
        
        Args:
            account_holder_name (str): The name of the account holder
            initial_balance (float): The initial balance in the account (default: 0.0)
        """
        # Store the account holder's name
        self.account_holder_name = account_holder_name
        
        # Store the current balance (ensure it's not negative)
        if initial_balance < 0:
            print("Warning: Initial balance cannot be negative. Setting to 0.0")
            self.balance = 0.0
        else:
            self.balance = float(initial_balance)
        
        # Account number can be auto-generated (for simplicity, using a simple counter)
        # In a real application, this would be more sophisticated
        self.account_number = None
    
    def deposit(self, amount):
        """
        Deposit money into the bank account.
        
        Args:
            amount (float): The amount of money to deposit (must be positive)
            
        Returns:
            bool: True if deposit was successful, False otherwise
        """
        # Validate the deposit amount
        if amount <= 0:
            print(f"Error: Deposit amount must be positive. You entered: ${amount:.2f}")
            return False
        
        # Add the amount to the current balance
        self.balance += amount
        print(f"✓ Successfully deposited ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the bank account.
        
        Args:
            amount (float): The amount of money to withdraw (must be positive and not exceed balance)
            
        Returns:
            bool: True if withdrawal was successful, False otherwise
        """
        # Validate the withdrawal amount
        if amount <= 0:
            print(f"Error: Withdrawal amount must be positive. You entered: ${amount:.2f}")
            return False
        
        # Check if there are sufficient funds
        if amount > self.balance:
            print(f"Error: Insufficient funds!")
            print(f"  Requested: ${amount:.2f}")
            print(f"  Available: ${self.balance:.2f}")
            return False
        
        # Subtract the amount from the current balance
        self.balance -= amount
        print(f"✓ Successfully withdrew ${amount:.2f}")
        print(f"  Remaining balance: ${self.balance:.2f}")
        return True
    
    def get_balance(self):
        """
        Get the current balance of the bank account.
        
        Returns:
            float: The current balance in the account
        """
        return self.balance
    
    def display_account_info(self):
        """
        Display all account information including holder name and current balance.
        """
        print("\n" + "=" * 50)
        print("Account Information")
        print("=" * 50)
        print(f"Account Holder: {self.account_holder_name}")
        if self.account_number:
            print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("=" * 50)


def get_account_details_from_keyboard():
    """
    Get account details from keyboard input.
    
    Returns:
        tuple: (account_holder_name, initial_balance)
    """
    print("\n" + "=" * 50)
    print("Create New Bank Account")
    print("=" * 50)
    
    # Get account holder name from keyboard
    while True:
        account_holder_name = input("\nEnter account holder name: ").strip()
        if account_holder_name:
            break
        print("Error: Account holder name cannot be empty. Please try again.")
    
    # Get initial balance from keyboard
    while True:
        try:
            initial_balance_input = input("Enter initial balance (default: 0.0): ").strip()
            
            # If user presses Enter without input, use default value
            if not initial_balance_input:
                initial_balance = 0.0
                break
            
            # Try to convert input to float
            initial_balance = float(initial_balance_input)
            
            # Check if balance is negative
            if initial_balance < 0:
                print("Error: Initial balance cannot be negative. Please try again.")
                continue
            
            break
        except ValueError:
            print("Error: Invalid input! Please enter a valid number (e.g., 100.50).")
    
    return account_holder_name, initial_balance


def explain_code():
    """
    Explain the Bank Account code structure and functionality.
    This function provides a detailed explanation of how the code works.
    """
    print("\n" + "=" * 70)
    print("CODE EXPLANATION - Bank Account Management System")
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print("1. BANK ACCOUNT CLASS")
    print("-" * 70)
    print("""
    The BankAccount class is the core of this program. It represents a bank 
    account with the following components:
    
    a) __init__() method (Constructor):
       - Initializes a new bank account object
       - Takes two parameters: account_holder_name (required) and initial_balance (optional, defaults to 0.0)
       - Stores the account holder's name in self.account_holder_name
       - Validates that initial_balance is not negative (if negative, sets to 0.0)
       - Stores the balance in self.balance attribute
    
    b) deposit(amount) method:
       - Allows adding money to the account
       - Validates that the deposit amount is positive (> 0)
       - If valid, adds the amount to self.balance
       - Returns True if successful, False if validation fails
       - Displays success message with new balance
    
    c) withdraw(amount) method:
       - Allows removing money from the account
       - Validates that withdrawal amount is positive (> 0)
       - Checks if sufficient funds are available (amount <= balance)
       - If valid, subtracts the amount from self.balance
       - Returns True if successful, False if validation fails
       - Displays success message with remaining balance
    
    d) get_balance() method:
       - Returns the current balance of the account
       - Simple getter method that returns self.balance
    
    e) display_account_info() method:
       - Displays formatted account information
       - Shows account holder name and current balance
       - Uses formatted output with separators for readability
    """)
    
    print("\n" + "-" * 70)
    print("2. GET ACCOUNT DETAILS FUNCTION")
    print("-" * 70)
    print("""
    get_account_details_from_keyboard() function:
    
    - Purpose: Collects account creation information from the user via keyboard input
    - Process:
      1. Prompts user to enter account holder name (cannot be empty)
      2. Prompts user to enter initial balance (optional, defaults to 0.0 if empty)
      3. Validates all inputs:
         * Name must not be empty (uses while loop to keep asking until valid)
         * Balance must be a valid number (uses try-except for error handling)
         * Balance must not be negative
    - Returns: A tuple containing (account_holder_name, initial_balance)
    - Uses input validation loops to ensure data quality
    """)
    
    print("\n" + "-" * 70)
    print("3. MAIN FUNCTION")
    print("-" * 70)
    print("""
    main() function - The program's entry point:
    
    Step 1: Display welcome message
    Step 2: Get account details using get_account_details_from_keyboard()
    Step 3: Create a BankAccount object with the collected details
    Step 4: Display account creation confirmation
    Step 5: Enter interactive transaction menu loop:
    
    Transaction Menu Options:
    - Option 1: Deposit money
      * Gets amount from user input
      * Calls account.deposit(amount) method
      * Handles invalid input with try-except
    
    - Option 2: Withdraw money
      * Gets amount from user input
      * Calls account.withdraw(amount) method
      * Handles invalid input with try-except
    
    - Option 3: Check balance
      * Calls account.get_balance() method
      * Displays current balance
    
    - Option 4: Display account info
      * Calls account.display_account_info() method
      * Shows formatted account details
    
    - Option 5: Exit
      * Breaks the while loop
      * Displays final balance and goodbye message
    
    The menu uses a while True loop that continues until user chooses to exit.
    """)
    
    print("\n" + "-" * 70)
    print("4. KEY PROGRAMMING CONCEPTS USED")
    print("-" * 70)
    print("""
    a) Object-Oriented Programming (OOP):
       - Class definition with methods (encapsulation)
       - Instance attributes (self.account_holder_name, self.balance)
       - Object instantiation
    
    b) Input Validation:
       - Try-except blocks for handling invalid input
       - While loops to repeatedly ask until valid input is received
       - Checking conditions (positive amounts, sufficient funds)
    
    c) Error Handling:
       - ValueError exception handling for type conversion
       - Conditional checks before operations
       - User-friendly error messages
    
    d) String Formatting:
       - f-strings for formatted output (f"${balance:.2f}")
       - String repetition for separators ("=" * 50)
    
    e) Control Flow:
       - If-elif-else statements for menu selection
       - While loops for continuous input and menu display
       - Break statement to exit loops
    
    f) Function Design:
       - Modular code with separate functions for different tasks
       - Clear function names that describe their purpose
       - Docstrings for documentation
    """)
    
    print("\n" + "-" * 70)
    print("5. HOW THE CODE EXECUTES")
    print("-" * 70)
    print("""
    Execution Flow:
    
    1. Python checks if script is run directly (if __name__ == "__main__")
    2. main() function is called
    3. User is prompted to enter account details (name and balance)
    4. BankAccount object is created with those details
    5. Interactive menu appears allowing user to:
       - Deposit money (updates balance)
       - Withdraw money (updates balance, checks for sufficient funds)
       - Check current balance
       - View account information
       - Exit the program
    6. Program continues in a loop until user chooses to exit
    
    Example Execution:
    - User enters: Name = "John Doe", Balance = 100.0
    - Account created with $100.00
    - User selects option 1, deposits $50.00
    - Balance becomes $150.00
    - User selects option 2, withdraws $30.00
    - Balance becomes $120.00
    - User selects option 3, sees balance of $120.00
    - User selects option 5, exits program
    """)
    
    print("\n" + "=" * 70)
    print("END OF CODE EXPLANATION")
    print("=" * 70 + "\n")


def main():
    """
    Main function to demonstrate the Bank Account class functionality.
    Allows user to create an account and perform transactions.
    """
    # Display code explanation first
    explain_code()
    
    print("\n" + "=" * 50)
    print("Bank Account Management System")
    print("=" * 50)
    
    # Step 1: Get account details from keyboard
    account_holder_name, initial_balance = get_account_details_from_keyboard()
    
    # Step 2: Create a Bank Account object
    account = BankAccount(account_holder_name, initial_balance)
    
    # Display account creation confirmation
    print(f"\n✓ Account created successfully for {account_holder_name}!")
    account.display_account_info()
    
    # Step 3: Interactive menu for transactions
    print("\n" + "=" * 50)
    print("Transaction Menu")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("  1. Deposit money")
        print("  2. Withdraw money")
        print("  3. Check balance")
        print("  4. Display account info")
        print("  5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            # Deposit operation
            try:
                amount = float(input("Enter amount to deposit: $"))
                account.deposit(amount)
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
        
        elif choice == "2":
            # Withdraw operation
            try:
                amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(amount)
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
        
        elif choice == "3":
            # Check balance operation
            current_balance = account.get_balance()
            print(f"\nCurrent Balance: ${current_balance:.2f}")
        
        elif choice == "4":
            # Display account information
            account.display_account_info()
        
        elif choice == "5":
            # Exit the program
            print("\nThank you for using the Bank Account Management System!")
            print(f"Final balance: ${account.get_balance():.2f}")
            break
        
        else:
            print("Error: Invalid choice! Please enter a number between 1-5.")


# Run the program when this script is executed directly
if __name__ == "__main__":
    main()
