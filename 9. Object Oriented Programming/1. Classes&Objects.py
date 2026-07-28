"""
LESSON: Classes & Objects
─────────────────────────
# Class: A blueprint for creating objects
# Object (Instance): A real entity created from a class
# Class Attributes: Shared by all objects (same value for all objects)
# Instance Attributes: Belong to individual object (can have different value for individual objects)
# Constructor (__init__): A special method called automatically when an object is created
# Methods: Functions inside a class
"""

class Student:
    # class attributes
    college = "SKFGI"
    dept = "AIML"
    
    # constructor
    def __init__(self, name, roll):
        # instance attributes
        self.name = name
        self.roll = roll
    
    # class method(s)
    def info(self):
        return f"Student Name: {self.name}\nCollege Name: {Student.college}\nDepartment: {Student.dept}\nRoll: {self.roll}"


s1 = Student(name="Suvadip Kushari", roll=43)   # an object/instance of class Student
print(s1.name)
print(s1.college)
print(s1.dept)
print(s1.roll)

s2 = Student(name="Alice", roll=9)
s3 = Student(name="Bob", roll=13)

print(s2.info())
print(s3.info())

