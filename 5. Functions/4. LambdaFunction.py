"""
LESSON: Lambda Functions
────────────────────────
Lambda functions are anonymous (no name) functions defined using the 'lambda' keyword.
They are typically used for short, simple functions that are used only once or inline.

Syntax: lambda arguments: expression
"""

greet = lambda: "Hello, this is lambda function!"
print(greet())

sqrt = lambda x: x**0.5
print(sqrt(9))       # 3.0

add = lambda a, b: a + b
print(add(3, 7))     # 10


# Using lambda with map()
"""map() applies a function to every element of a list"""
nums = [1, 2, 3, 4, 5, 6, 7]
squares = list(map(lambda x: x**2, nums))
print(squares)       # [1, 4, 9, 16, 25, 36, 49]


# Using lambda with filter()
"""filter() keeps elements that satisfy a condition"""
nums = [1, 2, 3, 4, 5, 6, 7]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)         # [2, 4, 6]


# Using lambda with sorted() — very common in practice
"""sorted(key=...) uses a function to determine sort order"""
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print("\nSorted by score:", by_score)
# Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

