"""
LESSON: Type Casting
--------------------
Converting one data type to another.
Implicit  = Python does it automatically (type promotion).
Explicit  = You do it manually using int(), float(), str(), bool(), etc.
"""

# IMPLICIT TYPE CASTING
"""
Python automatically converts smaller data type into a larger one (type promotion).
"""
x = 10      # int
y = 3.5     # float
result = x + y   # int is promoted to float automatically
print("Result:", result, "| Type:", type(result))
# Output: Result: 13.5 | Type: <class 'float'>


# EXPLICIT TYPE CASTING
"""
Manually converting data types using int(), float(), str(), bool()
"""
# String to int
num_str = "100"
num_int = int(num_str)
print(num_str, "->", num_int, "| Type:", type(num_int))
# Output: 100 -> 100 | Type: <class 'int'>

# String to float
num_float = float("12.34")
print(num_float, "| Type:", type(num_float))
# Output: 12.34 | Type: <class 'float'>

# Float to int (decimal part is truncated, not rounded)
value = int(9.99)
print(value, "| Type:", type(value))
# Output: 9 | Type: <class 'int'>

# Number to string
num = 123
num_str = str(num)
print(num_str, "| Type:", type(num_str))
# Output: 123 | Type: <class 'str'>

# Boolean to int
print(int(True), int(False))
# Output: 1 0

# Int to boolean
print(bool(0), bool(1), bool(-5))
# Output: False True True


# COLLECTION CASTING
print("\nCollection casting:")
print(list("hello"))          # ['h', 'e', 'l', 'l', 'o']
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(tuple([1, 2, 3]))      # (1, 2, 3)
print(set([1, 2, 2, 3]))     # {1, 2, 3}

