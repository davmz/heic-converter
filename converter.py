# Import necessary modules
import time
from utils import (
    get_input_file_path,
    create_output_folder,
    convert_heic_to_jpg
)

def main():
    print("\U0001F4F8 HEIC to JPG Converter\n")

    # Step 1: Get valid input file path from user
    input_path = get_input_file_path()

    # Start timing after input
    start_time = time.time()

    # Step 2: Create output folder if it doesn't exist
    output_folder = create_output_folder()

    # Step 3: Convert the HEIC file to JPG
    output_path, success = convert_heic_to_jpg(input_path, output_folder)

    # End timing after conversion
    end_time = time.time()
    total_time = end_time - start_time

    # Step 4: Display result
    if success:
        print(f"\n✅ Conversion successful!")
        print(f"Original file: {input_path}")
        print(f"Converted file: {output_path}")
        print(f"⏱️ Total time: {total_time:.2f} seconds")
    else:
        print(f"\n❌ Conversion failed. Please check the file and try again.")

if __name__ == "__main__":
    main()