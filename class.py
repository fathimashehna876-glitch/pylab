class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            grade = 'A+'
        elif self.marks >= 80:
            grade = 'A'
        elif self.marks >= 70:
            grade = 'B'
        elif self.marks >= 60:
            grade = 'C'
        else:
            grade = 'D'
        return grade

    def display_details(self):
        grade = self.calculate_grade()
        print("\nStudent Details")
        print(f"Name      : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Marks     : {self.marks}")
        print(f"Grade     : {grade}")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks (out of 100): "))
student = Student(name, roll_no, marks)
student.display_details()
