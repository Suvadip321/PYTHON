"""
LESSON: Tuples
──────────────
Tuples are immutable, ordered sequences.
Use tuples for fixed collections that shouldn't change (coordinates, configs, return values).
"""

# 1. TUPLE CREATION
print("1) TUPLE CREATION")
# Empty tuple
t1 = ()
# Tuple with elements
t2 = (1, 2, 3, 4)
# Tuple with mixed data types
t3 = (1, "Python", 3.14, True)
# Nested tuple
t4 = (1, (2, 3), 4)

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)
print("-" * 40)


# 2. LENGTH, INDEXING & SLICING
print("2) LENGTH, INDEXING & SLICING")
t = ("p", "y", "t", "h", "o", "n")
print(f"Original tuple: {t}")

# len() -> returns number of elements in a tuple
print("Length:", len(t))

# Indexing: Access individual elements
print("\nIndexing:")
print("t[0]:", t[0])    # First element 'p'
print("t[-1]:", t[-1])   # Last element 'n'
tuple_2d = ((1, 2), (3, 4), (5, 6))
print("tuple_2d[0][1]:", tuple_2d[0][1])

# Slicing: Extract a subtuple [start:end:step]
print("\nSlicing:")
print("t[0:6:1]:", t[0:6:1])
print("t[0:4]:", t[0:4])
print("t[:3]:", t[:3])
print("t[2:]:", t[2:])
print("t[:]:", t[:])
print("t[::2]:", t[::2])
print("t[::-1]:", t[::-1])
print("-" * 40)


# 3. TUPLE IMMUTABILITY
print("3) TUPLE IMMUTABILITY")
t = (10, 20, 30)
print("Original:", t)
# t[0] = 100            # Error, tuples are immutable
new_t = (100,) + t[1:]  # Create a new tuple
print("Modified tuple:", new_t)
print("-" * 40)


# 4. TUPLE OPERATIONS
print("4) TUPLE OPERATIONS")
a = (1, 2, 3)
b = (4, 5, 6)
print("Tuple a:", a)
print("Tuple b:", b)

print("Concatenation (a + b):", a + b)  # Combine tuples
print("Repetition (a * 3):", a * 3)       # Repeat tuple
print("-" * 40)


# 5. TUPLE METHODS
print("5) TUPLE METHODS")
t = (3, 1, 4, 1, 5, 9)
print("Original tuple:", t)

# Counting occurrences
print("Count of 1:", t.count(1))
# Index of first occurrence
print("Index of 4:", t.index(4))
print("-" * 40)


# 6. TUPLE UNPACKING
print("6) TUPLE UNPACKING")
# Basic unpacking
t = (10, 20, 30)
a, b, c = t
print("Tuple:", t)
print("Unpacked values:", a, b, c)

# Nested tuple unpacking
nested = (1, (2, 3), 4)
x, (y, z), w = nested
print("\nNested tuple:", nested)
print("Unpacked values:", x, y, z, w)

# Using * for variable-length unpacking
t2 = (1, 2, 3, 4, 5)
first, *middle, last = t2
print("\nTuple with * unpacking:", t2)
print("First:", first)       # 1
print("Middle:", middle)     # [2, 3, 4]
print("Last:", last)         # 5

# Swapping values using tuple unpacking
x, y = 5, 10
print("\nBefore swap: x =", x, ", y =", y)
x, y = y, x
print("After swap: x =", x, ", y =", y)
print("-" * 40)

