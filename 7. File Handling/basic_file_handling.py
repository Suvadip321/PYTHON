"""
LESSON: Paths & Basic File Handling
───────────────────────────────────
Use `pathlib` to safely build file paths on any OS.
Use Python's built-in `with open()` to read and write files securely.
"""
from pathlib import Path

# 1. PATH BUILDING & DIRECTORIES
print("1) Path Building")
# Get the folder this script is inside
BASE_DIR = Path(__file__).resolve().parent

# Build safe paths (Works on Windows/Mac/Linux)
data_dir = BASE_DIR / "data"
output_file = data_dir / "data.txt"

# Create the folder if it doesn't exist
data_dir.mkdir(parents=True, exist_ok=True)
print(f"Directory ready: {data_dir}")
print("-" * 40)

# 2. WRITING TEXT FILES
print("2) Writing to a file (Overwrites)")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello World!\n")
    f.write("Line 2: Learning Python.\n")
print(f"Successfully wrote to {output_file.name}")

print("-" * 40)

print("3) Appending to a file (Adds to end)")

with open(output_file, "a", encoding="utf-8") as f:
    f.write("Line 3: This was appended!\n")
print(f"Successfully appended to {output_file.name}")

print("-" * 40)

# 3. READING TEXT FILES
print("4) Reading a file")

with open(output_file, "r", encoding="utf-8") as f:
    content = f.read()
    print("File Contents:")
    print(content)

print("-" * 40)

# 4. PATH PROPERTIES
print("5) File Properties")
print("Full Path:", output_file)
print("Filename only:", output_file.name)
print("Extension:", output_file.suffix)
print("Exists?:", output_file.exists())
print("-" * 40)

