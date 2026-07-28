"""
LESSON: Lists
─────────────
Lists are mutable, ordered sequences. The most used data structure in Python.
Covers: creation, indexing, slicing, methods, shallow vs deep copy.
"""

# 1. LIST CREATION
print("1) LIST CREATION")
# Empty list
l1 = []
# List with same data type
l2 = [1, 2, 3, 4, 5]
# List with mixed data types
l3 = [3, "Python", 3.14, True]
# Nested list
l4 = [[1, 2], [3, 4]]

print("l1:", l1)
print("l2:", l2)
print("l3:", l3)
print("l4:", l4)
print("-" * 40)


# 2. LENGTH, INDEXING & SLICING
print("2) LENGTH, INDEXING & SLICING")
l = ["p", "y", "t", "h", "o", "n"]
print(f"Original list: {l}")

# len() -> returns number of elements in a list
print("Length:", len(l))

# Indexing: Access individual elements
print("\nIndexing:")
print("l[0]:", l[0])    # First element 'p'
print("l[-1]:", l[-1])   # Last element 'n'

# Slicing: Extract a sublist [start:end:step]
print("\nSlicing:")
print("l[0:6:1]:", l[0:6:1])
print("l[0:4]:", l[0:4])
print("l[:3]:", l[:3])
print("l[2:]:", l[2:])
print("l[:]:", l[:])
print("l[::2]:", l[::2])
print("l[::-1]:", l[::-1])
print("-" * 40)


# 3. LIST MUTABILITY
print("3) LIST MUTABILITY")
lst = [10, 20, 30]
print("Original:", lst)
lst[0] = 100
print("Modified list:", lst)
print("-" * 40)


# 4. LIST OPERATIONS
print("4) LIST OPERATIONS")
a = [1, 2, 3]
b = [4, 5, 6]
print("List a:", a)
print("List b:", b)

print("Concatenation (a + b):", a + b)  # Combine lists
print("Repetition (a * 3):", a * 3)       # Repeat list
print("-" * 40)


# 5. COMMON LIST METHODS
print("5) COMMON LIST METHODS")
lst = [3, 1, 4, 1, 5, 9]
print("Original list:", lst)

# Adding elements
lst.append(2)             # Add at end
lst.insert(1, 8)          # Add at index 1
lst.extend([10, 12, 16])  # Add multiple elements at the end
print("\nAfter append, insert, extend:", lst)

# Removing elements
lst.remove(1)   # Remove first occurrence of 1
popped_val = lst.pop()       # Remove last element and return it
lst.pop(0)      # Remove at index 0
print("After remove and pop:", lst)
print("Popped value:", popped_val)

# Sorting and reversing
lst.sort()               # Sort list in ascending order
print("\nSorted list:", lst)
lst.reverse()            # Reverse list
print("Reversed list:", lst)

# sorted() with key parameter
words = ["banana", "apple", "cherry"]
print("\nSorted by length:", sorted(words, key=len))
# Output: ['apple', 'banana', 'cherry']

# Counting and index
print("\nCount of 1:", lst.count(1))
print("Index of 5:", lst.index(5))

# Copying and clearing
lst_copy = lst.copy()
lst.clear()
print("\nCopied list:", lst_copy)
print("Cleared list:", lst)
print("-" * 40)


# 6. SHALLOW VS DEEP COPY
print("6) SHALLOW VS DEEP COPY")
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()       # inner lists are still shared
deep = copy.deepcopy(original)  # fully independent copy

print("Before modification:")
print("Original:", original)

original[0][0] = 999
print("\nAfter modifying original[0][0] = 999:")
print("Original:", original)    # [[999, 2], [3, 4]]
print("Shallow copy:", shallow)   # [[999, 2], [3, 4]]  — affected!
print("Deep copy:", deep)         # [[1, 2], [3, 4]]    — safe!
print("-" * 40)

