"""
LESSON: Custom Exceptions
─────────────────────────
In Software Engineering, you shouldn't just raise generic `ValueError`s.
You create your own custom exceptions so your API can catch specific 
business logic failures (e.g. InsufficientFundsError).
"""


class InsufficientFundsError(Exception):
    """Raised when a user tries to buy something they can't afford."""
    pass


def process_payment(balance, cost):
    if balance < cost:
        raise InsufficientFundsError(f"Need {cost}, but only have {balance}")
    print("Payment successful!")


try:
    process_payment(balance=50, cost=100)
except InsufficientFundsError as e:
    print("Caught our custom error:", e)

