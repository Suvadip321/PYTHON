"""
LESSON: for Loop
────────────────
Iterates over any iterable (range, str, list, tuple, set, dict, etc.).
Covers: range(), iterating data structures, nested loops.
"""

# for loop with range()
print("for loop with range:\n")

# range(stop) → 0 to stop-1
for i in range(5):
    print(i, end=" ")
print()
# Output: 0 1 2 3 4

# range(start, stop) → start to stop-1
for i in range(1, 6):
    print(i, end=" ")
print()
# Output: 1 2 3 4 5

# range(start, stop, step) → skips by step
for i in range(1, 10, 2):
    print(i, end=" ")
print()
# Output: 1 3 5 7 9

# Decreasing loop using negative step
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")
# Output: 10 9 8 7 6 5 4 3 2 1


# Iterating with for loop over different data structures
# String
print("Iterating over a string:")
name = "Python"
for ch in name:
    print(ch)
print()

# List
print("Iterating over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()

# Tuple
print("Iterating over a tuple:")
numbers = (2, 4, 6, 8)
for num in numbers:
    print(num)
print()

# Set
print("Iterating over a set:")
unique_nums = {10, 20, 30, 40}
for val in unique_nums:
    print(val)
print()

# Dictionary (keys)
print("Iterating over a dictionary (keys):")
student = {"name": "Suvadip", "age": 20, "grade": "A"}
for key in student:
    print(key, "->", student[key])
print()

# Dictionary (keys and values)
print("Iterating over a dictionary (keys and values):")
for key, value in student.items():
    print(key, "->", value)
print()


# Nested for loops
# Example: Pattern printing
print("Right-angled triangle pattern:")
row = 5
for i in range(1, row+1):
    for j in range(i):
        print("*", end=" ")
    print()

