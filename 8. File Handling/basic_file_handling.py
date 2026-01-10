# Reading entire file
with open("input.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line (for large files)
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        print(line)

# Readong all lines into list
with open("input.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Writing file (overwrites existing)
with open("output.txt", "w") as f:
    f.write(
        "This is first line\nThis is second line\nThis is third line\n"
    )

# Appending to a file
with open("output.txt", "a") as f:
    f.write("This is fourth line\n")

# Writing multiple lines
lines = ["line1\n", "line2\n", "line3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Handle encoding issues
with open("input.txt", "r", encoding='utf-8') as f:
    content = f.read()


# JSON file
import json

# Write json file
data = {
    "name": "Suvadip",
    "age": 20,
    "scores": [85, 92, 78]
}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read json file
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
