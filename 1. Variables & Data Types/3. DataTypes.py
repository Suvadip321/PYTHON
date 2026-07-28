"""
LESSON: Data Types
──────────────────
A datatype defines the type of value stored in a variable.

Python built-in scalar types:
    int, float, complex, str, bool, NoneType, bytes
Use type() to check, isinstance() to verify.
"""

# INTEGER (int)
age = 20
print("Age:", age, "| Type:", type(age))
# Output: Age: 20 | Type: <class 'int'>

# FLOAT (float)
pi = 3.14159
print("Pi:", pi, "| Type:", type(pi))
# Output: Pi: 3.14159 | Type: <class 'float'>

# COMPLEX (complex)
x = 7j
print("x:", x, "| Type:", type(x))
# Output: x: 7j | Type: <class 'complex'>

# STRING (str)
language = "Python"
print("Language:", language, "| Type:", type(language))
# Output: Language: Python | Type: <class 'str'>

# BOOLEAN (bool) -> True / False
is_student = True
print("is_student:", is_student, "| Type:", type(is_student))
# Output: is_student: True | Type: <class 'bool'>

# NONE TYPE (None) — represents absence of value
data = None
print("data:", data, "| Type:", type(data))
# Output: data: None | Type: <class 'NoneType'>

# isinstance() — check if a value is of a specific type
print("\nisinstance checks:")
print(isinstance(age, int))           # True

# id() — memory address of an object
print("\nMemory address of age:", id(age))
# Output: <some unique number>

