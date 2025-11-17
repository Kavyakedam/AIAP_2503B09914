class Student:
    """
    A class to represent a student with various attributes and methods.
    """
    
    def __init__(self, name, student_id, age, grade):
        """
        Initialize a Student object with basic information.
        
        Parameters:
        name (str): The student's name
        student_id (str): Unique identifier for the student
        age (int): The student's age
        grade (float): The student's current grade (0.0 to 100.0)
        """
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grade = grade
    
    def display_info(self):
        """
        Display all information about the student.
        
        Returns:
        str: Formatted string with student information
        """
        info = f"Student Information:\n"
        info += f"  Name: {self.name}\n"
        info += f"  ID: {self.student_id}\n"
        info += f"  Age: {self.age}\n"
        info += f"  Grade: {self.grade:.2f}"
        return info
    
    def update_grade(self, new_grade):
        """
        Update the student's grade.
        
        Parameters:
        new_grade (float): The new grade to assign
        """
        if 0.0 <= new_grade <= 100.0:
           self.grade = new_grade
        print(f"Grade updated to {new_grade:.2f}")
        else:
    print("Error: Grade must be between 0.0 and 100.0")return None
    
    def get_letter_grade(self):
        """
        Convert numeric grade to letter grade.
        
        Returns:
        str: Letter grade (A, B, C, D, or F)
        """
        if self.grade >= 90:
            return "A"
        elif self.grade >= 80:
            return "B"
        elif self.grade >= 70:
            return "C"
        elif self.grade >= 60:
            return "D"
        else:
            return "F"
    
    def is_passing(self):
        """
        Check if the student is passing (grade >= 60).
        
        Returns:
        bool: True if passing, False otherwise
        """
        return self.grade >= 60.0


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("Student Information System")
    print("=" * 50)
    
    # Get student information from keyboard
    print("\nEnter Student Details:")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    
    # Validate and get age
    while True:
        try:
            age = int(input("Enter student age: "))
            if age > 0:
                break
            else:
                print("Age must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
    
    # Validate and get grade
    while True:
        try:
            grade = float(input("Enter student grade (0.0 to 100.0): "))
            if 0.0 <= grade <= 100.0:
                break
            else:
                print("Grade must be between 0.0 and 100.0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for grade.")
    
    # Create a student instance with input values
    student = Student(name, student_id, age, grade)
    
    # Display student information
    print("\n" + "=" * 50)
    print(student.display_info())
    print(f"\nLetter Grade: {student.get_letter_grade()}")
    print(f"Passing: {'Yes' if student.is_passing() else 'No'}")
    
    # Option to update grade
    print("\n" + "=" * 50)
    update_choice = input("Do you want to update the grade? (yes/no): ").lower()
    if update_choice in ['yes', 'y']:
        while True:
            try:
                new_grade = float(input("Enter new grade (0.0 to 100.0): "))
                if 0.0 <= new_grade <= 100.0:
                    student.update_grade(new_grade)
                    print(f"Updated Letter Grade: {student.get_letter_grade()}")
                    print(f"Passing: {'Yes' if student.is_passing() else 'No'}")
                    break
                else:
                    print("Grade must be between 0.0 and 100.0. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number for grade.")
    
    print("\n" + "=" * 50)
    print("Thank you for using the Student Information System!")

