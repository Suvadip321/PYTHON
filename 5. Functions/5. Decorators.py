"""
LESSON: Decorators (@decorator)
──────────────────
A decorator is simply a function that wraps another function. 
It allows you to run code BEFORE and AFTER the original function 
without actually modifying the original function's code.
"""

# 1. THE BASIC DECORATOR
def my_decorator(func):
    """This is the wrapper function."""
    def wrapper():
        print("--- Something happens BEFORE the function runs ---")
        func()  # Run the original function
        print("--- Something happens AFTER the function runs ---")
    
    return wrapper


@my_decorator
def say_hello():
    print("Hello! I am the original function.")

say_hello()


# 2. HANDLING ARGUMENTS (*args, **kwargs)
# If you try to use `my_decorator` on a function that takes arguments (like `greet(name)`), 
# it will crash! To fix this, we use *args and **kwargs in the wrapper.

def smart_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n--- Decorator Started ---")
        func(*args, **kwargs)  # Pass any arguments straight through to the function!
        print("--- Decorator Finished ---")
    
    return wrapper


@smart_decorator
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("Alice", 25)
