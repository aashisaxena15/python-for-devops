#Develop a Python script that creates a new directory with a given name.

import os

def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"The directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied to create the directory '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_name = input("Enter the name of the directory to create: ")
    create_directory(directory_name)
