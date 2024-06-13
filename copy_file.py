#Create a Python script that copies a file from one location to another.

import shutil
import os

def copy_file(src, dst):
    try:
        # Copy the file from src to dst
        shutil.copy2(src, dst)
        print(f"File copied from {src} to {dst}")
    except FileNotFoundError:
        print(f"The file '{src}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{src}' or '{dst}'.")
    except IsADirectoryError:
        print(f"The destination '{dst}' is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    src = input("Enter the source file path: ")
    dst = input("Enter the destination file path: ")
    copy_file(src, dst)
