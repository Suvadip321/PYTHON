"""
LESSON: enumerate() & zip()
---------------------------
enumerate() ? adds an index counter to any iterable
zip()       ? pairs elements from multiple iterables together
"""

# -- ENUMERATE --
"""Returns (index, element) pairs. Avoids manual counter variables."""

fruits = ["apple", "banana", "cherry"]

for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# Output: 0 apple / 1 banana / 2 cherry

# Start from a custom index
print("\nWith start=1:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")
# Output: 1. apple / 2. banana / 3. cherry

print()

# -- ZIP --
"""Pairs elements from two or more iterables. Stops at the shortest."""

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(name, score)
# Output: Alice 85 / Bob 92 / Charlie 78

# Zip to create a dictionary
name_score_dict = dict(zip(names, scores))
print("\nDict from zip:", name_score_dict)
# Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}

