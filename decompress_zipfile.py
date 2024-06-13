 #Create a Python script to decompress a ZIP file and extract its contents.

import zipfile
import os

def decompress_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"ZIP file '{zip_path}' has been decompressed to '{extract_to}'")
    except FileNotFoundError:
        print(f"The file '{zip_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{zip_path}' or write to '{extract_to}'.")
    except zipfile.BadZipFile:
        print(f"The file '{zip_path}' is not a valid ZIP file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    zip_path = input("Enter the path of the ZIP file to decompress: ")
    extract_to = input("Enter the destination directory to extract the contents to: ")
    decompress_zip(zip_path, extract_to)
