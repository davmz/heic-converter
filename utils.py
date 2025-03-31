# utils.py

import os
from PIL import Image
import pillow_heif

# Prompt user to enter a file or folder path
# Continues prompting until a valid path is given
def get_input_file_path():
    while True:
        path = input("Enter the path to a .heic file or folder: ").strip()
        if not os.path.exists(path):
            print("❌ Path does not exist. Please try again.")
        else:
            return path

# Create the output folder (if it doesn't exist)
# Returns the folder path (default: 'converted_images')
def create_output_folder(folder_name="converted_images"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

# Convert a single .heic file to .jpg
# Adds a numeric suffix if a file with the same name already exists
# Returns the output path and a success status (True/False)
def convert_heic_to_jpg(input_path, output_folder):
    try:
        # Read the HEIC file using pillow-heif
        heif_file = pillow_heif.read_heif(input_path)

        # Convert HEIC bytes into a Pillow image
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw"
        )

        # Build output path
        base_name = os.path.basename(input_path)
        name_without_ext = os.path.splitext(base_name)[0]
        output_path = os.path.join(output_folder, f"{name_without_ext}.jpg")

        # If a file with the same name already exists, add a numeric suffix
        counter = 1
        while os.path.exists(output_path):
            output_path = os.path.join(output_folder, f"{name_without_ext}_{counter}.jpg")
            counter += 1

        # Save the image in JPEG format
        image.save(output_path, "JPEG")
        return output_path, True

    except Exception as e:
        # If there's an error, return the file path and mark it as failed
        print(f"Error converting '{input_path}': {e}")
        return input_path, False

# Process either a single file or a folder of .heic files
# Returns total files found, number of successful conversions, and any failed file paths
def process_path(path, output_folder):
    # Case 1: Single file
    if os.path.isfile(path) and path.lower().endswith(".heic"):
        output_path, success = convert_heic_to_jpg(path, output_folder)
        return 1, 1 if success else 0, [path] if not success else [], output_path if success else None

    # Case 2: Folder
    elif os.path.isdir(path):
        # Filter for .heic files in the folder
        heic_files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(".heic")]

        if not heic_files:
            print("⚠️ No .heic files found in the folder.")
            return 0, 0, [], None

        total = len(heic_files)
        success_count = 0
        failed_files = []

        # Convert each HEIC file in the folder
        for file in heic_files:
            _, success = convert_heic_to_jpg(file, output_folder)
            if success:
                success_count += 1
            else:
                failed_files.append(file)

        return total, success_count, failed_files, None

    # Case 3: Invalid input (not a file or folder)
    else:
        print("❌ Invalid file or unsupported format.")
        return 0, 0, [path]