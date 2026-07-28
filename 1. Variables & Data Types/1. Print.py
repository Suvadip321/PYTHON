"""
LESSON: print() Function
─────────────────────────
The print() function is Python's primary way to display output.
Covers: basic usage, sep, end, escape characters, f-strings, .format()
"""

# BASIC USAGE
"""
The print() function is used to display output on the screen.
"""
print("My name is Suvadip and I am 20 years old.")
# Output: My name is Suvadip and I am 20 years old.


# PRINTING MULTIPLE ITEMS
"""
We can pass multiple values separated by commas.
"""
print("My name is", "Suvadip", "and I am", 20, "years old.")
# Output: My name is Suvadip and I am 20 years old.


# USING VARIABLES INSIDE PRINT
name = "Python"
version = 3.12
print("I am learning", name, "version", version)
# Output: I am learning Python version 3.12


# SEPARATOR (sep)
"""
By default, print() separates items with a space.
We can change it using 'sep' parameter.
"""
print("30", "06", "2025", sep="-")
# Output: 30-06-2025


# END PARAMETER
"""
By default, print() ends with a newline (\n).
We can change it using 'end' parameter.
"""
print("Hello", end=" ")
print("World")
# Output: Hello World


# ESCAPE CHARACTERS
"""
We can use escape characters like \n (new line), \t (tab), etc.
"""
print("First Line\nSecond Line")
# Output:
# First Line
# Second Line

print("Column1\tColumn2")
# Output: Column1    Column2


# FORMATTED STRINGS (f-strings) — Python 3.6+
"""
We can insert variables directly into strings using f-strings
"""
lang = "Python"
year = 2025
print(f"I am learning {lang} in {year}.")
# Output: I am learning Python in 2025.

