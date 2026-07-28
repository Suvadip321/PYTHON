"""
LESSON: Dunder (Magic) Methods
──────────────────────────────
# Dunder Methods: "Double Underscore" methods (e.g., __init__) built into Python
# Operator Overloading: Customizing how standard operators (+, -, ==) work on your objects
# Object Representation: Customizing how an object looks when printed (__str__, __repr__)
"""

class Vector:
    def __init__(self, x=0, y=0):      # __init__: object constructor
        self.x = x
        self.y = y

    def __str__(self):             # __str__: user-friendly string
        return f"({self.x}, {self.y})"
    
    def __repr__(self):            # __repr__: unambiguous representation
        return f"Vector({self.x}, {self.y})"

    def __len__(self):             # __len__: length (used with len())
        return 2

    def __getitem__(self, index):   # __getitem__: get at index
        return (self.x, self.y)[index]

    def __setitem__(self, key, value):  # __getitem__: set at index
        if key == 0: self.x = value
        elif key == 1: self.y = value
        else: raise IndexError("Vector index out of range. Use 0 or 1.")

    def __iter__(self):            # __iter__: makes object iterable
        return iter((self.x, self.y))

    def __eq__(self, other):       # __eq__: equality check
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):      # __add__: + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):     # __mul__: * operator
        return Vector(self.x * other.x, self.y * other.y)

    def __call__(self):            # __call__: make object callable
        return f"Vector at ({self.x}, {self.y})"

v1 = Vector(3, 4)

print("str:", v1)                # (2, 3)
print("repr:", repr(v1))         # Vector(2, 3)
print("len:", len(v1))           # 2
print("iter:", list(v1))         # [2, 3]
print("indexing:", v1[0], v1[1]) # 2 3
v2 = Vector()
v2[0] = 6
v2[1] = 8
print(v1)
print("equality:", v1 == v2)     # False
print("addition:", v1 + v2)      # (9, 12)
print("multiplication:", v1 * v2) # (18, 32)
print("call:", v1())             # Vector at (3, 4)

