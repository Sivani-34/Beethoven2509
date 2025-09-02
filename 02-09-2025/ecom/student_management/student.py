class Student:
    def __init__(self, name, course, marks):
        self.id = None
        self.name = name
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Course: {self.course}, Marks: {self.marks}"
    