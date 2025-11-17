"""
Electricity Bill Calculator
This application calculates the electricity bill based on:
- PU (Previous Units)
- CU (Current Units)
- Type of customer
- Various charges (Energy Charges, Fixed Charges, Customer Charges, Electricity Duty)
"""

def calculate_electricity_bill():
    """
    Calculate electricity bill based on units consumed and customer type.
    """
    
    # Read input data
    print("=== Electricity Bill Calculator ===\n")
    
    pu = int(input("Enter Previous Units (PU): "))
    cu = int(input("Enter Current Units (CU): "))
    customer_type = input("Enter Type of Customer (Domestic/Commercial/Industrial): ").strip().lower()
    
    # Calculate units consumed
    units_consumed = cu - pu
    
    if units_consumed < 0:
        print("\nError: Current Units cannot be less than Previous Units!")
        return
    
    # Determine rates based on customer type
    if customer_type == "domestic":
        # Domestic rates (per unit)
        if units_consumed <= 100:
            rate_per_unit = 0
            fc = 0  # No fixed charges for first 100 units
        elif units_consumed <= 300:
            rate_per_unit = 3
            fc = 50  # Fixed charge
        else:
            rate_per_unit = 5
            fc = 100  # Fixed charge
        cc = 20  # Customer charges for Domestic
        ed_rate = 0.05  # Electricity duty rate (5%)
        
    elif customer_type == "commercial":
        # Commercial rates (per unit)
        if units_consumed <= 100:
            rate_per_unit = 5
            fc = 100
        elif units_consumed <= 300:
            rate_per_unit = 8
            fc = 150
        else:
            rate_per_unit = 10
            fc = 200
        cc = 50  # Customer charges for Commercial
        ed_rate = 0.08  # Electricity duty rate (8%)
        
    elif customer_type == "industrial":
        # Industrial rates (per unit)
        if units_consumed <= 500:
            rate_per_unit = 4
            fc = 200
        elif units_consumed <= 1000:
            rate_per_unit = 6
            fc = 300
        else:
            rate_per_unit = 8
            fc = 500
        cc = 100  # Customer charges for Industrial
        ed_rate = 0.10  # Electricity duty rate (10%)
        
    else:
        print("\nError: Invalid customer type!")
        return
    
    # Calculate charges
    ec = units_consumed * rate_per_unit  # Energy Charges
    # fc = Fixed Charges (already determined above)
    # cc = Customer Charges (already determined above)
    ed = (ec + fc + cc) * ed_rate  # Electricity Duty (calculated on total of EC, FC, CC)
    
    # Calculate total bill
    bill = ec + fc + cc + ed
    
    # Print results
    print("\n" + "="*50)
    print("ELECTRICITY BILL SUMMARY")
    print("="*50)
    print(f"Previous Units (PU)        : {pu}")
    print(f"Current Units (CU)         : {cu}")
    print(f"Units Consumed             : {units_consumed}")
    print(f"Customer Type              : {customer_type.capitalize()}")
    print("-"*50)
    print(f"Energy Charges (EC)        : Rs. {ec:.2f}")
    print(f"Fixed Charges (FC)         : Rs. {fc:.2f}")
    print(f"Customer Charges (CC)      : Rs. {cc:.2f}")
    print(f"Electricity Duty (ED)      : Rs. {ed:.2f}")
    print("-"*50)
    print(f"TOTAL BILL AMOUNT          : Rs. {bill:.2f}")
    print("="*50)


if __name__ == "__main__":
    calculate_electricity_bill()
    
    # Option to calculate again
    while True:
        choice = input("\nDo you want to calculate another bill? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            print("\n")
            calculate_electricity_bill()
        elif choice in ['no', 'n']:
            print("\nThank you for using Electricity Bill Calculator!")
            break
        else:
            print("Please enter 'yes' or 'no'")
