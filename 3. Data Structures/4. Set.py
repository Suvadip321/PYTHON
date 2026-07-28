"""
LESSON: Sets
────────────
Sets are mutable, unordered collections of unique elements.
Key advantage: O(1) membership test vs O(n) for lists.
"""

# 1. SET CREATION
print("1) SET CREATION")
# Empty set (use set(), {} creates a dict)
s1 = set()
# Set with elements
s2 = {1, 2, 3, 4, 5}
# Set with mixed data types
s3 = {1, "Python", 3.14, True}
# Duplicate elements are automatically removed
s4 = {1, 2, 2, 3, 3, 3}

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)   # {1, 2, 3}
print("-" * 40)


# 2. SET MUTABILITY (Adding / Removing)
print("2) SET MUTABILITY")
s = {1, 2, 3}
print("Original:", s)

s.add(4)          # Add single element
s.update({5, 6})  # Add multiple elements
print("After add and update:", s)

s.remove(2)    # Remove element (error if not found)
s.discard(10)  # Remove element (no error if not found)
print("After remove and discard:", s)

popped = s.pop()  # Remove arbitrary element
print("After pop:", s)

# Copying and clearing
s_copy = s.copy()
s.clear()      # Remove all elements
print("\nCopied set:", s_copy)
print("After clear:", s)
print("-" * 40)


# 3. SET OPERATIONS (Math logic)
print("3) SET OPERATIONS")
a = {1, 2, 3}
b = {3, 4, 5}
print("Set a:", a)
print("Set b:", b)

print("Union (a | b):", a.union(b))                              # {1, 2, 3, 4, 5}
print("Intersection (a & b):", a.intersection(b))                  # {3}
print("Difference (a - b):", a.difference(b))                      # {1, 2}
print("Symmetric Difference (a ^ b):", a.symmetric_difference(b))  # {1, 2, 4, 5}
print("-" * 40)


# 4. SET METHODS (Checking conditions)
print("4) SET METHODS")
s = {1, 2, 3, 4}

print("Original set:", s)
print("Length:", len(s))
print("Is disjoint with {6,7}?:", s.isdisjoint({6, 7}))           # True
print("Is subset of {1,2,3,4,5,6}?:", s.issubset({1,2,3,4,5,6}))  # True
print("Is superset of {1,2}?:", s.issuperset({1,2}))              # True
print("-" * 40)


# 5. FROZEN SET (IMMUTABLE)
print("5) FROZEN SET")
frozen = frozenset([1, 2, 3])
print(f"frozen set: {frozen}")
# frozen.add(4)  # This would raise an AttributeError!
print("-" * 40)

