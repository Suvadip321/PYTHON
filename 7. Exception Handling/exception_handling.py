# 1. try / except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")

# 2. Catch exception object
try:
    value = int("abc")
except ValueError as e:
    print(e)

# 3. Multiple except blocks (preferred)
try:
    value = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalid integer")
except ZeroDivisionError:
    print("Division by zero")

# 4. Catch multiple exceptions together
try:
    d = {}
    print(d["missing"])
except (KeyError, TypeError) as e:
    print(e)

# 5. Generic exception (use carefully)
def operation():
    pass

try:
    operation()
except Exception as e:
    print(e)

# 6. else block (runs only if no exception)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", result)

# 7. finally block (always runs)
try:
    f = open("file.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    if 'f' in locals():
        f.close()

# 8. Recommended real-world pattern
def load_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise RuntimeError("Required file is missing")

# 9. Raising exceptions manually
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# 10. Re-raising exceptions
try:
    operation()
except ValueError:
    print("Logging error")
    raise

# 11. Custom exceptions
class ValidationError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise ValidationError("Score must be between 0 and 100")

try:
    validate_score(150)
except ValidationError as e:
    print(e)

# 12. Common built-in exceptions (know these)
"""
ValueError          # Wrong value: int("abc")
TypeError           # Wrong type: "5" + 5
KeyError            # Dict key missing: d["missing"]
IndexError          # List index out of range: lst[100]
FileNotFoundError   # File doesn't exist
ZeroDivisionError   # Division by zero
AttributeError      # Attribute doesn't exist: obj.missing
ImportError         # Cannot import module
RuntimeError        # Generic runtime error
Exception           # Base class (catches all)
"""
