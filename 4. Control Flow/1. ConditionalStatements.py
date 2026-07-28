"""
LESSON: Conditional Statements
──────────────────────────────
Execute different blocks of code based on conditions.
Covers: if, if-else, if-elif-else, nested if-else
"""

# ── 1. if ──
"""Used to run a block of code only if a condition is True"""
age = 20
if age >= 18:
    print("You are eligible to vote.")
# Output: You are eligible to vote.


# ── 2. if-else ──
"""Adds an alternative block if the condition is False"""
age = 15
if age >= 18:
    print("You can vote.")
else:
    print("You are not eligible to vote yet.")
# Output: You are not eligible to vote yet.


# ── 3. if-elif-else ──
"""Used to check multiple conditions one after another"""
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
# Output: Grade B


# ── 4. Nested if-else ──
"""Placing one if (or if-else) statement inside another"""
age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Bring your ID next time.")
else:
    print("You are underage.")
# Output: Bring your ID next time.


# ── 5. Shorthand (Ternary Operator) ──
"""A concise one-line if-else. Highly used in data processing and ML assignments."""
score = 85
status = "Pass" if score >= 50 else "Fail"
print(f"\nTernary Operator: score={score} -> {status}")
# Output: Ternary Operator: score=85 -> Pass

