from core.reader import read_data
from core.writer import write_data

INPUT_PATH = "data/input.txt"
OUTPUT_PATH = "data/output.txt"

def main():
    data = read_data(INPUT_PATH)
    write_data(OUTPUT_PATH, data)

if __name__ == "__main__":
    main()
