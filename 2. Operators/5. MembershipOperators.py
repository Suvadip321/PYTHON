"""
LESSON: Membership Operators (in, not in)
──────────────────────────────────────────
'in'     -> True if value is found in the sequence
'not in' -> True if value is NOT found in the sequence
Works with: str, list, tuple, set, dict (keys only)
"""

# In STRING
text = "Python Programming"
print('P' in text)          # True
print('z' in text)          # False
print('Pro' in text)        # True
print('thon' not in text)   # False


# In LIST / TUPLE
fruits = ["apple", "banana", "cherry"]
print("\napple in fruits:", "apple" in fruits)        # True
print("mango in fruits:", "mango" in fruits)          # False
print("banana not in fruits:", "banana" not in fruits) # False

numbers = (1, 2, 3, 4, 5)
print("3 in numbers:", 3 in numbers)       # True
print("10 not in numbers:", 10 not in numbers)  # True


# In SET
colors = {"red", "green", "blue"}
print("\nred in colors:", "red" in colors)          # True
print("yellow not in colors:", "yellow" not in colors)   # True


# In DICTIONARY (checks only keys, not values)
person = {"name": "Alice", "age": 25, "city": "Delhi"}
print("\nname in person:", "name" in person)      # True (key check)
print("Alice in person:", "Alice" in person)       # False (values not checked)
print("city not in person:", "city" not in person)  # False


# Combine with conditional logic
if "banana" in fruits:
    print("\nBanana is in the fruit list!")

if "mango" not in fruits:
    print("Mango is not in the fruit list!")

