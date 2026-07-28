"""
LESSON: Type Hints
──────────────────
Type hints don't enforce types at runtime, but they:
    1. Enable IDE autocompletion (VS Code, PyCharm)
    2. Are MANDATORY for modern web frameworks (FastAPI)
    3. Make your code 10x easier to read.
"""
from typing import Optional, Any

# 1. BASIC VARIABLES & FUNCTIONS
print("1) Basic Variables & Functions")

# Variables
age: int = 25
is_active: bool = True
name: str = "Suvadip"

# Functions (Specify params and return type)
def greet(user: str) -> str:
    return f"Hello, {user}!"

print(greet(name))

print("-" * 40)


# 2. COLLECTIONS (Lists & Dictionaries)
print("2) Collections")

# In Python 3.9+, you can use lowercase 'list' and 'dict'
scores: list[float] = [95.5, 88.0, 92.5]
config: dict[str, int] = {"timeout": 30, "retries": 3}

def get_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

print(f"Average score: {get_average(scores)}")

print("-" * 40)


# 3. OPTIONAL & ANY
print("3) Optional & Any")

# Optional means the value can be the Type OR it can be None
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found

# Any means the value can literally be anything (Avoid this when possible!)
def process_data(data: Any) -> None:
    pass # Data could be a list, dict, str, int...

print("User 1:", find_user(1))
print("User 99:", find_user(99))

print("-" * 40)

