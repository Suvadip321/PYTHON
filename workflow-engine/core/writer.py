def write_data(file_path, records):
    """
    Writes records to a text file, one per line.
    """
    with open(file_path, "w") as file:
        for record in records:
            file.write(record + "\n")
