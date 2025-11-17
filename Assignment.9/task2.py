class sru_student:
    """
    A class to represent a SRU student with name, roll number, and hostel status.
    """
    
    def __init__(self, name, roll_no, hostel_status):
        """
        Initialize a student with name, roll number, and hostel status.
        
        Args:
            name: Student's name
            roll_no: Student's roll number
            hostel_status: Whether student is in hostel (True/False or "Yes"/"No")
        """
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False  # Default fee status
    
    def fee_update(self, fee_status):
        """
        Update the fee payment status of the student.
        
        Args:
            fee_status: Boolean or string indicating fee payment status
        """
        if isinstance(fee_status, bool):
            self.fee_paid = fee_status
        elif isinstance(fee_status, str):
            self.fee_paid = fee_status.lower() in ['yes', 'true', 'paid', '1']
        else:
            self.fee_paid = bool(fee_status)
        print(f"Fee status updated for {self.name}")
    
    def display_details(self):
        """
        Display all details of the student.
        """
        print("\n" + "="*50)
        print("STUDENT DETAILS")
        print("="*50)
        print(f"Name           : {self.name}")
        print(f"Roll Number    : {self.roll_no}")
        print(f"Hostel Status  : {self.hostel_status}")
        print(f"Fee Status     : {'Paid' if self.fee_paid else 'Not Paid'}")
        print("="*50 + "\n")


# Main program to take input from keyboard
if __name__ == "__main__":
    print("Enter Student Details:")
    print("-" * 30)
    
    # Taking input from keyboard
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    hostel_status = input("Enter hostel status (Yes/No): ")
    
    # Creating student object
    student = sru_student(name, roll_no, hostel_status)
    
    # Taking fee status input
    fee_input = input("Enter fee status (Paid/Not Paid): ")
    fee_status = fee_input.lower() in ['paid', 'yes', 'true', '1']
    student.fee_update(fee_status)
    
    # Display student details
    student.display_details()

