def main():
    n = int(input("Enter number of students: "))

    students = []
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        mark = float(input(f"Enter marks of {name}: "))
        students.append((name, mark))

    # Calculate mean
    mean_marks = sum(mark for _, mark in students) / n
    print(f"\nMean Marks = {mean_marks:.2f}")

    # Students above mean
    above_mean = [name for name, mark in students if mark > mean_marks]

    print("\nStudents scoring above the mean:")
    if above_mean:
        for s in above_mean:
            print(s)
    else:
        print("No student scored above the mean.")

# Run the program
main()