"""
LESSON: Polymorphism (Duck Typing)
──────────────────────────────────
# Polymorphism: "Many forms", using a single interface for different data types
# Method Overriding: Child class replacing a parent's method with its own version
# Duck Typing: Python's dynamic polymorphism ("If it walks and quacks like a duck, it's a duck")
"""

# Polymorphism allows the same interface or method name to behave differently depending on the object or context

# Method Overriding
class Animal:  # Parent Class
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):  # Child Class
    def sound(self):  # Overrides the parent's sound method
        print("Dog barks.")
        
Animal().sound()
Dog().sound()

# Duck Typing
class Human:
    def talk(self):  # Same method name
        print("Hello!")
    
class Duck:
    def talk(self):  # Same method name
        print("Quack")
    
Human().talk()
Duck().talk()
