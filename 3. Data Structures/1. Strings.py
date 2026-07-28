"""
LESSON: Strings
───────────────
Strings are immutable sequences of characters.
Covers: creation, indexing, slicing, operations, and common methods.
"""

# 1. STRING CREATION
print("1) STRING CREATION")
s1 = 'Hello'
s2 = "World"
s3 = '''
Python supports
multi-line strings
'''
s4 = ""

print("s1:", s1)
print("s2:", s2)
print("s3:", s3.strip()) # Stripped just for clean output
print("s4 (Empty string):", s4)
print("-" * 40)


# 2. LENGTH, INDEXING & SLICING
print("2) LENGTH, INDEXING & SLICING")
s = "python"
print(f"Original string: '{s}'")

# len() -> returns number of characters in a string
print("Length:", len(s))

# Indexing: Access individual characters
print("\nIndexing:")
print("s[0]:", s[0])    # First character 'p'
print("s[-1]:", s[-1])   # Last character 'n'

# Slicing: Extract a substring [start:end:step]
print("\nSlicing:")
print("s[0:6:1]:", s[0:6:1])     # 'python' (full string)
print("s[0:4]:", s[0:4])       # 'pyth' (from index 0 to 3)
print("s[:3]:", s[:3])        # 'pyt' (from start to 2)
print("s[2:]:", s[2:])        # 'thon' (from index 2 to end)
print("s[:]:", s[:])         # 'python' (full string)
print("s[::2]:", s[::2])       # 'pto' (every 2nd character)
print("s[::-1]:", s[::-1])      # 'nohtyp' (reversed string)
print("-" * 40)


# 3. STRING IMMUTABILITY
print("3) STRING IMMUTABILITY")
word = "Hello"
# word[0] = "J"             # Cannot change string directly
new_word = "J" + word[1:]   # Correct way: create a new string
print("Original:", word)
print("New word:", new_word)
print("-" * 40)


# 4. STRING OPERATIONS
print("4) STRING OPERATIONS")
a = "Python"
b = "Programming"

print("Concatenation:", a + " " + b)   # Join strings
print("Repetition:", a * 3)            # Repeat string 3 times
print("-" * 40)


# 5. COMMON STRING METHODS
print("5) COMMON STRING METHODS")
s = "python programming is fun!"
print(f"Original string: '{s}'\n")

# Conversion
print("capitalize():", s.capitalize())  # Capitalize first letter of string
print("lower():", s.lower())            # Convert all characters to lowercase
print("upper():", s.upper())            # Convert all characters to uppercase
print("title():", s.title())            # Capitalize first letter of each word
print("strip():", s.strip())            # Remove spaces from both ends

# Searching and counting
print("\nfind('prog'):", s.find("prog"))                  # Index of substring
print("count('m'):", s.count('m'))                      # Count occurrences of 'm'
print("startswith('python'):", s.startswith("python"))  # Check if starts with
print("endswith('fun!'):", s.endswith("fun!"))           # Check if ends with

# Replacing substring
print("\nreplace('fun', 'awesome'):", s.replace("fun", "awesome"))

# Splitting and Joining
words = s.split()                         # Split string into list of words
print("\nsplit():", words)
joined = "-".join(words)                  # Join list into string with delimiter '-'
print("join():", joined)
print("-" * 40)


# 6. STRING CHECKING METHODS
print("6) STRING CHECKING METHODS")
check_str = "Python3"
print(f"Checking string: '{check_str}'\n")

print("isalpha():", check_str.isalpha())     # False, contains a number
print("isdigit():", check_str.isdigit())     # False, contains letters
print("isalnum():", check_str.isalnum())     # True, letters + numbers
print("islower():", check_str.islower())     # False, not all lowercase
print("isupper():", check_str.isupper())     # False, not all uppercase
print("-" * 40)

