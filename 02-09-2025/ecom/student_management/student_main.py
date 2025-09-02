from student_manager import create_student, read_all, read_by_id, update, delete_by_id
from student import Student

def menu():
    while True:
        print("\n===== Student Management System ====")
        print("1. Create Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            course = input("Course: ")
            marks = int(input("Marks: "))
            student = Student(name, course, marks)
            create_student(student)
            print(f"Student added successfully ID: {student.id}")
            

        elif choice == "2":
            students = read_all()
            if len(students) == 0:
                print("No students found")
            else:
                for s in students:
                    print(s)
                
        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            student = read_by_id(student_id)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = int(input("Enter Student ID to update: "))
            student = read_by_id(student_id)
            if student:
                name = input("New Name: ")
                course = input("New Course: ")
                marks = int(input("New Marks: "))
                updated_student = Student(name, course, marks)
                updated_student.id = student_id
                update(updated_student)
                print("Student updated sucessfully")
            else:
                print("Student not found")

        

        elif choice == "5":
            student_id = int(input("Enter Student ID to delete: "))
            student = read_by_id(student_id)
            if student:
                delete_by_id(student_id)
                print("Student deleted successfully")
            else:
                print("Student not found")
            

        elif choice == 6:
            print("Existing program...")
            break

        else:
            print("Invalid choice! Try again.")

menu()

    

