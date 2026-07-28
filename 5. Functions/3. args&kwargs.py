"""
LESSON: *args and **kwargs
──────────────────────────
*args   → packs extra positional arguments into a tuple
**kwargs → packs extra keyword arguments into a dict
"""

# 1. *args (packs positional arguments into a tuple)
def print_args(*args):
    print(args)

print_args(1, 2, 3) 
# Output: (1, 2, 3)


# 2. **kwargs (packs keyword arguments into a dictionary)
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="Alice", age=25) 
# Output: {'name': 'Alice', 'age': 25}


# 3. Unpacking (Passing a dictionary to a function)
def create_profile(name, age):
    print(f"Profile created for {name}, Age: {age}")

user_data = {"name": "Suvadip", "age": 20}
create_profile(**user_data) 
# Output: Profile created for Suvadip, Age: 20
