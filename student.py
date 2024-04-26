students = []

def add_student(name):
    students.append(name)
    print("Student ",name," added successfully.")

def remove_student(name):
    try:
        students.remove(name)
        print("Student ",name," removed successfully.")
    except ValueError:
        print("Student ",name," not found.")

def display_students():
    print("List of students:")
    for student in students:
        print(student)

while True:
    print("\nStudent Management System\nBy AAKHS BATCH-6")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter the student's name to add: ")
        add_student(name)
    elif choice == '2':
        name = input("Enter the student's name to remove: ")
        remove_student(name)
    elif choice == '3':
        display_students()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1-4.")
