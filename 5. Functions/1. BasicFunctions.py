"""
LESSON: Built-in Functions
--------------------------
Python's most commonly used built-in functions.
No imports needed — these are always available.
"""

# 1. Output and Input
print("1) Output and Input")
name = input("Enter your name: ")
print(f"Welcome, {name}!")
print("-" * 40)


# 2. Type Checking and Conversion
print("2) Type Checking and Conversion")
x = "100"
print(x, type(x))

y = int(x)
z = float(x)
print(y, type(y))
print(z, type(z))
print("-" * 40)


# 3. Abs, Rounding, Power
print("3) Abs, Rounding and Power")
print(abs(-25))            # 25
print(round(3.14159, 2))   # 3.14
print(pow(2, 3))           # 8
print("-" * 40)


# 4. Length, Min, Max, Sum
print("4) Length, Min, Max, Sum")
print(len("Python"))         # 6
print(len([1, 2, 3, 4]))    # 4

numbers = [5, 10, 2, 8]
print(min(numbers))   # 2
print(max(numbers))   # 10
print(sum(numbers))   # 25
print("-" * 40)


# 5. Sorting
print("5) Sorting")
nums = [4, 1, 7, 3, 5]
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))
print("-" * 40)


# 6. Type Casting Helpers
print("6) Type Casting Helpers")
num = 122333

String = str(num)
print(String)

List = list(String)
print(List)

Set = set(List)
print(Set)
print("-" * 40)


# 7. Checking Conditions
print("7) Checking Conditions (all / any)")
print(all([True, True, True]))    # True  — all are True
print(all([True, False, True]))   # False — one is False
print(any([False, True, False]))  # True  — at least one True
print(any([False, False, False])) # False — none True
print("-" * 40)


# 8. Useful Iteration Helpers
print("8) Iteration Helpers")
print("reversed:", list(reversed([1, 2, 3])))       # [3, 2, 1]
print("enumerate:", list(enumerate(["a", "b"])))     # [(0, 'a'), (1, 'b')]
print("zip:", list(zip([1, 2], ["x", "y"])))         # [(1, 'x'), (2, 'y')]
print("map:", list(map(lambda x: x * 2, [1, 2, 3]))) # [2, 4, 6]
print("filter:", list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))) # [2, 4, 6]
print("-" * 40)


# 9. Character Encodings (ord, chr)
print("9) Character Encodings (ord, chr)")
print("ord('A'):", ord('A'))  # 65 (ASCII value)
print("chr(65):", chr(65))    # 'A' (Character from ASCII)
print("-" * 40)


# 10. Object Inspection (id, isinstance)
print("10) Object Inspection (id, isinstance)")
x = 10
print(f"id(x): {id(x)}")                              # Memory address
print(f"isinstance(x, int): {isinstance(x, int)}")    # True (better than type())
print("-" * 40)

