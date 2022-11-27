from student import Student

def print_menu():
    print("Choose the operation you want to do:")
    print("1. Add a student")
    print("2. Display the list of students")
    print("3. Delete a group of students")
    print("4. Undo")
    print("5. Exit")

def read_student():
    id = input("Student Id: ")
    name = input("Student Name: ")
    group = input("Student Group: ")
    
    student = Student(id, name, group)
    return student

