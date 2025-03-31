# utils.py

import os
from PIL import Image
import pillow_heif

def get_input_file_path():
    while True:
        file_path = input("Enter the path to the .heic file: ").strip()
        if not os.path.isfile(file_path):
            print("❌ File does not exist. Please try again.")
        elif not file_path.lower().endswith(".heic"):
            print("❌ The file is not a .heic image. Please provide a valid HEIC file.")
        else:
            return file_path

def create_output_folder(folder_name="converted_images"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def convert_heic_to_jpg(input_path, output_folder):
    try:
        heif_file = pillow_heif.read_heif(input_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw"
        )
        base_name = os.path.basename(input_path)
        name_without_ext = os.path.splitext(base_name)[0]
        output_path = os.path.join(output_folder, f"{name_without_ext}.jpg")

        # Check if file already exists, and add suffix if necessary
        counter = 1
        while os.path.exists(output_path):
            output_path = os.path.join(output_folder, f"{name_without_ext}_{counter}.jpg")
            counter += 1

        image.save(output_path, "JPEG")
        return output_path, True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None, False