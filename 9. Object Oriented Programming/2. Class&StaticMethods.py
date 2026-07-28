"""
LESSON: Class Methods & Static Methods
──────────────────────────────────────
# Instance Method: Takes 'self', modifies specific object
# Class Method: Takes 'cls', modifies class state (shared by all objects)
# Static Method: Doesn't take 'self' or 'cls', just a normal function bundled in a class
"""

class Math:
  pi = 3.141     # class attribute
  
  def __init__(self, radius):
    self.radius = radius     # instance attribute
    
  # Instance method (works on instance attributes as well as class attributes)
  def area(self):
    return Math.pi * self.radius * self.radius
  
  # Class method (works on class attributes only)
  @classmethod
  def circleArea(cls, radius):
    return cls.pi * radius * radius
  
  # Static method (utility function, independent of class/instance attributes)
  @staticmethod
  def add(a, b):
    return a + b


circle = Math(radius=7)
print(f"Instance method: {circle.area()}")

print(f"Class method: {Math.circleArea(radius=7)}")

print(f"Static method: {Math.add(3, 10)}")
