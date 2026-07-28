"""
LESSON: Assignment Operators
────────────────────────────
=    Assign
+=   Add and assign
-=   Subtract and assign
*=   Multiply and assign
/=   Divide and assign
//=  Floor-divide and assign
%=   Modulus and assign
**=  Exponent and assign
:=   Walrus operator (assign inside expressions, Python 3.8+)
"""

x = 10
print("x     =", x)    # 10

x += 5   # x = x + 5
print("x += 5:", x)     # 15

x -= 3   # x = x - 3
print("x -= 3:", x)     # 12

x *= 2   # x = x * 2
print("x *= 2:", x)     # 24

x /= 4   # x = x / 4
print("x /= 4:", x)     # 6.0

x //= 2  # x = x // 2
print("x //= 2:", x)    # 3.0

x %= 2   # x = x % 2
print("x %= 2:", x)     # 1.0

x **= 3  # x = x ** 3
print("x **= 3:", x)    # 1.0

