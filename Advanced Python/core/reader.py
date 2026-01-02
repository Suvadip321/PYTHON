def read_data(file_path):
    """
    Reads a text file and returns a list of lines.
    """
    records = []
    with open(file_path, "r") as file:
        for line in file:
            records.append(line.strip())
        return records
