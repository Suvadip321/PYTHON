"""
LESSON: Relational / Comparison Operators
──────────────────────────────────────────
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
"""

a = 10
b = 20

print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b :", a > b)    # False
print("a < b :", a < b)    # True
print("a >= b:", a >= b)   # False
print("a <= b:", a <= b)   # True


# CHAINED COMPARISONS — Pythonic way to check ranges
x = 15
print(f"\n1 < {x} < 20 :", 1 < x < 20)    # True
print(f"10 <= {x} <= 15:", 10 <= x <= 15)  # True

