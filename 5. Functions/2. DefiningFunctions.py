"""
LESSON: Defining Functions
──────────────────────────
How to create your own functions in Python.
Covers: basic functions, parameters, defaults, keywords, return, scope,
        recursion, type hints, and docstrings.
"""

# 1. Defining and Calling a Simple Function
def greet():
    """A basic function with no parameters"""
    print("Hello, welcome to Python!")

greet()  # Calling the function


# 2. Parameters and Arguments
def add(a, b):
    """Function with parameters"""
    return a + b

print("Sum:", add(5, 3))  # Arguments passed


# 3. Default Parameters
def power(base, exponent=2):
    """Default exponent is 2 (square)"""
    return base ** exponent

print("Square (default exponent):", power(4))
print("Cube (custom exponent):", power(4, 3))


# 4. Keyword Arguments
def introduce(name, age, city):
    """Using keyword arguments"""
    print(f"My name is {name}, I am {age} years old, from {city}.")

introduce(age=20, name="Alice", city="New York")  # Order doesn't matter with keywords


# 5. Print vs Return
def square_print(x):
    """Only prints result (cannot be reused)"""
    print(x ** 2)

def square_return(x):
    """Returns value (can be reused)"""
    return x ** 2

square_print(5)
result = square_return(5)
print("Square using return:", result, "and we can reuse it.")


# 6. Return statement
def check_even(num):
    """Return (None) ends function early"""
    if num % 2 == 0:
        return  # Exits function, returns None
    print(num, "is odd")

check_even(4)   # Nothing printed
check_even(7)   # Prints since it's odd


# 7. Scope of Variables and global keyword
x = 10  # Global variable

def modify_global():
    global x       # Modify global variable
    x = 20
    print("Inside function, x =", x)

modify_global()
print("Outside function, x =", x)  # Changed globally


# 8. Returning Multiple Values
def math_operations(a, b):
    """Return multiple values as a tuple"""
    return a + b, a - b, a * b, a / b

sum, diff, prod, div = math_operations(10, 5)
print("Multiple returns:", sum, diff, prod, div)


# 9. Nested Function
def outer_function(text):
    """A function inside another function"""
    def inner_function():
        print("Inner function says:", text)
    inner_function()  # Call inner function

outer_function("Hello from inner function!")


# 10. Recursion (example: factorial of a number)
def factorial(n):
    """Recursive factorial function"""
    if n == 0:
        return 1   # Base case
    return n * factorial(n - 1)  # Recursive call

print("Factorial of 5:", factorial(5))


# 11. Passing Functions as Arguments (First-Class Functions)
def apply_operation(func, value):
    """Takes another function as an argument and executes it"""
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

print("\nPassing 'double' function:", apply_operation(double, 5))   # 10
print("Passing 'square' function:", apply_operation(square, 5))   # 25


# 12. Closures (Functions that remember variables)
def multiplier(factor):
    """The outer function takes a factor"""
    def inner(number):
        """The inner function 'remembers' the factor even after outer finishes!"""
        return number * factor
    return inner

# Create a function that always multiplies by 5
multiply_by_5 = multiplier(5)

print("\nClosure execution:")
print("3 * 5 =", multiply_by_5(3))   # 15
print("10 * 5 =", multiply_by_5(10)) # 50

