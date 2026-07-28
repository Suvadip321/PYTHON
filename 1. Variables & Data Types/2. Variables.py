"""
LESSON: Variables
─────────────────
A variable is a name that stores a value in memory.
Python is dynamically typed -> no need to declare type explicitly.
"""

x = 10            # int
y = 3.14          # float
z = 5j            # complex
name = "Python"   # str
is_active = True  # bool
data = None       # NoneType

print(x, y, z, name, is_active, data)
# Output: 10 3.14 5j Python True None

# Dynamic typing — a variable can change type
x = "now I'm a string"
print(x, type(x))
# Output: now I'm a string <class 'str'>


# Assigning multiple values to multiple variables in one line
a, b, c = 1, 2, 3
print(a, b, c)
# Output: 1 2 3

# Assigning the same value to multiple variables
p = q = r = 0
print(p, q, r)
# Output: 0 0 0


# VARIABLE NAMING RULES
"""
- Cannot start with a number
- Can contain letters, numbers, underscores
- Case-sensitive (age, Age, AGE are all different)
- Keywords (like for, if, while) cannot be used as variable names
"""

