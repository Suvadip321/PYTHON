"""
LESSON: Abstraction
───────────────────
# Abstraction: Hiding complex implementation details and showing only essential features
# Abstract Class (ABC): A blueprint class that cannot be instantiated on its own
# Abstract Method: A method declared in a parent that MUST be written in the child
"""

# Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class (Blueprint)
    @abstractmethod
    def start(self):
        return "Vehicle must start"
    
    @abstractmethod
    def stop(self):
        return "Vehicle must stop"
    
class Bike(Vehicle):  # Concrete Class (Usable)
    def start(self):
        return "Bike starts"
    def stop(self):
        return "Bike stops"

bike = Bike()
print(bike.start())
print(bike.stop())

class Car(Vehicle):  # Incomplete Concrete Class (does not have stop method)
    def start(self):
        pass

# car = Car() # this will throw error, because to be a vehicle it must have start and stop function

