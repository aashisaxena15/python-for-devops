#Write a Python script that lists all files and directories in a specified path.

import os

def list_files_and_directories(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except FileNotFoundError:
        print(f"The path '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input("Enter the path to list files and directories: ")
    list_files_and_directories(path)
