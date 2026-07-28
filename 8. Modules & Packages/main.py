"""
LESSON: Modules & Packages
──────────────────────────
A module is a single .py file containing reusable code.
A package is a folder containing multiple modules.
"""
# 1. Importing a whole library
import math

# 2. Importing specific functions
from math import ceil, floor

# 3. Importing with an alias (Used constantly in Data Science, e.g., import pandas as pd)
import datetime as dt

# 4. Importing from your own local files
from src.math_utils import add, sub, mul, div


def main():
    print("1) Using Standard Libraries")

    print("pi:", math.pi)
    print("ceil(2.5):", ceil(2.5), "floor(2.5):", floor(2.5))
    print("Today:", dt.date.today())

    print("-" * 40)

    print("2) Using Your Own Code (from src.math_utils)")

    print("add(7, 3):", add(7, 3))
    print("sub(7, 3):", sub(7, 3))
    print("mul(7, 3):", mul(7, 3))
    print("div(7, 3):", div(7, 3))

    print("-" * 40)


# The __name__ guard 
# This ensures that `main()` ONLY runs if you execute THIS file directly.
# If someone else imports this file, `main()` will safely be ignored.
if __name__ == "__main__":
    print("The Script Execution Guard")
    print("Starting script...")
    print("-" * 40)
    
    # Run all our logic
    main()
    
    print("Script finished.")

