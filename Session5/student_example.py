# student_example.py
import student

john = student.Student("John Smith", 25, "Math")
jane = student.Student("Jane Doe", 33, "Physics")

john.add_grade("A")
jane.add_grade("B")

john.display_grades()
john.add_grade("C+")
john.display_grades()
jane.display_grades()