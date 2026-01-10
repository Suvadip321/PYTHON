from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Build paths safely
data_dir = BASE_DIR / "data"
input_file = data_dir / "input.txt"
output_file = data_dir / "output.txt"

# Ensure directory exists
data_dir.mkdir(parents=True, exist_ok=True)

# Check file existence
if input_file.exists():
    with input_file.open("r", encoding="utf-8") as f:
        content = f.read()
        print(content)

# Write file (overwrite)
with output_file.open("w", encoding="utf-8") as f:
    f.write("Hello\n")

# Append file
with output_file.open("a", encoding="utf-8") as f:
    f.write("World\n")

# Iterate files in a directory
for file in data_dir.glob("*.txt"):
    print(file.name)
