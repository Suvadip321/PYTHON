"""
LESSON: Dictionaries
────────────────────
Dictionaries are mutable, unordered (insertion-ordered in 3.7+) key-value stores.
Keys must be hashable (immutable). The workhorse of config, JSON, and data handling.
"""

# 1. DICTIONARY CREATION
print("1) DICTIONARY CREATION")
# Empty dictionary
dict1 = {}
# Dictionary with key-value pairs
dict2 = {"name": "Alice", "age": 25, "city": "New York"}
# Dictionary with mixed keys
dict3 = {1: "one", "two": 2, 3.0: "three"}
# Nested dictionary
dict4 = {
    "person1": {"name": "Bob", "age": 30, "city": "Paris"},
    "person2": {"name": "Charlie", "age": 27, "city": "London"}
}

print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)
print("dict4:", dict4)
print("-" * 40)


# 2. ACCESSING ELEMENTS
print("2) ACCESSING ELEMENTS")
print("Accessing elements (dict2):")
print("Name:", dict2["name"])                          # Direct key access
print("Age:", dict2.get("age"))                        # Using get()
print("Country:", dict2.get("country", "Not Found"))   # Default if key missing

print("\nAccessing elements (dict4):")
print("person1 name:", dict4["person1"]["name"])
print("person1 age:", dict4["person1"]["age"])
print("person1 city:", dict4["person1"]["city"])
print("-" * 40)


# 3. DICTIONARY MUTABILITY
print("3) DICTIONARY MUTABILITY")
print("Original dict2:", dict2)

# Add and update
dict2["country"] = "USA"     # Add new key-value pair
dict2["age"] = 26            # Update existing key
print("\nAfter adding/updating:", dict2)

# Deleting elements
del dict2["city"]                  # Delete by key
popped_val = dict2.pop("country")  # Remove and return value
print("After deletions:", dict2)
print("Popped value:", popped_val)
print("-" * 40)


# 4. DICTIONARY METHODS
print("4) DICTIONARY METHODS")
sample = {"a": 1, "b": 2, "c": 3}
print("Original dictionary:", sample)

print("\nLength:", len(sample))
print("Keys:", sample.keys())     # dict_keys(['a', 'b', 'c'])
print("Values:", sample.values()) # dict_values([1, 2, 3])
print("Items:", sample.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])

copy_dict = sample.copy()         # Copy dictionary
sample.clear()                    # Clear dictionary
print("\nCopied dictionary:", copy_dict)
print("Cleared dictionary:", sample)
print("-" * 40)


# 5. ADDITIONAL USEFUL OPERATIONS (Merging)
print("5) ADDITIONAL USEFUL OPERATIONS")
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
print("dict_a:", dict_a)
print("dict_b:", dict_b)

# Merge two dictionaries (Python 3.9+)
merged_dict = dict_a | dict_b
print("\nMerged dictionary (dict_a | dict_b):", merged_dict)

# Update dictionary with another (modifies dict_a in place)
dict_a.update(dict_b)
print("Updated dict_a with dict_b (dict_a.update):", dict_a)
print("-" * 40)

