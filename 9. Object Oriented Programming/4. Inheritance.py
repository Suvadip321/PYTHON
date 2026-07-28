"""
LESSON: Inheritance
───────────────────
# Inheritance: A child class acquiring properties and methods from a parent class
# Parent Class (Superclass): The class being inherited from
# Child Class (Subclass): The class that inherits
# super(): Function used to call methods from the parent class
"""

class Employee:  # Parent Class (Superclass)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def work(self):
        return f"{self.name} is working at salary {self.salary}."

class Manager(Employee):  # Child Class (Subclass)
    def __init__(self, name, salary, department):
        # super() calls the parent's __init__ so we don't have to rewrite it!
        super().__init__(name, salary)
        self.department = department

    def work(self):
        # We can override parent methods
        return f"{self.name} is managing the {self.department} department."


emp = Employee("Alice", 50000)
mgr = Manager("Bob", 90000, "Engineering")

print(emp.work())
print(mgr.work())

