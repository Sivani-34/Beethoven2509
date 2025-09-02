from student import Student
students = [] #list to store all students

def create_student(student): #create
    global students
    if len(students) == 0:
        student.id = 1
    else:
        student.id = students[-1].id + 1
    students.append(student)
    return student

def read_all(): #read all
    return students

def read_by_id(student_id):
    for student in students:
        if student.id == student_id:
            return student
    return None

def update(student):  #update
    old_student = read_by_id(student.id)
    if old_student is None:
        return False
    
    old_student.name = student.name
    old_student.course = student.course
    old_student.marks = student.marks
    return True

def delete_by_id(student_id): #delete
    global students
    students = [s for s in students if s.id != student_id]
    return True

