"""
LESSON: Logical Operators
─────────────────────────
and  -> True only if BOTH conditions are True
or   -> True if AT LEAST ONE condition is True
not  -> Reverses the Boolean value
"""

# AND
print("AND Operator:")
print(True and True)    # True (both are True)
print(True and False)   # False (one is False)
print(False and False)  # False (both are False)

# OR
print("\nOR Operator:")
print(True or True)     # True (both True)
print(True or False)    # True (one True)
print(False or False)   # False (none True)

# NOT
print("\nNOT Operator:")
print(not True)   # False
print(not False)  # True


# TRUTHY & FALSY VALUES
"""
Falsy values: 0, 0.0, '', [], {}, set(), None, False
Truthy values: everything else
"""
