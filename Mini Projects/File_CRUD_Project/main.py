import os
from pathlib import Path

def file_and_folder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1}: {item}")

def createfile():
    try:
        name = input("Enter the file name you want to create: ")
        path = Path(name)
        if not path.exists():
            with open(path, 'w') as f:
                content = input("Enter your content here:\n")
                f.write(content)
            print("File Created Successfully.")

        else:
            print("This file already exist!")

    except Exception as e:
        print("Error: ", e)

def readfile():
    try:
        name = input("Enter file name you want to read: ")
        path = Path(name)
        if path.exists() and path.is_file():
            with open(path, 'r') as f:
                content = f.read()
                print(content)
            print("File Readed Successfully.")

        else:
            print("This file does not exist!")

    except Exception as e:
        print("Error: ", e)

def updatefile():
    try:
        name = input("Enter file name you want to update: ")
        path = Path(name)
        if path.exists() and path.is_file():
            print("Press 1 to rename your file")
            print("Press 2 to overwriting content in your file")
            print("Press 3 to appending content in your file")
            res = int(input("Enter your response: "))

            if res == 1:
                new_name = input("Enter new name: ")
                new_path = Path(new_name)
                path.rename(new_path)
                print("File renamed successfully.")

            elif res == 2:
                with open(path, 'w') as f:
                    content = input("Enter your content here:\n")
                    f.write(content)
                print("Content Overwritten Successfully.")

            elif res ==  3:
                with open(path, 'a') as f:
                    content = input("Enter your content here:\n")
                    f.write(content)
                print("Content Appended Successfully.")

            else:
                print("Please enter a valid response!")

        else:
            print("This file does not exist")

    except Exception as e:
        print("Error: ", e)

def deletefile():
    try:
        name = input("Enter file name you want to delete: ") 
        if os.path.exists(name):
            os.remove(name)
            print("File Deleted Successfully.")
        else:
            print("This file does not exist")
    
    except Exception as e:
        print("Error: ", e)

def main():
    print("Press 0 to see directory")
    print("Press 1 to create a file")
    print("Press 2 to read a file")
    print("Press 3 to update a file")
    print("Press 4 to delete a file")

    try:
        check = int(input("Enter your response: "))
        if check == 0:
            file_and_folder()
    
        elif check == 1:
            createfile()

        elif check == 2:
            readfile()

        elif check == 3:
            updatefile()

        elif check == 4:
            deletefile()

        else:
            print("Please enter a valid response!")

    except Exception as e:
        print("Error: ", e)


if __name__ == '__main__':
    main()

