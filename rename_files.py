# Develop a Python script to rename files in a directory with a specific naming pattern.
import os

def rename_files(directory, new_name_pattern):
    try:
        files = os.listdir(directory)
        for index, file_name in enumerate(files):
            # Construct the new file name
            file_extension = os.path.splitext(file_name)[1]
            new_name = f"{new_name_pattern}_{index + 1}{file_extension}"
            old_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file_name}' to '{new_name}'")
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory = input("Enter the path of the directory containing the files: ")
    new_name_pattern = input("Enter the new naming pattern: ")
    rename_files(directory, new_name_pattern)
