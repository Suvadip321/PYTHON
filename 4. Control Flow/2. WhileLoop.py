"""
LESSON: while Loop
------------------
Repeats a block of code as long as a condition is True.
Covers: basic while, conditional while with break, infinite while with break, input validation, nested while.
"""

# Basic while loop
print("Basic while loop (print 1 to 5):")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()
# Output: 1 2 3 4 5

print("\nBasic while loop (print 5 to 1):")
i = 5
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
# Output: 5 4 3 2 1


# Conditional while loop with break
print("\nConditional while loop with break (stop when i is 6):")
i = 1
while i < 11:
    if i == 6:
        print("Breaking out of loop!")
        break
    print(i, end=" ")
    i += 1
print()
# Output: 1 2 3 4 5 Breaking out of loop!


# Infinite while loop with break
print("\nInfinite while loop with break:")
i = 1
while True:         # Infinite loop
    print(i, end=" ")
    if i == 3:
        break       # Exit loop when i equals 3
    i += 1
print()
# Output: 1 2 3


# Input Validation
print("\nInput Validation:")
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Type 'quit' to exit: ")
    print(f"You typed: {user_input}")
print("Successfully exited!")


# Nested while loops
print("\nNested while loops:")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

