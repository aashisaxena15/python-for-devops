# Write a Python script to compress a file using ZIP format.
import zipfile
import os

def compress_file(file_path, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path), compress_type=zipfile.ZIP_DEFLATED)
        print(f"File '{file_path}' has been compressed to '{zip_path}'")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{file_path}' or write to '{zip_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to compress: ")
    zip_path = input("Enter the destination path for the compressed file (including the .zip extension): ")
    compress_file(file_path, zip_path)
