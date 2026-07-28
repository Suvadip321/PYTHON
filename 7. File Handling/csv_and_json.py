"""
LESSON: CSV & JSON File Handling
────────────────────────────────
Two of the most common data formats in Data Science and APIs.
We use pathlib to construct safe, professional file paths.
"""
import json
import csv
from pathlib import Path

# Get the folder this script is inside
BASE_DIR = Path(__file__).resolve().parent
data_dir = BASE_DIR / "data"
data_dir.mkdir(parents=True, exist_ok=True)

# 1. JSON (Writing and Reading)
print("1) JSON Handling")

json_file = data_dir / "data.json"

data = {"name": "Suvadip", "role": "AI Engineer", "skills": ["Python", "ML"]}

# Write JSON
with open(json_file, "w") as f:
    json.dump(data, f, indent=4)

# Read JSON
with open(json_file, "r") as f:
    loaded_data = json.load(f)
    print(f"Loaded JSON: {loaded_data['name']} is an {loaded_data['role']}")

print("-" * 40)


# 2. CSV (Writing and Reading using DictWriter/DictReader)
# (Note: In Data Science, you will usually just use Pandas for CSVs!)
print("2) CSV Handling")

csv_file = data_dir / "data.csv"

data = [
    {"id": 1, "label": "cat", "confidence": 0.95},
    {"id": 2, "label": "dog", "confidence": 0.87},
]

# Write CSV
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "label", "confidence"])
    writer.writeheader()
    writer.writerows(data)

# Read CSV
print("Reading CSV:")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"ID {row['id']} -> {row['label']} ({row['confidence']})")

print("-" * 40)

