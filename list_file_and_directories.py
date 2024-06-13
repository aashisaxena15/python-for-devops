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



"""Sure! Let's break down the script step-by-step in a simple way:

### What the Script Does
The script is designed to list all the files and directories in a folder that you specify.

### Parts of the Script

1. **Importing the `os` module**:
   ```python
   import os
   ```
   - This line imports the `os` module, which provides functions to interact with the operating system, like reading files and directories.

2. **Defining a function**:
   ```python
   def list_files_and_directories(path):
   ```
   - Here, we define a function named `list_files_and_directories` that will take a `path` as an input. A path is just the location of a folder on your computer.

3. **Using a `try` block**:
   ```python
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
   ```
   - **Try block**: This is used to attempt the main task, while also being ready to catch any errors that might occur.
   - **os.scandir(path)**: This opens the folder specified by `path` so we can look inside it.
   - **entries**: This is a list of all the things (files and directories) inside the folder.
   - **For loop**: This goes through each item in the folder one by one.
   - **entry.is_file()**: Checks if the item is a file.
   - **entry.is_dir()**: Checks if the item is a directory.
   - **Print statements**: These print the name of each file or directory.

4. **Handling errors**:
   - **FileNotFoundError**: If the folder path doesn't exist, it prints an error message.
   - **PermissionError**: If you don't have permission to access the folder, it prints an error message.
   - **General Exception**: Catches any other errors and prints a message.

5. **Main part of the script**:
   ```python
   if __name__ == "__main__":
       path = input("Enter the path to list files and directories: ")
       list_files_and_directories(path)
   ```
   - This part runs when you execute the script.
   - It asks you to enter the path of the folder you want to list.
   - It then calls the `list_files_and_directories` function with the path you entered.

### How to Run the Script

1. **Save the script**: Copy the code into a file named `list_files_and_directories.py`.
2. **Open a terminal** (or command prompt) on your computer.
3. **Navigate to the script location**: Use the `cd` command to go to the directory where your script is saved.
4. **Run the script**: Type `python list_files_and_directories.py` and hit Enter.
5. **Enter a path**: When the script asks for a path, type the location of the folder you want to inspect (for example, `C:\Users\YourName\Documents` on Windows or `/home/YourName/Documents` on Linux/Mac) and press Enter.

The script will then print out the names of all files and directories in that folder."""
