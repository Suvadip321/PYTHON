"""
LESSON: Identity Operators (is, is not)
---------------------------------------
'is'      -> checks if two objects have the SAME memory location (id)
'is not'  -> checks if two objects have DIFFERENT memory locations

Key difference: == checks VALUE equality, 'is' checks IDENTITY (same object).
"""

# Example 1: Numbers (small integers are cached in Python)
a = 10
b = 10
print(a is b)           # True (same memory for small integers)
print(a is not b)       # False

# Example 2: Large integers (may not share memory)
x = 1000
y = 1000
print(x is y)           # May or may not be True (depends on Python version/implementation)
print(x == y)           # True (values are equal even if memory differs)

# Example 3: Strings (interning may happen for small strings)
s1 = "hello"
s2 = "hello"
print(s1 is s2)       # True (string interning)
print(s1 == s2)       # True (values equal)

# Example 4: Lists (mutable, so memory is different)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True (same contents)
print(list1 is list2)   # False (different memory locations)

# Example 5: None check (best use of 'is')
val = None
print(val is None)         # True (recommended way to check None)
print(val is not None)     # False

