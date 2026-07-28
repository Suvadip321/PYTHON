"""
LESSON: Input & Output
----------------------
input()  -> reads user input as a string
print()  -> displays output (see 1. Print.py for full details)
"""

# OUTPUT (print)
"""
We use print() to display values on the screen
"""
print("Hello, World!")
# Output: Hello, World!


# INPUT (input)
"""
input() is used to take input from the user as a string
"""
name = input("Enter your name: ")
print("Hello,", name)
# Example Input: Suvadip
# Output: Hello, Suvadip


# TYPE CONVERSION FOR INPUT
"""
By default, input() returns a string.
We need to convert it to int, float, etc. if needed.
"""
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1, "years old.")
# Example Input: 20
# Output: Next year, you will be 21 years old.


# MULTIPLE INPUTS ON ONE LINE
"""
Use split() to take multiple inputs separated by spaces
"""
x, y = input("Enter two numbers (space-separated): ").split()
x, y = int(x), int(y)
print(f"Sum: {x + y}")
# Example Input: 5 3
# Output: Sum: 8

