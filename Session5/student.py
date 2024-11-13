# student.py

class Student:
    
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
        self.grades = []
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def display_grades(self):
        print(self.grades)
        