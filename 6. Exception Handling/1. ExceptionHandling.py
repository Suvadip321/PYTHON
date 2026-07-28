"""
LESSON: Exception Handling
──────────────────────────
Handle runtime errors gracefully.
Covers: try, except, finally, raising errors, and common exception types.
"""

# 1. Basic try / except
print("1) Basic try / except")

try:
    user_val = input("Enter an integer: ")
    value = int(user_val)
    print(f"Successfully parsed integer: {value}")
except Exception as e:
    print(f"Error caught: {e}")

print("-" * 40)


# 2. Multiple except blocks (Handling different failures)
print("2) Multiple except blocks")

try:
    user_div = input("Enter a number to divide 10 by: ")
    result = 10 / int(user_div)
    print(f"Result: {result}")
except ValueError:
    print("Invalid integer provided!")
except ZeroDivisionError:
    print("You cannot divide by zero!")

print("-" * 40)


# 3. The finally block (Always runs, used for cleanup)
print("3) The finally block")

try:
    print("Attempting to connect to database...")
    x = 0 / 0  
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    print("Cleaning up resources (This ALWAYS runs)")

print("-" * 40)


"""Common Built-in Exceptions"""

# 1. ValueError: Right type, but inappropriate value
# int("abc")

# 2. TypeError: Operation applied to an inappropriate type
# "5" + 5

# 3. KeyError: Dictionary key is not found
# my_dict = {"name": "Suvadip"}
# print(my_dict["age"])

# 4. IndexError: Sequence index is out of range
# my_list = [1, 2, 3]
# print(my_list[100])

# 5. FileNotFoundError: File requested does not exist
# open("this_file_does_not_exist.txt", "r")

# 6. ZeroDivisionError: Division or modulo by zero
# 10 / 0

