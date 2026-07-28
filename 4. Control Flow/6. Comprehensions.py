"""
LESSON: Comprehensions
----------------------
Concise syntax for creating lists, sets, dicts, and generators.

Syntax:
    List:      [expr for item in iterable if condition]
    Set:       {expr for item in iterable if condition}
    Dict:      {key: val for item in iterable if condition}
    Generator: (expr for item in iterable if condition)
"""

# LIST COMPREHENSIONS
print("LIST COMPREHENSIONS:")

nums = [x for x in range(1, 11)]           
print("Numbers:", nums)                      

sqrs = [x**2 for x in nums]            
print("Squares:", sqrs)                 

evens = [x for x in nums if x % 2 == 0] 
print("Evens:", evens)                            


# SET COMPREHENSIONS
print("\nSET COMPREHENSIONS:")

letters = {ch for ch in "hello world" if ch.isalpha()}   # Unique letters
print("Letters:", letters)


# DICTIONARY COMPREHENSIONS
print("\nDICT COMPREHENSIONS:")

word = "programming"
freq = {ch: word.count(ch) for ch in set(word) if ch.isalpha()}   # Character frequency
print("Char Frequency:", freq)


# GENERATOR EXPRESSIONS
print("\nGENERATOR (Tuple-like):")

gen = (x**2 for x in range(5))
print(gen)              # <generator object ...>
print(list(gen))        # [0, 1, 4, 9, 16]  — consumed once

# Convert generator to tuple
tuple_comp = tuple(x**3 for x in range(1, 6))
print("Tuple from Generator:", tuple_comp)   # (1, 8, 27, 64, 125)

